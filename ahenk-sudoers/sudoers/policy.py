#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Mine Dogan <mine.dogan@agem.com.tr>

import json
import subprocess
from subprocess import PIPE

from base.plugin.AbstractCommand import AbstractCommand


class GrantSudoAccess(AbstractCommand):
    def __init__(self, data, context):
        super(GrantSudoAccess, self).__init__()
        self.data = data
        self.context = context

        self.context.put('message_type', 'qwe')
        self.context.put('message_code', 'qwe')
        self.context.put('message', 'qwe')
        self.context.put('data', None)
        self.context.put('content_type', None)

    def handle_policy(self):

        username = self.context.get('username')

        try:
            if username is not None:
                exec_user = 'exec su -l ' + username
                priv = json.loads(self.data)

                if str(priv['privilege']) == 'True':
                    add_user = subprocess.Popen('adduser ' + username + ' sudo', stderr=PIPE, stdout=PIPE, shell=True)
                    add_user.wait()
                    process = self.context.execute(exec_user)
                    process.wait()
                else:
                    del_user = subprocess.Popen('deluser ' + username + ' sudo', stderr=PIPE, stdout=PIPE, shell=True)
                    del_user.wait()
                    process = self.context.execute(exec_user)
                    process.wait()

                self.set_result('POLICY_STATUS', 'POLICY_PROCESSED', 'User sudoers profile processed successfully.')
                self.logger.info('[Sudoers] Sudoers profile is handled successfully.')

            else:
                self.set_result('POLICY_STATUS', 'POLICY_PROCESSED', 'There is no username.')

        except Exception as e:
            self.logger.error('[Sudoers] A problem occured while handling sudoers profile: {0}'.format(str(e)))
            self.set_result('POLICY_STATUS', 'POLICY_PROCESSED',
                            'A problem occured while handling sudoers profile: {0}'.format(str(e)))

    def set_result(self, type=None, code=None, message=None, data=None, content_type=None):
        self.context.put('message_type', type)
        self.context.put('message_code', code)
        self.context.put('message', message)
        # self.context.put('data')
        # self.context.put('content_type')


def handle_policy(profile_data, context):
    print('GRANT-SUDO-ACCESS')
    quota = GrantSudoAccess(profile_data, context)
    quota.handle_policy()
