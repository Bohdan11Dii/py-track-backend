import json
from celery import shared_task
from quizzes.models import Test, Question, Answer


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=10, retry_kwargs={'max_retries': 3})
def parse_test_file(self, test_id):
    test = Test.objects.get(pk=test_id)

    if not test.source_file:
        test.import_status = 'failed'
        test.save(update_fields=['import_status'])
        return

    test.import_status = 'processing'
    test.save(update_fields=['import_status'])

    try:
        # Читаємо файл
        with test.source_file.open('rb') as f:
            content = f.read().decode('utf-8')
        data = json.loads(content)

        # Перевірка структури
        questions_data = data.get("questions")
        if not isinstance(questions_data, list):
            raise ValueError("Invalid JSON structure: 'questions' must be a list")

        # Створюємо Questions і Answers
        for q in questions_data:
            question = Question.objects.create(
                test=test,
                text=q["text"]
            )
            answers = [
                Answer(
                    question=question,
                    text=a["text"],
                    is_correct=a["is_correct"]
                )
                for a in q.get("answers", [])
            ]
            Answer.objects.bulk_create(answers)

        test.import_status = 'done'
        test.save(update_fields=['import_status'])

    except Exception as e:
        test.import_status = 'failed'
        test.save(update_fields=['import_status'])
        raise e
