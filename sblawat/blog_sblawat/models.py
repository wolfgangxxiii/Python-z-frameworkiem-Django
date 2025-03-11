from django.db import models

class PostSblawat(models.Model):
    title = models.CharField("Tytuł", max_length=200)
    content = models.TextField("Treść")
    created_at = models.DateTimeField("Data utworzenia", auto_now_add=True)
    likes_count = models.PositiveIntegerField("Polubienia", default=0)  # ⬅️ TO POLE MUSI BYĆ!
    views = models.PositiveIntegerField("Wyświetlenia", default=0)

    def __str__(self):
        return self.title


class Komentarz(models.Model):
    post = models.ForeignKey(PostSblawat, on_delete=models.CASCADE, related_name='komentarze')
    autor = models.CharField("Autor", max_length=100)
    tresc = models.TextField("Treść komentarza")
    created_at = models.DateTimeField("Data dodania", auto_now_add=True)

    def __str__(self):
        return f'Komentarz {self.autor} do "{self.post.title}"'
