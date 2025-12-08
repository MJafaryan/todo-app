import django_filters
from django_filters.rest_framework import OrderingFilter
from tasks.models import TaskModel

class TaskModelFilters(django_filters.FilterSet):
    """The filter set for TaskModel objects."""

    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    is_complete = django_filters.BooleanFilter(field_name="is_complete")
    due_time = django_filters.DateFromToRangeFilter(field_name="due_time")

    ordering = OrderingFilter(
        fields=(
            ("created_at", "created_at",),
            ("title", "title",),
        )
    )

    class Meta:
        module = TaskModel
        fields = ["title", "is_complete", "due_time",]
