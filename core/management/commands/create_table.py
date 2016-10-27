#coding: utf-8
from django.core.management.base import NoArgsCommand
from core.models import Table
from optparse import make_option


def get_or_create_table():
    first_table = Table.objects.filter(pk=1).first()
    if not first_table:
        first_table = Table(id=1, entries={})
    return first_table


def get_table_pattern():
    entries = []
    for i in range(100):
        entries.append([])
        for j in range(100):
            entries[i].append(i == j or i + j == 99)
    return entries


class Command(NoArgsCommand):

    help = "Comando idempotente para criar a tabela"

    option_list = NoArgsCommand.option_list + (
        make_option('--verbose', action='store_true'),
    )

    def handle_noargs(self, **options):
        table = get_or_create_table()
        table.entries = get_table_pattern()
        table.save()