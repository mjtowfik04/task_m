from django import forms
from tasks.models import Task


# Mixin for styling form fields
class StyledFormMixin:
    default_classes = "border-2 border-gray-300 w-full rounded-lg shadow-sm focus:border-rose-500 focus:ring-rose-500"

    def apply_styled_widget(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class': "border-2 border-gray-300 rounded-lg shadow-sm focus:border-rose-500 focus:ring-rose-500"

                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class': "space-t-2"
                })


# Django Form (without a model)
class TaskForm(StyledFormMixin, forms.Form):
    title = forms.CharField(max_length=250, label="Task Title")
    description = forms.CharField(widget=forms.Textarea, label="Task Description")
    due_date = forms.DateField(widget=forms.SelectDateWidget, label="Due Date")
    assigned_to = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[],
        label="Assign to"
    )

    def __init__(self, *args, **kwargs):
        employees = kwargs.pop("employees", [])  # Corrected 'employee' to 'employees'
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].choices = [(emp.id, emp.name) for emp in employees]
        self.apply_styled_widget()  # Apply custom styles


# Django Model Form
class TaskModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assigned_to']
        widgets={
            'due_date':forms.SelectDateWidget,
            'assigned_to':forms.CheckboxSelectMultiple
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widget()  # Apply custom styles
