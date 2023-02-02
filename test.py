def build_profile(**user_info):
    profile = {}
    print(user_info)
    for key, value in user_info.items():
        profile[key] = value
        return profile

#user_profile = build_profile(location='princeton',field='physics')

print(user_profile)