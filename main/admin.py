from django.contrib import admin
from main.models import Users, Recommendation, BusinessSubmission, Category, Comment
from ratings.handlers import ratings, RatingHandler
from ratings.forms import SliderVoteForm
# Register your models here.


class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

admin.site.register(Users)
admin.site.register(BusinessSubmission)
admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
# ratings.register(Recommendation)
ratings.register(Recommendation, RatingHandler,
    score_range=(1, 5), score_step=0.5, can_delete_vote=False)
