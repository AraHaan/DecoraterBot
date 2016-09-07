# coding=utf-8
"""
The MIT License (MIT)

Copyright (c) 2015-2016 AraHaan

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
import discord
import asyncio
import sys
import json
import io
import os.path
import importlib
import traceback
try:
    import BotCommands
except SyntaxError:
    sepa = os.sep
    exception_data = 'Fatal exception caused in BotCommands.py:\n{0}'.format(str(traceback.format_exc()))
    logfile = '{0}{1}resources{1}Logs{1}error_log.txt'.format(sys.path[0], sepa)
    try:
        file = io.open(logfile, 'a', encoding='utf-8')
        size = os.path.getsize(logfile)
        if size >= 32102400:
            file.seek(0)
            file.truncate()
        file.write(exception_data)
        file.close()
    except PermissionError:
        pass
    print('Cannot Continue as the Commands has a SyntaxError.')
    sys.exit(1)
import BotPMError
import BotVoiceCommands

sepa = os.sep

try:
    consoledatafile = io.open('{0}{1}resources{1}ConfigData{1}ConsoleWindow.json'.format(sys.path[0], sepa))
    consoletext = json.load(consoledatafile)
    consoledatafile.close()
except FileNotFoundError:
    print('ConsoleWindow.json is not Found. Cannot Continue.')
    sys.exit(2)
try:
    jsonfile = io.open('{0}{1}resources{1}ConfigData{1}IgnoreList.json'.format(sys.path[0], sepa))
    somedict = json.load(jsonfile)
    jsonfile.close()
except FileNotFoundError:
    print(str(consoletext['Missing_JSON_Errors'][0]))
    sys.exit(2)
try:
    botmessagesdata = io.open('{0}{1}resources{1}ConfigData{1}BotMessages.json'.format(sys.path[0], sepa))
    botmessages = json.load(botmessagesdata)
    botmessagesdata.close()
except FileNotFoundError:
    print(str(consoletext['Missing_JSON_Errors'][1]))
    sys.exit(2)

DBCommands = BotCommands.BotCommands()
DBVoiceCommands = BotVoiceCommands.VoiceBotCommands()

global _somebool
_somebool = False

# default to True in case options are not present in Credentials.json
_logging = True
_logbans = True
_logunbans = True
_logkicks = True
_discord_logger = True
_asyncio_logger = True
_log_available = True
_log_unavailable = True
log_channel_create = True
log_channel_delete = True
log_channel_update = True
log_member_update = True
log_server_join = True
log_server_remove = True
log_server_update = True
log_server_role_create = True
log_server_role_delete = True
log_server_role_update = True
log_group_join = True
log_group_remove = True
log_error = True
log_voice_state_update = True
log_typing = True
log_socket_raw_receive = True
log_socket_raw_send = True
log_resumed = True
log_member_join = True
# Will Always be True to prevent the Error Handler from Causing Issues later.
# Well only if the PM Error handler is False.
enable_error_handler = True


class BotConfigVars:
    """
    Class for getting the config Values.
    """
    def __init__(self):
        self.credsfile = io.open(PATH)
        self.credentials = json.load(self.credsfile)
        self.credsfile.close()

    @property
    def logging(self):
        """
        Function that returns weather to have normal logging or not.
        :return: Bool
        """
        value = str(self.credentials['logging'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def logbans(self):
        """
        Returns weather to log bans or not.
        :return: Bool
        """
        value = str(self.credentials['logbans'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def logunbans(self):
        """
        Returns weather to log unbans or not.
        :return: Bool
        """
        value = str(self.credentials['logunbans'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def logkicks(self):
        """
        Returns weather to log kicks or not.
        :return: Bool
        """
        value = str(self.credentials['logkicks'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def discord_logger(self):
        """
        Returns weather to use the discord.py logger or not.
        :return: Bool
        """
        value = str(self.credentials['discord_py_logger'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def asyncio_logger(self):
        """
        Returns weather to use the asyncio logger or not.
        :return: Bool
        """
        value = str(self.credentials['asyncio_logger'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_available(self):
        """
        Returns weather to log available servers or not.
        :return: Bool
        """
        value = str(self.credentials['LogServerAvailable'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_unavailable(self):
        """
        Returns weather to log unavailable servers or not.
        :return: Bool
        """
        value = str(self.credentials['LogServerUnavailable'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_channel_create(self):
        """
        Returns weather to log Created Channels or not.
        :return: Bool
        """
        value = str(self.credentials['log_channel_create'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_channel_delete(self):
        """
        Returns weather to log Deleted Channels or not.
        :return: Bool
        """
        value = str(self.credentials['log_channel_delete'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_channel_update(self):
        """
        Returns weather to log updated Channels or not.
        :return: Bool
        """
        value = str(self.credentials['log_channel_update'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_member_update(self):
        """
        Returns weather to log member updates or not.
        :return: Bool
        """
        value = str(self.credentials['log_member_update'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_server_join(self):
        """
        Returns weather to log Server Joins.
        :return: Bool
        """
        value = str(self.credentials['log_server_join'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_server_remove(self):
        """
        Returns weather to log when a Server is removed.
        :return: Bool
        """
        value = str(self.credentials['log_server_remove'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_server_update(self):
        """
        Returns weather to log when a Server is updated.
        :return: Bool
        """
        value = str(self.credentials['log_server_update'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_server_role_create(self):
        """
        Returns weather to log when a role is created.
        :return: Bool
        """
        value = str(self.credentials['log_server_role_create'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_server_role_delete(self):
        """
        Returns weather to log when a role was deleted.
        :return: Bool
        """
        value = str(self.credentials['log_server_role_delete'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_server_role_update(self):
        """
        Returns weather to log when a role was updated.
        :return:
        """
        value = str(self.credentials['log_server_role_update'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_group_join(self):
        """
        Returns weather to log group joins or not.
        :return: Bool
        """
        value = str(self.credentials['log_group_join'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_group_remove(self):
        """
        Returns weather to log group removes or not.
        :return: Bool
        """
        value = str(self.credentials['log_group_remove'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_error(self):
        """
        Returns weather to log bot errors or not.
        :return: Bool
        """
        value = str(self.credentials['log_error'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_voice_state_update(self):
        """
        Returns weather to log Voice State Updates or not.
        :return: Bool
        """
        value = str(self.credentials['log_voice_state_update'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_typing(self):
        """
        Returns Weather to log typing or not.
        :return: Bool
        """
        value = str(self.credentials['log_typing'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_socket_raw_receive(self):
        """
        Returns weather to log socket raw recieve data or not.
        :return: Bool
        """
        value = str(self.credentials['log_socket_raw_receive'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_socket_raw_send(self):
        """
        Returns weather to log raw socket send data.
        :return: Bool
        """
        value = str(self.credentials['log_socket_raw_send'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_resumed(self):
        """
        Returns weather to log bot connection resumes or not.
        :return: Bool
        """
        value = str(self.credentials['log_resumed'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def log_member_join(self):
        """
        Returns weather to log when a person joins a server.
        :return: Bool
        """
        value = str(self.credentials['log_member_join'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def pm_command_errors(self):
        value = str(self.credentials['pm_command_errors'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value

    @property
    def enable_error_handler(self):
        """
        Returns weather to use the Error Handler or not.
        :return: Bool
        """
        value = None
        if self.pm_command_errors:
            value = False
        else:
            value = True
        return value

    @property
    def bot_prefix(self):
        """
        Returns the Bot Prefix.
        :return:
        """
        value = str(self.credentials['bot_prefix'][0])
        if value == '':
            value = None
        if value is None:
            print('No Prefix specified in Credentials.json. The Bot cannot continue.')
            sys.exit(2)
        return value

    @property
    def discord_user_id(self):
        value = str(self.credentials['ownerid'][0])
        if value == 'None':
            value = None
        return value

    @property
    def bot_id(self):
        value = str(self.credentials['botid'][0])
        if value == 'None':
            value = None
        return value

    @property
    def disable_voice_commands(self):
        value = str(self.credentials['disable_voice'][0])
        if value == 'True':
            value = True
        if value == 'False':
            value = False
        return value


PATH = '{0}{1}resources{1}ConfigData{1}Credentials.json'.format(sys.path[0], sepa)
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    BotConfig = BotConfigVars()
    discord_user_id = BotConfig.discord_user_id
    bot_id = BotConfig.bot_id
    _logging = BotConfig.logging
    _logbans = BotConfig.logbans
    _logunbans = BotConfig.logunbans
    _logkicks = BotConfig.logkicks
    _bot_prefix = BotConfig.bot_prefix
    _disable_voice_commands = BotConfig.disable_voice_commands
    _pm_command_errors = BotConfig.pm_command_errors
    _discord_logger = BotConfig.discord_logger
    _asyncio_logger = BotConfig.asyncio_logger
    _log_available = BotConfig.log_available
    _log_unavailable = BotConfig.log_unavailable
    log_channel_create = BotConfig.log_channel_create
    log_channel_delete = BotConfig.log_channel_delete
    log_channel_update = BotConfig.log_channel_update
    log_member_update = BotConfig.log_member_update
    log_server_join = BotConfig.log_server_join
    log_server_remove = BotConfig.log_server_remove
    log_server_update = BotConfig.log_server_update
    log_server_role_create = BotConfig.log_server_role_create
    log_server_role_delete = BotConfig.log_server_role_delete
    log_server_role_update = BotConfig.log_server_role_update
    log_group_join = BotConfig.log_group_join
    log_group_remove = BotConfig.log_group_remove
    log_error = BotConfig.log_error
    log_voice_state_update = BotConfig.log_voice_state_update
    log_typing = BotConfig.log_typing
    log_socket_raw_receive = BotConfig.log_socket_raw_receive
    log_socket_raw_send = BotConfig.log_socket_raw_send
    log_resumed = BotConfig.log_resumed
    log_member_join = BotConfig.log_member_join

if (_logging or _logbans or _logunbans or _logkicks or _discord_logger or _asyncio_logger or _log_available or
        _log_unavailable or log_channel_create or log_channel_delete or log_channel_update or 
        log_member_update or log_server_join or log_server_remove or log_server_update or 
        log_server_role_create or log_server_role_delete or log_server_role_update or log_group_join or 
        log_group_remove or log_error or log_voice_state_update or log_typing or log_socket_raw_receive or 
        log_socket_raw_send or log_resumed or log_member_join or enable_error_handler):
    import BotLogs
    DBLogs = BotLogs.BotLogs()


class BotData001:
    """
        This Class is for Internal Use only!!!
    """

    def __init__(self):
        pass

    @asyncio.coroutine
    def ignore_channel_code(self, client, message):
        """
        Makes the bot Ignore or not Ignore channels.
        :param client: Discord client.
        :param message: Message.
        :return: Nothing.
        """
        if message.content.startswith(_bot_prefix + 'ignorechannel'):
            if message.channel.id not in somedict["channels"]:
                try:
                    somedict["channels"].append(message.channel.id)
                    json.dump(somedict, open("{0}{1}resources{1}ConfigData{1}IgnoreList.json".format(sys.path[0],
                                                                                                     sepa), "w"))
                    try:
                        yield from client.send_message(message.channel, str(botmessages['Ignore_Channel_Data'][0]))
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)
                except Exception as e:
                    try:
                        yield from client.send_message(message.channel, str(botmessages['Ignore_Channel_Data'][1]))
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)
        if message.content.startswith(_bot_prefix + 'unignorechannel'):
            if message.channel.id in somedict["channels"]:
                try:
                    ignored = somedict["channels"]
                    ignored.remove(message.channel.id)
                    json.dump(somedict, open("{0}{1}resources{1}ConfigData{1}IgnoreList.json".format(sys.path[0],
                                                                                                     sepa), "w"))
                    msg_info = str(botmessages['Unignore_Channel_Data'][0])
                    try:
                        yield from client.send_message(message.channel, msg_info)
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)
                except Exception as e:
                    msg_info = str(botmessages['Unignore_Channel_Data'][1])
                    try:
                        yield from client.send_message(message.channel, msg_info)
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)

    @asyncio.coroutine
    def reload_command_code(self, client, message):
        """
        Reloads Bot Command Files.
        :param client: Discord Client.
        :param message: Message.
        :return: Nothing.
        """
        global _somebool
        if message.content.startswith(_bot_prefix + 'reload'):
            if message.author.id == discord_user_id:
                desmod_new = message.content.lower()[len(_bot_prefix + 'reload '):].strip()
                rejoin_after_reload = False
                _somebool = False
                desmod = None
                reload_reason = None
                if len(desmod_new) < 1:
                    desmod = None
                if desmod_new.rfind('botlogs') is not -1:
                    desmod = 'BotLogs'
                    rsn = desmod_new.replace('botlogs', "")
                    if rsn.rfind(' | ') is not -1:
                        reason = rsn.strip(' | ')
                        reload_reason = reason
                        _somebool = True
                    else:
                        reason = None
                        reload_reason = reason
                        _somebool = True
                elif desmod_new.rfind('botcommands') is not -1:
                    desmod = 'BotCommands'
                    rsn = desmod_new.replace('botcommands', "")
                    if rsn.rfind(' | ') is not -1:
                        reason = rsn.strip(' | ')
                        reload_reason = reason
                        _somebool = True
                    else:
                        reason = None
                        reload_reason = reason
                        _somebool = True
                elif desmod_new.rfind("botvoicecommands") is not -1:
                    desmod = "BotVoiceCommands"
                    rsn = desmod_new.replace('botvoicecommands', "")
                    if rsn.rfind(' | ') is not -1:
                        reason = rsn.replace(' | ', "")
                        reload_reason = reason
                        _somebool = True
                    else:
                        reason = None
                        reload_reason = reason
                        _somebool = True
                else:
                    _somebool = False
                if _somebool is True:
                    if desmod_new is not None:
                        if desmod == 'BotCommands' or desmod == 'BotLogs' or desmod == 'BotVoiceCommands':
                            if desmod == 'BotVoiceCommands':
                                rsn = reload_reason
                                rejoin_after_reload = True
                                yield from DBVoiceCommands.reload_commands_bypass1_new(client, message, rsn)
                            try:
                                module = sys.modules.get(desmod)
                                importlib.reload(module)
                                if rejoin_after_reload:
                                    yield from DBVoiceCommands.reload_commands_bypass2_new(
                                        client, message)
                                try:
                                    msgdata = str(botmessages['reload_command_data'][0])
                                    message_data = msgdata + ' Reloaded ' + desmod + '.'
                                    if desmod == 'BotLogs':
                                        if reload_reason is not None:
                                            message_data = message_data + ' Reason: ' + reload_reason
                                            yield from client.send_message(message.channel, message_data)
                                        else:
                                            yield from client.send_message(message.channel, message_data)
                                    else:
                                        yield from client.send_message(message.channel, message_data)
                                except discord.errors.Forbidden:
                                    yield from BotPMError.resolve_send_message_error(client, message)
                            except Exception as e:
                                reloadexception = str(traceback.format_exc())
                                try:
                                    reload_data = str(botmessages['reload_command_data'][1]).format(reloadexception)
                                    yield from client.send_message(message.channel, reload_data)
                                except discord.errors.Forbidden:
                                    yield from BotPMError.resolve_send_message_error(client, message)
                else:
                    try:
                        yield from client.send_message(message.channel, str(botmessages['reload_command_data'][2]))
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)
            else:
                try:
                    yield from client.send_message(message.channel, str(botmessages['reload_command_data'][3]))
                except discord.errors.Forbidden:
                    yield from BotPMError.resolve_send_message_error(client, message)

    @asyncio.coroutine
    def ignored_channel_commands_code(self, client, message):
        """
        Listens for the Commands that can be done in muted Channels.
        :param client: Discord Client.
        :param message: Message.
        :return: Nothing.
        """
        yield from self.ignore_channel_code(client, message)
        yield from self.reload_command_code(client, message)

    @asyncio.coroutine
    def enable_all_commands_code(self, client, message):
        """
        Listens for all Bot Commands.
        :param client: Discord client.
        :param message: Message.
        :return: Nothing.
        """
        yield from DBCommands.prune(client, message)
        yield from DBCommands.invite(client, message)
        yield from DBCommands.kills(client, message)
        yield from DBCommands.colors(client, message)
        yield from DBCommands.games(client, message)
        yield from DBCommands.attack(client, message)
        yield from DBCommands.debug(client, message)
        yield from DBCommands.other_commands(client, message)
        yield from DBCommands.userdata(client, message)
        yield from DBCommands.bot_say(client, message)
        yield from DBCommands.randomcoin(client, message)
        yield from DBCommands.mod_commands(client, message)
        yield from DBCommands.bot_roles(client, message)
        yield from DBCommands.more_commands(client, message)
        yield from DBCommands.convert_url(client, message)
        if _disable_voice_commands is not True and sys.platform.startswith('win'):
            # Sorry but currently I only have opus for Windows and the same for ffmpeg.
            # You will have to get opus and ffmpeg for your platform and then add it to the list like you can see in
            # Core.py.
            yield from DBVoiceCommands.voice_stuff_new(client, message)
        else:
            yield from DBVoiceCommands.voice_stuff_new_disabled(client, message)
        yield from self.ignored_channel_commands_code(client, message)

    @asyncio.coroutine
    def enable_all_commands_with_send_logs_code(self, client, message):
        yield from self.enable_all_commands_code(client, message)
        if _logging:
            yield from DBLogs.send_logs(client, message)

    @asyncio.coroutine
    def enable_all_commands_with_logs_code(self, client, message):
        yield from self.enable_all_commands_code(client, message)
        if _logging:
            DBLogs.logs(client, message)

    @asyncio.coroutine
    def pm_commands_code(self, client, message):
        yield from DBCommands.scan_for_invite_url_only_pm(client, message)
        yield from DBCommands.invite(client, message)
        yield from DBCommands.kills(client, message)
        yield from DBCommands.games(client, message)
        yield from DBCommands.other_commands(client, message)
        yield from DBCommands.bot_say(client, message)
        yield from DBCommands.randomcoin(client, message)
        yield from DBCommands.convert_url(client, message)
        if _logging:
            DBLogs.logs(client, message)

    @asyncio.coroutine
    def cheesy_commands_code(self, client, message):
        yield from self.enable_all_commands_with_logs_code(client, message)
        serveridslistfile = io.open('{0}{1}resources{1}ConfigData{1}serverconfigs{1}servers.json'.format(sys.path[0],
                                                                                                         sepa))
        serveridslist = json.load(serveridslistfile)
        serveridslistfile.close()
        serverid = str(serveridslist['config_server_ids'][0])
        file_path = ('{0}resources{0}ConfigData{0}serverconfigs{0}{1}{0}verifications{0}'.format(sepa, serverid))
        filename_1 = 'verifycache.json'
        filename_2 = 'verifycommand.json'
        filename_3 = 'verifyrole.json'
        filename_4 = 'verifymessages.json'
        filename_5 = 'verifycache.json'
        joinedlistfile = io.open(sys.path[0] + file_path + filename_1)
        newlyjoinedlist = json.load(joinedlistfile)
        joinedlistfile.close()
        memberjoinverifymessagefile = io.open(sys.path[0] + file_path + filename_2)
        memberjoinverifymessagedata = json.load(memberjoinverifymessagefile)
        memberjoinverifymessagefile.close()
        memberjoinverifyrolefile = io.open(sys.path[0] + file_path + filename_3)
        memberjoinverifyroledata = json.load(memberjoinverifyrolefile)
        memberjoinverifyrolefile.close()
        memberjoinverifymessagefile2 = io.open(sys.path[0] + file_path + filename_4)
        memberjoinverifymessagedata2 = json.load(memberjoinverifymessagefile2)
        memberjoinverifymessagefile2.close()
        role_name = str(memberjoinverifyroledata['verify_role_id'][0])
        msg_command = str(memberjoinverifymessagedata['verify_command'][0])
        try:
            msgdata = None
            if '>' or '<' or '`' in message.content:
                msgdata = message.content.replace('<', '').replace('>', '').replace('`', '')
            else:
                msgdata = message.content
            if msgdata == msg_command:
                if message.author.id in newlyjoinedlist['users_to_be_verified']:
                    yield from client.delete_message(message)
                    role = discord.utils.find(lambda role: role.id == role_name, message.channel.server.roles)
                    msg_data = str(memberjoinverifymessagedata2['verify_messages'][1]).format(message.server.name)
                    yield from client.add_roles(message.author, role)
                    yield from client.send_message(message.author, msg_data)
                    newlyjoinedlist['users_to_be_verified'].remove(message.author.id)
                    json.dump(newlyjoinedlist, open(sys.path[0] + file_path + filename_5, "w"))
                else:
                    yield from client.delete_message(message)
                    yield from client.send_message(message.channel, str(
                        memberjoinverifymessagedata2['verify_messages'][2]))
            else:
                if message.author.id != client.user.id:
                    if message.author.id in newlyjoinedlist['users_to_be_verified']:
                        yield from client.delete_message(message)
                        yield from client.send_message(message.channel, str(
                            memberjoinverifymessagedata2['verify_messages'][3]).format(message.author.mention))
        except NameError:
            yield from client.send_message(message.channel, str(
                memberjoinverifymessagedata2['verify_messages'][4]).format(message.author.mention))

    @asyncio.coroutine
    def everyone_mention_logger_code(self, client, message):
        # if message.content.find('@everyone') != -1:
        #     yield from client.send_message(message.channel.server.owner,
        #                                    "{0} has mentioned everyone in {1} on the {1} server.".format(
        #                                        message.author.name, message.channel.name,
        #                                        message.channel.server.name))
        pass  # this does not yet work right so commented this out.


class BotData002:
    """
        This Class is for Internal Use only!!!
    """
    def __init__(self):
        self.DBCommandData = BotCommandData()

    @asyncio.coroutine
    def ignore_code(self, client, message):
        if message.channel.id not in somedict['channels']:
            try:
                if message.channel.is_private is not False:
                    yield from self.DBCommandData.pm_commands(client, message)
                elif message.channel.server and message.channel.server.id == "81812480254291968":
                    if message.author.id == bot_id:
                        return
                    elif message.channel.id == "153055192873566208":
                        yield from self.DBCommandData.enable_all_commands(client, message)
                    elif message.channel.id == "87382611688689664":
                        yield from self.DBCommandData.enable_all_commands(client, message)
                    else:
                        yield from self.DBCommandData.enable_all_commands_with_send_logs(client, message)
                elif message.channel.server and message.channel.server.id == "71324306319093760":
                    if message.channel.id == '141489876200718336':
                        yield from self.DBCommandData.cheesy_commands(client, message)
                    else:
                        yield from self.DBCommandData.everyone_mention_logger(client, message)
                        yield from self.DBCommandData.enable_all_commands_with_logs(client, message)
                else:
                    yield from self.DBCommandData.enable_all_commands_with_logs(client, message)
            except Exception as e:
                if _pm_command_errors:
                    if discord_user_id is not None:
                        owner = discord_user_id
                        exception_data = str(traceback.format_exc())
                        message_data = '```py\n' + exception_data + "\n```"
                        try:
                            yield from client.send_message(discord.User(id=owner), message_data)
                        except discord.errors.Forbidden:
                            return
                        except discord.errors.HTTPException:
                            funcname = 'ignore_code'
                            tbinfo = str(traceback.format_exc())
                            yield from DBLogs.on_bot_error(funcname, tbinfo, e)
                    else:
                        return
                else:
                    funcname = 'ignore_code'
                    tbinfo = str(traceback.format_exc())
                    yield from DBLogs.on_bot_error(funcname, tbinfo, e)
        else:
            yield from self.DBCommandData.ignored_channel_commands(client, message)


class BotData003:
    """
        This Class is for Internal Use only!!!
    """
    def __init__(self):
        pass

    @asyncio.coroutine
    def resolve_delete_method_code(self, client, message):
        try:
            if message.channel.is_private is not False:
                if _logging == 'True':
                    DBLogs.delete_logs(client, message)
            elif message.channel.server and message.channel.server.id == "81812480254291968":
                if message.author.id == bot_id:
                    return
                elif message.channel.id == "153055192873566208":
                    return
                elif message.channel.id == "87382611688689664":
                    return
                else:
                    yield from DBLogs.send_delete_logs(client, message)
            else:
                if message.channel.is_private is not False:
                    return
                elif message.channel.server.id == '95342850102796288':
                    return
                else:
                    if _logging == 'True':
                        DBLogs.delete_logs(client, message)
        except Exception as e:
            funcname = '_resolve_delete_method_code'
            tbinfo = str(traceback.format_exc())
            yield from DBLogs.on_bot_error(funcname, tbinfo, e)

    @asyncio.coroutine
    def resolve_edit_method_code(self, client, before, after):
        try:
            if before.channel.is_private is not False:
                if _logging == 'True':
                    DBLogs.edit_logs(client, before, after)
            elif before.channel.server and before.channel.server.id == "81812480254291968":
                if before.author.id == bot_id:
                    return
                elif before.channel.id == "153055192873566208":
                    return
                elif before.channel.id == "87382611688689664":
                    return
                else:
                    yield from DBLogs.send_edit_logs(client, before, after)
            else:
                if before.channel.is_private is not False:
                    return
                elif before.channel.server.id == '95342850102796288':
                    return
                else:
                    if _logging == 'True':
                        DBLogs.edit_logs(client, before, after)
        except Exception as e:
            funcname = '_resolve_edit_method_code'
            tbinfo = str(traceback.format_exc())
            yield from DBLogs.on_bot_error(funcname, tbinfo, e)

    @asyncio.coroutine
    def resolve_verify_cache_cleanup_2_code(self, client, member):
        try:
            serveridslistfile = io.open('{0}{1}resources{1}ConfigData{1}serverconfigs{1}servers.json'.format(
                sys.path[0], sepa))
            serveridslist = json.load(serveridslistfile)
            serveridslistfile.close()
            serverid = str(serveridslist['config_server_ids'][0])
            file_path = ('{0}resources{0}ConfigData{0}serverconfigs{0}{1}{0}verifications{0}'.format(sepa, serverid))
            filename_1 = 'verifycache.json'
            joinedlistfile = io.open(sys.path[0] + file_path + filename_1)
            newlyjoinedlist = json.load(joinedlistfile)
            joinedlistfile.close()
            if member.id in newlyjoinedlist['users_to_be_verified']:
                yield from client.send_message(discord.Object(id='141489876200718336'),
                                               "{0} has left the {1} Server.".format(
                                                   member.mention, member.server.name))
                newlyjoinedlist['users_to_be_verified'].remove(member.id)
                file_name = "{0}verifications{0}verifycache.json".format(sepa)
                filename = "{0}{1}resources{1}ConfigData{1}serverconfigs{1}71324306319093760{2}".format(sys.path[0],
                                                                                                        sepa, file_name)
                json.dump(newlyjoinedlist, open(filename, "w"))
        except Exception as e:
            funcname = '_resolve_verify_cache_cleanup_2_code'
            tbinfo = str(traceback.format_exc())
            yield from DBLogs.on_bot_error(funcname, tbinfo, e)

    @asyncio.coroutine
    def resolve_verify_cache_cleanup_code(self, client, member):
        try:
            serveridslistfile = io.open('{0}{1}resources{1}ConfigData{1}serverconfigs{1}servers.json'.format(
                sys.path[0], sepa))
            serveridslist = json.load(serveridslistfile)
            serveridslistfile.close()
            serverid = str(serveridslist['config_server_ids'][0])
            file_path = '{0}resources{0}ConfigData{0}serverconfigs{0}{1}{0}verifications{0}'.format(sepa, serverid)
            filename_1 = 'verifycache.json'
            joinedlistfile = io.open(sys.path[0] + file_path + filename_1)
            newlyjoinedlist = json.load(joinedlistfile)
            joinedlistfile.close()
            if member.id in newlyjoinedlist['users_to_be_verified']:
                newlyjoinedlist['users_to_be_verified'].remove(member.id)
                file_name = "{0}verifications{0}verifycache.json".format(sepa)
                filename = "{0}{1}resources{1}ConfigData{1}serverconfigs{1}71324306319093760{2}".format(sys.path[0],
                                                                                                        sepa, file_name)
                json.dump(newlyjoinedlist, open(filename, "w"))
        except Exception as e:
            funcname = '_resolve_verify_cache_cleanup_code'
            tbinfo = str(traceback.format_exc())
            yield from DBLogs.on_bot_error(funcname, tbinfo, e)

    @asyncio.coroutine
    def resolve_onban_code(self, client, member):
        try:
            if _logbans == 'True':
                yield from DBLogs.onban(client, member)
            if member.server and member.server.id == "71324306319093760":
                yield from self.resolve_verify_cache_cleanup_code(client, member)
        except Exception as e:
            funcname = '_resolve_onban_code'
            tbinfo = str(traceback.format_exc())
            yield from DBLogs.on_bot_error(funcname, tbinfo, e)

    @asyncio.coroutine
    def resolve_onunban_code(self, client, user):
        try:
            if _logunbans == 'True':
                yield from DBLogs.onunban(client, user)
        except Exception as e:
            funcname = '_resolve_onunban_code'
            tbinfo = str(traceback.format_exc())
            yield from DBLogs.on_bot_error(funcname, tbinfo, e)

    @asyncio.coroutine
    def resolve_onremove_code(self, client, member):
        try:
            try:
                banslist = yield from client.get_bans(member.server)
                if member in banslist:
                    return
                else:
                    if _logkicks == 'True':
                        yield from DBLogs.onkick(client, member)
            except (discord.errors.HTTPException, discord.errors.Forbidden):
                if _logkicks == 'True':
                    yield from DBLogs.onkick(client, member)
            if member.server and member.server.id == "71324306319093760":
                yield from self.resolve_verify_cache_cleanup_2_code(client, member)
        except Exception as e:
            funcname = '_resolve_onremove_code'
            tbinfo = str(traceback.format_exc())
            yield from DBLogs.on_bot_error(funcname, tbinfo, e)

    @asyncio.coroutine
    def resolve_onjoin_code(self, client, member):
        try:
            # TODO: Add logging for this.
            if member.server.id == '71324306319093760' and member.bot is not True:
                file_path_join_1 = '{0}resources{0}ConfigData{0}serverconfigs{0}'.format(sepa)
                filename_join_1 = 'servers.json'
                serveridslistfile = io.open(sys.path[0] + file_path_join_1 + filename_join_1)
                serveridslist = json.load(serveridslistfile)
                serveridslistfile.close()
                serverid = str(serveridslist['config_server_ids'][0])
                file_path_join_2 = '{0}resources{0}ConfigData{0}serverconfigs{0}{1}{0}verifications{0}'.format(sepa,
                                                                                                               serverid)
                filename_join_2 = 'verifymessages.json'
                filename_join_3 = 'verifycache.json'
                filename_join_4 = 'verifycache.json'
                memberjoinmessagedatafile = io.open(sys.path[0] + file_path_join_2 + filename_join_2)
                memberjoinmessagedata = json.load(memberjoinmessagedatafile)
                memberjoinmessagedatafile.close()
                msg_info = str(memberjoinmessagedata['verify_messages'][0])
                message_data = msg_info.format(member.id, member.server.name)
                des_channel = str(memberjoinmessagedata['verify_messages_channel'][0])
                joinedlistfile = io.open(sys.path[0] + file_path_join_2 + filename_join_3)
                newlyjoinedlist = json.load(joinedlistfile)
                joinedlistfile.close()
                yield from client.send_message(discord.Object(id=des_channel), message_data)
                if member.id in newlyjoinedlist['users_to_be_verified']:
                    # since this person is already in the list lets not readd them.
                    pass
                else:
                    newlyjoinedlist['users_to_be_verified'].append(member.id)
                    json.dump(newlyjoinedlist, open(sys.path[0] + file_path_join_2 + filename_join_4, "w"))
        except Exception as e:
            funcname = '_resolve_onjoin_code'
            tbinfo = str(traceback.format_exc())
            yield from DBLogs.on_bot_error(funcname, tbinfo, e)

    @asyncio.coroutine
    def resolve_on_login_voice_channel_join_code(self, client):
        try:
            if _disable_voice_commands is not True:
                yield from DBVoiceCommands.reload_commands_bypass3_new(client)
            else:
                return
        except Exception as e:
            funcname = '_resolve_on_login_voice_channel_join_code'
            tbinfo = str(traceback.format_exc())
            yield from DBLogs.on_bot_error(funcname, tbinfo, e)

    @asyncio.coroutine
    def high_level_reload_helper_code(self, client, message, reload_reason):
        try:
            if _disable_voice_commands is not True:
                yield from DBVoiceCommands.reload_commands_bypass4_new(client, message, reload_reason)
            else:
                return
        except Exception as e:
            funcname = 'high_level_reload_helper_code'
            tbinfo = str(traceback.format_exc())
            yield from DBLogs.on_bot_error(funcname, tbinfo, e)

    @staticmethod
    def resolve_discord_logger_code():
        if _discord_logger:
            DBLogs.set_up_discord_logger()

    @staticmethod
    def resolve_asyncio_logger_code():
        if _asyncio_logger:
            DBLogs.set_up_asyncio_logger()

    @asyncio.coroutine
    def server_available_code(self, server):
        if _log_available:
            yield from DBLogs.onavailable(server)

    @asyncio.coroutine
    def server_unavailable_code(self, server):
        if _log_unavailable:
            yield from DBLogs.onunavailable(server)

    @asyncio.coroutine
    def resolve_ongroupjoin_code(self, channel, user):
        try:
            if log_group_join:
                yield from DBLogs.ongroupjoin(channel, user)
        except Exception as e:
            funcname = '_resolve_ongroupjoin_code'
            tbinfo = str(traceback.format_exc())
            yield from DBLogs.on_bot_error(funcname, tbinfo, e)

    @asyncio.coroutine
    def resolve_ongroupremove_code(self, channel, user):
        try:
            if log_group_remove:
                yield from DBLogs.ongroupremove(channel, user)
        except Exception as e:
            funcname = '_resolve_ongroupremove_code'
            tbinfo = str(traceback.format_exc())
            yield from DBLogs.on_bot_error(funcname, tbinfo, e)

    @asyncio.coroutine
    def high_level_reload_helper2_code(self, client, message):
        try:
            if _disable_voice_commands is not True:
                yield from DBVoiceCommands.reload_commands_bypass2_new(client, message)
            else:
                return
        except Exception as e:
            funcname = 'high_level_reload_helper2_code'
            tbinfo = str(traceback.format_exc())
            yield from DBLogs.on_bot_error(funcname, tbinfo, e)


class BotCommandData:
    """
    Bot Command Data Class.
    """
    def __init__(self):
        self.bot = BotData001()

    @asyncio.coroutine
    def ignore_channel(self, client, message):
        yield from self.bot.ignore_channel_code(client, message)

    @asyncio.coroutine
    def reload_command(self, client, message):
        yield from self.bot.reload_command_code(client, message)

    @asyncio.coroutine
    def ignored_channel_commands(self, client, message):
        yield from self.bot.ignored_channel_commands_code(client, message)

    @asyncio.coroutine
    def enable_all_commands(self, client, message):
        yield from self.bot.enable_all_commands_code(client, message)

    @asyncio.coroutine
    def enable_all_commands_with_send_logs(self, client, message):
        yield from self.bot.enable_all_commands_with_send_logs_code(client, message)

    @asyncio.coroutine
    def enable_all_commands_with_logs(self, client, message):
        yield from self.bot.enable_all_commands_with_logs_code(client, message)

    @asyncio.coroutine
    def pm_commands(self, client, message):
        yield from self.bot.pm_commands_code(client, message)

    @asyncio.coroutine
    def cheesy_commands(self, client, message):
        yield from self.bot.cheesy_commands_code(client, message)

    @asyncio.coroutine
    def everyone_mention_logger(self, client, message):
        yield from self.bot.everyone_mention_logger_code(client, message)


class BotIgnores:
    """
    Bot Ignores Class.
    """
    def __init__(self):
        self.bot = BotData002()

    @asyncio.coroutine
    def ignore(self, client, message):
        yield from self.bot.ignore_code(client, message)


class BotEvents:
    """
    Bot Events Class.
    """
    def __init__(self):
        self.bot = BotData003()

    @asyncio.coroutine
    def resolve_delete_method(self, client, message):
        yield from self.bot.resolve_delete_method_code(client, message)

    @asyncio.coroutine
    def resolve_edit_method(self, client, before, after):
        yield from self.bot.resolve_edit_method_code(client, before, after)

    @asyncio.coroutine
    def resolve_onban(self, client, member):
        yield from self.bot.resolve_onban_code(client, member)

    @asyncio.coroutine
    def resolve_onunban(self, client, user):
        yield from self.bot.resolve_onunban_code(client, user)

    @asyncio.coroutine
    def resolve_onremove(self, client, member):
        yield from self.bot.resolve_onremove_code(client, member)

    @asyncio.coroutine
    def resolve_onjoin(self, client, member):
        yield from self.bot.resolve_onjoin_code(client, member)

    @asyncio.coroutine
    def resolve_on_login_voice_channel_join(self, client):
        yield from self.bot.resolve_on_login_voice_channel_join_code(client)

    @asyncio.coroutine
    def high_level_reload_helper(self, client, message, reload_reason):
        yield from self.bot.high_level_reload_helper_code(client, message, reload_reason)

    def resolve_discord_logger(self):
        self.bot.resolve_discord_logger_code()

    def resolve_asyncio_logger(self):
        self.bot.resolve_asyncio_logger_code()

    @asyncio.coroutine
    def server_available(self, server):
        yield from self.bot.server_available_code(server)

    @asyncio.coroutine
    def server_unavailable(self, server):
        yield from self.bot.server_unavailable_code(server)

    @asyncio.coroutine
    def resolve_ongroupjoin(self, channel, user):
        yield from self.bot.resolve_ongroupjoin_code(channel, user)

    @asyncio.coroutine
    def resolve_ongroupremove(self, channel, user):
        yield from self.bot.resolve_ongroupremove_code(channel, user)

    @asyncio.coroutine
    def high_level_reload_helper2(self, client, message):
        yield from self.bot.high_level_reload_helper2_code(client, message)
