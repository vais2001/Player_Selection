# serializers.py
from rest_framework import serializers
from .models import Skill, Player

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'skillname', 'value']

class PlayerSerializer(serializers.ModelSerializer):
    # skills = SkillSerializer(many=True,read_only=True)

    class Meta:
        model = Player
        fields = ['id', 'name', 'position', 'skills']
        # def create(self,validated_data):  #create method
        #     skills = self.initial_data['skillname']
            
        #     skillslist = []
            
        #     for skill in skills:
        #         skillslist.append(Skill.objects.get(pk = skill['id']))
        #     player = Player.objects.create(**validated_data)
        #     player.skillname.set(skillslist)
        #     return player