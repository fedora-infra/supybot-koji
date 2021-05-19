###
# Copyright (c) 2007, Mike McGrath
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
###

import supybot.utils as utils
import supybot.conf as conf
from datetime import datetime
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import urllib
import koji

class Koji(callbacks.Plugin):
    """Add the help for "@plugin help Koji" here
    This should describe *how* to use this plugin."""
    threaded = True
    def __init__(self, irc):
        self.__parent = super(Koji, self)
        self.__parent.__init__(irc)
        koji_server = self.registryValue('server')
        self.koji_client = koji.ClientSession(koji_server, {})

    def building(self, irc, msg, args, builder):
        """<builder>

        See what's building on a particular builder."""
        k = self.koji_client
        try:
            for host in k.listHosts():
                if not host['name'].find(builder):
                    id = host['id']
        except AttributeError:
            irc.reply("Couldn't find builder: %s" % builder)
        else:
            try:
                tasks = k.listTasks(opts={'host_id': id, 'method': 'buildArch',
                                          'state': [koji.TASK_STATES['OPEN']],
                                          'decode': True})
                for task in tasks:
                    irc.reply("%s - %s:%s" % (builder, task['request'][0],
                                              task['request'][2]))
                if not tasks:
                    irc.reply("%s - Not doing anything" % builder)
            except UnboundLocalError:
                irc.reply("Builder %s doesn't exist" % builder)
    building = wrap(building, ['text'])

    def taskload(self, irc, msg, args):
        """takes no arguments

        Return the number of running tasks."""
        k = self.koji_client
        open = k.listTasks(opts={'state': [1]})
        total = k.listTasks(opts={'state': [0, 1, 4]})
        irc.reply(str("Tasks running - Open: %s Total: %s" % (len(open),
                                                              len(total))))
    taskload = wrap(taskload)

    def buildload(self, irc, msg, args):
        """takes no arguments

        Return the total load average of the build system."""
        k = self.koji_client
        hosts = hosts = k.listHosts()
        total = 0
        load = 0
        for host in hosts:
            total = total + host['capacity']
            load = load + host['task_load']
        perc = (load / total * 100)
        if perc > 95:
            status = "Overload!"
        elif perc > 80:
            status = "Very High Load"
        elif perc > 60:
            status = "High Load"
        elif perc > 40:
            status = "Medium Load"
        elif perc > 30:
            status = "Light Load"
        elif perc > 0:
            status = "Very Light Load"
        elif perc == 0:
            status = "No Load"
        irc.reply(str('Load: %.1f Total: %.1f Use: %.1f%% (%s)'
                      % (load, total, perc, status)))
    buildload = wrap(buildload)

    def builders(self, irc, msg, args):
        """takes no arguments

        Check the status of the builders."""
        k = self.koji_client
        hosts = hosts = k.listHosts()
        total = 0
        ready = 0
        enabled = 0
        status = "Unknown"
        for host in hosts:
            ready = ready + host['ready']
            enabled = enabled + host['enabled']
            total = total + 1

        disabled = total - enabled

        irc.reply(str('Enabled: %i Ready: %i Disabled: %i'
                      % (enabled, ready, disabled)))
    buildload = wrap(buildload)


Class = Koji


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
