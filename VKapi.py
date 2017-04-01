import vk
def connectVK(scope = "wall"):
	session = vk.AuthSession(app_id = '5813182', user_login = '89296301367',
                             user_password = 'danjusha', scope = scope)
	api = vk.API(session)
	return api