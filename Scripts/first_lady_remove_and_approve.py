from Scripts.approve_all_roles_using_images import approve_5_role_and_handel_exceptions
from Scripts.remove_stale_roles_by_images import remove_stale_roles_and_handel_exception


def first_lady_approve_and_remove_roles():
    while True:
        approve_5_role_and_handel_exceptions()
        remove_stale_roles_and_handel_exception()


if __name__ == "__main__":
    first_lady_approve_and_remove_roles()
