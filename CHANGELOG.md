# Changelog

<!--
   You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
-->

<!-- towncrier release notes start -->

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
