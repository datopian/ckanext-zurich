import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.zurich.logic.action import (
    package_show, package_search
)


class ZurichPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IActions)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "zurich")

    # IActions
    def get_actions(self):
        return {
            'package_show': package_show, 
            'package_search': package_search
        }
