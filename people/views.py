from people.models import Person
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required
def index(request):
	#Get the people ordered by id
    people_list = Person.objects.all().order_by('-id')

    #Add it to the context
    context = {'people_list': people_list}

    return render(request, 'people/index.html', context)

