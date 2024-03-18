import win32net

def list_users():
    users = []
    resume_handle = 0

    while True:
        # Obtem a lista de usuários. level=0 retorna dados básicos de usuário.
        result, total_entries, resume_handle = win32net.NetUserEnum(None, 0, 0, resume_handle)
        users.extend([user['name'] for user in result])

        if not resume_handle:
            break

    return users

# Listar os usuários e imprimir cada um
for user in list_users():
    print(user)
