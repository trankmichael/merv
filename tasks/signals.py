from django.dispatch import Signal, receiver

get_rating_item = Signal(providing_args=["user"])

@receiver(get_rating_item)
def handle_get_rating_item(sender, **kwargs):
	print sender