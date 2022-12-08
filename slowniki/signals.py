from django.forms import model_to_dict
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.dispatch import receiver
from django.utils import timezone
from .models import Dictionary, DictionaryHistory


@receiver(signal=pre_delete, sender=Dictionary)
def dictionary_deleted_handler(sender, instance, *args, **kwargs):

    try:
        former_record = sender.objects.get(id=instance.id)
        record_as_dict = model_to_dict(former_record)
        print(record_as_dict)
        record_as_dict.pop('modifiedBy')
        record_as_dict.pop('createdBy')

        deletion_date = timezone.now()
        for k in record_as_dict:
            newEntry = DictionaryHistory(
                field=k,
                prev_value=record_as_dict[k],
                next_value=None,
                deleted=True,
                user_edited='CurrentUser',
                date_edited=deletion_date)
            print(newEntry.__dict__)

    except Exception:
        print("Some error!!!")