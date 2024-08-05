# Assuming you have imported the Generator class properly
from identifier import Generator

class Build:
    def __init__(self):
        self.build()  # Call the build method correctly

    def build(self):
        gen = Generator()
        print(gen.key)  # Print the key attribute of the Generator instance

# Create an instance of Build
Build()
