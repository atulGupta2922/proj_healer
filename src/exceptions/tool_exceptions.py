class UnknownAppException(Exception):
    """Custom exception for unknown App names."""

    def __init__(
        self,
        message: str = "An unknown App was encountered, this app is not supported.",
    ):
        super().__init__(message)
