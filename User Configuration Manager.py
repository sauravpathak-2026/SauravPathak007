test_settings = {
    'theme': 'dark',
    'language': 'english',
    'notifications': 'enabled',

}

def add_setting(settings_dict, new_pair):
    key, value = new_pair
    key = key.lower()
    value = value.lower()
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings_dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings_dict, new_pair):
    key, value = new_pair
    key = key.lower()
    value = value.lower()
    if key in settings_dict:
        settings_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings_dict, key):

    key = key.lower()
    if key in settings_dict:
        settings_dict.pop(key, None)
        return f"Setting '{key}' deleted successfully!"
    else:
        return 'Setting not found!'

def view_settings(settings_dict):
    if not settings_dict:
        return 'No settings available.'
    else:
        result = "Current User Settings:\n"
        for key, value in settings_dict.items():
            result += f"{key.capitalize()}: {value}\n"
        return result
add_setting(test_settings, ('Profile', 'Gaming'))
print(view_settings(test_settings))
