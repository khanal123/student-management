from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


from course.models import Course, Subjects
from .serializers import CourseSerializer, SubjectSerializer
# Create your views here.

# Start view for course

# view for get all the course and post the course
@api_view(['GET', 'POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def course_list(request, format=None):
    
    if request.method == "GET":
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# view for getting detail, update and delete single course
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request, pk, format=None):
    try:
        course = Course.objects.get(id=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# end view for course


#Start View for subject

# view for get all the subjects and post the course
@api_view(['GET', 'POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def subject_list(request, format=None):
    if request.method == "GET":
        subjects = Subjects.objects.all()
        serializer = CourseSerializer(subjects, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


 # view for getting detail, update and delete single subject  
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def subject_detail(request, pk, format=None):
    try:
        subject = Subjects.objects.get(id=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
