# coding=utf-8
from __future__ import absolute_import

from octoprint_oauthfit.oauth_user_manager import OAuthbasedUserManager
import octoprint.plugin
import logging
import yaml

# config = "~/.octoprint/config.yaml"
# stream = open(config, 'r')
# data = yaml.load(stream)



class HelloWorldPlugin(octoprint.plugin.StartupPlugin,
					   octoprint.plugin.TemplatePlugin,
					   octoprint.plugin.SettingsPlugin,
					   octoprint.plugin.AssetPlugin
					   ):
	def on_after_startup(self):
		self._logger.info("############# Hello World FIT OAuth 0003!")
		self._logger.info("Mistr hanus vice na: %s" %self._settings.get(["url"]))


	# Settings plugin mixin
	def get_settings_defaults(self):
		self._logger.info("####### getting settings 44444")
		return dict(url="https://en.wikipedia.org/wiki/Hello_world")

	# def get_template_vars(self):
	# 	return dict(url=self._settings.get(["url"]))

	# Template plugin mixin
	def get_template_configs(self):
		self._logger.info("************ Template configs *************")
		return [
			dict(type="navbar", template="oauthfit_login.jinja2", custom_bindings=False, replaces="login"),
			# dict(type="navbar", template="oauthfit_name.jinja2", custom_bindings=False),
			# dict(type="navbar", custom_bindings=True),
			dict(type="settings", custom_bindings=True)
		]


	# Asset plugin mixin

	def get_assets(self):
		self._logger.info("****** getting Assets ******")
		return dict(
			js=["js/oauthfit.js"],
			css=["css/oauthfit.css"]
		)

def user_factory_hook(components, settings, *args, **kwargs):
	logging.getLogger("octoprint.plugins." + __name__).info("#######111111######")
	return OAuthbasedUserManager()


__plugin_name__ = "OAuth"
__plugin_implementation__ = HelloWorldPlugin()
__plugin_hooks__ = {
	"octoprint.users.factory": user_factory_hook
}
