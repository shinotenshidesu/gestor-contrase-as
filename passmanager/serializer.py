from rest_framework import serializers
from .models import PassManager

class PassManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassManager
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = super().create(validated_data)
        if password:
            instance.set_password(password)
            instance.save()  # Guardar la instancia para que la contraseña encriptada se almacene en la base de datos
        return instance
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)