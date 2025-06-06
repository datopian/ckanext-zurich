import ckan.plugins.toolkit as tk
import ckan.lib.uploader as uploader
import os 
from logging import getLogger

log = getLogger(__name__)

def add_resource_download_uri(package):
    for resource in package.get('resources', []):
        if resource['url_type'] != 'upload':
            resource['download_url'] = resource['url']
            continue
        resource['download_url'] = f"{resource['url']}?proxied_download=true"

@tk.side_effect_free
@tk.chained_action
def package_show(up_func, context, data_dict):
    package = up_func(context, data_dict)

    add_resource_download_uri(package)

    return package
    
@tk.side_effect_free
@tk.chained_action
def package_search(up_func, context, data_dict):
    result = up_func(context, data_dict)

    for package in result.get("results", []):
        add_resource_download_uri(package)

    return result
