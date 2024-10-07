from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "size", "price", "description", "notes"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)  # Menghapus tag HTML dari 'name'

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)  # Menghapus tag HTML dari 'description'

    def clean_size(self):
        size = self.cleaned_data["size"]
        return strip_tags(size)  # Menghapus tag HTML dari 'size'

    def clean_notes(self):
        notes = self.cleaned_data["notes"]
        return strip_tags(notes)  # Menghapus tag HTML dari 'notes'