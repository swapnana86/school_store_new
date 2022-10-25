from django import forms

from .models import Userdata, Course


class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Userdata
        fields = '__all__'
        # fields = ['name', 'user', 'dept', 'course']
        widgets = {
            'gender': forms.RadioSelect(),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        # print("data")
        # print(self.data)
        # print("fields")
        # print(self.fields)

        if 'dept' in self.data:
            try:
                dept_id = int(self.data.get('dept'))
                # print("DEEEE")
                # print(dept_id)

                self.fields['course'].queryset = Course.objects.filter(dept_id=dept_id).order_by('course_name')
                # print(self.fields['course'].queryset)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty course queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.Department.dept_set.order_by('dept_name')
