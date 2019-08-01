from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from users.models import Messages

def user_list(request):
    if request.method == 'GET':
        messages = Messages.objects.all()
        return render(
            request,
            'chat.html',
            {
                "messages": messages,
            }
        )


        # for m in messages:
        #     try:
        #         s = Users.objects.filter(id=m.sender)[0]
        #         r = Users.objects.filter(id=m.receiver)[0]
        #         print(
        #             s,
        #             "->",
        #             r,
        #             ": ",
        #             m.text,
        #             m.date
        #         )
        #     except IndexError:
        #         pass



        return render(
            request,
            'chat.html',
            {
                "messages": messages,
            }
        )
    elif request.method == "POST":
        Messages(
            text=request.POST['message']
        ).save()
        messages = Messages.objects.all()
        return render(
            request,
            'chat.html',
            {
                "messages": messages,
            }
        )


# Create your views here.
