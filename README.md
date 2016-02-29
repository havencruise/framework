# Django-Skeleton


A skeleton for a django site that organizes code into:

*   apps/ - Where all apps reside
*   static - Our static files directory ( will be created upon 'syncdb' )
*   <site-name> - where our manage.py is.
*   conf - where our environment specific settings will live (ex. production, integration, etc)
*   bin - where we have a script to create the base site (Usage: `setup-site.py <site-name>`)


You should setup your virtualenv in the root directory.

### Usage

    cd <checkout-location>
    virtualenv env
    pip install -r requirements.txt
    python bin/setup_site.py <site_name>

### Environment import order

There are many different ways to organize environment specific settings
Settings are imported in this order so that deployment to servers becomes easier.
However edit `manage.py` and `<site_name>/settings/__init__.py` if you want to manage it in another way.

Here's how the order goes:

1. `conf/settings_override/default/`
2. `<site_name>/settings/`
3. `conf/settings_override/<env>/`
