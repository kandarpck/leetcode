config_dependencies = list()


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))


# Prints to standard output.
def findLongestCycle(lines):
    # IMPLEMENTATION GOES HERE
    for line in lines:
        if line.startswith('['):
            dependency = line.split(':')
            if len(dependency) > 1:
                found = False
                for config_ll in config_dependencies:
                    dummy = ListNode(-1)
                    dummy.next = config_ll
                    while dummy.next:
                        dummy = dummy.next
                        if dummy.val == dependency[0][1:]:
                            while dummy.next:
                                dummy = dummy.next
                            dummy.next = ListNode(dependency[1][:-1])
                            found = True
                if not found:
                    append_head = ListNode(dependency[0][1:])
                    append_head.next = ListNode(dependency[1][:-1])
                    config_dependencies.append(append_head)
            else:
                config_dependencies.append(ListNode(dependency[0][1:-1]))

    print(config_dependencies)


if __name__ == '__main__':
    ip = ['[base_server]', '[admin_console:custom_console]', '[custom_console:dev_console]', '[console:base_server]',
          '[dev_console:admin_console]']
    findLongestCycle(ip)
