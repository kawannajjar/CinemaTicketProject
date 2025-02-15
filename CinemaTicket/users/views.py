from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def test_log(request):
    logger.debug('این یک لاگ تست است!')
    return HttpResponse('لاگ تست با موفقیت ثبت شد.')