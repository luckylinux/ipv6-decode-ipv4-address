#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import Libraries
import ipaddress
import argparse

# Main
if __name__ == "__main__":
   # Declare Arguments Parser
   parser = argparse.ArgumentParser(description='Pass Arguments to Script.')

   parser.add_argument('-i', '--ip', default="none",
                   help='IPv6 Address Containing the IPv4 Representation')

   #parser.add_argument('-p', '--nat46-prefix', default="64:ff9b:1::",
   #                help='NAT46 Prefix Address for the IPv4 Representation')

   #parser.add_argument('-n', '--nat46-netmask', default="96",
   #                help='NAT46 Netmask for the IPv4 Representation')

   # Parse Arguments
   args = parser.parse_args()

   # No checks for now, just get the Value
   # Get Value
   if args.ip != "none":
      ip = args.ip
   #else
   #   exit
   #

   v6 = ipaddress.IPv6Address(ip)
   print(v6)
   last4bytes = v6.packed[-4:]
   print(last4bytes)
   v4 = ipaddress.IPv4Address(last4bytes)
   print(v4)
