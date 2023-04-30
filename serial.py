"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        self.start = start
        self.count = start

    def __repr__(self):
        return f"<SerialGenerator start= {self.start} next= {self.count + 1}>"

    def reset(self):
        """Resest the counter to orginal start value."""
        self.count = self.start

    def generate(self):
        """Return the next serial."""
        self.count += 1
