import vk
def connectVK(scope = "wall"):
	session = vk.AuthSession(app_id = 'XXXXXXXXXX', user_login = 'XXXXXXXXXXX',
                             user_password = 'XXXXXXXXXXX', scope = scope)
	api = vk.API(session)
	return api