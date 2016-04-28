# recommendations.py
from accounts.models import User
from recommends.providers import RecommendationProvider
from recommends.providers import recommendation_registry

from .models import Vote
from tasks import Task

class TaskRecommendationProvider(RecommendationProvider):
    def get_users(self):
        return User.objects.filter(is_active=True, votes__isnull=False).distinct()

    def get_items(self):
        return Task.objects.all()

    def get_ratings(self, obj):
        return Vote.objects.filter(product=obj)

    def get_rating_score(self, rating):
        return rating.score

    def get_rating_site(self, rating):
        return rating.site

    def get_rating_user(self, rating):
        return rating.user

    def get_rating_item(self, rating):
        return rating.product

recommendation_registry.register(Vote, [Task], TaskRecommendationProvider)