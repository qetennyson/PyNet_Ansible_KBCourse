import getpass
import snmp_helper


DESCR = '1.3.6.1.2.1.1.1.0'
NAME = '1.3.6.1.2.1.1.5.0'

def main():

    ip_addr1 = raw_input("enter pyrtr1 address: ")
    ip_addr2 = raw_input("enter pyrtr2 address: ")
    community = raw_input("enter community string: ")

    py_rtr1 = (ip_addr1, community, 161)
    py_rtr2 = (ip_addr2, community, 161)

    for device in (py_rtr1, py_rtr2):
        print "\n***"
        for the_oid in (NAME, DESCR):
            snmp_data = snmp_helper.snmp_get_oid(device, oid=the_oid)
            output = snmp_helper.snmp_extract(snmp_data)

            print output
        print "***"

if __name__ == "__main__":
    main()

