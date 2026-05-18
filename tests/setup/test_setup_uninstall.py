from collective.contact_behaviors import PACKAGE_NAME


class TestSetupUninstall:
    def test_product_uninstalled(self, uninstalled, installer):
        """Test if collective.contact_behaviors is cleanly uninstalled."""
        assert installer.is_product_installed(PACKAGE_NAME) is False
