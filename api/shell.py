import io
from covid_test.models import Test
from django.contrib.auth.models import User
from covid_test.serializers import TestSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.core.files import File
from PIL import Image

im = Image.open("D:/covid-proj/api/api/media/images/tacila.JPG")

blob = BytesIO()

test_1 = Test(isPositive=False, image=im)
test_2 = Test(isPositive=True, image=im)
test_3 = Test(isPositive=False, image=im)
test_4 = Test(isPositive=True, image=im)


img_bytes = io.BytesIO()

tests = Test.objects.all()

s = TestSerializer(test_1)
s.data

content = JSONRenderer().render(s.data)
content
stream = io.BytesIO(content)
data = JSONParser().parse(stream)

serializer = TestSerializer(data=data)
serializer.is_valid()
serializer.errors
serializer.validated_data

serializer.save()
