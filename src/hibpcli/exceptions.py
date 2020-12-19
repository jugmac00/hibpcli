class HibpError(Exception):
    pass


class ApiError(HibpError):
    pass


class KeepassError(HibpError):
    pass
