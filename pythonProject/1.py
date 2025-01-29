from Web.cvtestcase import CVTestCase
from datetime import datetime
from Web.AdminConsole.AdminConsolePages.server_group_details import ServerGroupConfiguration
from Web.AdminConsole.adminconsole import AdminConsole
from Web.Common.cvbrowser import BrowserFactory, Browser
from Web.AdminConsole.Components.table import Rtable
from Web.Common.page_object import handle_testcase_exception, TestStep
from Web.AdminConsole.Components.panel import Security, RPanelInfo, RDropDown, RSecurityPanel
from Web.AdminConsole.AdminConsolePages.server_groups import ServerGroups
from cvpysdk.clientgroup import ClientGroup, ClientGroups
from Web.AdminConsole.Components.dialog import RSecurity
from cvpysdk.security.user import Users
import pytz
from Web.AdminConsole.Components.panel import Backup


class TestCase(CVTestCase):
    test_step = TestStep()

    def _init_(self):
        super(TestCase, self)._init_()
        self.Rsecurity1 = None
        self.rtable = None
        self.panelinfo1 = None
        self.dropdown = None
        self.panelinfo = None
        self.Rsecurity = None
        self.client_group = None
        self.security_associations = None
        self.sg_details = None
        self.whole_sg_page = None
        self.name = None
        self.browser = None
        self.admin_console = None
        self.user = None
        self.navigator = None
        self.client_groups = None
        self.tcinputs = {
            "file server": None,
            "servers name": None,
            "Allow owners to enable data encryption": None,
            "Enable auto discover": None,
            "Job start time": None,
            "Download software from internet": None,
            "Workload region": None,
            "Data restore": None,
            "Data aging": None,
            "Data backup": None,
        }

    def setup(self):

        self.log.info("Started executing %s testcase", self.id)
        self.log.info("" * 10 + " Initialize browser objects " + "" * 10)
        self.browser = BrowserFactory().create_browser_object()
        self.browser.open()
        self.admin_console = AdminConsole(self.browser, self.commcell.webconsole_hostname)
        self.admin_console.login(
            username=self.inputJSONnode['commcell']['commcellUsername'],
            password=self.inputJSONnode['commcell']['commcellPassword'],
            stay_logged_in=True
        )
        self.navigator = self.admin_console.navigator
        self.whole_sg_page = ServerGroups(self.admin_console)
        self.sg_details = ServerGroupConfiguration(self.admin_console, self.commcell)
        self.security_associations = Security(self.admin_console)
        self.user = Users(self.commcell)
        self.Rsecurity = RSecurity(self.admin_console)
        self.Rsecurity1 = RSecurityPanel(self.admin_console)
        self.rtable = Rtable(self.admin_console, title='Security')
        self.panelinfo = RPanelInfo(self.admin_console)
        self.panelinfo1 = RPanelInfo(self.admin_console, title='General')
        self.panelinfo2 = RPanelInfo(self.admin_console, title='Permissions')
        self.dropdown = RDropDown(self.admin_console)
        self.client_groups = ClientGroups(self.commcell)

    def run(self):
        try:
            self.user.add("user_65538", "user_65538@commvault.com", "user_65538", password="Commvault!12Commvault!12")
            self.navigator.navigate_to_server_groups()
            self.whole_sg_page.add_manual_server_group('servergroup_65538', self.tcinputs['servers name'])

            self.sg_details.access_configuration_tab()

            # self.sg_details.edit_general_settings({
            #     'Allow_owners_to_enable_data_encryption': self.tcinputs['Allow owners to enable data encryption'],
            #     'Enable_auto_discover': self.tcinputs['Enable auto discover'],
            #     'set_job_start_time': self.tcinputs['Job start time'],
            #     'Download_software_from_internet': self.tcinputs['Download software from internet'],
            #     'set_workload_region': self.tcinputs['Workload region']
            # })
            #
            self.panelinfo.edit_tile(tile_label='Security')
            self.Rsecurity.edit_security_association(
                {"admin": ["Compliance"]})
            #
            # self.sg_details.enable_activity({
            #     'backup': self.tcinputs['Data backup'],
            #     'restore': self.tcinputs['Data restore'],
            #     'aging': self.tcinputs['Data aging']
            # })
            #
            # self.sg_details.add_owners(user_names=['user_65538', 'master', 'admin']

            self.panelinfo2.edit_tile('Permissions')
            self.sg_details.edit_permissions(items=['Create Alert', 'File Analytics', 'Administration'])
            # self.navigator.navigate_to_file_servers()
            # self.sg_details.backup_check(entity_name=self.tcinputs['file server'], Subclient_name='siva',
            #                              backup_type=Backup.BackupType.FULL)
            # self.navigator.navigate_to_file_servers()
            # self.sg_details.restore_check(entity_name=self.tcinputs['file server'], Subclient_name='siva')
            # self.client_group = ClientGroup(self.commcell, clientgroup_name='servergroup_65538')
            # UI2 = [self.sg_details.get_owners(), self.Rsecurity1.get_details()]
            # UI = self.panelinfo1.get_details()
            # for k, v in UI.items():
            #     UI2.append(v)
            # backend = [self.client_group.Owners,
            #            self.client_group.security_associations,
            #            self.client_group.is_data_encryption_enabled,
            #            self.client_group.is_auto_discover_enabled,
            #            datetime.utcfromtimestamp(self.client_group.job_start_time).replace(tzinfo=pytz.utc).astimezone(
            #                pytz.timezone('GMT')).strftime('%I:%M %p'),
            #            bool(self.client_group.download_software_from_internet),
            #            self.client_group.workload_region,
            #            self.client_group.is_backup_enabled,
            #            self.client_group.is_restore_enabled,
            #            self.client_group.is_data_aging_enabled
            #            ]
            #
            # expected = [
            #     ['master', 'admin', 'user_65538'],
            #     {"admin": ["Compliance"]},
            #     self.tcinputs['Allow owners to enable data encryption'],
            #     self.tcinputs['Enable auto discover'], self.tcinputs['Job start time'],
            #     self.tcinputs['Download software from internet'], self.tcinputs['Workload region'],
            #     self.tcinputs['Data backup'], self.tcinputs['Data restore'], self.tcinputs['Data aging']
            # ]
            #
            # for key, value in enumerate(expected):
            #     if value == "ON":
            #         expected[key] = True
            #     elif value == "OFF":
            #         expected[key] = False
            #
            # if isinstance(expected[4], dict):
            #     time_str = f"{expected[4]['hours']}:{expected[4]['minutes']} {expected[4]['meridian']}"
            #     expected[4] = time_str
            #     print("UI: ", UI2)
            #     print("backend: ", backend)
            #     print("expected : ", expected)
            #
            # if UI2 == backend == expected:
            #     self.log.info('Execution successful')
            # else:
            #     raise Exception('Execution Failed')

        except Exception as exp:
            handle_testcase_exception(self, exp)

    def tear_down(self):
        self.user.delete("user_65538", new_user='admin')
        self.client_groups.refresh()
        self.client_groups.delete('servergroup_65538')
        self.browser.close()
