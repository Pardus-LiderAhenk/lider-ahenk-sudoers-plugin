#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Mine Dogan <mine.dogan@agem.com.tr>

import json

from base.plugin.abstract_plugin import AbstractPlugin


class GrantSudoAccess(AbstractPlugin):
    def __init__(self, data, context):
        super(AbstractPlugin, self).__init__()
        self.data = data
        self.context = context
        self.logger = self.get_logger()

    def handle_policy(self):

        username = self.context.get('username')

        try:
            if username is not None:
                json_data = json.loads(self.data)

                if str(json_data['privilege']) == 'True':
                    self.execute('adduser {} sudo'.format(username))
                    self.logger.debug('[Sudoers]User sudoers set privilege to {}.'.format(username))
                    # TODO command instead reboot

                    self.logger.debug('[Sudoers] Creating response...')
                    self.context.create_response(self.get_message_code().POLICY_PROCESSED, 'User sudoers set privilege to {} successfully.'.format(username))

                elif str(json_data['privilege']) == 'False':
                    self.execute('deluser {} sudo'.format(username))
                    self.logger.debug('[Sudoers]User sudoers removed privilege from {}.'.format(username))
                    # TODO command instead reboot

                    self.logger.debug('[Sudoers] Creating response...')
                    self.context.create_response(self.get_message_code().POLICY_PROCESSED, 'User sudoers removed privilege from {} successfully.'.format(username))

                else:
                    self.context.create_response(self.get_message_code().POLICY_PROCESSED, 'Missing parameter error.')

                self.logger.debug('[Sudoers] Sudoers profile is handled successfully.')
            else:
                self.logger.error('[Sudoers] Username parameter is missing.')
                self.context.create_response(self.get_message_code().POLICY_ERROR, 'Username is missing')

        except Exception as e:
            self.logger.error('[Sudoers] A problem occurred while handling sudoers profile: {0}'.format(str(e)))
            self.context.create_response(self.get_message_code().POLICY_ERROR, 'A problem occurred while handling sudoers profile: {0}'.format(str(e)))


def handle_policy(profile_data, context):
    print('GRANT-SUDO-ACCESS')
    quota = GrantSudoAccess(profile_data, context)
    quota.handle_policy()
