import os
import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()


# Fake data generator
fakegen = Faker()
topics = ["social", "search", "marketplace", "news", "game"]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # Get or create a topic for the entry
        top = add_topic()

        # Generate fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create a webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create an access record entry
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == "__main__":
    print("Starting population script...")
    populate(20)
    print("Population complete!")
