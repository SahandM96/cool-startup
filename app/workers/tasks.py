from celery import Celery

celery_app = Celery("tasks", broker="redis://localhost:6379")

@celery_app.task
def process_word_data(word):
    return f"Processed {word}"