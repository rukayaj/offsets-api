from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from core import models
from rest_framework.metadata import SimpleMetadata

from collections import OrderedDict
from django.utils.encoding import force_text
from rest_framework import serializers
from rest_framework.utils.field_mapping import ClassLookupDict
from rest_framework_gis.fields import GeometryField


class GeoMetadata(SimpleMetadata):
    """Overriding the SimpleMetadata DRF to add geometryfield for metadata options"""
    label_lookup = ClassLookupDict({
        serializers.Field: 'field',
        serializers.BooleanField: 'boolean',
        serializers.NullBooleanField: 'boolean',
        serializers.CharField: 'string',
        serializers.URLField: 'url',
        serializers.EmailField: 'email',
        serializers.RegexField: 'regex',
        serializers.SlugField: 'slug',
        serializers.IntegerField: 'integer',
        serializers.FloatField: 'float',
        serializers.DecimalField: 'decimal',
        serializers.DateField: 'date',
        serializers.DateTimeField: 'datetime',
        serializers.TimeField: 'time',
        serializers.ChoiceField: 'choice',
        serializers.MultipleChoiceField: 'multiple choice',
        serializers.FileField: 'file upload',
        serializers.ImageField: 'image upload',
        serializers.ListField: 'list',
        serializers.DictField: 'nested object',
        serializers.Serializer: 'nested object',
        GeometryField: 'geojson',
        serializers.ManyRelatedField: 'foreign key - multi'
    })

    def get_field_info(self, field):
        """
        Given an instance of a serializer field, return a dictionary
        of metadata about it.
        """
        field_info = super(GeoMetadata, self).get_field_info(field)
        field_info['field'] = str(field)

        # Override the DRF standard metadata with some additional stuff for FKs
        if field_info['type'] == 'foreign key - multi':
            # Note that we must make sure the url prefixes put into the router in urls.py follow this convention
            field_info['endpoint'] = str(field.child_relation.queryset.model.__name__).lower() + 's'

        return field_info


class PermitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Permit
        fields = ('id', 'name', 'url')


class DevelopmentSerializer(GeoFeatureModelSerializer):
    #permits = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = models.Development
        geo_field = 'footprint'
        fields = ('id', 'year', 'permits', 'type', 'url', 'province')


class OffsetImplementationTimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.OffsetImplementationTime
        fields = ('id', 'time', 'url')


class OffsetSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Offset
        geo_field = 'polygon'
        fields = ('id', 'development', 'type', 'duration', 'implementation_times', 'url')