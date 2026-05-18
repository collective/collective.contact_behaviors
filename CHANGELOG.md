# Changelog

<!--
   You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
-->

<!-- towncrier release notes start -->

## 1.0.0b6 (2026-05-18)


### New features:

- Added support for Plone 6.2: introduced the `6.2-latest` cell in the CI test matrix and the `Framework :: Plone :: 6.2` trove classifier. @ericof [#14](https://github.com/collective/collective.contact_behaviors/issues/14)
- Added support for Python 3.14: added `"3.14"` to the CI test matrix (paired with Plone 6.2; older Plone releases don't yet support 3.14) and the `Programming Language :: Python :: 3.14` classifier. @ericof [#15](https://github.com/collective/collective.contact_behaviors/issues/15)


### Bug fixes:

- Avoid error in countries vocabulary if there is unexpected country data in the catalog. @davisagli [#10](https://github.com/collective/collective.contact_behaviors/issues/10)


### Internal:

- Disabled fail-fast in the GitHub Actions test matrix so a single cell failure no longer cancels the other Python/Plone combinations. @ericof [#12](https://github.com/collective/collective.contact_behaviors/issues/12)
- Bumped `pytest-plone` to `>=1.0.0a3` and adopted the new built-in fixtures: dropped the local `uninstalled`, `request_factory`, `manager_request`, and `anon_request` overrides, keeping a thin `functional_portal` override only to seed and publish the content the REST API tests need. @ericof [#16](https://github.com/collective/collective.contact_behaviors/issues/16)
- Consolidated the historical `CHANGES.md` entries into `CHANGELOG.md` and removed the now-redundant `CHANGES.md`. @ericof [#17](https://github.com/collective/collective.contact_behaviors/issues/17)
- Bumped `actions/checkout` to v6 and `dorny/paths-filter` to v4.0.1 in the CI workflows. @ericof 
- Bumped default Plone version used in CI to 6.1.4. @ericof 
- Bumped local default Plone version to 6.1.4 (matching CI) and made the `uv venv` step idempotent, pinning Python 3.12 outside CI. @ericof 

## 1.0.0b5 (2025-09-17)


### New features:

- Update Brazilian Portuguese translations. @ericof [#9](https://github.com/collective/collective.contact_behaviors/issues/9)
- Add Telefon and Fax fields in contact_info behaviors. @iFlameing 

## 1.0.0b4 (2025-09-11)


### Bug fixes:

- Move phone before email in IContactInfo behavior, and add missing German translations. @davisagli [#6](https://github.com/collective/collective.contact_behaviors/issues/6)

## 1.0.0b3 (2025-09-08)


### Internal:

- Use native namespace. @ericof 

## 1.0.0b2 (2025-09-08)


### Bug fixes:

- Drop support to pkg_resources. @ericof 

## 1.0.0b1 (2025-09-08)


### Internal:

- Modernize packaging. @ericof [#4](https://github.com/collective/collective.contact_behaviors/issues/4)

## 1.0.0a3 (2023-06-27)


### New features:

- Allow other packages to set default values for address fields [@ericof] #2


## 1.0.0a2 (2023-06-21)


### New features:

- Implement `collective.contact_behaviors.address_info behavior` @ericof address
- Implement `collective.contact_behaviors.contact_info behavior` @ericof contact
- Implement `plone.app.querystring.field.country` querystring filter @ericof querystring
- Implement `collective.contact_behaviors.available_countries` and  `collective.contact_behaviors.countries` @ericof vocabularies


### Internal:

- Update configuration files.
  [plone devs] 23d5b8e1
- Added towncrier as a package dependency. @ericof towncrier


## 1.0.0a1 (2023-06-21)
