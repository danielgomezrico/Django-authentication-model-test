from people.models import Person
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.core import serializers
from django.http import HttpResponse

@login_required
def index(request):

	#Get the people ordered by id
	people_list = Person.objects.all().order_by('-id')

	if request.is_ajax():
		#Encode to json
		output = serializers.serialize('json', people_list)

		#Respond to ajax request
		return HttpResponse(output, mimetype='application/javascript')
	else:
		return render(request, 'people/index.html', {'people_list': people_list})