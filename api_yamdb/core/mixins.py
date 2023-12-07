class FieldListMixin:
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
