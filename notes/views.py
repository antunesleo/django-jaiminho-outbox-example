import json

from django.db import transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .kafka_producer import publish_note_created
from .models import Note


@csrf_exempt
def note_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title", "")
        content = data.get("content", "")

        if title and content:
            with transaction.atomic():
                note = Note.objects.create(title=title, content=content)
                publish_note_created(note.as_dict())

            return JsonResponse(
                {"id": note.id, "title": note.title, "content": note.content}
            )
        else:
            return JsonResponse({"error": "Missing title or content"}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
