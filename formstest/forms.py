from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100)

'''
form will be rendered as -

<label for="your_name">Your name: </label>
<input id="your_name" type="text" name="your_name" maxlength="100" required>
'''
