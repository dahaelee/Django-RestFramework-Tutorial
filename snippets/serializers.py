from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

owner = serializers.ReadOnlyField(source='owner.username')

class SnippetSerializer(serializers.ModelSerializer):
    '''
    ModelSerializer 클래스는 Serializer 클래스의 단축 버전.
     - 필드를 자동으로 인식
     - creat() 메서드와 update() 메서드가 이미 구현되어 있음
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']