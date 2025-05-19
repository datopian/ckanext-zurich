import ckan.plugins.toolkit as tk
import ckan.lib.uploader as uploader
import os 

@tk.side_effect_free
@tk.chained_action
def package_show(up_func, context, data_dict):
    package = up_func(context, data_dict)

    for resource in package['resources'] or []:
        upload = uploader.get_resource_uploader(resource)
        filename = os.path.basename(resource['url'])
        key_path = upload.get_path(resource['id'], filename)
        params = {
                    'ResponseContentDisposition':
                        'attachment; filename=' + filename,
                }
        resource['download_url'] = upload.get_signed_url_to_key(key_path, params, read_only=True)

    return package