from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView,status
from .models import ContactMessage
from .serializers import ContactSerializer
from rest_framework.permissions import AllowAny

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]

    # 🔥 THIS LINE IS REQUIRED FOR IMAGE UPLOAD
    parser_classes = (MultiPartParser, FormParser)

    @action(detail=False, methods=['get'])
    def slider(self, request):
        limit = int(request.query_params.get('limit', 5))
        qs = Project.objects.filter(featured=True).order_by('-created_at')[:limit]
        if not qs:
            qs = Project.objects.all().order_by('-created_at')[:limit]

        serializer = self.get_serializer(qs, many=True, context={'request': request})
        return Response(serializer.data)
# views.py



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    """
    Return the current logged-in user info
    """
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        'is_superuser': user.is_superuser
    })
class AddProjectView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        return Response(
            {"detail": "Only admin can add project"},
            status=status.HTTP_200_OK
        )

 # Create a standard serializer

@api_view(['GET', 'POST'])
@permission_classes([AllowAny]) #
# Sirf login user hi GET request kar payega
def contact_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            messages = ContactMessage.objects.all().order_by('-created_at')
            serializer = ContactSerializer(messages, many=True)
            return Response(serializer.data)
        return Response({"detail": "Not authorized"}, status=403)

    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Sent"}, status=201)
        return Response(serializer.errors, status=400)