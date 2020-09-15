from django.test import TestCase
from ..models import (InstitutionalRole, Person, Organisation,
                      Subject, CstUser as User
                      )


class SubjectTestCase(TestCase):

    def test_can_create_person_as_subject(self):
        kot1 = Person.objects.create(
            firstname='lula',
            lastname='sleepingclaw',
            pesel='pesel-12345'
        )
        kot2 = Subject.objects.first().person
        self.assertEquals(kot1.pesel, kot2.pesel)

    def test_common_subjects_string_representation(self):
        kot = Person.objects.create(
            firstname='lula',
            lastname='sleepingclaw',
            pesel='pesel-12345'
        )
        policja = Organisation.objects.create(
            name='Policja', kind='jednostki budżetowe', nip='nip-1')

        self.assertEquals(
            [s.__str__() for s in Subject.objects.all()],
            [str(kot), str(policja)]
        )

    def test_can_create_subject_manager(self):
        kot1 = Person.objects.create(
            firstname='lula',
            lastname='sleepingclaw',
            pesel='pesel-12345'
        )
        subject_kot1 = Subject.objects.get(id=kot1.subject_ptr_id)
        user = User.objects.create_user('adam', 'adam@o2.pl', 'Qwert123$')
        subject_kot1.managing_person = user
        subject_kot1.save()
        self.assertEquals(subject_kot1.managing_person, user)

    def test_set_superior_inferior_relation(self):
        msw = Organisation.objects.create(
            name='MSW', kind='jednostki budżetowe', nip='nip-1')
        policja = Organisation.objects.create(
            name='Policja', kind='jednostki budżetowe', nip='nip-2',
            superior=msw)
        print(msw.inferiors.all())
        self.assertEquals(msw.inferiors.all()[0], policja)
