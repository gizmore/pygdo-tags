from gdo.base.GDO_Module import GDO_Module
from gdo.ui.GDT_Page import GDT_Page


class module_tags(GDO_Module):

    def gdo_load_scripts(self, page: 'GDT_Page'):
        self.add_bower_css('')
        self.add_bower_js('')
        self.add_js('js/gdo_tags.js')
