from pybo.models import Question
from django.utils import timezone

# for i in range(300):
#     q = Question(subject='테스트 데이터입니다:[%03d]' % i, content='내용무', create_date=timezone.now())
#     q.save()


# 조회
question_list = Question.objects.order_by('-create_date')
# 삭제
for question in question_list:
    if question.id > 4:
        question.delete()
