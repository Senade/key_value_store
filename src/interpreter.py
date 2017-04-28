import data_store as ds
import cmd


class Data_Store_Interpreter(cmd.Cmd):
    """ Python key value data store"""

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '\nEnter command: '
        self.intro = 'Python key value data store'

    # Overridden methods
    def default(self, line):
        print 'Wrong entry'
        return

    # Methods
    def do_set(self, line):
        """
        set key value
        """
        command = line.strip().split()
        if self.validate_set(command):
            key, value = command[0], ' '.join(command[1:])
            ds.set(key, value)
            ds.display_data_store()
            ds.display_max_vf_store()
            # ds.display_vf_store()

    def do_delete(self, line):
        """
        delete key
        """
        command = line.strip().split()
        if self.validate_delete(command):
            ds.delete(command[0])
            ds.display_data_store()
            ds.display_max_vf_store()
            # ds.display_vf_store()

    # Helper functions
    def validate_set(self, command):
        try:
            assert len(command) >= 2
        except AssertionError as e:
            print 'Enter a value for the value. Usage: set key value'
            return False
        return True

    def validate_delete(self, command):
        try:
            assert len(command) == 1
        except AssertionError as e:
            print 'Key should be a string without spaces. Usage: delete key'
            return False
        return True

if __name__ == '__main__':
    Data_Store_Interpreter().cmdloop()
