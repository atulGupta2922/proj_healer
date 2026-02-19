class UnknownAgentException(Exception):
    """Custom exception for unknown agent names or versions."""

    def __init__(self, message: str = "An unknown agent was encountered."):
        super().__init__(message)
