
"""
This example module shows various types of documentation available for use
with pydoc.  To generate HTML documentation for this module issue the
command:

    - source venv/bin/activate
    - cd doc
    - make html

"""

class House:
    """
    House encapsulates a name and an age.
    """
    def __init__(self, name, age):
        """
        Construct a new House object.

        :param name: The name of this house
        :param age: The age of this house
        :return: returns nothing
        """
        self.name = name
        self.age = age

if __name__ == '__main__':
    h = House('Casa del koen', -1)
