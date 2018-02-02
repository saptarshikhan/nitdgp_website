from rest_framework import serializers
from department.models import *
import collections


class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name', 'short_code')


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('name', 'research_interest', 'email', 'mobile', 'joining_year')


class OfferingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Programme
        fields = ('degree',)
        depth = 1


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = ('title', 'short_code', 'semester', 'course_type', 'credits',)


class MainSerializer(serializers.ModelSerializer):

    offerings = serializers.SerializerMethodField()

    def get_offerings(self, obj):

        result = collections.defaultdict()
        for i in self.instance.programme_set.all():
            try:
                result[i.degree.name].append({
                    'programme_title': i.title,
                    'courses': CourseSerializer(i.courses_set.order_by('semester'), many=True).data
                })
            except KeyError:
                result[i.degree.name] = [{
                    'programme_title': i.title,
                    'courses': CourseSerializer(i.courses_set.order_by('semester'), many=True).data
                }]
        return result

    class Meta:
        model = Department
        fields = ('offerings',)