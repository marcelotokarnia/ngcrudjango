from rest_framework import test
from core.models import Table
from core.views import NoTableException
from core.management.commands.create_table import get_or_create_table, get_table_pattern
import json


class GetTableTest(test.APITestCase):
    def test_caso_vazio(self):
        table = Table.objects.first()
        self.assertIsNone(table)
        with self.assertRaises(NoTableException):
            self.client.post('/core/get_table', {})

    def test_tabela_preenchida(self):
        table = Table.objects.first()
        self.assertIsNone(table)
        table = get_or_create_table()
        table.entries = get_table_pattern()
        table.save()
        table = Table.objects.first()
        self.assertIsNotNone(table)
        r1 = json.loads(self.client.post('/core/get_table', {}).content)
        entries = r1['table']['entries']
        self.assertTrue(entries[0][0])
        self.assertTrue(entries[1][1])
        self.assertTrue(entries[2][2])
        self.assertTrue(entries[0][99])
        self.assertTrue(entries[99][0])
        self.assertTrue(entries[99][99])
        self.assertFalse(entries[95][99])
        self.assertFalse(entries[96][99])
        self.assertFalse(entries[94][99])
        self.assertFalse(entries[93][99])
        self.assertFalse(entries[92][99])
