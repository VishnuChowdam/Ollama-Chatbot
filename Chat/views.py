from django.shortcuts import render
from django.http import JsonResponse
import ollama

def index(request):
    return render(request, "index.html")

def chat(request):
    if request.method == "POST":
        query = request.POST.get('query', '').strip()

        if not query:
            return JsonResponse({'response': "Please type something!"})

        try:
            response = ollama.generate(
                model='llama3.2:1b',
                prompt=query,
            )
            bot_reply = response.get('response', '').strip()
        except Exception as e:
            bot_reply = f"Error: {str(e)}"

        return JsonResponse({'response': bot_reply})

    return JsonResponse({'response': 'Invalid request method'}, status=405)

