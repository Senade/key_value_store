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
        print 'Command does not exist\n'
        print 'Usage: \n------'
        print 'set key value'
        print 'delete key'

    # Methods
    def do_set(self, line):
        """
        Usage: set key value
        sets key=value in the data store
        """
        command = line.strip().split()
        if self.validate_set(command):
            key, value = command[0], ' '.join(command[1:])
            if key[-1] == '/':
                key = key[:-1]
            keys = key.strip().split('/')
            ds.ds_set(keys, value)
            ds.display_data_store()
            ds.display_max_vf_store()

    def do_delete(self, line):
        """
        Usage: delete key
        deletes key from the data store if it exists
        """
        command = line.strip().split()
        if self.validate_delete(command):
            keys = command[0].strip().split('/')
            ds.ds_delete(keys)
            ds.display_data_store()
            ds.display_max_vf_store()

    # Helper functions
    def validate_set(self, command):
        """
        Returns True iff the given set command is valid
        """
        try:
            assert len(command) >= 2
        except AssertionError:
            print 'Enter a value for the value. Usage: set key value'
            return False
        return True

    def validate_delete(self, command):
        """
        Returns True iff the given delete command is valid
        """
        try:
            assert len(command) == 1
        except AssertionError:
            print 'Key should be a string without spaces. Usage: delete key'
            return False
        return True


if __name__ == '__main__':
    Data_Store_Interpreter().cmdloop()
