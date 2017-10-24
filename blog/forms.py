from django.forms import Form, ChoiceField,Select

class Header(Form):
    moda = ChoiceField(label="lol", choices=(
        (1, ("Not relevant")),
        (2, ("Review")),
        (3, ("Maybe relevant")),
         ),initial='',  widget=Select(),required=True)


