from django.db.models import Model
from slowniki.models import Dictionary, EntryFieldSpecification


def add_creator_name_before_object_creation(*,
                                            target_dict: dict,  # serializer.data after validation
                                            creator_name: str) -> int:
    extra_data = {'createdBy': creator_name, 'modifiedBy': creator_name}
    target_dict.update(extra_data)
    return target_dict


def create_dictionary(*,
                      target_dict: dict,
                      creator_name: str) -> int:
    data_dict = add_creator_name_before_object_creation(
        target_dict=target_dict, creator_name=creator_name)
    new_obj = Dictionary.objects.create(**data_dict)
    print(new_obj)
    return new_obj.id


def create_dictionary_specification(*,
                                    target_dict: dict,
                                    creator_name: str) -> int:
    data_dict = add_creator_name_before_object_creation(
        target_dict=target_dict, creator_name=creator_name)
    dictionaryId = data_dict['dictionaryId'].split('/')[-2]
    dictionary = Dictionary.objects.get(pk=dictionaryId)
    data_dict['dictionaryId'] = dictionary
    new_obj = EntryFieldSpecification.objects.create(**data_dict)
    return new_obj.id
