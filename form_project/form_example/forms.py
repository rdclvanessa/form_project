from django.forms import (
    BooleanField,
    CharField,
    ChoiceField,
    DateField,
    DateInput,
    DecimalField,
    EmailField,
    FloatField,
    Form,
    HiddenInput,
    IntegerField,
    ModelForm,
    MultipleChoiceField,
    PasswordInput,
    RadioSelect,
    Textarea,
)

from .models import Course


class CourseModelForm(ModelForm):
    class Meta:
        model = Course
        fields = ["name", "prefix", "number", "description"]


RADIO_CHOICES = (
    ("Value One", "Value One Display"),
    ("Value Two", "Text For Value Two"),
    ("Value Three", "Value Three's Display Text"),
)

BOOK_CHOICES = (
    (
        "Non-Fiction",
        (("1", "Deep Learning with Keras"), ("2", "Web Development with Django")),
    ),
    ("Fiction", (("3", "Brave New World"), ("4", "The Great Gatsby"))),
)


class ExampleForm(Form):
    text_input = CharField()
    password_input = CharField(widget=PasswordInput)
    checkbox_on = BooleanField()
    radio_input = ChoiceField(choices=RADIO_CHOICES, widget=RadioSelect)
    favorite_book = ChoiceField(choices=BOOK_CHOICES)
    books_you_own = MultipleChoiceField(choices=BOOK_CHOICES)
    text_area = CharField(widget=Textarea)
    integer_input = IntegerField()
    float_input = FloatField()
    decimal_input = DecimalField()
    email_input = EmailField()
    date_input = DateField(widget=DateInput(attrs={"type": "date"}))
    hidden_input = CharField(widget=HiddenInput, initial="Hidden Value")
