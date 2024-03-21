from rest_framework import viewsets
from .serializer import PassManagerSerializer
from .models import PassManager

# Create your views here.
class PassManagerView(viewsets.ModelViewSet):
    serializer_class = PassManagerSerializer
    queryset = PassManager.objects.all()
