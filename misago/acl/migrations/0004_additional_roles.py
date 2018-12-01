# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


_ = lambda s: s


def create_additional_roles(apps, schema_editor):
    Role = apps.get_model('misago_acl', 'Role')

    Role.objects.create(
        name=_("Subscriber"),
        permissions={
            # account
            'misago.users.permissions.account': {
                'name_changes_allowed': 2,
                'name_changes_expire': 180,
                'can_have_signature': 0,
                'allow_signature_links': 0,
                'allow_signature_images': 0,
            },

            # profiles
            'misago.users.permissions.profiles': {
                'can_browse_users_list': 1,
                'can_search_users': 1,
                'can_follow_users': 1,
                'can_be_blocked': 1,
                'can_see_users_name_history': 0,
                'can_see_users_emails': 0,
                'can_see_users_ips': 0,
                'can_see_hidden_users': 0,
            },

            # attachments
            'misago.threads.permissions.attachments': {
                'max_attachment_size': 4 * 1024,
                'can_download_other_users_attachments': True,
            },

            # polls
            'misago.threads.permissions.polls': {
                'can_start_polls': 1,
                'can_edit_polls': 1
            },

            # search
            'misago.search.permissions': {
                'can_search': 1,
            },
        }
    )


class Migration(migrations.Migration):

    dependencies = [
        ('misago_acl', '0003_default_roles'),
    ]

    operations = [
        migrations.RunPython(create_additional_roles),
    ]
