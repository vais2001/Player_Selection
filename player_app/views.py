from django.shortcuts import render
from .models import Player, Skill
from rest_framework.response import Response
from .serializers import PlayerSerializer, SkillSerializer
from rest_framework import status, viewsets
from rest_framework.views import APIView
from django.db.models import Max




 
class PlayerViewset(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    def get_queryset(self):
       player = Player.objects.all()
       return player
    
    def create(self, request, *args, **kwargs):
        data=request.data
        new_player=Player.objects.create(name=data['name'],position=data['position'])
        new_player.save()
        for skill in data['skills']:
            print(skill)
            skill_obj, created = Skill.objects.get_or_create(skillname=skill["skillname"], value=skill["value"])
            new_player.skills.add(skill_obj)
            serializer=PlayerSerializer(new_player)
        return Response(serializer.data) 
    
      
    def update(self, request, pk, *args, **kwargs):
        player = Player.objects.get(id=pk)
        data = request.data
        player.name = data['name']
        player.position = data['position']
        player.save()
    
        player.skills.clear()
        for skill_data in data['skills']:
            skill_obj = Skill.objects.filter(skillname=skill_data["skillname"]).first()
            player.skills.add(skill_obj)
        
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    
    
    def destroy(self, request, pk):
        try:
          player =Player.objects.get(id=pk)
        except Player.DoesNotExist:
            return Response({'msg':'not exist'})
        player.delete()
        return Response({'msg':'delet'},status=status.HTTP_204_NO_CONTENT)


class TeamSelectionAPIView(APIView):
    def post(self, request, *args, **kwargs):
        requirements = request.data
        print(requirements,111111111)
        selected_team = self.select_team(requirements)
        print(selected_team,222222222222)
        if selected_team:
            serializer = PlayerSerializer(selected_team, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Unable to select a team based on the given requirements"}, status=status.HTTP_400_BAD_REQUEST)

    def select_team(self, requirements):
        selected_team = []

        for req in requirements:
            position = req.get('position')
            skill = req.get('mainSkill')
            num_players = req.get('numberOfPlayers')

            # Rule 1: Select the best player 
            players = self.get_players_with_skill_and_position(position, skill, num_players)
            
            # Rule 6: Return error 
            if not players.exists():
                return None  

            selected_team += list(players)
          
        # Remove duplicate players 
        selected_team = list({player.id: player for player in selected_team}.values())

        return selected_team

    def get_players_with_skill_and_position(self, position, skill, num_players):
        # If skill is not  get players based on position only
        if skill is None:
            return Player.objects.filter(position=position).order_by('-skills__value')[:num_players]

        # Rule 4:  select the player with the highest skill value in that position.
        players_with_skill = Player.objects.filter(position=position, skills__skillname=skill).annotate(overall_skill=Max('skills__value')).order_by('-overall_skill')[:num_players]

        return players_with_skill
