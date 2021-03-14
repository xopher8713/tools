#!/usr/bin/env python

import sys
import dns.resolver
import dns.exception

def dnsquery(hostname):

    resolve = dns.resolver.Resolver()
    resolve.nameservers = ['1.1.1.1', '1.0.0.1']
    try:
        response = resolve.resolve(hostname)
        for rdata in response:
            ipaddress = rdata.address
            return ipaddress
    except dns.exception.DNSException:
        print("Unable to resolve DNS, no entries found.")
    except Exception as e:
        print("Unable to resolve DNS for {} due to the following error, {}.".format(hostname, e))

if __name__ in '__main__':
    try:
        hostname = sys.argv[1]
        ipaddress = dnsquery(hostname)
        print("IP address {} returned for hostname {}.".format(ipaddress, hostname))
    except Exception as e:
        print("Unable to resolve DNS for {} due to the following error, {}.".format(hostname, e))
    except KeyboardInterrupt:
        print("\nProcess interupted by user. Exiting...")
