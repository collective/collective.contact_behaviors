from plone import api
from plone.app.testing import SITE_OWNER_NAME

import pytest
import transaction


@pytest.fixture()
def functional_portal(functional, contents_payload):
    portal = functional["portal"]
    with api.env.adopt_user(SITE_OWNER_NAME):
        content = api.content.create(container=portal, **contents_payload[0])
        api.content.transition(content, transition="publish")
    transaction.commit()
    return portal
