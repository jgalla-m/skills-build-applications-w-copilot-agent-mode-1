from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **options):
        # Usuń stare dane w poprawnej kolejności i tylko z id
        Leaderboard.objects.filter(id__isnull=False).delete()
        Activity.objects.filter(id__isnull=False).delete()
        Workout.objects.filter(id__isnull=False).delete()
        User.objects.filter(id__isnull=False).delete()
        Team.objects.filter(id__isnull=False).delete()

        # Dodaj drużyny
        marvel = Team.objects.create(name='marvel', description='Marvel team')
        dc = Team.objects.create(name='dc', description='DC team')

        # Dodaj użytkowników
        ironman = User.objects.create(email='ironman@marvel.com', name='Tony Stark', team='marvel', is_superhero=True)
        batman = User.objects.create(email='batman@dc.com', name='Bruce Wayne', team='dc', is_superhero=True)
        spiderman = User.objects.create(email='spiderman@marvel.com', name='Peter Parker', team='marvel', is_superhero=True)
        superman = User.objects.create(email='superman@dc.com', name='Clark Kent', team='dc', is_superhero=True)

        # Dodaj aktywności
        Activity.objects.create(user=ironman, type='run', duration=30, date='2024-01-01')
        Activity.objects.create(user=batman, type='cycle', duration=45, date='2024-01-02')
        Activity.objects.create(user=spiderman, type='swim', duration=25, date='2024-01-03')
        Activity.objects.create(user=superman, type='fly', duration=60, date='2024-01-04')

        # Dodaj treningi
        Workout.objects.create(name='Pushups', description='Do pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do situps', suggested_for='dc')

        # Dodaj leaderboard
        Leaderboard.objects.create(team=marvel, points=200)
        Leaderboard.objects.create(team=dc, points=180)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
