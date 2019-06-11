from django.db import models

# Create your models here.

class ImgTxtPair(models.Model):
    recipe_id = models.CharField(max_length=100)

    question_text = models.CharField(max_length=5000)

    image_src = models.CharField(max_length=100)

    choice1_src = models.CharField(max_length=100)

    choice2_src = models.CharField(max_length=100)



    def __str__(self):
        return self.question_text


class Choice(models.Model):

    imgtxtid = models.ForeignKey(ImgTxtPair, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    userid = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text
