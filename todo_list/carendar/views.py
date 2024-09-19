
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Todo
from .forms import TodoForm
from django.utils.dateparse import parse_datetime
from django.utils import timezone

class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        today = timezone.now().date()
        todos = Todo.objects.order_by("deadline", "dt")
        upcoming_todos = []

        for todo in todos:
            if todo.deadline.date() == today + timezone.timedelta(days=1):
                upcoming_todos.append(todo)

        context["todos"] = todos
        context["upcoming_todos"] = upcoming_todos
        return render(request, "carendar/calendar.html", context)

    def post(self, request, *args, **kwargs):
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("carendar:index")

index = IndexView.as_view()

class DoneView(View):
    def post(self, request, pk, *args, **kwargs):
        todo = Todo.objects.filter(id=pk).first()
        todo.done = not todo.done
        todo.save()
        return redirect("carendar:index")

done = DoneView.as_view()

class DeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        todo = get_object_or_404(Todo, id=pk)
        todo.delete()
        return redirect("carendar:index")

delete = DeleteView.as_view()

@csrf_exempt
def update_event(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        event_id = data.get('id')
        start = data.get('start')
        end = data.get('end')

        todo = Todo.objects.filter(id=event_id).first()
        if todo:
            todo.deadline = parse_datetime(start)  # start を日時形式に変換
            todo.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False}, status=400)
    return JsonResponse({'success': False}, status=405)

