from django import forms
from .models import Post,Category,Comment

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body','snippet','header_image','snippet_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'write you blog title here'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
            # 'snippet_image': form.
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body','snippet','snippet_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'write you blog title here'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    
    # name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'write you blog title here'}))
    # body = forms.CharField(max_length=100, widget=(attrs={'class':'form-control'}))
    
    
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets = {
            'name': forms.HiddenInput(attrs={'class':'comment_username','placeholder':'write you blog title here','id':"comment_username"}),
            'body': forms.TextInput(attrs={'class':'comment_body','style':'background-color: transparent; border: none; border-bottom: 1px solid black; outline: none; width: 100%;','placeholder':'Add a comment'}),
        }

        labels = {
            'body': '',  # Customize the label for the body field
        }
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True