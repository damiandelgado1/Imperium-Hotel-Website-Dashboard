from client.forms import Contact


def form_processor(request):
    return {"form": Contact()}