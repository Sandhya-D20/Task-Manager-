from datetime import date, timedelta

from django.shortcuts import get_object_or_404, redirect, render

from .models import WeeklyTask, DailyTodo


def home(request):
    today = date.today()

    # Find the Monday of the current week
    week_start = today - timedelta(days=today.weekday())

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "weekly_task":
            title = request.POST.get("title")
            description = request.POST.get("description")
            category = request.POST.get("category")
            priority = request.POST.get("priority")
            deadline = request.POST.get("deadline")

            WeeklyTask.objects.create(
                title=title,
                description=description,
                category=category,
                priority=priority,
                deadline=deadline,
                week_start=week_start,
            )

        elif form_type == "daily_todo":
            title = request.POST.get("todo_title")

            DailyTodo.objects.create(
                title=title,
                date=today,
            )

        return redirect("home")

    weekly_tasks = WeeklyTask.objects.filter(
        week_start=week_start
    ).order_by("deadline")

    daily_todos = DailyTodo.objects.filter(
        date=today
    ).order_by("created_at")

    completed_tasks = weekly_tasks.filter(
        status="done"
    ).count()
    total_tasks = 3

    progress_percentage = (completed_tasks / total_tasks) * 100

    weekly_tasks = weekly_tasks[:3]

    context = {
        "weekly_tasks": weekly_tasks,
        "daily_todos": daily_todos,
        "completed_tasks": completed_tasks,
        "progress_percentage": progress_percentage,
    }

    return render(request, "tasks/home.html", context)


def update_task(request, task_id):
    task = get_object_or_404(WeeklyTask, id=task_id)

    if request.method == "POST":
        task.status = request.POST.get("status")
        task.save()

    return redirect("home")

def toggle_todo(request, todo_id):
    todo = get_object_or_404(DailyTodo, id=todo_id)

    if request.method == "POST":
        todo.completed = not todo.completed
        todo.save()

    return redirect("home")

def delete_task(request, task_id):
    task = get_object_or_404(WeeklyTask, id=task_id)

    if request.method == "POST":
        task.delete()

    return redirect("home")