from rest_framework.views import APIView
from .serializers import UserSerializers
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
import datetime
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class Register(APIView):
	permission_classes = []
	def post(self,request):
		serializer=UserSerializers(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)

class Login(APIView):
	permission_classes = []
	def post(self, request):
		email=request.data['email']
		password=request.data['password']
		user=User.objects.filter(email=email).first()
		if user is None:
			raise AuthenticationFailed("Provide the Username details")
		if not user.check_password(password):
			raise AuthenticationFailed("Wrong password")
	
		refresh=RefreshToken.for_user(user)
		access_token=refresh.access_token
		access_token.set_exp(lifetime=datetime.timedelta(minutes=15))
		response=Response()
		response.data={
			"access":str(access_token)
		}
		response.set_cookie(key='jwt',value=refresh)
		return response

