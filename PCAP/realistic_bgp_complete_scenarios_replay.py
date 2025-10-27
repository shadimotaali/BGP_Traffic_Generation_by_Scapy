#!/usr/bin/env python3
"""Replay script generated 2025-10-26T13:59:45ZZ"""
import argparse
import time
from scapy.all import *

pkt1 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=58079,
        dport=179,
        seq=4925,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt2 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=58079,
        seq=4197,
        ack=4926,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt3 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=58079,
        dport=179,
        seq=4926,
        ack=4198,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt4 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=58079,
        dport=179,
        seq=4926,
        ack=4198,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt5 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=58079,
        seq=4198,
        ack=4990,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=4002,
        hold_time=180,
        bgp_id='100.105.160.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=4002 |>)
        ]
    )
)

pkt6 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=58079,
        dport=179,
        seq=4990,
        ack=4262,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt7 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=58079,
        seq=4262,
        ack=5009,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt8 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=58079,
        dport=179,
        seq=5009,
        ack=4281,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(16, '203.112.0.0'))
        ]
    )
)

pkt9 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=58079,
        seq=4281,
        ack=5074,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt10 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:d8:9::1',
        dst='2001:db8:d8:a::2'
    )/
    TCP(
        sport=58080,
        dport=179,
        seq=2496,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt11 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:d8:a::2',
        dst='2001:db8:d8:9::1'
    )/
    TCP(
        sport=179,
        dport=58080,
        seq=6424,
        ack=2497,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt12 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:d8:9::1',
        dst='2001:db8:d8:a::2'
    )/
    TCP(
        sport=58080,
        dport=179,
        seq=2497,
        ack=6425,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt13 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:d8:9::1',
        dst='2001:db8:d8:a::2'
    )/
    TCP(
        sport=58080,
        dport=179,
        seq=2497,
        ack=6425,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt14 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:d8:a::2',
        dst='2001:db8:d8:9::1'
    )/
    TCP(
        sport=179,
        dport=58080,
        seq=6425,
        ack=2561,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=4002,
        hold_time=180,
        bgp_id='100.105.160.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=4002 |>)
        ]
    )
)

pkt15 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:d8:9::1',
        dst='2001:db8:d8:a::2'
    )/
    TCP(
        sport=58080,
        dport=179,
        seq=2561,
        ack=6489,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt16 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:d8:a::2',
        dst='2001:db8:d8:9::1'
    )/
    TCP(
        sport=179,
        dport=58080,
        seq=6489,
        ack=2580,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt17 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:d8:9::1',
        dst='2001:db8:d8:a::2'
    )/
    TCP(
        sport=58080,
        dport=179,
        seq=2580,
        ack=6508,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:d8:9::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8::/64 |>] |>)
        ]
    )
)

pkt18 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:d8:a::2',
        dst='2001:db8:d8:9::1'
    )/
    TCP(
        sport=179,
        dport=58080,
        seq=6508,
        ack=2668,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt19 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.69.92.209',
        dst='10.69.92.210'
    )/
    TCP(
        sport=47183,
        dport=179,
        seq=1820,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt20 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.69.92.210',
        dst='10.69.92.209'
    )/
    TCP(
        sport=179,
        dport=47183,
        seq=1816,
        ack=1821,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt21 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.69.92.209',
        dst='10.69.92.210'
    )/
    TCP(
        sport=47183,
        dport=179,
        seq=1821,
        ack=1817,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt22 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.69.92.209',
        dst='10.69.92.210'
    )/
    TCP(
        sport=47183,
        dport=179,
        seq=1821,
        ack=1817,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt23 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.69.92.210',
        dst='10.69.92.209'
    )/
    TCP(
        sport=179,
        dport=47183,
        seq=1817,
        ack=1885,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt24 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.69.92.209',
        dst='10.69.92.210'
    )/
    TCP(
        sport=47183,
        dport=179,
        seq=1885,
        ack=1881,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt25 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.69.92.210',
        dst='10.69.92.209'
    )/
    TCP(
        sport=179,
        dport=47183,
        seq=1881,
        ack=1904,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt26 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.69.92.209',
        dst='10.69.92.210'
    )/
    TCP(
        sport=47183,
        dport=179,
        seq=1904,
        ack=1900,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.69.92.209 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(16, '203.112.0.0'))
        ]
    )
)

pkt27 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.69.92.210',
        dst='10.69.92.209'
    )/
    TCP(
        sport=179,
        dport=47183,
        seq=1900,
        ack=1969,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt28 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:5c:d1::1',
        dst='2001:db8:5c:d2::2'
    )/
    TCP(
        sport=47184,
        dport=179,
        seq=2952,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt29 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:5c:d2::2',
        dst='2001:db8:5c:d1::1'
    )/
    TCP(
        sport=179,
        dport=47184,
        seq=6584,
        ack=2953,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt30 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:5c:d1::1',
        dst='2001:db8:5c:d2::2'
    )/
    TCP(
        sport=47184,
        dport=179,
        seq=2953,
        ack=6585,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt31 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:5c:d1::1',
        dst='2001:db8:5c:d2::2'
    )/
    TCP(
        sport=47184,
        dport=179,
        seq=2953,
        ack=6585,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt32 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:5c:d2::2',
        dst='2001:db8:5c:d1::1'
    )/
    TCP(
        sport=179,
        dport=47184,
        seq=6585,
        ack=3017,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt33 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:5c:d1::1',
        dst='2001:db8:5c:d2::2'
    )/
    TCP(
        sport=47184,
        dport=179,
        seq=3017,
        ack=6649,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt34 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:5c:d2::2',
        dst='2001:db8:5c:d1::1'
    )/
    TCP(
        sport=179,
        dport=47184,
        seq=6649,
        ack=3036,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt35 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:5c:d1::1',
        dst='2001:db8:5c:d2::2'
    )/
    TCP(
        sport=47184,
        dport=179,
        seq=3036,
        ack=6668,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:5c:d1::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8::/64 |>] |>)
        ]
    )
)

pkt36 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:5c:d2::2',
        dst='2001:db8:5c:d1::1'
    )/
    TCP(
        sport=179,
        dport=47184,
        seq=6668,
        ack=3124,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt37 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.208.150.209',
        dst='10.208.150.210'
    )/
    TCP(
        sport=34702,
        dport=179,
        seq=1220,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt38 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.208.150.210',
        dst='10.208.150.209'
    )/
    TCP(
        sport=179,
        dport=34702,
        seq=4330,
        ack=1221,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt39 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.208.150.209',
        dst='10.208.150.210'
    )/
    TCP(
        sport=34702,
        dport=179,
        seq=1221,
        ack=4331,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt40 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.208.150.209',
        dst='10.208.150.210'
    )/
    TCP(
        sport=34702,
        dport=179,
        seq=1221,
        ack=4331,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt41 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.208.150.210',
        dst='10.208.150.209'
    )/
    TCP(
        sport=179,
        dport=34702,
        seq=4331,
        ack=1285,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=18497,
        hold_time=180,
        bgp_id='172.18.35.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=18497 |>)
        ]
    )
)

pkt42 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.208.150.209',
        dst='10.208.150.210'
    )/
    TCP(
        sport=34702,
        dport=179,
        seq=1285,
        ack=4395,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt43 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.208.150.210',
        dst='10.208.150.209'
    )/
    TCP(
        sport=179,
        dport=34702,
        seq=4395,
        ack=1304,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt44 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.208.150.209',
        dst='10.208.150.210'
    )/
    TCP(
        sport=34702,
        dport=179,
        seq=1304,
        ack=4414,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.208.150.209 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(16, '203.112.0.0'))
        ]
    )
)

pkt45 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.208.150.210',
        dst='10.208.150.209'
    )/
    TCP(
        sport=179,
        dport=34702,
        seq=4414,
        ack=1369,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt46 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:96:d1::1',
        dst='2001:db8:96:d2::2'
    )/
    TCP(
        sport=34703,
        dport=179,
        seq=2127,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt47 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:96:d2::2',
        dst='2001:db8:96:d1::1'
    )/
    TCP(
        sport=179,
        dport=34703,
        seq=6649,
        ack=2128,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt48 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:96:d1::1',
        dst='2001:db8:96:d2::2'
    )/
    TCP(
        sport=34703,
        dport=179,
        seq=2128,
        ack=6650,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt49 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:96:d1::1',
        dst='2001:db8:96:d2::2'
    )/
    TCP(
        sport=34703,
        dport=179,
        seq=2128,
        ack=6650,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt50 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:96:d2::2',
        dst='2001:db8:96:d1::1'
    )/
    TCP(
        sport=179,
        dport=34703,
        seq=6650,
        ack=2192,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=18497,
        hold_time=180,
        bgp_id='172.18.35.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=18497 |>)
        ]
    )
)

pkt51 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:96:d1::1',
        dst='2001:db8:96:d2::2'
    )/
    TCP(
        sport=34703,
        dport=179,
        seq=2192,
        ack=6714,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt52 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:96:d2::2',
        dst='2001:db8:96:d1::1'
    )/
    TCP(
        sport=179,
        dport=34703,
        seq=6714,
        ack=2211,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt53 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:96:d1::1',
        dst='2001:db8:96:d2::2'
    )/
    TCP(
        sport=34703,
        dport=179,
        seq=2211,
        ack=6733,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:96:d1::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8::/64 |>] |>)
        ]
    )
)

pkt54 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:96:d2::2',
        dst='2001:db8:96:d1::1'
    )/
    TCP(
        sport=179,
        dport=34703,
        seq=6733,
        ack=2299,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt55 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.146.61.193',
        dst='10.146.61.194'
    )/
    TCP(
        sport=31120,
        dport=179,
        seq=8399,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt56 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.146.61.194',
        dst='10.146.61.193'
    )/
    TCP(
        sport=179,
        dport=31120,
        seq=4950,
        ack=8400,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt57 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.146.61.193',
        dst='10.146.61.194'
    )/
    TCP(
        sport=31120,
        dport=179,
        seq=8400,
        ack=4951,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt58 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.146.61.193',
        dst='10.146.61.194'
    )/
    TCP(
        sport=31120,
        dport=179,
        seq=8400,
        ack=4951,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt59 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.146.61.194',
        dst='10.146.61.193'
    )/
    TCP(
        sport=179,
        dport=31120,
        seq=4951,
        ack=8464,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt60 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.146.61.193',
        dst='10.146.61.194'
    )/
    TCP(
        sport=31120,
        dport=179,
        seq=8464,
        ack=5015,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt61 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.146.61.194',
        dst='10.146.61.193'
    )/
    TCP(
        sport=179,
        dport=31120,
        seq=5015,
        ack=8483,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt62 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.146.61.193',
        dst='10.146.61.194'
    )/
    TCP(
        sport=31120,
        dport=179,
        seq=8483,
        ack=5034,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.146.61.193 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(16, '203.112.0.0'))
        ]
    )
)

pkt63 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.146.61.194',
        dst='10.146.61.193'
    )/
    TCP(
        sport=179,
        dport=31120,
        seq=5034,
        ack=8548,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt64 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:3d:c1::1',
        dst='2001:db8:3d:c2::2'
    )/
    TCP(
        sport=31121,
        dport=179,
        seq=2177,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt65 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:3d:c2::2',
        dst='2001:db8:3d:c1::1'
    )/
    TCP(
        sport=179,
        dport=31121,
        seq=6961,
        ack=2178,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt66 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:3d:c1::1',
        dst='2001:db8:3d:c2::2'
    )/
    TCP(
        sport=31121,
        dport=179,
        seq=2178,
        ack=6962,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt67 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:3d:c1::1',
        dst='2001:db8:3d:c2::2'
    )/
    TCP(
        sport=31121,
        dport=179,
        seq=2178,
        ack=6962,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt68 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:3d:c2::2',
        dst='2001:db8:3d:c1::1'
    )/
    TCP(
        sport=179,
        dport=31121,
        seq=6962,
        ack=2242,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt69 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:3d:c1::1',
        dst='2001:db8:3d:c2::2'
    )/
    TCP(
        sport=31121,
        dport=179,
        seq=2242,
        ack=7026,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt70 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:3d:c2::2',
        dst='2001:db8:3d:c1::1'
    )/
    TCP(
        sport=179,
        dport=31121,
        seq=7026,
        ack=2261,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt71 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:3d:c1::1',
        dst='2001:db8:3d:c2::2'
    )/
    TCP(
        sport=31121,
        dport=179,
        seq=2261,
        ack=7045,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:3d:c1::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8::/64 |>] |>)
        ]
    )
)

pkt72 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:3d:c2::2',
        dst='2001:db8:3d:c1::1'
    )/
    TCP(
        sport=179,
        dport=31121,
        seq=7045,
        ack=2349,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt73 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.109.42.73',
        dst='10.109.42.74'
    )/
    TCP(
        sport=39312,
        dport=179,
        seq=5469,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt74 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.109.42.74',
        dst='10.109.42.73'
    )/
    TCP(
        sport=179,
        dport=39312,
        seq=1843,
        ack=5470,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt75 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.109.42.73',
        dst='10.109.42.74'
    )/
    TCP(
        sport=39312,
        dport=179,
        seq=5470,
        ack=1844,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt76 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.109.42.73',
        dst='10.109.42.74'
    )/
    TCP(
        sport=39312,
        dport=179,
        seq=5470,
        ack=1844,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt77 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.109.42.74',
        dst='10.109.42.73'
    )/
    TCP(
        sport=179,
        dport=39312,
        seq=1844,
        ack=5534,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=56054,
        hold_time=180,
        bgp_id='10.130.43.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=56054 |>)
        ]
    )
)

pkt78 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.109.42.73',
        dst='10.109.42.74'
    )/
    TCP(
        sport=39312,
        dport=179,
        seq=5534,
        ack=1908,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt79 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.109.42.74',
        dst='10.109.42.73'
    )/
    TCP(
        sport=179,
        dport=39312,
        seq=1908,
        ack=5553,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt80 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.109.42.73',
        dst='10.109.42.74'
    )/
    TCP(
        sport=39312,
        dport=179,
        seq=5553,
        ack=1927,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.109.42.73 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(16, '203.112.0.0'))
        ]
    )
)

pkt81 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.109.42.74',
        dst='10.109.42.73'
    )/
    TCP(
        sport=179,
        dport=39312,
        seq=1927,
        ack=5618,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt82 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:2a:49::1',
        dst='2001:db8:2a:4a::2'
    )/
    TCP(
        sport=39313,
        dport=179,
        seq=2070,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt83 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:2a:4a::2',
        dst='2001:db8:2a:49::1'
    )/
    TCP(
        sport=179,
        dport=39313,
        seq=6601,
        ack=2071,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt84 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:2a:49::1',
        dst='2001:db8:2a:4a::2'
    )/
    TCP(
        sport=39313,
        dport=179,
        seq=2071,
        ack=6602,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt85 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:2a:49::1',
        dst='2001:db8:2a:4a::2'
    )/
    TCP(
        sport=39313,
        dport=179,
        seq=2071,
        ack=6602,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt86 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:2a:4a::2',
        dst='2001:db8:2a:49::1'
    )/
    TCP(
        sport=179,
        dport=39313,
        seq=6602,
        ack=2135,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=56054,
        hold_time=180,
        bgp_id='10.130.43.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=56054 |>)
        ]
    )
)

pkt87 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:2a:49::1',
        dst='2001:db8:2a:4a::2'
    )/
    TCP(
        sport=39313,
        dport=179,
        seq=2135,
        ack=6666,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt88 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:2a:4a::2',
        dst='2001:db8:2a:49::1'
    )/
    TCP(
        sport=179,
        dport=39313,
        seq=6666,
        ack=2154,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt89 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:2a:49::1',
        dst='2001:db8:2a:4a::2'
    )/
    TCP(
        sport=39313,
        dport=179,
        seq=2154,
        ack=6685,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:2a:49::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8::/64 |>] |>)
        ]
    )
)

pkt90 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:2a:4a::2',
        dst='2001:db8:2a:49::1'
    )/
    TCP(
        sport=179,
        dport=39313,
        seq=6685,
        ack=2242,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt91 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=51019,
        dport=179,
        seq=5444,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt92 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=179,
        dport=51019,
        seq=2420,
        ack=5445,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt93 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=51019,
        dport=179,
        seq=5445,
        ack=2421,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt94 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=51019,
        dport=179,
        seq=5445,
        ack=2421,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=4002,
        hold_time=180,
        bgp_id='100.105.160.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=4002 |>)
        ]
    )
)

pkt95 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=179,
        dport=51019,
        seq=2421,
        ack=5509,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt96 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=51019,
        dport=179,
        seq=5509,
        ack=2485,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt97 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=179,
        dport=51019,
        seq=2485,
        ack=5528,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt98 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=51019,
        dport=179,
        seq=5528,
        ack=2504,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[4002] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.10 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(16, '203.159.0.0'))
        ]
    )
)

pkt99 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=179,
        dport=51019,
        seq=2504,
        ack=5593,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt100 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:d8:a::1',
        dst='2001:db8:d8:9::2'
    )/
    TCP(
        sport=51020,
        dport=179,
        seq=2358,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt101 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:d8:9::2',
        dst='2001:db8:d8:a::1'
    )/
    TCP(
        sport=179,
        dport=51020,
        seq=6974,
        ack=2359,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt102 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:d8:a::1',
        dst='2001:db8:d8:9::2'
    )/
    TCP(
        sport=51020,
        dport=179,
        seq=2359,
        ack=6975,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt103 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:d8:a::1',
        dst='2001:db8:d8:9::2'
    )/
    TCP(
        sport=51020,
        dport=179,
        seq=2359,
        ack=6975,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=4002,
        hold_time=180,
        bgp_id='100.105.160.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=4002 |>)
        ]
    )
)

pkt104 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:d8:9::2',
        dst='2001:db8:d8:a::1'
    )/
    TCP(
        sport=179,
        dport=51020,
        seq=6975,
        ack=2423,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt105 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:d8:a::1',
        dst='2001:db8:d8:9::2'
    )/
    TCP(
        sport=51020,
        dport=179,
        seq=2423,
        ack=7039,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt106 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:d8:9::2',
        dst='2001:db8:d8:a::1'
    )/
    TCP(
        sport=179,
        dport=51020,
        seq=7039,
        ack=2442,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt107 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:d8:a::1',
        dst='2001:db8:d8:9::2'
    )/
    TCP(
        sport=51020,
        dport=179,
        seq=2442,
        ack=7058,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[4002] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:d8:a::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8::/64 |>] |>)
        ]
    )
)

pkt108 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:d8:9::2',
        dst='2001:db8:d8:a::1'
    )/
    TCP(
        sport=179,
        dport=51020,
        seq=7058,
        ack=2530,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt109 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.156.131.41',
        dst='10.156.131.42'
    )/
    TCP(
        sport=60434,
        dport=179,
        seq=9466,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt110 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.156.131.42',
        dst='10.156.131.41'
    )/
    TCP(
        sport=179,
        dport=60434,
        seq=9676,
        ack=9467,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt111 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.156.131.41',
        dst='10.156.131.42'
    )/
    TCP(
        sport=60434,
        dport=179,
        seq=9467,
        ack=9677,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt112 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.156.131.41',
        dst='10.156.131.42'
    )/
    TCP(
        sport=60434,
        dport=179,
        seq=9467,
        ack=9677,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=4002,
        hold_time=180,
        bgp_id='100.105.160.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=4002 |>)
        ]
    )
)

pkt113 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.156.131.42',
        dst='10.156.131.41'
    )/
    TCP(
        sport=179,
        dport=60434,
        seq=9677,
        ack=9531,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt114 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.156.131.41',
        dst='10.156.131.42'
    )/
    TCP(
        sport=60434,
        dport=179,
        seq=9531,
        ack=9741,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt115 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.156.131.42',
        dst='10.156.131.41'
    )/
    TCP(
        sport=179,
        dport=60434,
        seq=9741,
        ack=9550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt116 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.156.131.41',
        dst='10.156.131.42'
    )/
    TCP(
        sport=60434,
        dport=179,
        seq=9550,
        ack=9760,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[4002] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.156.131.41 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(16, '203.159.0.0'))
        ]
    )
)

pkt117 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.156.131.42',
        dst='10.156.131.41'
    )/
    TCP(
        sport=179,
        dport=60434,
        seq=9760,
        ack=9615,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt118 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:83:29::1',
        dst='2001:db8:83:2a::2'
    )/
    TCP(
        sport=60435,
        dport=179,
        seq=2791,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt119 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:83:2a::2',
        dst='2001:db8:83:29::1'
    )/
    TCP(
        sport=179,
        dport=60435,
        seq=6545,
        ack=2792,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt120 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:83:29::1',
        dst='2001:db8:83:2a::2'
    )/
    TCP(
        sport=60435,
        dport=179,
        seq=2792,
        ack=6546,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt121 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:83:29::1',
        dst='2001:db8:83:2a::2'
    )/
    TCP(
        sport=60435,
        dport=179,
        seq=2792,
        ack=6546,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=4002,
        hold_time=180,
        bgp_id='100.105.160.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=4002 |>)
        ]
    )
)

pkt122 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:83:2a::2',
        dst='2001:db8:83:29::1'
    )/
    TCP(
        sport=179,
        dport=60435,
        seq=6546,
        ack=2856,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt123 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:83:29::1',
        dst='2001:db8:83:2a::2'
    )/
    TCP(
        sport=60435,
        dport=179,
        seq=2856,
        ack=6610,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt124 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:83:2a::2',
        dst='2001:db8:83:29::1'
    )/
    TCP(
        sport=179,
        dport=60435,
        seq=6610,
        ack=2875,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt125 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:83:29::1',
        dst='2001:db8:83:2a::2'
    )/
    TCP(
        sport=60435,
        dport=179,
        seq=2875,
        ack=6629,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[4002] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:83:29::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8::/64 |>] |>)
        ]
    )
)

pkt126 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:83:2a::2',
        dst='2001:db8:83:29::1'
    )/
    TCP(
        sport=179,
        dport=60435,
        seq=6629,
        ack=2963,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt127 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.220.96.249',
        dst='10.220.96.250'
    )/
    TCP(
        sport=40911,
        dport=179,
        seq=4233,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt128 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.220.96.250',
        dst='10.220.96.249'
    )/
    TCP(
        sport=179,
        dport=40911,
        seq=1249,
        ack=4234,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt129 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.220.96.249',
        dst='10.220.96.250'
    )/
    TCP(
        sport=40911,
        dport=179,
        seq=4234,
        ack=1250,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt130 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.220.96.249',
        dst='10.220.96.250'
    )/
    TCP(
        sport=40911,
        dport=179,
        seq=4234,
        ack=1250,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=4002,
        hold_time=180,
        bgp_id='100.105.160.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=4002 |>)
        ]
    )
)

pkt131 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.220.96.250',
        dst='10.220.96.249'
    )/
    TCP(
        sport=179,
        dport=40911,
        seq=1250,
        ack=4298,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt132 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.220.96.249',
        dst='10.220.96.250'
    )/
    TCP(
        sport=40911,
        dport=179,
        seq=4298,
        ack=1314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt133 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.220.96.250',
        dst='10.220.96.249'
    )/
    TCP(
        sport=179,
        dport=40911,
        seq=1314,
        ack=4317,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt134 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.220.96.249',
        dst='10.220.96.250'
    )/
    TCP(
        sport=40911,
        dport=179,
        seq=4317,
        ack=1333,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[4002] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.220.96.249 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(16, '203.159.0.0'))
        ]
    )
)

pkt135 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.220.96.250',
        dst='10.220.96.249'
    )/
    TCP(
        sport=179,
        dport=40911,
        seq=1333,
        ack=4382,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt136 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:60:f9::1',
        dst='2001:db8:60:fa::2'
    )/
    TCP(
        sport=40912,
        dport=179,
        seq=2960,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt137 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:60:fa::2',
        dst='2001:db8:60:f9::1'
    )/
    TCP(
        sport=179,
        dport=40912,
        seq=6791,
        ack=2961,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt138 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:60:f9::1',
        dst='2001:db8:60:fa::2'
    )/
    TCP(
        sport=40912,
        dport=179,
        seq=2961,
        ack=6792,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt139 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:60:f9::1',
        dst='2001:db8:60:fa::2'
    )/
    TCP(
        sport=40912,
        dport=179,
        seq=2961,
        ack=6792,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=4002,
        hold_time=180,
        bgp_id='100.105.160.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=4002 |>)
        ]
    )
)

pkt140 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:60:fa::2',
        dst='2001:db8:60:f9::1'
    )/
    TCP(
        sport=179,
        dport=40912,
        seq=6792,
        ack=3025,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt141 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:60:f9::1',
        dst='2001:db8:60:fa::2'
    )/
    TCP(
        sport=40912,
        dport=179,
        seq=3025,
        ack=6856,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt142 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:60:fa::2',
        dst='2001:db8:60:f9::1'
    )/
    TCP(
        sport=179,
        dport=40912,
        seq=6856,
        ack=3044,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt143 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:60:f9::1',
        dst='2001:db8:60:fa::2'
    )/
    TCP(
        sport=40912,
        dport=179,
        seq=3044,
        ack=6875,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[4002] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:60:f9::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8::/64 |>] |>)
        ]
    )
)

pkt144 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:60:fa::2',
        dst='2001:db8:60:f9::1'
    )/
    TCP(
        sport=179,
        dport=40912,
        seq=6875,
        ack=3132,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt145 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.156.131.42',
        dst='10.156.131.41'
    )/
    TCP(
        sport=57128,
        dport=179,
        seq=9634,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt146 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.156.131.41',
        dst='10.156.131.42'
    )/
    TCP(
        sport=179,
        dport=57128,
        seq=5751,
        ack=9635,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt147 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.156.131.42',
        dst='10.156.131.41'
    )/
    TCP(
        sport=57128,
        dport=179,
        seq=9635,
        ack=5752,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt148 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.156.131.42',
        dst='10.156.131.41'
    )/
    TCP(
        sport=57128,
        dport=179,
        seq=9635,
        ack=5752,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt149 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.156.131.41',
        dst='10.156.131.42'
    )/
    TCP(
        sport=179,
        dport=57128,
        seq=5752,
        ack=9699,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=4002,
        hold_time=180,
        bgp_id='100.105.160.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=4002 |>)
        ]
    )
)

pkt150 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.156.131.42',
        dst='10.156.131.41'
    )/
    TCP(
        sport=57128,
        dport=179,
        seq=9699,
        ack=5816,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt151 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.156.131.41',
        dst='10.156.131.42'
    )/
    TCP(
        sport=179,
        dport=57128,
        seq=5816,
        ack=9718,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt152 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.156.131.42',
        dst='10.156.131.41'
    )/
    TCP(
        sport=57128,
        dport=179,
        seq=9718,
        ack=5835,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[14710] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.156.131.42 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.84.0'))
        ]
    )
)

pkt153 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.156.131.41',
        dst='10.156.131.42'
    )/
    TCP(
        sport=179,
        dport=57128,
        seq=5835,
        ack=9784,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt154 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.156.131.42',
        dst='10.156.131.41'
    )/
    TCP(
        sport=57128,
        dport=179,
        seq=9784,
        ack=5835,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[14710] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.156.131.42 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.30.0'))
        ]
    )
)

pkt155 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.156.131.41',
        dst='10.156.131.42'
    )/
    TCP(
        sport=179,
        dport=57128,
        seq=5835,
        ack=9850,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt156 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:83:2a::1',
        dst='2001:db8:83:29::2'
    )/
    TCP(
        sport=57129,
        dport=179,
        seq=2900,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt157 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:83:29::2',
        dst='2001:db8:83:2a::1'
    )/
    TCP(
        sport=179,
        dport=57129,
        seq=6558,
        ack=2901,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt158 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:83:2a::1',
        dst='2001:db8:83:29::2'
    )/
    TCP(
        sport=57129,
        dport=179,
        seq=2901,
        ack=6559,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt159 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:83:2a::1',
        dst='2001:db8:83:29::2'
    )/
    TCP(
        sport=57129,
        dport=179,
        seq=2901,
        ack=6559,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt160 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:83:29::2',
        dst='2001:db8:83:2a::1'
    )/
    TCP(
        sport=179,
        dport=57129,
        seq=6559,
        ack=2965,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=4002,
        hold_time=180,
        bgp_id='100.105.160.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=4002 |>)
        ]
    )
)

pkt161 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:83:2a::1',
        dst='2001:db8:83:29::2'
    )/
    TCP(
        sport=57129,
        dport=179,
        seq=2965,
        ack=6623,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt162 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:83:29::2',
        dst='2001:db8:83:2a::1'
    )/
    TCP(
        sport=179,
        dport=57129,
        seq=6623,
        ack=2984,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt163 = (
    Ether()/
    IPv6(
        plen=117,
        nh=6,
        src='2001:db8:83:2a::1',
        dst='2001:db8:83:29::2'
    )/
    TCP(
        sport=57129,
        dport=179,
        seq=2984,
        ack=6642,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=97,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[14710] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=39, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:83:2a::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:54::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:1e::/64 |>] |>)
        ]
    )
)

pkt164 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:83:29::2',
        dst='2001:db8:83:2a::1'
    )/
    TCP(
        sport=179,
        dport=57129,
        seq=6642,
        ack=3081,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt165 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.69.92.210',
        dst='10.69.92.209'
    )/
    TCP(
        sport=38037,
        dport=179,
        seq=8248,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt166 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.69.92.209',
        dst='10.69.92.210'
    )/
    TCP(
        sport=179,
        dport=38037,
        seq=4160,
        ack=8249,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt167 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.69.92.210',
        dst='10.69.92.209'
    )/
    TCP(
        sport=38037,
        dport=179,
        seq=8249,
        ack=4161,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt168 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.69.92.210',
        dst='10.69.92.209'
    )/
    TCP(
        sport=38037,
        dport=179,
        seq=8249,
        ack=4161,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt169 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.69.92.209',
        dst='10.69.92.210'
    )/
    TCP(
        sport=179,
        dport=38037,
        seq=4161,
        ack=8313,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt170 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.69.92.210',
        dst='10.69.92.209'
    )/
    TCP(
        sport=38037,
        dport=179,
        seq=8313,
        ack=4225,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt171 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.69.92.209',
        dst='10.69.92.210'
    )/
    TCP(
        sport=179,
        dport=38037,
        seq=4225,
        ack=8332,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt172 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.69.92.210',
        dst='10.69.92.209'
    )/
    TCP(
        sport=38037,
        dport=179,
        seq=8332,
        ack=4244,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[14710] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.69.92.210 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.84.0'))
        ]
    )
)

pkt173 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.69.92.209',
        dst='10.69.92.210'
    )/
    TCP(
        sport=179,
        dport=38037,
        seq=4244,
        ack=8398,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt174 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.69.92.210',
        dst='10.69.92.209'
    )/
    TCP(
        sport=38037,
        dport=179,
        seq=8398,
        ack=4244,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[14710] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.69.92.210 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.30.0'))
        ]
    )
)

pkt175 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.69.92.209',
        dst='10.69.92.210'
    )/
    TCP(
        sport=179,
        dport=38037,
        seq=4244,
        ack=8464,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt176 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:5c:d2::1',
        dst='2001:db8:5c:d1::2'
    )/
    TCP(
        sport=38038,
        dport=179,
        seq=2280,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt177 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:5c:d1::2',
        dst='2001:db8:5c:d2::1'
    )/
    TCP(
        sport=179,
        dport=38038,
        seq=6048,
        ack=2281,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt178 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:5c:d2::1',
        dst='2001:db8:5c:d1::2'
    )/
    TCP(
        sport=38038,
        dport=179,
        seq=2281,
        ack=6049,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt179 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:5c:d2::1',
        dst='2001:db8:5c:d1::2'
    )/
    TCP(
        sport=38038,
        dport=179,
        seq=2281,
        ack=6049,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt180 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:5c:d1::2',
        dst='2001:db8:5c:d2::1'
    )/
    TCP(
        sport=179,
        dport=38038,
        seq=6049,
        ack=2345,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt181 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:5c:d2::1',
        dst='2001:db8:5c:d1::2'
    )/
    TCP(
        sport=38038,
        dport=179,
        seq=2345,
        ack=6113,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt182 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:5c:d1::2',
        dst='2001:db8:5c:d2::1'
    )/
    TCP(
        sport=179,
        dport=38038,
        seq=6113,
        ack=2364,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt183 = (
    Ether()/
    IPv6(
        plen=117,
        nh=6,
        src='2001:db8:5c:d2::1',
        dst='2001:db8:5c:d1::2'
    )/
    TCP(
        sport=38038,
        dport=179,
        seq=2364,
        ack=6132,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=97,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[14710] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=39, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:5c:d2::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:54::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:1e::/64 |>] |>)
        ]
    )
)

pkt184 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:5c:d1::2',
        dst='2001:db8:5c:d2::1'
    )/
    TCP(
        sport=179,
        dport=38038,
        seq=6132,
        ack=2461,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt185 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.22.155.249',
        dst='10.22.155.250'
    )/
    TCP(
        sport=54727,
        dport=179,
        seq=6165,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt186 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.22.155.250',
        dst='10.22.155.249'
    )/
    TCP(
        sport=179,
        dport=54727,
        seq=3273,
        ack=6166,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt187 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.22.155.249',
        dst='10.22.155.250'
    )/
    TCP(
        sport=54727,
        dport=179,
        seq=6166,
        ack=3274,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt188 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.22.155.249',
        dst='10.22.155.250'
    )/
    TCP(
        sport=54727,
        dport=179,
        seq=6166,
        ack=3274,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt189 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.22.155.250',
        dst='10.22.155.249'
    )/
    TCP(
        sport=179,
        dport=54727,
        seq=3274,
        ack=6230,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=35152,
        hold_time=180,
        bgp_id='192.168.158.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=35152 |>)
        ]
    )
)

pkt190 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.22.155.249',
        dst='10.22.155.250'
    )/
    TCP(
        sport=54727,
        dport=179,
        seq=6230,
        ack=3338,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt191 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.22.155.250',
        dst='10.22.155.249'
    )/
    TCP(
        sport=179,
        dport=54727,
        seq=3338,
        ack=6249,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt192 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.22.155.249',
        dst='10.22.155.250'
    )/
    TCP(
        sport=54727,
        dport=179,
        seq=6249,
        ack=3357,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[14710] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.22.155.249 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.84.0'))
        ]
    )
)

pkt193 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.22.155.250',
        dst='10.22.155.249'
    )/
    TCP(
        sport=179,
        dport=54727,
        seq=3357,
        ack=6315,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt194 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.22.155.249',
        dst='10.22.155.250'
    )/
    TCP(
        sport=54727,
        dport=179,
        seq=6315,
        ack=3357,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[14710] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.22.155.249 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.30.0'))
        ]
    )
)

pkt195 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.22.155.250',
        dst='10.22.155.249'
    )/
    TCP(
        sport=179,
        dport=54727,
        seq=3357,
        ack=6381,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt196 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:9b:f9::1',
        dst='2001:db8:9b:fa::2'
    )/
    TCP(
        sport=54728,
        dport=179,
        seq=2468,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt197 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:9b:fa::2',
        dst='2001:db8:9b:f9::1'
    )/
    TCP(
        sport=179,
        dport=54728,
        seq=6297,
        ack=2469,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt198 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:9b:f9::1',
        dst='2001:db8:9b:fa::2'
    )/
    TCP(
        sport=54728,
        dport=179,
        seq=2469,
        ack=6298,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt199 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:9b:f9::1',
        dst='2001:db8:9b:fa::2'
    )/
    TCP(
        sport=54728,
        dport=179,
        seq=2469,
        ack=6298,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt200 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:9b:fa::2',
        dst='2001:db8:9b:f9::1'
    )/
    TCP(
        sport=179,
        dport=54728,
        seq=6298,
        ack=2533,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=35152,
        hold_time=180,
        bgp_id='192.168.158.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=35152 |>)
        ]
    )
)

pkt201 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:9b:f9::1',
        dst='2001:db8:9b:fa::2'
    )/
    TCP(
        sport=54728,
        dport=179,
        seq=2533,
        ack=6362,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt202 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:9b:fa::2',
        dst='2001:db8:9b:f9::1'
    )/
    TCP(
        sport=179,
        dport=54728,
        seq=6362,
        ack=2552,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt203 = (
    Ether()/
    IPv6(
        plen=117,
        nh=6,
        src='2001:db8:9b:f9::1',
        dst='2001:db8:9b:fa::2'
    )/
    TCP(
        sport=54728,
        dport=179,
        seq=2552,
        ack=6381,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=97,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[14710] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=39, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:9b:f9::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:54::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:1e::/64 |>] |>)
        ]
    )
)

pkt204 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:9b:fa::2',
        dst='2001:db8:9b:f9::1'
    )/
    TCP(
        sport=179,
        dport=54728,
        seq=6381,
        ack=2649,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt205 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.200.191.185',
        dst='10.200.191.186'
    )/
    TCP(
        sport=40090,
        dport=179,
        seq=1952,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt206 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.200.191.186',
        dst='10.200.191.185'
    )/
    TCP(
        sport=179,
        dport=40090,
        seq=6191,
        ack=1953,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt207 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.200.191.185',
        dst='10.200.191.186'
    )/
    TCP(
        sport=40090,
        dport=179,
        seq=1953,
        ack=6192,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt208 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.200.191.185',
        dst='10.200.191.186'
    )/
    TCP(
        sport=40090,
        dport=179,
        seq=1953,
        ack=6192,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt209 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.200.191.186',
        dst='10.200.191.185'
    )/
    TCP(
        sport=179,
        dport=40090,
        seq=6192,
        ack=2017,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=41273,
        hold_time=180,
        bgp_id='192.168.78.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=41273 |>)
        ]
    )
)

pkt210 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.200.191.185',
        dst='10.200.191.186'
    )/
    TCP(
        sport=40090,
        dport=179,
        seq=2017,
        ack=6256,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt211 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.200.191.186',
        dst='10.200.191.185'
    )/
    TCP(
        sport=179,
        dport=40090,
        seq=6256,
        ack=2036,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt212 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.200.191.185',
        dst='10.200.191.186'
    )/
    TCP(
        sport=40090,
        dport=179,
        seq=2036,
        ack=6275,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[14710] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.200.191.185 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.84.0'))
        ]
    )
)

pkt213 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.200.191.186',
        dst='10.200.191.185'
    )/
    TCP(
        sport=179,
        dport=40090,
        seq=6275,
        ack=2102,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt214 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.200.191.185',
        dst='10.200.191.186'
    )/
    TCP(
        sport=40090,
        dport=179,
        seq=2102,
        ack=6275,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[14710] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.200.191.185 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.30.0'))
        ]
    )
)

pkt215 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.200.191.186',
        dst='10.200.191.185'
    )/
    TCP(
        sport=179,
        dport=40090,
        seq=6275,
        ack=2168,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt216 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:bf:b9::1',
        dst='2001:db8:bf:ba::2'
    )/
    TCP(
        sport=40091,
        dport=179,
        seq=2870,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt217 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:bf:ba::2',
        dst='2001:db8:bf:b9::1'
    )/
    TCP(
        sport=179,
        dport=40091,
        seq=6418,
        ack=2871,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt218 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:bf:b9::1',
        dst='2001:db8:bf:ba::2'
    )/
    TCP(
        sport=40091,
        dport=179,
        seq=2871,
        ack=6419,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt219 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:bf:b9::1',
        dst='2001:db8:bf:ba::2'
    )/
    TCP(
        sport=40091,
        dport=179,
        seq=2871,
        ack=6419,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt220 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:bf:ba::2',
        dst='2001:db8:bf:b9::1'
    )/
    TCP(
        sport=179,
        dport=40091,
        seq=6419,
        ack=2935,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=41273,
        hold_time=180,
        bgp_id='192.168.78.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=41273 |>)
        ]
    )
)

pkt221 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:bf:b9::1',
        dst='2001:db8:bf:ba::2'
    )/
    TCP(
        sport=40091,
        dport=179,
        seq=2935,
        ack=6483,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt222 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:bf:ba::2',
        dst='2001:db8:bf:b9::1'
    )/
    TCP(
        sport=179,
        dport=40091,
        seq=6483,
        ack=2954,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt223 = (
    Ether()/
    IPv6(
        plen=117,
        nh=6,
        src='2001:db8:bf:b9::1',
        dst='2001:db8:bf:ba::2'
    )/
    TCP(
        sport=40091,
        dport=179,
        seq=2954,
        ack=6502,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=97,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[14710] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=39, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:bf:b9::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:54::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:1e::/64 |>] |>)
        ]
    )
)

pkt224 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:bf:ba::2',
        dst='2001:db8:bf:b9::1'
    )/
    TCP(
        sport=179,
        dport=40091,
        seq=6502,
        ack=3051,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt225 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.207.241',
        dst='10.247.207.242'
    )/
    TCP(
        sport=45559,
        dport=179,
        seq=7621,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt226 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.247.207.242',
        dst='10.247.207.241'
    )/
    TCP(
        sport=179,
        dport=45559,
        seq=9708,
        ack=7622,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt227 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.207.241',
        dst='10.247.207.242'
    )/
    TCP(
        sport=45559,
        dport=179,
        seq=7622,
        ack=9709,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt228 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.207.241',
        dst='10.247.207.242'
    )/
    TCP(
        sport=45559,
        dport=179,
        seq=7622,
        ack=9709,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt229 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.247.207.242',
        dst='10.247.207.241'
    )/
    TCP(
        sport=179,
        dport=45559,
        seq=9709,
        ack=7686,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt230 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.207.241',
        dst='10.247.207.242'
    )/
    TCP(
        sport=45559,
        dport=179,
        seq=7686,
        ack=9773,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt231 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.247.207.242',
        dst='10.247.207.241'
    )/
    TCP(
        sport=179,
        dport=45559,
        seq=9773,
        ack=7705,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt232 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.207.241',
        dst='10.247.207.242'
    )/
    TCP(
        sport=45559,
        dport=179,
        seq=7705,
        ack=9792,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[14710] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.247.207.241 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.84.0'))
        ]
    )
)

pkt233 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.247.207.242',
        dst='10.247.207.241'
    )/
    TCP(
        sport=179,
        dport=45559,
        seq=9792,
        ack=7771,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt234 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.207.241',
        dst='10.247.207.242'
    )/
    TCP(
        sport=45559,
        dport=179,
        seq=7771,
        ack=9792,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[14710] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.247.207.241 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.30.0'))
        ]
    )
)

pkt235 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.247.207.242',
        dst='10.247.207.241'
    )/
    TCP(
        sport=179,
        dport=45559,
        seq=9792,
        ack=7837,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt236 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:cf:f1::1',
        dst='2001:db8:cf:f2::2'
    )/
    TCP(
        sport=45560,
        dport=179,
        seq=2705,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt237 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:cf:f2::2',
        dst='2001:db8:cf:f1::1'
    )/
    TCP(
        sport=179,
        dport=45560,
        seq=6898,
        ack=2706,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt238 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:cf:f1::1',
        dst='2001:db8:cf:f2::2'
    )/
    TCP(
        sport=45560,
        dport=179,
        seq=2706,
        ack=6899,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt239 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:cf:f1::1',
        dst='2001:db8:cf:f2::2'
    )/
    TCP(
        sport=45560,
        dport=179,
        seq=2706,
        ack=6899,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt240 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:cf:f2::2',
        dst='2001:db8:cf:f1::1'
    )/
    TCP(
        sport=179,
        dport=45560,
        seq=6899,
        ack=2770,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt241 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:cf:f1::1',
        dst='2001:db8:cf:f2::2'
    )/
    TCP(
        sport=45560,
        dport=179,
        seq=2770,
        ack=6963,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt242 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:cf:f2::2',
        dst='2001:db8:cf:f1::1'
    )/
    TCP(
        sport=179,
        dport=45560,
        seq=6963,
        ack=2789,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt243 = (
    Ether()/
    IPv6(
        plen=117,
        nh=6,
        src='2001:db8:cf:f1::1',
        dst='2001:db8:cf:f2::2'
    )/
    TCP(
        sport=45560,
        dport=179,
        seq=2789,
        ack=6982,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=97,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[14710] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=39, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:cf:f1::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:54::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:1e::/64 |>] |>)
        ]
    )
)

pkt244 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:cf:f2::2',
        dst='2001:db8:cf:f1::1'
    )/
    TCP(
        sport=179,
        dport=45560,
        seq=6982,
        ack=2886,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt245 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.158.241.233',
        dst='10.158.241.234'
    )/
    TCP(
        sport=31150,
        dport=179,
        seq=4678,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt246 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.158.241.234',
        dst='10.158.241.233'
    )/
    TCP(
        sport=179,
        dport=31150,
        seq=5166,
        ack=4679,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt247 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.158.241.233',
        dst='10.158.241.234'
    )/
    TCP(
        sport=31150,
        dport=179,
        seq=4679,
        ack=5167,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt248 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.158.241.233',
        dst='10.158.241.234'
    )/
    TCP(
        sport=31150,
        dport=179,
        seq=4679,
        ack=5167,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt249 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.158.241.234',
        dst='10.158.241.233'
    )/
    TCP(
        sport=179,
        dport=31150,
        seq=5167,
        ack=4743,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=56054,
        hold_time=180,
        bgp_id='10.130.43.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=56054 |>)
        ]
    )
)

pkt250 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.158.241.233',
        dst='10.158.241.234'
    )/
    TCP(
        sport=31150,
        dport=179,
        seq=4743,
        ack=5231,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt251 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.158.241.234',
        dst='10.158.241.233'
    )/
    TCP(
        sport=179,
        dport=31150,
        seq=5231,
        ack=4762,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt252 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.158.241.233',
        dst='10.158.241.234'
    )/
    TCP(
        sport=31150,
        dport=179,
        seq=4762,
        ack=5250,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[14710] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.158.241.233 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.84.0'))
        ]
    )
)

pkt253 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.158.241.234',
        dst='10.158.241.233'
    )/
    TCP(
        sport=179,
        dport=31150,
        seq=5250,
        ack=4828,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt254 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.158.241.233',
        dst='10.158.241.234'
    )/
    TCP(
        sport=31150,
        dport=179,
        seq=4828,
        ack=5250,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[14710] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.158.241.233 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.30.0'))
        ]
    )
)

pkt255 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.158.241.234',
        dst='10.158.241.233'
    )/
    TCP(
        sport=179,
        dport=31150,
        seq=5250,
        ack=4894,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt256 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:f1:e9::1',
        dst='2001:db8:f1:ea::2'
    )/
    TCP(
        sport=31151,
        dport=179,
        seq=2439,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt257 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:f1:ea::2',
        dst='2001:db8:f1:e9::1'
    )/
    TCP(
        sport=179,
        dport=31151,
        seq=6021,
        ack=2440,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt258 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:f1:e9::1',
        dst='2001:db8:f1:ea::2'
    )/
    TCP(
        sport=31151,
        dport=179,
        seq=2440,
        ack=6022,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt259 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:f1:e9::1',
        dst='2001:db8:f1:ea::2'
    )/
    TCP(
        sport=31151,
        dport=179,
        seq=2440,
        ack=6022,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt260 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:f1:ea::2',
        dst='2001:db8:f1:e9::1'
    )/
    TCP(
        sport=179,
        dport=31151,
        seq=6022,
        ack=2504,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=56054,
        hold_time=180,
        bgp_id='10.130.43.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=56054 |>)
        ]
    )
)

pkt261 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:f1:e9::1',
        dst='2001:db8:f1:ea::2'
    )/
    TCP(
        sport=31151,
        dport=179,
        seq=2504,
        ack=6086,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt262 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:f1:ea::2',
        dst='2001:db8:f1:e9::1'
    )/
    TCP(
        sport=179,
        dport=31151,
        seq=6086,
        ack=2523,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt263 = (
    Ether()/
    IPv6(
        plen=117,
        nh=6,
        src='2001:db8:f1:e9::1',
        dst='2001:db8:f1:ea::2'
    )/
    TCP(
        sport=31151,
        dport=179,
        seq=2523,
        ack=6105,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=97,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[14710] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=39, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:f1:e9::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:54::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:1e::/64 |>] |>)
        ]
    )
)

pkt264 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:f1:ea::2',
        dst='2001:db8:f1:e9::1'
    )/
    TCP(
        sport=179,
        dport=31151,
        seq=6105,
        ack=2620,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt265 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.208.150.210',
        dst='10.208.150.209'
    )/
    TCP(
        sport=53430,
        dport=179,
        seq=3580,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt266 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.208.150.209',
        dst='10.208.150.210'
    )/
    TCP(
        sport=179,
        dport=53430,
        seq=4222,
        ack=3581,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt267 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.208.150.210',
        dst='10.208.150.209'
    )/
    TCP(
        sport=53430,
        dport=179,
        seq=3581,
        ack=4223,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt268 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.208.150.210',
        dst='10.208.150.209'
    )/
    TCP(
        sport=53430,
        dport=179,
        seq=3581,
        ack=4223,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=18497,
        hold_time=180,
        bgp_id='172.18.35.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=18497 |>)
        ]
    )
)

pkt269 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.208.150.209',
        dst='10.208.150.210'
    )/
    TCP(
        sport=179,
        dport=53430,
        seq=4223,
        ack=3645,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt270 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.208.150.210',
        dst='10.208.150.209'
    )/
    TCP(
        sport=53430,
        dport=179,
        seq=3645,
        ack=4287,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt271 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.208.150.209',
        dst='10.208.150.210'
    )/
    TCP(
        sport=179,
        dport=53430,
        seq=4287,
        ack=3664,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt272 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.208.150.210',
        dst='10.208.150.209'
    )/
    TCP(
        sport=53430,
        dport=179,
        seq=3664,
        ack=4306,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[18497] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.208.150.210 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.95.0'))
        ]
    )
)

pkt273 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.208.150.209',
        dst='10.208.150.210'
    )/
    TCP(
        sport=179,
        dport=53430,
        seq=4306,
        ack=3730,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt274 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.208.150.210',
        dst='10.208.150.209'
    )/
    TCP(
        sport=53430,
        dport=179,
        seq=3730,
        ack=4306,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[18497] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.208.150.210 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.89.0'))
        ]
    )
)

pkt275 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.208.150.209',
        dst='10.208.150.210'
    )/
    TCP(
        sport=179,
        dport=53430,
        seq=4306,
        ack=3796,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt276 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.208.150.210',
        dst='10.208.150.209'
    )/
    TCP(
        sport=53430,
        dport=179,
        seq=3796,
        ack=4306,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[18497] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.208.150.210 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.94.0'))
        ]
    )
)

pkt277 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.208.150.209',
        dst='10.208.150.210'
    )/
    TCP(
        sport=179,
        dport=53430,
        seq=4306,
        ack=3862,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt278 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:96:d2::1',
        dst='2001:db8:96:d1::2'
    )/
    TCP(
        sport=53431,
        dport=179,
        seq=2360,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt279 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:96:d1::2',
        dst='2001:db8:96:d2::1'
    )/
    TCP(
        sport=179,
        dport=53431,
        seq=6584,
        ack=2361,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt280 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:96:d2::1',
        dst='2001:db8:96:d1::2'
    )/
    TCP(
        sport=53431,
        dport=179,
        seq=2361,
        ack=6585,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt281 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:96:d2::1',
        dst='2001:db8:96:d1::2'
    )/
    TCP(
        sport=53431,
        dport=179,
        seq=2361,
        ack=6585,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=18497,
        hold_time=180,
        bgp_id='172.18.35.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=18497 |>)
        ]
    )
)

pkt282 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:96:d1::2',
        dst='2001:db8:96:d2::1'
    )/
    TCP(
        sport=179,
        dport=53431,
        seq=6585,
        ack=2425,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt283 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:96:d2::1',
        dst='2001:db8:96:d1::2'
    )/
    TCP(
        sport=53431,
        dport=179,
        seq=2425,
        ack=6649,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt284 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:96:d1::2',
        dst='2001:db8:96:d2::1'
    )/
    TCP(
        sport=179,
        dport=53431,
        seq=6649,
        ack=2444,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt285 = (
    Ether()/
    IPv6(
        plen=126,
        nh=6,
        src='2001:db8:96:d2::1',
        dst='2001:db8:96:d1::2'
    )/
    TCP(
        sport=53431,
        dport=179,
        seq=2444,
        ack=6668,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=106,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[18497] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=48, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:96:d2::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:5f::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:59::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:5e::/64 |>] |>)
        ]
    )
)

pkt286 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:96:d1::2',
        dst='2001:db8:96:d2::1'
    )/
    TCP(
        sport=179,
        dport=53431,
        seq=6668,
        ack=2550,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt287 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.21.181.209',
        dst='10.21.181.210'
    )/
    TCP(
        sport=37255,
        dport=179,
        seq=5178,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt288 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.21.181.210',
        dst='10.21.181.209'
    )/
    TCP(
        sport=179,
        dport=37255,
        seq=6018,
        ack=5179,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt289 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.21.181.209',
        dst='10.21.181.210'
    )/
    TCP(
        sport=37255,
        dport=179,
        seq=5179,
        ack=6019,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt290 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.21.181.209',
        dst='10.21.181.210'
    )/
    TCP(
        sport=37255,
        dport=179,
        seq=5179,
        ack=6019,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=18497,
        hold_time=180,
        bgp_id='172.18.35.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=18497 |>)
        ]
    )
)

pkt291 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.21.181.210',
        dst='10.21.181.209'
    )/
    TCP(
        sport=179,
        dport=37255,
        seq=6019,
        ack=5243,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=39479,
        hold_time=180,
        bgp_id='192.168.202.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=39479 |>)
        ]
    )
)

pkt292 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.21.181.209',
        dst='10.21.181.210'
    )/
    TCP(
        sport=37255,
        dport=179,
        seq=5243,
        ack=6083,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt293 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.21.181.210',
        dst='10.21.181.209'
    )/
    TCP(
        sport=179,
        dport=37255,
        seq=6083,
        ack=5262,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt294 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.21.181.209',
        dst='10.21.181.210'
    )/
    TCP(
        sport=37255,
        dport=179,
        seq=5262,
        ack=6102,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[18497] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.21.181.209 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.95.0'))
        ]
    )
)

pkt295 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.21.181.210',
        dst='10.21.181.209'
    )/
    TCP(
        sport=179,
        dport=37255,
        seq=6102,
        ack=5328,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt296 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.21.181.209',
        dst='10.21.181.210'
    )/
    TCP(
        sport=37255,
        dport=179,
        seq=5328,
        ack=6102,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[18497] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.21.181.209 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.89.0'))
        ]
    )
)

pkt297 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.21.181.210',
        dst='10.21.181.209'
    )/
    TCP(
        sport=179,
        dport=37255,
        seq=6102,
        ack=5394,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt298 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.21.181.209',
        dst='10.21.181.210'
    )/
    TCP(
        sport=37255,
        dport=179,
        seq=5394,
        ack=6102,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[18497] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.21.181.209 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.94.0'))
        ]
    )
)

pkt299 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.21.181.210',
        dst='10.21.181.209'
    )/
    TCP(
        sport=179,
        dport=37255,
        seq=6102,
        ack=5460,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt300 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:b5:d1::1',
        dst='2001:db8:b5:d2::2'
    )/
    TCP(
        sport=37256,
        dport=179,
        seq=2164,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt301 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:b5:d2::2',
        dst='2001:db8:b5:d1::1'
    )/
    TCP(
        sport=179,
        dport=37256,
        seq=6497,
        ack=2165,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt302 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:b5:d1::1',
        dst='2001:db8:b5:d2::2'
    )/
    TCP(
        sport=37256,
        dport=179,
        seq=2165,
        ack=6498,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt303 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:b5:d1::1',
        dst='2001:db8:b5:d2::2'
    )/
    TCP(
        sport=37256,
        dport=179,
        seq=2165,
        ack=6498,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=18497,
        hold_time=180,
        bgp_id='172.18.35.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=18497 |>)
        ]
    )
)

pkt304 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:b5:d2::2',
        dst='2001:db8:b5:d1::1'
    )/
    TCP(
        sport=179,
        dport=37256,
        seq=6498,
        ack=2229,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=39479,
        hold_time=180,
        bgp_id='192.168.202.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=39479 |>)
        ]
    )
)

pkt305 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:b5:d1::1',
        dst='2001:db8:b5:d2::2'
    )/
    TCP(
        sport=37256,
        dport=179,
        seq=2229,
        ack=6562,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt306 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:b5:d2::2',
        dst='2001:db8:b5:d1::1'
    )/
    TCP(
        sport=179,
        dport=37256,
        seq=6562,
        ack=2248,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt307 = (
    Ether()/
    IPv6(
        plen=126,
        nh=6,
        src='2001:db8:b5:d1::1',
        dst='2001:db8:b5:d2::2'
    )/
    TCP(
        sport=37256,
        dport=179,
        seq=2248,
        ack=6581,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=106,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[18497] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=48, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:b5:d1::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:5f::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:59::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:5e::/64 |>] |>)
        ]
    )
)

pkt308 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:b5:d2::2',
        dst='2001:db8:b5:d1::1'
    )/
    TCP(
        sport=179,
        dport=37256,
        seq=6581,
        ack=2354,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt309 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.255.206.25',
        dst='10.255.206.26'
    )/
    TCP(
        sport=44015,
        dport=179,
        seq=9197,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt310 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.255.206.26',
        dst='10.255.206.25'
    )/
    TCP(
        sport=179,
        dport=44015,
        seq=6213,
        ack=9198,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt311 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.255.206.25',
        dst='10.255.206.26'
    )/
    TCP(
        sport=44015,
        dport=179,
        seq=9198,
        ack=6214,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt312 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.255.206.25',
        dst='10.255.206.26'
    )/
    TCP(
        sport=44015,
        dport=179,
        seq=9198,
        ack=6214,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=18497,
        hold_time=180,
        bgp_id='172.18.35.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=18497 |>)
        ]
    )
)

pkt313 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.255.206.26',
        dst='10.255.206.25'
    )/
    TCP(
        sport=179,
        dport=44015,
        seq=6214,
        ack=9262,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt314 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.255.206.25',
        dst='10.255.206.26'
    )/
    TCP(
        sport=44015,
        dport=179,
        seq=9262,
        ack=6278,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt315 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.255.206.26',
        dst='10.255.206.25'
    )/
    TCP(
        sport=179,
        dport=44015,
        seq=6278,
        ack=9281,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt316 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.255.206.25',
        dst='10.255.206.26'
    )/
    TCP(
        sport=44015,
        dport=179,
        seq=9281,
        ack=6297,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[18497] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.255.206.25 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.95.0'))
        ]
    )
)

pkt317 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.255.206.26',
        dst='10.255.206.25'
    )/
    TCP(
        sport=179,
        dport=44015,
        seq=6297,
        ack=9347,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt318 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.255.206.25',
        dst='10.255.206.26'
    )/
    TCP(
        sport=44015,
        dport=179,
        seq=9347,
        ack=6297,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[18497] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.255.206.25 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.89.0'))
        ]
    )
)

pkt319 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.255.206.26',
        dst='10.255.206.25'
    )/
    TCP(
        sport=179,
        dport=44015,
        seq=6297,
        ack=9413,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt320 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.255.206.25',
        dst='10.255.206.26'
    )/
    TCP(
        sport=44015,
        dport=179,
        seq=9413,
        ack=6297,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[18497] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.255.206.25 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.94.0'))
        ]
    )
)

pkt321 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.255.206.26',
        dst='10.255.206.25'
    )/
    TCP(
        sport=179,
        dport=44015,
        seq=6297,
        ack=9479,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt322 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:ce:19::1',
        dst='2001:db8:ce:1a::2'
    )/
    TCP(
        sport=44016,
        dport=179,
        seq=2047,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt323 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:ce:1a::2',
        dst='2001:db8:ce:19::1'
    )/
    TCP(
        sport=179,
        dport=44016,
        seq=6170,
        ack=2048,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt324 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:ce:19::1',
        dst='2001:db8:ce:1a::2'
    )/
    TCP(
        sport=44016,
        dport=179,
        seq=2048,
        ack=6171,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt325 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:ce:19::1',
        dst='2001:db8:ce:1a::2'
    )/
    TCP(
        sport=44016,
        dport=179,
        seq=2048,
        ack=6171,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=18497,
        hold_time=180,
        bgp_id='172.18.35.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=18497 |>)
        ]
    )
)

pkt326 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:ce:1a::2',
        dst='2001:db8:ce:19::1'
    )/
    TCP(
        sport=179,
        dport=44016,
        seq=6171,
        ack=2112,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt327 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:ce:19::1',
        dst='2001:db8:ce:1a::2'
    )/
    TCP(
        sport=44016,
        dport=179,
        seq=2112,
        ack=6235,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt328 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:ce:1a::2',
        dst='2001:db8:ce:19::1'
    )/
    TCP(
        sport=179,
        dport=44016,
        seq=6235,
        ack=2131,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt329 = (
    Ether()/
    IPv6(
        plen=126,
        nh=6,
        src='2001:db8:ce:19::1',
        dst='2001:db8:ce:1a::2'
    )/
    TCP(
        sport=44016,
        dport=179,
        seq=2131,
        ack=6254,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=106,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[18497] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=48, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:ce:19::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:5f::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:59::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:5e::/64 |>] |>)
        ]
    )
)

pkt330 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:ce:1a::2',
        dst='2001:db8:ce:19::1'
    )/
    TCP(
        sport=179,
        dport=44016,
        seq=6254,
        ack=2237,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt331 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.220.96.250',
        dst='10.220.96.249'
    )/
    TCP(
        sport=51238,
        dport=179,
        seq=9743,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt332 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.220.96.249',
        dst='10.220.96.250'
    )/
    TCP(
        sport=179,
        dport=51238,
        seq=4472,
        ack=9744,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt333 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.220.96.250',
        dst='10.220.96.249'
    )/
    TCP(
        sport=51238,
        dport=179,
        seq=9744,
        ack=4473,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt334 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.220.96.250',
        dst='10.220.96.249'
    )/
    TCP(
        sport=51238,
        dport=179,
        seq=9744,
        ack=4473,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt335 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.220.96.249',
        dst='10.220.96.250'
    )/
    TCP(
        sport=179,
        dport=51238,
        seq=4473,
        ack=9808,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=4002,
        hold_time=180,
        bgp_id='100.105.160.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=4002 |>)
        ]
    )
)

pkt336 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.220.96.250',
        dst='10.220.96.249'
    )/
    TCP(
        sport=51238,
        dport=179,
        seq=9808,
        ack=4537,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt337 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.220.96.249',
        dst='10.220.96.250'
    )/
    TCP(
        sport=179,
        dport=51238,
        seq=4537,
        ack=9827,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt338 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.220.96.250',
        dst='10.220.96.249'
    )/
    TCP(
        sport=51238,
        dport=179,
        seq=9827,
        ack=4556,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.220.96.250 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.99.0'))
        ]
    )
)

pkt339 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.220.96.249',
        dst='10.220.96.250'
    )/
    TCP(
        sport=179,
        dport=51238,
        seq=4556,
        ack=9893,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt340 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.220.96.250',
        dst='10.220.96.249'
    )/
    TCP(
        sport=51238,
        dport=179,
        seq=9893,
        ack=4556,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.220.96.250 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.91.0'))
        ]
    )
)

pkt341 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.220.96.249',
        dst='10.220.96.250'
    )/
    TCP(
        sport=179,
        dport=51238,
        seq=4556,
        ack=9959,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt342 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:60:fa::1',
        dst='2001:db8:60:f9::2'
    )/
    TCP(
        sport=51239,
        dport=179,
        seq=2852,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt343 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:60:f9::2',
        dst='2001:db8:60:fa::1'
    )/
    TCP(
        sport=179,
        dport=51239,
        seq=6184,
        ack=2853,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt344 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:60:fa::1',
        dst='2001:db8:60:f9::2'
    )/
    TCP(
        sport=51239,
        dport=179,
        seq=2853,
        ack=6185,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt345 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:60:fa::1',
        dst='2001:db8:60:f9::2'
    )/
    TCP(
        sport=51239,
        dport=179,
        seq=2853,
        ack=6185,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt346 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:60:f9::2',
        dst='2001:db8:60:fa::1'
    )/
    TCP(
        sport=179,
        dport=51239,
        seq=6185,
        ack=2917,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=4002,
        hold_time=180,
        bgp_id='100.105.160.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=4002 |>)
        ]
    )
)

pkt347 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:60:fa::1',
        dst='2001:db8:60:f9::2'
    )/
    TCP(
        sport=51239,
        dport=179,
        seq=2917,
        ack=6249,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt348 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:60:f9::2',
        dst='2001:db8:60:fa::1'
    )/
    TCP(
        sport=179,
        dport=51239,
        seq=6249,
        ack=2936,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt349 = (
    Ether()/
    IPv6(
        plen=117,
        nh=6,
        src='2001:db8:60:fa::1',
        dst='2001:db8:60:f9::2'
    )/
    TCP(
        sport=51239,
        dport=179,
        seq=2936,
        ack=6268,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=97,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=39, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:60:fa::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:63::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:5b::/64 |>] |>)
        ]
    )
)

pkt350 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:60:f9::2',
        dst='2001:db8:60:fa::1'
    )/
    TCP(
        sport=179,
        dport=51239,
        seq=6268,
        ack=3033,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt351 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.146.61.194',
        dst='10.146.61.193'
    )/
    TCP(
        sport=34818,
        dport=179,
        seq=6683,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt352 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.146.61.193',
        dst='10.146.61.194'
    )/
    TCP(
        sport=179,
        dport=34818,
        seq=1431,
        ack=6684,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt353 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.146.61.194',
        dst='10.146.61.193'
    )/
    TCP(
        sport=34818,
        dport=179,
        seq=6684,
        ack=1432,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt354 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.146.61.194',
        dst='10.146.61.193'
    )/
    TCP(
        sport=34818,
        dport=179,
        seq=6684,
        ack=1432,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt355 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.146.61.193',
        dst='10.146.61.194'
    )/
    TCP(
        sport=179,
        dport=34818,
        seq=1432,
        ack=6748,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt356 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.146.61.194',
        dst='10.146.61.193'
    )/
    TCP(
        sport=34818,
        dport=179,
        seq=6748,
        ack=1496,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt357 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.146.61.193',
        dst='10.146.61.194'
    )/
    TCP(
        sport=179,
        dport=34818,
        seq=1496,
        ack=6767,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt358 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.146.61.194',
        dst='10.146.61.193'
    )/
    TCP(
        sport=34818,
        dport=179,
        seq=6767,
        ack=1515,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.146.61.194 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.99.0'))
        ]
    )
)

pkt359 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.146.61.193',
        dst='10.146.61.194'
    )/
    TCP(
        sport=179,
        dport=34818,
        seq=1515,
        ack=6833,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt360 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.146.61.194',
        dst='10.146.61.193'
    )/
    TCP(
        sport=34818,
        dport=179,
        seq=6833,
        ack=1515,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.146.61.194 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.91.0'))
        ]
    )
)

pkt361 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.146.61.193',
        dst='10.146.61.194'
    )/
    TCP(
        sport=179,
        dport=34818,
        seq=1515,
        ack=6899,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt362 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:3d:c2::1',
        dst='2001:db8:3d:c1::2'
    )/
    TCP(
        sport=34819,
        dport=179,
        seq=2322,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt363 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:3d:c1::2',
        dst='2001:db8:3d:c2::1'
    )/
    TCP(
        sport=179,
        dport=34819,
        seq=6616,
        ack=2323,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt364 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:3d:c2::1',
        dst='2001:db8:3d:c1::2'
    )/
    TCP(
        sport=34819,
        dport=179,
        seq=2323,
        ack=6617,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt365 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:3d:c2::1',
        dst='2001:db8:3d:c1::2'
    )/
    TCP(
        sport=34819,
        dport=179,
        seq=2323,
        ack=6617,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt366 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:3d:c1::2',
        dst='2001:db8:3d:c2::1'
    )/
    TCP(
        sport=179,
        dport=34819,
        seq=6617,
        ack=2387,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt367 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:3d:c2::1',
        dst='2001:db8:3d:c1::2'
    )/
    TCP(
        sport=34819,
        dport=179,
        seq=2387,
        ack=6681,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt368 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:3d:c1::2',
        dst='2001:db8:3d:c2::1'
    )/
    TCP(
        sport=179,
        dport=34819,
        seq=6681,
        ack=2406,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt369 = (
    Ether()/
    IPv6(
        plen=117,
        nh=6,
        src='2001:db8:3d:c2::1',
        dst='2001:db8:3d:c1::2'
    )/
    TCP(
        sport=34819,
        dport=179,
        seq=2406,
        ack=6700,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=97,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=39, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:3d:c2::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:63::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:5b::/64 |>] |>)
        ]
    )
)

pkt370 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:3d:c1::2',
        dst='2001:db8:3d:c2::1'
    )/
    TCP(
        sport=179,
        dport=34819,
        seq=6700,
        ack=2503,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt371 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.104.214.249',
        dst='10.104.214.250'
    )/
    TCP(
        sport=44420,
        dport=179,
        seq=7848,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt372 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.104.214.250',
        dst='10.104.214.249'
    )/
    TCP(
        sport=179,
        dport=44420,
        seq=1025,
        ack=7849,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt373 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.104.214.249',
        dst='10.104.214.250'
    )/
    TCP(
        sport=44420,
        dport=179,
        seq=7849,
        ack=1026,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt374 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.104.214.249',
        dst='10.104.214.250'
    )/
    TCP(
        sport=44420,
        dport=179,
        seq=7849,
        ack=1026,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt375 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.104.214.250',
        dst='10.104.214.249'
    )/
    TCP(
        sport=179,
        dport=44420,
        seq=1026,
        ack=7913,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=39479,
        hold_time=180,
        bgp_id='192.168.202.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=39479 |>)
        ]
    )
)

pkt376 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.104.214.249',
        dst='10.104.214.250'
    )/
    TCP(
        sport=44420,
        dport=179,
        seq=7913,
        ack=1090,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt377 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.104.214.250',
        dst='10.104.214.249'
    )/
    TCP(
        sport=179,
        dport=44420,
        seq=1090,
        ack=7932,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt378 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.104.214.249',
        dst='10.104.214.250'
    )/
    TCP(
        sport=44420,
        dport=179,
        seq=7932,
        ack=1109,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.104.214.249 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.99.0'))
        ]
    )
)

pkt379 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.104.214.250',
        dst='10.104.214.249'
    )/
    TCP(
        sport=179,
        dport=44420,
        seq=1109,
        ack=7998,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt380 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.104.214.249',
        dst='10.104.214.250'
    )/
    TCP(
        sport=44420,
        dport=179,
        seq=7998,
        ack=1109,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.104.214.249 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.91.0'))
        ]
    )
)

pkt381 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.104.214.250',
        dst='10.104.214.249'
    )/
    TCP(
        sport=179,
        dport=44420,
        seq=1109,
        ack=8064,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt382 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:d6:f9::1',
        dst='2001:db8:d6:fa::2'
    )/
    TCP(
        sport=44421,
        dport=179,
        seq=2861,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt383 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:d6:fa::2',
        dst='2001:db8:d6:f9::1'
    )/
    TCP(
        sport=179,
        dport=44421,
        seq=6719,
        ack=2862,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt384 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:d6:f9::1',
        dst='2001:db8:d6:fa::2'
    )/
    TCP(
        sport=44421,
        dport=179,
        seq=2862,
        ack=6720,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt385 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:d6:f9::1',
        dst='2001:db8:d6:fa::2'
    )/
    TCP(
        sport=44421,
        dport=179,
        seq=2862,
        ack=6720,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt386 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:d6:fa::2',
        dst='2001:db8:d6:f9::1'
    )/
    TCP(
        sport=179,
        dport=44421,
        seq=6720,
        ack=2926,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=39479,
        hold_time=180,
        bgp_id='192.168.202.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=39479 |>)
        ]
    )
)

pkt387 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:d6:f9::1',
        dst='2001:db8:d6:fa::2'
    )/
    TCP(
        sport=44421,
        dport=179,
        seq=2926,
        ack=6784,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt388 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:d6:fa::2',
        dst='2001:db8:d6:f9::1'
    )/
    TCP(
        sport=179,
        dport=44421,
        seq=6784,
        ack=2945,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt389 = (
    Ether()/
    IPv6(
        plen=117,
        nh=6,
        src='2001:db8:d6:f9::1',
        dst='2001:db8:d6:fa::2'
    )/
    TCP(
        sport=44421,
        dport=179,
        seq=2945,
        ack=6803,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=97,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=39, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:d6:f9::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:63::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:5b::/64 |>] |>)
        ]
    )
)

pkt390 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:d6:fa::2',
        dst='2001:db8:d6:f9::1'
    )/
    TCP(
        sport=179,
        dport=44421,
        seq=6803,
        ack=3042,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt391 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.118.189.189',
        dst='10.118.189.190'
    )/
    TCP(
        sport=44831,
        dport=179,
        seq=4167,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt392 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.118.189.190',
        dst='10.118.189.189'
    )/
    TCP(
        sport=179,
        dport=44831,
        seq=6681,
        ack=4168,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt393 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.118.189.189',
        dst='10.118.189.190'
    )/
    TCP(
        sport=44831,
        dport=179,
        seq=4168,
        ack=6682,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt394 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.118.189.189',
        dst='10.118.189.190'
    )/
    TCP(
        sport=44831,
        dport=179,
        seq=4168,
        ack=6682,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt395 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.118.189.190',
        dst='10.118.189.189'
    )/
    TCP(
        sport=179,
        dport=44831,
        seq=6682,
        ack=4232,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=41273,
        hold_time=180,
        bgp_id='192.168.78.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=41273 |>)
        ]
    )
)

pkt396 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.118.189.189',
        dst='10.118.189.190'
    )/
    TCP(
        sport=44831,
        dport=179,
        seq=4232,
        ack=6746,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt397 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.118.189.190',
        dst='10.118.189.189'
    )/
    TCP(
        sport=179,
        dport=44831,
        seq=6746,
        ack=4251,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt398 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.118.189.189',
        dst='10.118.189.190'
    )/
    TCP(
        sport=44831,
        dport=179,
        seq=4251,
        ack=6765,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.118.189.189 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.99.0'))
        ]
    )
)

pkt399 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.118.189.190',
        dst='10.118.189.189'
    )/
    TCP(
        sport=179,
        dport=44831,
        seq=6765,
        ack=4317,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt400 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.118.189.189',
        dst='10.118.189.190'
    )/
    TCP(
        sport=44831,
        dport=179,
        seq=4317,
        ack=6765,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.118.189.189 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.91.0'))
        ]
    )
)

pkt401 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.118.189.190',
        dst='10.118.189.189'
    )/
    TCP(
        sport=179,
        dport=44831,
        seq=6765,
        ack=4383,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt402 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:bd:bd::1',
        dst='2001:db8:bd:be::2'
    )/
    TCP(
        sport=44832,
        dport=179,
        seq=2209,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt403 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:bd:be::2',
        dst='2001:db8:bd:bd::1'
    )/
    TCP(
        sport=179,
        dport=44832,
        seq=6125,
        ack=2210,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt404 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:bd:bd::1',
        dst='2001:db8:bd:be::2'
    )/
    TCP(
        sport=44832,
        dport=179,
        seq=2210,
        ack=6126,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt405 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:bd:bd::1',
        dst='2001:db8:bd:be::2'
    )/
    TCP(
        sport=44832,
        dport=179,
        seq=2210,
        ack=6126,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt406 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:bd:be::2',
        dst='2001:db8:bd:bd::1'
    )/
    TCP(
        sport=179,
        dport=44832,
        seq=6126,
        ack=2274,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=41273,
        hold_time=180,
        bgp_id='192.168.78.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=41273 |>)
        ]
    )
)

pkt407 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:bd:bd::1',
        dst='2001:db8:bd:be::2'
    )/
    TCP(
        sport=44832,
        dport=179,
        seq=2274,
        ack=6190,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt408 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:bd:be::2',
        dst='2001:db8:bd:bd::1'
    )/
    TCP(
        sport=179,
        dport=44832,
        seq=6190,
        ack=2293,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt409 = (
    Ether()/
    IPv6(
        plen=117,
        nh=6,
        src='2001:db8:bd:bd::1',
        dst='2001:db8:bd:be::2'
    )/
    TCP(
        sport=44832,
        dport=179,
        seq=2293,
        ack=6209,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=97,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=39, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:bd:bd::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:63::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:5b::/64 |>] |>)
        ]
    )
)

pkt410 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:bd:be::2',
        dst='2001:db8:bd:bd::1'
    )/
    TCP(
        sport=179,
        dport=44832,
        seq=6209,
        ack=2390,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt411 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.38.150.161',
        dst='10.38.150.162'
    )/
    TCP(
        sport=48741,
        dport=179,
        seq=6591,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt412 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.38.150.162',
        dst='10.38.150.161'
    )/
    TCP(
        sport=179,
        dport=48741,
        seq=6882,
        ack=6592,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt413 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.38.150.161',
        dst='10.38.150.162'
    )/
    TCP(
        sport=48741,
        dport=179,
        seq=6592,
        ack=6883,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt414 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.38.150.161',
        dst='10.38.150.162'
    )/
    TCP(
        sport=48741,
        dport=179,
        seq=6592,
        ack=6883,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt415 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.38.150.162',
        dst='10.38.150.161'
    )/
    TCP(
        sport=179,
        dport=48741,
        seq=6883,
        ack=6656,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=37466,
        hold_time=180,
        bgp_id='192.168.189.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=37466 |>)
        ]
    )
)

pkt416 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.38.150.161',
        dst='10.38.150.162'
    )/
    TCP(
        sport=48741,
        dport=179,
        seq=6656,
        ack=6947,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt417 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.38.150.162',
        dst='10.38.150.161'
    )/
    TCP(
        sport=179,
        dport=48741,
        seq=6947,
        ack=6675,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt418 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.38.150.161',
        dst='10.38.150.162'
    )/
    TCP(
        sport=48741,
        dport=179,
        seq=6675,
        ack=6966,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.38.150.161 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.99.0'))
        ]
    )
)

pkt419 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.38.150.162',
        dst='10.38.150.161'
    )/
    TCP(
        sport=179,
        dport=48741,
        seq=6966,
        ack=6741,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt420 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.38.150.161',
        dst='10.38.150.162'
    )/
    TCP(
        sport=48741,
        dport=179,
        seq=6741,
        ack=6966,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.38.150.161 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.91.0'))
        ]
    )
)

pkt421 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.38.150.162',
        dst='10.38.150.161'
    )/
    TCP(
        sport=179,
        dport=48741,
        seq=6966,
        ack=6807,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt422 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:96:a1::1',
        dst='2001:db8:96:a2::2'
    )/
    TCP(
        sport=48742,
        dport=179,
        seq=2422,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt423 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:96:a2::2',
        dst='2001:db8:96:a1::1'
    )/
    TCP(
        sport=179,
        dport=48742,
        seq=6011,
        ack=2423,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt424 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:96:a1::1',
        dst='2001:db8:96:a2::2'
    )/
    TCP(
        sport=48742,
        dport=179,
        seq=2423,
        ack=6012,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt425 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:96:a1::1',
        dst='2001:db8:96:a2::2'
    )/
    TCP(
        sport=48742,
        dport=179,
        seq=2423,
        ack=6012,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt426 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:96:a2::2',
        dst='2001:db8:96:a1::1'
    )/
    TCP(
        sport=179,
        dport=48742,
        seq=6012,
        ack=2487,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=37466,
        hold_time=180,
        bgp_id='192.168.189.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=37466 |>)
        ]
    )
)

pkt427 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:96:a1::1',
        dst='2001:db8:96:a2::2'
    )/
    TCP(
        sport=48742,
        dport=179,
        seq=2487,
        ack=6076,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt428 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:96:a2::2',
        dst='2001:db8:96:a1::1'
    )/
    TCP(
        sport=179,
        dport=48742,
        seq=6076,
        ack=2506,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt429 = (
    Ether()/
    IPv6(
        plen=117,
        nh=6,
        src='2001:db8:96:a1::1',
        dst='2001:db8:96:a2::2'
    )/
    TCP(
        sport=48742,
        dport=179,
        seq=2506,
        ack=6095,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=97,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=39, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:96:a1::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:63::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:5b::/64 |>] |>)
        ]
    )
)

pkt430 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:96:a2::2',
        dst='2001:db8:96:a1::1'
    )/
    TCP(
        sport=179,
        dport=48742,
        seq=6095,
        ack=2603,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt431 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.10.211.81',
        dst='10.10.211.82'
    )/
    TCP(
        sport=45770,
        dport=179,
        seq=4585,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt432 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.10.211.82',
        dst='10.10.211.81'
    )/
    TCP(
        sport=179,
        dport=45770,
        seq=1475,
        ack=4586,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt433 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.10.211.81',
        dst='10.10.211.82'
    )/
    TCP(
        sport=45770,
        dport=179,
        seq=4586,
        ack=1476,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt434 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.10.211.81',
        dst='10.10.211.82'
    )/
    TCP(
        sport=45770,
        dport=179,
        seq=4586,
        ack=1476,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt435 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.10.211.82',
        dst='10.10.211.81'
    )/
    TCP(
        sport=179,
        dport=45770,
        seq=1476,
        ack=4650,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt436 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.10.211.81',
        dst='10.10.211.82'
    )/
    TCP(
        sport=45770,
        dport=179,
        seq=4650,
        ack=1540,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt437 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.10.211.82',
        dst='10.10.211.81'
    )/
    TCP(
        sport=179,
        dport=45770,
        seq=1540,
        ack=4669,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt438 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.10.211.81',
        dst='10.10.211.82'
    )/
    TCP(
        sport=45770,
        dport=179,
        seq=4669,
        ack=1559,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.10.211.81 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.99.0'))
        ]
    )
)

pkt439 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.10.211.82',
        dst='10.10.211.81'
    )/
    TCP(
        sport=179,
        dport=45770,
        seq=1559,
        ack=4735,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt440 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.10.211.81',
        dst='10.10.211.82'
    )/
    TCP(
        sport=45770,
        dport=179,
        seq=4735,
        ack=1559,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.10.211.81 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.91.0'))
        ]
    )
)

pkt441 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.10.211.82',
        dst='10.10.211.81'
    )/
    TCP(
        sport=179,
        dport=45770,
        seq=1559,
        ack=4801,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt442 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:d3:51::1',
        dst='2001:db8:d3:52::2'
    )/
    TCP(
        sport=45771,
        dport=179,
        seq=2070,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt443 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:d3:52::2',
        dst='2001:db8:d3:51::1'
    )/
    TCP(
        sport=179,
        dport=45771,
        seq=6817,
        ack=2071,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt444 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:d3:51::1',
        dst='2001:db8:d3:52::2'
    )/
    TCP(
        sport=45771,
        dport=179,
        seq=2071,
        ack=6818,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt445 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:d3:51::1',
        dst='2001:db8:d3:52::2'
    )/
    TCP(
        sport=45771,
        dport=179,
        seq=2071,
        ack=6818,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt446 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:d3:52::2',
        dst='2001:db8:d3:51::1'
    )/
    TCP(
        sport=179,
        dport=45771,
        seq=6818,
        ack=2135,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt447 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:d3:51::1',
        dst='2001:db8:d3:52::2'
    )/
    TCP(
        sport=45771,
        dport=179,
        seq=2135,
        ack=6882,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt448 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:d3:52::2',
        dst='2001:db8:d3:51::1'
    )/
    TCP(
        sport=179,
        dport=45771,
        seq=6882,
        ack=2154,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt449 = (
    Ether()/
    IPv6(
        plen=117,
        nh=6,
        src='2001:db8:d3:51::1',
        dst='2001:db8:d3:52::2'
    )/
    TCP(
        sport=45771,
        dport=179,
        seq=2154,
        ack=6901,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=97,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=39, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:d3:51::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:63::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:5b::/64 |>] |>)
        ]
    )
)

pkt450 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:d3:52::2',
        dst='2001:db8:d3:51::1'
    )/
    TCP(
        sport=179,
        dport=45771,
        seq=6901,
        ack=2251,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt451 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.86.228.1',
        dst='10.86.228.2'
    )/
    TCP(
        sport=61951,
        dport=179,
        seq=8113,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt452 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.86.228.2',
        dst='10.86.228.1'
    )/
    TCP(
        sport=179,
        dport=61951,
        seq=3602,
        ack=8114,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt453 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.86.228.1',
        dst='10.86.228.2'
    )/
    TCP(
        sport=61951,
        dport=179,
        seq=8114,
        ack=3603,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt454 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.86.228.1',
        dst='10.86.228.2'
    )/
    TCP(
        sport=61951,
        dport=179,
        seq=8114,
        ack=3603,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt455 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.86.228.2',
        dst='10.86.228.1'
    )/
    TCP(
        sport=179,
        dport=61951,
        seq=3603,
        ack=8178,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=56054,
        hold_time=180,
        bgp_id='10.130.43.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=56054 |>)
        ]
    )
)

pkt456 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.86.228.1',
        dst='10.86.228.2'
    )/
    TCP(
        sport=61951,
        dport=179,
        seq=8178,
        ack=3667,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt457 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.86.228.2',
        dst='10.86.228.1'
    )/
    TCP(
        sport=179,
        dport=61951,
        seq=3667,
        ack=8197,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt458 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.86.228.1',
        dst='10.86.228.2'
    )/
    TCP(
        sport=61951,
        dport=179,
        seq=8197,
        ack=3686,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.86.228.1 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.99.0'))
        ]
    )
)

pkt459 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.86.228.2',
        dst='10.86.228.1'
    )/
    TCP(
        sport=179,
        dport=61951,
        seq=3686,
        ack=8263,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt460 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.86.228.1',
        dst='10.86.228.2'
    )/
    TCP(
        sport=61951,
        dport=179,
        seq=8263,
        ack=3686,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.86.228.1 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.91.0'))
        ]
    )
)

pkt461 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.86.228.2',
        dst='10.86.228.1'
    )/
    TCP(
        sport=179,
        dport=61951,
        seq=3686,
        ack=8329,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt462 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:e4:1::1',
        dst='2001:db8:e4:2::2'
    )/
    TCP(
        sport=61952,
        dport=179,
        seq=2685,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt463 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:e4:2::2',
        dst='2001:db8:e4:1::1'
    )/
    TCP(
        sport=179,
        dport=61952,
        seq=6440,
        ack=2686,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt464 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:e4:1::1',
        dst='2001:db8:e4:2::2'
    )/
    TCP(
        sport=61952,
        dport=179,
        seq=2686,
        ack=6441,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt465 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:e4:1::1',
        dst='2001:db8:e4:2::2'
    )/
    TCP(
        sport=61952,
        dport=179,
        seq=2686,
        ack=6441,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt466 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:e4:2::2',
        dst='2001:db8:e4:1::1'
    )/
    TCP(
        sport=179,
        dport=61952,
        seq=6441,
        ack=2750,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=56054,
        hold_time=180,
        bgp_id='10.130.43.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=56054 |>)
        ]
    )
)

pkt467 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:e4:1::1',
        dst='2001:db8:e4:2::2'
    )/
    TCP(
        sport=61952,
        dport=179,
        seq=2750,
        ack=6505,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt468 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:e4:2::2',
        dst='2001:db8:e4:1::1'
    )/
    TCP(
        sport=179,
        dport=61952,
        seq=6505,
        ack=2769,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt469 = (
    Ether()/
    IPv6(
        plen=117,
        nh=6,
        src='2001:db8:e4:1::1',
        dst='2001:db8:e4:2::2'
    )/
    TCP(
        sport=61952,
        dport=179,
        seq=2769,
        ack=6524,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=97,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[15500] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=39, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:e4:1::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:63::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:5b::/64 |>] |>)
        ]
    )
)

pkt470 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:e4:2::2',
        dst='2001:db8:e4:1::1'
    )/
    TCP(
        sport=179,
        dport=61952,
        seq=6524,
        ack=2866,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt471 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.22.155.250',
        dst='10.22.155.249'
    )/
    TCP(
        sport=54272,
        dport=179,
        seq=2049,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt472 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.22.155.249',
        dst='10.22.155.250'
    )/
    TCP(
        sport=179,
        dport=54272,
        seq=8642,
        ack=2050,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt473 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.22.155.250',
        dst='10.22.155.249'
    )/
    TCP(
        sport=54272,
        dport=179,
        seq=2050,
        ack=8643,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt474 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.22.155.250',
        dst='10.22.155.249'
    )/
    TCP(
        sport=54272,
        dport=179,
        seq=2050,
        ack=8643,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=35152,
        hold_time=180,
        bgp_id='192.168.158.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=35152 |>)
        ]
    )
)

pkt475 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.22.155.249',
        dst='10.22.155.250'
    )/
    TCP(
        sport=179,
        dport=54272,
        seq=8643,
        ack=2114,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt476 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.22.155.250',
        dst='10.22.155.249'
    )/
    TCP(
        sport=54272,
        dport=179,
        seq=2114,
        ack=8707,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt477 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.22.155.249',
        dst='10.22.155.250'
    )/
    TCP(
        sport=179,
        dport=54272,
        seq=8707,
        ack=2133,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt478 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.22.155.250',
        dst='10.22.155.249'
    )/
    TCP(
        sport=54272,
        dport=179,
        seq=2133,
        ack=8726,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.22.155.250 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt479 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.22.155.249',
        dst='10.22.155.250'
    )/
    TCP(
        sport=179,
        dport=54272,
        seq=8726,
        ack=2199,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt480 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.22.155.250',
        dst='10.22.155.249'
    )/
    TCP(
        sport=54272,
        dport=179,
        seq=2199,
        ack=8726,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.22.155.250 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.100.0'))
        ]
    )
)

pkt481 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.22.155.249',
        dst='10.22.155.250'
    )/
    TCP(
        sport=179,
        dport=54272,
        seq=8726,
        ack=2265,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt482 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.22.155.250',
        dst='10.22.155.249'
    )/
    TCP(
        sport=54272,
        dport=179,
        seq=2265,
        ack=8726,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.22.155.250 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.2.0'))
        ]
    )
)

pkt483 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.22.155.249',
        dst='10.22.155.250'
    )/
    TCP(
        sport=179,
        dport=54272,
        seq=8726,
        ack=2331,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt484 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:9b:fa::1',
        dst='2001:db8:9b:f9::2'
    )/
    TCP(
        sport=54273,
        dport=179,
        seq=2158,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt485 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:9b:f9::2',
        dst='2001:db8:9b:fa::1'
    )/
    TCP(
        sport=179,
        dport=54273,
        seq=6523,
        ack=2159,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt486 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:9b:fa::1',
        dst='2001:db8:9b:f9::2'
    )/
    TCP(
        sport=54273,
        dport=179,
        seq=2159,
        ack=6524,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt487 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:9b:fa::1',
        dst='2001:db8:9b:f9::2'
    )/
    TCP(
        sport=54273,
        dport=179,
        seq=2159,
        ack=6524,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=35152,
        hold_time=180,
        bgp_id='192.168.158.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=35152 |>)
        ]
    )
)

pkt488 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:9b:f9::2',
        dst='2001:db8:9b:fa::1'
    )/
    TCP(
        sport=179,
        dport=54273,
        seq=6524,
        ack=2223,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt489 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:9b:fa::1',
        dst='2001:db8:9b:f9::2'
    )/
    TCP(
        sport=54273,
        dport=179,
        seq=2223,
        ack=6588,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt490 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:9b:f9::2',
        dst='2001:db8:9b:fa::1'
    )/
    TCP(
        sport=179,
        dport=54273,
        seq=6588,
        ack=2242,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt491 = (
    Ether()/
    IPv6(
        plen=126,
        nh=6,
        src='2001:db8:9b:fa::1',
        dst='2001:db8:9b:f9::2'
    )/
    TCP(
        sport=54273,
        dport=179,
        seq=2242,
        ack=6607,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=106,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=48, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:9b:fa::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:71::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:64::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:2::/64 |>] |>)
        ]
    )
)

pkt492 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:9b:f9::2',
        dst='2001:db8:9b:fa::1'
    )/
    TCP(
        sport=179,
        dport=54273,
        seq=6607,
        ack=2348,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt493 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.54.66.73',
        dst='10.54.66.74'
    )/
    TCP(
        sport=60902,
        dport=179,
        seq=3135,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt494 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.54.66.74',
        dst='10.54.66.73'
    )/
    TCP(
        sport=179,
        dport=60902,
        seq=9420,
        ack=3136,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt495 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.54.66.73',
        dst='10.54.66.74'
    )/
    TCP(
        sport=60902,
        dport=179,
        seq=3136,
        ack=9421,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt496 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.54.66.73',
        dst='10.54.66.74'
    )/
    TCP(
        sport=60902,
        dport=179,
        seq=3136,
        ack=9421,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=35152,
        hold_time=180,
        bgp_id='192.168.158.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=35152 |>)
        ]
    )
)

pkt497 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.54.66.74',
        dst='10.54.66.73'
    )/
    TCP(
        sport=179,
        dport=60902,
        seq=9421,
        ack=3200,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt498 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.54.66.73',
        dst='10.54.66.74'
    )/
    TCP(
        sport=60902,
        dport=179,
        seq=3200,
        ack=9485,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt499 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.54.66.74',
        dst='10.54.66.73'
    )/
    TCP(
        sport=179,
        dport=60902,
        seq=9485,
        ack=3219,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt500 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.54.66.73',
        dst='10.54.66.74'
    )/
    TCP(
        sport=60902,
        dport=179,
        seq=3219,
        ack=9504,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.54.66.73 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt501 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.54.66.74',
        dst='10.54.66.73'
    )/
    TCP(
        sport=179,
        dport=60902,
        seq=9504,
        ack=3285,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt502 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.54.66.73',
        dst='10.54.66.74'
    )/
    TCP(
        sport=60902,
        dport=179,
        seq=3285,
        ack=9504,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.54.66.73 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.100.0'))
        ]
    )
)

pkt503 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.54.66.74',
        dst='10.54.66.73'
    )/
    TCP(
        sport=179,
        dport=60902,
        seq=9504,
        ack=3351,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt504 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.54.66.73',
        dst='10.54.66.74'
    )/
    TCP(
        sport=60902,
        dport=179,
        seq=3351,
        ack=9504,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.54.66.73 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.2.0'))
        ]
    )
)

pkt505 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.54.66.74',
        dst='10.54.66.73'
    )/
    TCP(
        sport=179,
        dport=60902,
        seq=9504,
        ack=3417,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt506 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:42:49::1',
        dst='2001:db8:42:4a::2'
    )/
    TCP(
        sport=60903,
        dport=179,
        seq=2152,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt507 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:42:4a::2',
        dst='2001:db8:42:49::1'
    )/
    TCP(
        sport=179,
        dport=60903,
        seq=6634,
        ack=2153,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt508 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:42:49::1',
        dst='2001:db8:42:4a::2'
    )/
    TCP(
        sport=60903,
        dport=179,
        seq=2153,
        ack=6635,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt509 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:42:49::1',
        dst='2001:db8:42:4a::2'
    )/
    TCP(
        sport=60903,
        dport=179,
        seq=2153,
        ack=6635,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=35152,
        hold_time=180,
        bgp_id='192.168.158.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=35152 |>)
        ]
    )
)

pkt510 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:42:4a::2',
        dst='2001:db8:42:49::1'
    )/
    TCP(
        sport=179,
        dport=60903,
        seq=6635,
        ack=2217,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt511 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:42:49::1',
        dst='2001:db8:42:4a::2'
    )/
    TCP(
        sport=60903,
        dport=179,
        seq=2217,
        ack=6699,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt512 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:42:4a::2',
        dst='2001:db8:42:49::1'
    )/
    TCP(
        sport=179,
        dport=60903,
        seq=6699,
        ack=2236,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt513 = (
    Ether()/
    IPv6(
        plen=126,
        nh=6,
        src='2001:db8:42:49::1',
        dst='2001:db8:42:4a::2'
    )/
    TCP(
        sport=60903,
        dport=179,
        seq=2236,
        ack=6718,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=106,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=48, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:42:49::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:71::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:64::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:2::/64 |>] |>)
        ]
    )
)

pkt514 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:42:4a::2',
        dst='2001:db8:42:49::1'
    )/
    TCP(
        sport=179,
        dport=60903,
        seq=6718,
        ack=2342,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt515 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=62543,
        dport=179,
        seq=5634,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt516 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=62543,
        seq=9022,
        ack=5635,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt517 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=62543,
        dport=179,
        seq=5635,
        ack=9023,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt518 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=62543,
        dport=179,
        seq=5635,
        ack=9023,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=35152,
        hold_time=180,
        bgp_id='192.168.158.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=35152 |>)
        ]
    )
)

pkt519 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=62543,
        seq=9023,
        ack=5699,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=39479,
        hold_time=180,
        bgp_id='192.168.202.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=39479 |>)
        ]
    )
)

pkt520 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=62543,
        dport=179,
        seq=5699,
        ack=9087,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt521 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=62543,
        seq=9087,
        ack=5718,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt522 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=62543,
        dport=179,
        seq=5718,
        ack=9106,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt523 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=62543,
        seq=9106,
        ack=5784,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt524 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=62543,
        dport=179,
        seq=5784,
        ack=9106,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.100.0'))
        ]
    )
)

pkt525 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=62543,
        seq=9106,
        ack=5850,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt526 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=62543,
        dport=179,
        seq=5850,
        ack=9106,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.2.0'))
        ]
    )
)

pkt527 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=62543,
        seq=9106,
        ack=5916,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt528 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:a3:cd::1',
        dst='2001:db8:a3:ce::2'
    )/
    TCP(
        sport=62544,
        dport=179,
        seq=2633,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt529 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:a3:ce::2',
        dst='2001:db8:a3:cd::1'
    )/
    TCP(
        sport=179,
        dport=62544,
        seq=6627,
        ack=2634,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt530 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:a3:cd::1',
        dst='2001:db8:a3:ce::2'
    )/
    TCP(
        sport=62544,
        dport=179,
        seq=2634,
        ack=6628,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt531 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:a3:cd::1',
        dst='2001:db8:a3:ce::2'
    )/
    TCP(
        sport=62544,
        dport=179,
        seq=2634,
        ack=6628,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=35152,
        hold_time=180,
        bgp_id='192.168.158.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=35152 |>)
        ]
    )
)

pkt532 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:a3:ce::2',
        dst='2001:db8:a3:cd::1'
    )/
    TCP(
        sport=179,
        dport=62544,
        seq=6628,
        ack=2698,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=39479,
        hold_time=180,
        bgp_id='192.168.202.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=39479 |>)
        ]
    )
)

pkt533 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:a3:cd::1',
        dst='2001:db8:a3:ce::2'
    )/
    TCP(
        sport=62544,
        dport=179,
        seq=2698,
        ack=6692,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt534 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:a3:ce::2',
        dst='2001:db8:a3:cd::1'
    )/
    TCP(
        sport=179,
        dport=62544,
        seq=6692,
        ack=2717,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt535 = (
    Ether()/
    IPv6(
        plen=126,
        nh=6,
        src='2001:db8:a3:cd::1',
        dst='2001:db8:a3:ce::2'
    )/
    TCP(
        sport=62544,
        dport=179,
        seq=2717,
        ack=6711,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=106,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=48, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:a3:cd::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:71::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:64::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:2::/64 |>] |>)
        ]
    )
)

pkt536 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:a3:ce::2',
        dst='2001:db8:a3:cd::1'
    )/
    TCP(
        sport=179,
        dport=62544,
        seq=6711,
        ack=2823,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt537 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.21.181.210',
        dst='10.21.181.209'
    )/
    TCP(
        sport=54137,
        dport=179,
        seq=3630,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt538 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.21.181.209',
        dst='10.21.181.210'
    )/
    TCP(
        sport=179,
        dport=54137,
        seq=4228,
        ack=3631,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt539 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.21.181.210',
        dst='10.21.181.209'
    )/
    TCP(
        sport=54137,
        dport=179,
        seq=3631,
        ack=4229,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt540 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.21.181.210',
        dst='10.21.181.209'
    )/
    TCP(
        sport=54137,
        dport=179,
        seq=3631,
        ack=4229,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=39479,
        hold_time=180,
        bgp_id='192.168.202.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=39479 |>)
        ]
    )
)

pkt541 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.21.181.209',
        dst='10.21.181.210'
    )/
    TCP(
        sport=179,
        dport=54137,
        seq=4229,
        ack=3695,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=18497,
        hold_time=180,
        bgp_id='172.18.35.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=18497 |>)
        ]
    )
)

pkt542 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.21.181.210',
        dst='10.21.181.209'
    )/
    TCP(
        sport=54137,
        dport=179,
        seq=3695,
        ack=4293,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt543 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.21.181.209',
        dst='10.21.181.210'
    )/
    TCP(
        sport=179,
        dport=54137,
        seq=4293,
        ack=3714,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt544 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.21.181.210',
        dst='10.21.181.209'
    )/
    TCP(
        sport=54137,
        dport=179,
        seq=3714,
        ack=4312,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[39479] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.21.181.210 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.246.0'))
        ]
    )
)

pkt545 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.21.181.209',
        dst='10.21.181.210'
    )/
    TCP(
        sport=179,
        dport=54137,
        seq=4312,
        ack=3780,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt546 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.21.181.210',
        dst='10.21.181.209'
    )/
    TCP(
        sport=54137,
        dport=179,
        seq=3780,
        ack=4312,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[39479] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.21.181.210 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.5.0'))
        ]
    )
)

pkt547 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.21.181.209',
        dst='10.21.181.210'
    )/
    TCP(
        sport=179,
        dport=54137,
        seq=4312,
        ack=3846,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt548 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:b5:d2::1',
        dst='2001:db8:b5:d1::2'
    )/
    TCP(
        sport=54138,
        dport=179,
        seq=2215,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt549 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:b5:d1::2',
        dst='2001:db8:b5:d2::1'
    )/
    TCP(
        sport=179,
        dport=54138,
        seq=6586,
        ack=2216,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt550 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:b5:d2::1',
        dst='2001:db8:b5:d1::2'
    )/
    TCP(
        sport=54138,
        dport=179,
        seq=2216,
        ack=6587,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt551 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:b5:d2::1',
        dst='2001:db8:b5:d1::2'
    )/
    TCP(
        sport=54138,
        dport=179,
        seq=2216,
        ack=6587,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=39479,
        hold_time=180,
        bgp_id='192.168.202.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=39479 |>)
        ]
    )
)

pkt552 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:b5:d1::2',
        dst='2001:db8:b5:d2::1'
    )/
    TCP(
        sport=179,
        dport=54138,
        seq=6587,
        ack=2280,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=18497,
        hold_time=180,
        bgp_id='172.18.35.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=18497 |>)
        ]
    )
)

pkt553 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:b5:d2::1',
        dst='2001:db8:b5:d1::2'
    )/
    TCP(
        sport=54138,
        dport=179,
        seq=2280,
        ack=6651,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt554 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:b5:d1::2',
        dst='2001:db8:b5:d2::1'
    )/
    TCP(
        sport=179,
        dport=54138,
        seq=6651,
        ack=2299,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt555 = (
    Ether()/
    IPv6(
        plen=117,
        nh=6,
        src='2001:db8:b5:d2::1',
        dst='2001:db8:b5:d1::2'
    )/
    TCP(
        sport=54138,
        dport=179,
        seq=2299,
        ack=6670,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=97,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[39479] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=39, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:b5:d2::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:f6::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:5::/64 |>] |>)
        ]
    )
)

pkt556 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:b5:d1::2',
        dst='2001:db8:b5:d2::1'
    )/
    TCP(
        sport=179,
        dport=54138,
        seq=6670,
        ack=2396,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt557 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.104.214.250',
        dst='10.104.214.249'
    )/
    TCP(
        sport=46690,
        dport=179,
        seq=8910,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt558 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.104.214.249',
        dst='10.104.214.250'
    )/
    TCP(
        sport=179,
        dport=46690,
        seq=1878,
        ack=8911,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt559 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.104.214.250',
        dst='10.104.214.249'
    )/
    TCP(
        sport=46690,
        dport=179,
        seq=8911,
        ack=1879,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt560 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.104.214.250',
        dst='10.104.214.249'
    )/
    TCP(
        sport=46690,
        dport=179,
        seq=8911,
        ack=1879,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=39479,
        hold_time=180,
        bgp_id='192.168.202.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=39479 |>)
        ]
    )
)

pkt561 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.104.214.249',
        dst='10.104.214.250'
    )/
    TCP(
        sport=179,
        dport=46690,
        seq=1879,
        ack=8975,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt562 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.104.214.250',
        dst='10.104.214.249'
    )/
    TCP(
        sport=46690,
        dport=179,
        seq=8975,
        ack=1943,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt563 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.104.214.249',
        dst='10.104.214.250'
    )/
    TCP(
        sport=179,
        dport=46690,
        seq=1943,
        ack=8994,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt564 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.104.214.250',
        dst='10.104.214.249'
    )/
    TCP(
        sport=46690,
        dport=179,
        seq=8994,
        ack=1962,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[39479] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.104.214.250 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.246.0'))
        ]
    )
)

pkt565 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.104.214.249',
        dst='10.104.214.250'
    )/
    TCP(
        sport=179,
        dport=46690,
        seq=1962,
        ack=9060,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt566 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.104.214.250',
        dst='10.104.214.249'
    )/
    TCP(
        sport=46690,
        dport=179,
        seq=9060,
        ack=1962,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[39479] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.104.214.250 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.5.0'))
        ]
    )
)

pkt567 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.104.214.249',
        dst='10.104.214.250'
    )/
    TCP(
        sport=179,
        dport=46690,
        seq=1962,
        ack=9126,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt568 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:d6:fa::1',
        dst='2001:db8:d6:f9::2'
    )/
    TCP(
        sport=46691,
        dport=179,
        seq=2564,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt569 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:d6:f9::2',
        dst='2001:db8:d6:fa::1'
    )/
    TCP(
        sport=179,
        dport=46691,
        seq=6471,
        ack=2565,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt570 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:d6:fa::1',
        dst='2001:db8:d6:f9::2'
    )/
    TCP(
        sport=46691,
        dport=179,
        seq=2565,
        ack=6472,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt571 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:d6:fa::1',
        dst='2001:db8:d6:f9::2'
    )/
    TCP(
        sport=46691,
        dport=179,
        seq=2565,
        ack=6472,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=39479,
        hold_time=180,
        bgp_id='192.168.202.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=39479 |>)
        ]
    )
)

pkt572 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:d6:f9::2',
        dst='2001:db8:d6:fa::1'
    )/
    TCP(
        sport=179,
        dport=46691,
        seq=6472,
        ack=2629,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt573 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:d6:fa::1',
        dst='2001:db8:d6:f9::2'
    )/
    TCP(
        sport=46691,
        dport=179,
        seq=2629,
        ack=6536,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt574 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:d6:f9::2',
        dst='2001:db8:d6:fa::1'
    )/
    TCP(
        sport=179,
        dport=46691,
        seq=6536,
        ack=2648,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt575 = (
    Ether()/
    IPv6(
        plen=117,
        nh=6,
        src='2001:db8:d6:fa::1',
        dst='2001:db8:d6:f9::2'
    )/
    TCP(
        sport=46691,
        dport=179,
        seq=2648,
        ack=6555,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=97,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[39479] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=39, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:d6:fa::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:f6::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:5::/64 |>] |>)
        ]
    )
)

pkt576 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:d6:f9::2',
        dst='2001:db8:d6:fa::1'
    )/
    TCP(
        sport=179,
        dport=46691,
        seq=6555,
        ack=2745,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt577 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=31216,
        dport=179,
        seq=6585,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt578 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=179,
        dport=31216,
        seq=5821,
        ack=6586,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt579 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=31216,
        dport=179,
        seq=6586,
        ack=5822,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt580 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=31216,
        dport=179,
        seq=6586,
        ack=5822,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=39479,
        hold_time=180,
        bgp_id='192.168.202.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=39479 |>)
        ]
    )
)

pkt581 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=179,
        dport=31216,
        seq=5822,
        ack=6650,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=35152,
        hold_time=180,
        bgp_id='192.168.158.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=35152 |>)
        ]
    )
)

pkt582 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=31216,
        dport=179,
        seq=6650,
        ack=5886,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt583 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=179,
        dport=31216,
        seq=5886,
        ack=6669,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt584 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=31216,
        dport=179,
        seq=6669,
        ack=5905,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[39479] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.206 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.246.0'))
        ]
    )
)

pkt585 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=179,
        dport=31216,
        seq=5905,
        ack=6735,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt586 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=31216,
        dport=179,
        seq=6735,
        ack=5905,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[39479] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.206 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.5.0'))
        ]
    )
)

pkt587 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=179,
        dport=31216,
        seq=5905,
        ack=6801,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt588 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:a3:ce::1',
        dst='2001:db8:a3:cd::2'
    )/
    TCP(
        sport=31217,
        dport=179,
        seq=2567,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt589 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:a3:cd::2',
        dst='2001:db8:a3:ce::1'
    )/
    TCP(
        sport=179,
        dport=31217,
        seq=6155,
        ack=2568,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt590 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:a3:ce::1',
        dst='2001:db8:a3:cd::2'
    )/
    TCP(
        sport=31217,
        dport=179,
        seq=2568,
        ack=6156,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt591 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:a3:ce::1',
        dst='2001:db8:a3:cd::2'
    )/
    TCP(
        sport=31217,
        dport=179,
        seq=2568,
        ack=6156,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=39479,
        hold_time=180,
        bgp_id='192.168.202.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=39479 |>)
        ]
    )
)

pkt592 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:a3:cd::2',
        dst='2001:db8:a3:ce::1'
    )/
    TCP(
        sport=179,
        dport=31217,
        seq=6156,
        ack=2632,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=35152,
        hold_time=180,
        bgp_id='192.168.158.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=35152 |>)
        ]
    )
)

pkt593 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:a3:ce::1',
        dst='2001:db8:a3:cd::2'
    )/
    TCP(
        sport=31217,
        dport=179,
        seq=2632,
        ack=6220,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt594 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:a3:cd::2',
        dst='2001:db8:a3:ce::1'
    )/
    TCP(
        sport=179,
        dport=31217,
        seq=6220,
        ack=2651,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt595 = (
    Ether()/
    IPv6(
        plen=117,
        nh=6,
        src='2001:db8:a3:ce::1',
        dst='2001:db8:a3:cd::2'
    )/
    TCP(
        sport=31217,
        dport=179,
        seq=2651,
        ack=6239,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=97,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[39479] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=39, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:a3:ce::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:f6::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:5::/64 |>] |>)
        ]
    )
)

pkt596 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:a3:cd::2',
        dst='2001:db8:a3:ce::1'
    )/
    TCP(
        sport=179,
        dport=31217,
        seq=6239,
        ack=2748,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt597 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.200.191.186',
        dst='10.200.191.185'
    )/
    TCP(
        sport=56730,
        dport=179,
        seq=3182,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt598 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.200.191.185',
        dst='10.200.191.186'
    )/
    TCP(
        sport=179,
        dport=56730,
        seq=6349,
        ack=3183,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt599 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.200.191.186',
        dst='10.200.191.185'
    )/
    TCP(
        sport=56730,
        dport=179,
        seq=3183,
        ack=6350,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt600 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.200.191.186',
        dst='10.200.191.185'
    )/
    TCP(
        sport=56730,
        dport=179,
        seq=3183,
        ack=6350,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=41273,
        hold_time=180,
        bgp_id='192.168.78.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=41273 |>)
        ]
    )
)

pkt601 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.200.191.185',
        dst='10.200.191.186'
    )/
    TCP(
        sport=179,
        dport=56730,
        seq=6350,
        ack=3247,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt602 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.200.191.186',
        dst='10.200.191.185'
    )/
    TCP(
        sport=56730,
        dport=179,
        seq=3247,
        ack=6414,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt603 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.200.191.185',
        dst='10.200.191.186'
    )/
    TCP(
        sport=179,
        dport=56730,
        seq=6414,
        ack=3266,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt604 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.200.191.186',
        dst='10.200.191.185'
    )/
    TCP(
        sport=56730,
        dport=179,
        seq=3266,
        ack=6433,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[41273] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.200.191.186 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.145.0'))
        ]
    )
)

pkt605 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.200.191.185',
        dst='10.200.191.186'
    )/
    TCP(
        sport=179,
        dport=56730,
        seq=6433,
        ack=3332,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt606 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:bf:ba::1',
        dst='2001:db8:bf:b9::2'
    )/
    TCP(
        sport=56731,
        dport=179,
        seq=2497,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt607 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:bf:b9::2',
        dst='2001:db8:bf:ba::1'
    )/
    TCP(
        sport=179,
        dport=56731,
        seq=6576,
        ack=2498,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt608 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:bf:ba::1',
        dst='2001:db8:bf:b9::2'
    )/
    TCP(
        sport=56731,
        dport=179,
        seq=2498,
        ack=6577,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt609 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:bf:ba::1',
        dst='2001:db8:bf:b9::2'
    )/
    TCP(
        sport=56731,
        dport=179,
        seq=2498,
        ack=6577,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=41273,
        hold_time=180,
        bgp_id='192.168.78.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=41273 |>)
        ]
    )
)

pkt610 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:bf:b9::2',
        dst='2001:db8:bf:ba::1'
    )/
    TCP(
        sport=179,
        dport=56731,
        seq=6577,
        ack=2562,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt611 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:bf:ba::1',
        dst='2001:db8:bf:b9::2'
    )/
    TCP(
        sport=56731,
        dport=179,
        seq=2562,
        ack=6641,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt612 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:bf:b9::2',
        dst='2001:db8:bf:ba::1'
    )/
    TCP(
        sport=179,
        dport=56731,
        seq=6641,
        ack=2581,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt613 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:bf:ba::1',
        dst='2001:db8:bf:b9::2'
    )/
    TCP(
        sport=56731,
        dport=179,
        seq=2581,
        ack=6660,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[41273] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:bf:ba::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:91::/64 |>] |>)
        ]
    )
)

pkt614 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:bf:b9::2',
        dst='2001:db8:bf:ba::1'
    )/
    TCP(
        sport=179,
        dport=56731,
        seq=6660,
        ack=2669,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt615 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.118.189.190',
        dst='10.118.189.189'
    )/
    TCP(
        sport=64947,
        dport=179,
        seq=6278,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt616 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.118.189.189',
        dst='10.118.189.190'
    )/
    TCP(
        sport=179,
        dport=64947,
        seq=9558,
        ack=6279,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt617 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.118.189.190',
        dst='10.118.189.189'
    )/
    TCP(
        sport=64947,
        dport=179,
        seq=6279,
        ack=9559,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt618 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.118.189.190',
        dst='10.118.189.189'
    )/
    TCP(
        sport=64947,
        dport=179,
        seq=6279,
        ack=9559,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=41273,
        hold_time=180,
        bgp_id='192.168.78.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=41273 |>)
        ]
    )
)

pkt619 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.118.189.189',
        dst='10.118.189.190'
    )/
    TCP(
        sport=179,
        dport=64947,
        seq=9559,
        ack=6343,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt620 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.118.189.190',
        dst='10.118.189.189'
    )/
    TCP(
        sport=64947,
        dport=179,
        seq=6343,
        ack=9623,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt621 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.118.189.189',
        dst='10.118.189.190'
    )/
    TCP(
        sport=179,
        dport=64947,
        seq=9623,
        ack=6362,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt622 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.118.189.190',
        dst='10.118.189.189'
    )/
    TCP(
        sport=64947,
        dport=179,
        seq=6362,
        ack=9642,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[41273] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.118.189.190 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.145.0'))
        ]
    )
)

pkt623 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.118.189.189',
        dst='10.118.189.190'
    )/
    TCP(
        sport=179,
        dport=64947,
        seq=9642,
        ack=6428,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt624 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:bd:be::1',
        dst='2001:db8:bd:bd::2'
    )/
    TCP(
        sport=64948,
        dport=179,
        seq=2329,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt625 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:bd:bd::2',
        dst='2001:db8:bd:be::1'
    )/
    TCP(
        sport=179,
        dport=64948,
        seq=6651,
        ack=2330,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt626 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:bd:be::1',
        dst='2001:db8:bd:bd::2'
    )/
    TCP(
        sport=64948,
        dport=179,
        seq=2330,
        ack=6652,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt627 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:bd:be::1',
        dst='2001:db8:bd:bd::2'
    )/
    TCP(
        sport=64948,
        dport=179,
        seq=2330,
        ack=6652,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=41273,
        hold_time=180,
        bgp_id='192.168.78.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=41273 |>)
        ]
    )
)

pkt628 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:bd:bd::2',
        dst='2001:db8:bd:be::1'
    )/
    TCP(
        sport=179,
        dport=64948,
        seq=6652,
        ack=2394,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt629 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:bd:be::1',
        dst='2001:db8:bd:bd::2'
    )/
    TCP(
        sport=64948,
        dport=179,
        seq=2394,
        ack=6716,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt630 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:bd:bd::2',
        dst='2001:db8:bd:be::1'
    )/
    TCP(
        sport=179,
        dport=64948,
        seq=6716,
        ack=2413,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt631 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:bd:be::1',
        dst='2001:db8:bd:bd::2'
    )/
    TCP(
        sport=64948,
        dport=179,
        seq=2413,
        ack=6735,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[41273] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:bd:be::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:91::/64 |>] |>)
        ]
    )
)

pkt632 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:bd:bd::2',
        dst='2001:db8:bd:be::1'
    )/
    TCP(
        sport=179,
        dport=64948,
        seq=6735,
        ack=2501,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt633 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.38.150.162',
        dst='10.38.150.161'
    )/
    TCP(
        sport=36343,
        dport=179,
        seq=2542,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt634 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.38.150.161',
        dst='10.38.150.162'
    )/
    TCP(
        sport=179,
        dport=36343,
        seq=6306,
        ack=2543,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt635 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.38.150.162',
        dst='10.38.150.161'
    )/
    TCP(
        sport=36343,
        dport=179,
        seq=2543,
        ack=6307,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt636 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.38.150.162',
        dst='10.38.150.161'
    )/
    TCP(
        sport=36343,
        dport=179,
        seq=2543,
        ack=6307,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=37466,
        hold_time=180,
        bgp_id='192.168.189.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=37466 |>)
        ]
    )
)

pkt637 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.38.150.161',
        dst='10.38.150.162'
    )/
    TCP(
        sport=179,
        dport=36343,
        seq=6307,
        ack=2607,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt638 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.38.150.162',
        dst='10.38.150.161'
    )/
    TCP(
        sport=36343,
        dport=179,
        seq=2607,
        ack=6371,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt639 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.38.150.161',
        dst='10.38.150.162'
    )/
    TCP(
        sport=179,
        dport=36343,
        seq=6371,
        ack=2626,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt640 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.38.150.162',
        dst='10.38.150.161'
    )/
    TCP(
        sport=36343,
        dport=179,
        seq=2626,
        ack=6390,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[37466] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.38.150.162 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.168.0'))
        ]
    )
)

pkt641 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.38.150.161',
        dst='10.38.150.162'
    )/
    TCP(
        sport=179,
        dport=36343,
        seq=6390,
        ack=2692,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt642 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:96:a2::1',
        dst='2001:db8:96:a1::2'
    )/
    TCP(
        sport=36344,
        dport=179,
        seq=2807,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt643 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:96:a1::2',
        dst='2001:db8:96:a2::1'
    )/
    TCP(
        sport=179,
        dport=36344,
        seq=6041,
        ack=2808,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt644 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:96:a2::1',
        dst='2001:db8:96:a1::2'
    )/
    TCP(
        sport=36344,
        dport=179,
        seq=2808,
        ack=6042,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt645 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:96:a2::1',
        dst='2001:db8:96:a1::2'
    )/
    TCP(
        sport=36344,
        dport=179,
        seq=2808,
        ack=6042,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=37466,
        hold_time=180,
        bgp_id='192.168.189.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=37466 |>)
        ]
    )
)

pkt646 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:96:a1::2',
        dst='2001:db8:96:a2::1'
    )/
    TCP(
        sport=179,
        dport=36344,
        seq=6042,
        ack=2872,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt647 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:96:a2::1',
        dst='2001:db8:96:a1::2'
    )/
    TCP(
        sport=36344,
        dport=179,
        seq=2872,
        ack=6106,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt648 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:96:a1::2',
        dst='2001:db8:96:a2::1'
    )/
    TCP(
        sport=179,
        dport=36344,
        seq=6106,
        ack=2891,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt649 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:96:a2::1',
        dst='2001:db8:96:a1::2'
    )/
    TCP(
        sport=36344,
        dport=179,
        seq=2891,
        ack=6125,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[37466] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:96:a2::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:a8::/64 |>] |>)
        ]
    )
)

pkt650 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:96:a1::2',
        dst='2001:db8:96:a2::1'
    )/
    TCP(
        sport=179,
        dport=36344,
        seq=6125,
        ack=2979,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt651 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.101.117',
        dst='10.247.101.118'
    )/
    TCP(
        sport=52477,
        dport=179,
        seq=2217,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt652 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.247.101.118',
        dst='10.247.101.117'
    )/
    TCP(
        sport=179,
        dport=52477,
        seq=9613,
        ack=2218,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt653 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.101.117',
        dst='10.247.101.118'
    )/
    TCP(
        sport=52477,
        dport=179,
        seq=2218,
        ack=9614,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt654 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.101.117',
        dst='10.247.101.118'
    )/
    TCP(
        sport=52477,
        dport=179,
        seq=2218,
        ack=9614,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=37466,
        hold_time=180,
        bgp_id='192.168.189.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=37466 |>)
        ]
    )
)

pkt655 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.247.101.118',
        dst='10.247.101.117'
    )/
    TCP(
        sport=179,
        dport=52477,
        seq=9614,
        ack=2282,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt656 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.101.117',
        dst='10.247.101.118'
    )/
    TCP(
        sport=52477,
        dport=179,
        seq=2282,
        ack=9678,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt657 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.247.101.118',
        dst='10.247.101.117'
    )/
    TCP(
        sport=179,
        dport=52477,
        seq=9678,
        ack=2301,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt658 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.101.117',
        dst='10.247.101.118'
    )/
    TCP(
        sport=52477,
        dport=179,
        seq=2301,
        ack=9697,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[37466] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.247.101.117 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.168.0'))
        ]
    )
)

pkt659 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.247.101.118',
        dst='10.247.101.117'
    )/
    TCP(
        sport=179,
        dport=52477,
        seq=9697,
        ack=2367,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt660 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:65:75::1',
        dst='2001:db8:65:76::2'
    )/
    TCP(
        sport=52478,
        dport=179,
        seq=2492,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt661 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:65:76::2',
        dst='2001:db8:65:75::1'
    )/
    TCP(
        sport=179,
        dport=52478,
        seq=6573,
        ack=2493,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt662 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:65:75::1',
        dst='2001:db8:65:76::2'
    )/
    TCP(
        sport=52478,
        dport=179,
        seq=2493,
        ack=6574,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt663 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:65:75::1',
        dst='2001:db8:65:76::2'
    )/
    TCP(
        sport=52478,
        dport=179,
        seq=2493,
        ack=6574,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=37466,
        hold_time=180,
        bgp_id='192.168.189.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=37466 |>)
        ]
    )
)

pkt664 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:65:76::2',
        dst='2001:db8:65:75::1'
    )/
    TCP(
        sport=179,
        dport=52478,
        seq=6574,
        ack=2557,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt665 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:65:75::1',
        dst='2001:db8:65:76::2'
    )/
    TCP(
        sport=52478,
        dport=179,
        seq=2557,
        ack=6638,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt666 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:65:76::2',
        dst='2001:db8:65:75::1'
    )/
    TCP(
        sport=179,
        dport=52478,
        seq=6638,
        ack=2576,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt667 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:65:75::1',
        dst='2001:db8:65:76::2'
    )/
    TCP(
        sport=52478,
        dport=179,
        seq=2576,
        ack=6657,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[37466] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:65:75::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:a8::/64 |>] |>)
        ]
    )
)

pkt668 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:65:76::2',
        dst='2001:db8:65:75::1'
    )/
    TCP(
        sport=179,
        dport=52478,
        seq=6657,
        ack=2664,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt669 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.207.242',
        dst='10.247.207.241'
    )/
    TCP(
        sport=53282,
        dport=179,
        seq=7321,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt670 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.247.207.241',
        dst='10.247.207.242'
    )/
    TCP(
        sport=179,
        dport=53282,
        seq=2725,
        ack=7322,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt671 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.207.242',
        dst='10.247.207.241'
    )/
    TCP(
        sport=53282,
        dport=179,
        seq=7322,
        ack=2726,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt672 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.207.242',
        dst='10.247.207.241'
    )/
    TCP(
        sport=53282,
        dport=179,
        seq=7322,
        ack=2726,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt673 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.247.207.241',
        dst='10.247.207.242'
    )/
    TCP(
        sport=179,
        dport=53282,
        seq=2726,
        ack=7386,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt674 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.207.242',
        dst='10.247.207.241'
    )/
    TCP(
        sport=53282,
        dport=179,
        seq=7386,
        ack=2790,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt675 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.247.207.241',
        dst='10.247.207.242'
    )/
    TCP(
        sport=179,
        dport=53282,
        seq=2790,
        ack=7405,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt676 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.207.242',
        dst='10.247.207.241'
    )/
    TCP(
        sport=53282,
        dport=179,
        seq=7405,
        ack=2809,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[52064] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.247.207.242 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.18.220.0'))
        ]
    )
)

pkt677 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.247.207.241',
        dst='10.247.207.242'
    )/
    TCP(
        sport=179,
        dport=53282,
        seq=2809,
        ack=7471,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt678 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:cf:f2::1',
        dst='2001:db8:cf:f1::2'
    )/
    TCP(
        sport=53283,
        dport=179,
        seq=2305,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt679 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:cf:f1::2',
        dst='2001:db8:cf:f2::1'
    )/
    TCP(
        sport=179,
        dport=53283,
        seq=6258,
        ack=2306,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt680 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:cf:f2::1',
        dst='2001:db8:cf:f1::2'
    )/
    TCP(
        sport=53283,
        dport=179,
        seq=2306,
        ack=6259,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt681 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:cf:f2::1',
        dst='2001:db8:cf:f1::2'
    )/
    TCP(
        sport=53283,
        dport=179,
        seq=2306,
        ack=6259,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt682 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:cf:f1::2',
        dst='2001:db8:cf:f2::1'
    )/
    TCP(
        sport=179,
        dport=53283,
        seq=6259,
        ack=2370,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt683 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:cf:f2::1',
        dst='2001:db8:cf:f1::2'
    )/
    TCP(
        sport=53283,
        dport=179,
        seq=2370,
        ack=6323,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt684 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:cf:f1::2',
        dst='2001:db8:cf:f2::1'
    )/
    TCP(
        sport=179,
        dport=53283,
        seq=6323,
        ack=2389,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt685 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:cf:f2::1',
        dst='2001:db8:cf:f1::2'
    )/
    TCP(
        sport=53283,
        dport=179,
        seq=2389,
        ack=6342,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[52064] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:cf:f2::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:dc::/64 |>] |>)
        ]
    )
)

pkt686 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:cf:f1::2',
        dst='2001:db8:cf:f2::1'
    )/
    TCP(
        sport=179,
        dport=53283,
        seq=6342,
        ack=2477,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt687 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.255.206.26',
        dst='10.255.206.25'
    )/
    TCP(
        sport=42196,
        dport=179,
        seq=2433,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt688 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.255.206.25',
        dst='10.255.206.26'
    )/
    TCP(
        sport=179,
        dport=42196,
        seq=5036,
        ack=2434,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt689 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.255.206.26',
        dst='10.255.206.25'
    )/
    TCP(
        sport=42196,
        dport=179,
        seq=2434,
        ack=5037,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt690 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.255.206.26',
        dst='10.255.206.25'
    )/
    TCP(
        sport=42196,
        dport=179,
        seq=2434,
        ack=5037,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt691 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.255.206.25',
        dst='10.255.206.26'
    )/
    TCP(
        sport=179,
        dport=42196,
        seq=5037,
        ack=2498,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=18497,
        hold_time=180,
        bgp_id='172.18.35.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=18497 |>)
        ]
    )
)

pkt692 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.255.206.26',
        dst='10.255.206.25'
    )/
    TCP(
        sport=42196,
        dport=179,
        seq=2498,
        ack=5101,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt693 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.255.206.25',
        dst='10.255.206.26'
    )/
    TCP(
        sport=179,
        dport=42196,
        seq=5101,
        ack=2517,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt694 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.255.206.26',
        dst='10.255.206.25'
    )/
    TCP(
        sport=42196,
        dport=179,
        seq=2517,
        ack=5120,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[52064] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.255.206.26 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.18.220.0'))
        ]
    )
)

pkt695 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.255.206.25',
        dst='10.255.206.26'
    )/
    TCP(
        sport=179,
        dport=42196,
        seq=5120,
        ack=2583,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt696 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:ce:1a::1',
        dst='2001:db8:ce:19::2'
    )/
    TCP(
        sport=42197,
        dport=179,
        seq=2162,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt697 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:ce:19::2',
        dst='2001:db8:ce:1a::1'
    )/
    TCP(
        sport=179,
        dport=42197,
        seq=6066,
        ack=2163,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt698 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:ce:1a::1',
        dst='2001:db8:ce:19::2'
    )/
    TCP(
        sport=42197,
        dport=179,
        seq=2163,
        ack=6067,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt699 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:ce:1a::1',
        dst='2001:db8:ce:19::2'
    )/
    TCP(
        sport=42197,
        dport=179,
        seq=2163,
        ack=6067,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt700 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:ce:19::2',
        dst='2001:db8:ce:1a::1'
    )/
    TCP(
        sport=179,
        dport=42197,
        seq=6067,
        ack=2227,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=18497,
        hold_time=180,
        bgp_id='172.18.35.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=18497 |>)
        ]
    )
)

pkt701 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:ce:1a::1',
        dst='2001:db8:ce:19::2'
    )/
    TCP(
        sport=42197,
        dport=179,
        seq=2227,
        ack=6131,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt702 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:ce:19::2',
        dst='2001:db8:ce:1a::1'
    )/
    TCP(
        sport=179,
        dport=42197,
        seq=6131,
        ack=2246,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt703 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:ce:1a::1',
        dst='2001:db8:ce:19::2'
    )/
    TCP(
        sport=42197,
        dport=179,
        seq=2246,
        ack=6150,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[52064] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:ce:1a::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:dc::/64 |>] |>)
        ]
    )
)

pkt704 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:ce:19::2',
        dst='2001:db8:ce:1a::1'
    )/
    TCP(
        sport=179,
        dport=42197,
        seq=6150,
        ack=2334,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt705 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.10.211.82',
        dst='10.10.211.81'
    )/
    TCP(
        sport=36170,
        dport=179,
        seq=8960,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt706 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.10.211.81',
        dst='10.10.211.82'
    )/
    TCP(
        sport=179,
        dport=36170,
        seq=5577,
        ack=8961,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt707 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.10.211.82',
        dst='10.10.211.81'
    )/
    TCP(
        sport=36170,
        dport=179,
        seq=8961,
        ack=5578,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt708 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.10.211.82',
        dst='10.10.211.81'
    )/
    TCP(
        sport=36170,
        dport=179,
        seq=8961,
        ack=5578,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt709 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.10.211.81',
        dst='10.10.211.82'
    )/
    TCP(
        sport=179,
        dport=36170,
        seq=5578,
        ack=9025,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt710 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.10.211.82',
        dst='10.10.211.81'
    )/
    TCP(
        sport=36170,
        dport=179,
        seq=9025,
        ack=5642,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt711 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.10.211.81',
        dst='10.10.211.82'
    )/
    TCP(
        sport=179,
        dport=36170,
        seq=5642,
        ack=9044,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt712 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.10.211.82',
        dst='10.10.211.81'
    )/
    TCP(
        sport=36170,
        dport=179,
        seq=9044,
        ack=5661,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[52064] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.10.211.82 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.18.220.0'))
        ]
    )
)

pkt713 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.10.211.81',
        dst='10.10.211.82'
    )/
    TCP(
        sport=179,
        dport=36170,
        seq=5661,
        ack=9110,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt714 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:d3:52::1',
        dst='2001:db8:d3:51::2'
    )/
    TCP(
        sport=36171,
        dport=179,
        seq=2074,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt715 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:d3:51::2',
        dst='2001:db8:d3:52::1'
    )/
    TCP(
        sport=179,
        dport=36171,
        seq=6637,
        ack=2075,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt716 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:d3:52::1',
        dst='2001:db8:d3:51::2'
    )/
    TCP(
        sport=36171,
        dport=179,
        seq=2075,
        ack=6638,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt717 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:d3:52::1',
        dst='2001:db8:d3:51::2'
    )/
    TCP(
        sport=36171,
        dport=179,
        seq=2075,
        ack=6638,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt718 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:d3:51::2',
        dst='2001:db8:d3:52::1'
    )/
    TCP(
        sport=179,
        dport=36171,
        seq=6638,
        ack=2139,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt719 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:d3:52::1',
        dst='2001:db8:d3:51::2'
    )/
    TCP(
        sport=36171,
        dport=179,
        seq=2139,
        ack=6702,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt720 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:d3:51::2',
        dst='2001:db8:d3:52::1'
    )/
    TCP(
        sport=179,
        dport=36171,
        seq=6702,
        ack=2158,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt721 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:d3:52::1',
        dst='2001:db8:d3:51::2'
    )/
    TCP(
        sport=36171,
        dport=179,
        seq=2158,
        ack=6721,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[52064] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:d3:52::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:dc::/64 |>] |>)
        ]
    )
)

pkt722 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:d3:51::2',
        dst='2001:db8:d3:52::1'
    )/
    TCP(
        sport=179,
        dport=36171,
        seq=6721,
        ack=2246,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt723 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.101.118',
        dst='10.247.101.117'
    )/
    TCP(
        sport=37338,
        dport=179,
        seq=2658,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt724 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.247.101.117',
        dst='10.247.101.118'
    )/
    TCP(
        sport=179,
        dport=37338,
        seq=2210,
        ack=2659,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt725 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.101.118',
        dst='10.247.101.117'
    )/
    TCP(
        sport=37338,
        dport=179,
        seq=2659,
        ack=2211,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt726 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.101.118',
        dst='10.247.101.117'
    )/
    TCP(
        sport=37338,
        dport=179,
        seq=2659,
        ack=2211,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt727 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.247.101.117',
        dst='10.247.101.118'
    )/
    TCP(
        sport=179,
        dport=37338,
        seq=2211,
        ack=2723,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=37466,
        hold_time=180,
        bgp_id='192.168.189.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=37466 |>)
        ]
    )
)

pkt728 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.101.118',
        dst='10.247.101.117'
    )/
    TCP(
        sport=37338,
        dport=179,
        seq=2723,
        ack=2275,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt729 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.247.101.117',
        dst='10.247.101.118'
    )/
    TCP(
        sport=179,
        dport=37338,
        seq=2275,
        ack=2742,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt730 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.247.101.118',
        dst='10.247.101.117'
    )/
    TCP(
        sport=37338,
        dport=179,
        seq=2742,
        ack=2294,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[52064] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.247.101.118 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.18.220.0'))
        ]
    )
)

pkt731 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.247.101.117',
        dst='10.247.101.118'
    )/
    TCP(
        sport=179,
        dport=37338,
        seq=2294,
        ack=2808,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt732 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:65:76::1',
        dst='2001:db8:65:75::2'
    )/
    TCP(
        sport=37339,
        dport=179,
        seq=2874,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt733 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:65:75::2',
        dst='2001:db8:65:76::1'
    )/
    TCP(
        sport=179,
        dport=37339,
        seq=6517,
        ack=2875,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt734 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:65:76::1',
        dst='2001:db8:65:75::2'
    )/
    TCP(
        sport=37339,
        dport=179,
        seq=2875,
        ack=6518,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt735 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:65:76::1',
        dst='2001:db8:65:75::2'
    )/
    TCP(
        sport=37339,
        dport=179,
        seq=2875,
        ack=6518,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt736 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:65:75::2',
        dst='2001:db8:65:76::1'
    )/
    TCP(
        sport=179,
        dport=37339,
        seq=6518,
        ack=2939,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=37466,
        hold_time=180,
        bgp_id='192.168.189.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=37466 |>)
        ]
    )
)

pkt737 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:65:76::1',
        dst='2001:db8:65:75::2'
    )/
    TCP(
        sport=37339,
        dport=179,
        seq=2939,
        ack=6582,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt738 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:65:75::2',
        dst='2001:db8:65:76::1'
    )/
    TCP(
        sport=179,
        dport=37339,
        seq=6582,
        ack=2958,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt739 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:65:76::1',
        dst='2001:db8:65:75::2'
    )/
    TCP(
        sport=37339,
        dport=179,
        seq=2958,
        ack=6601,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[52064] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:65:76::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:dc::/64 |>] |>)
        ]
    )
)

pkt740 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:65:75::2',
        dst='2001:db8:65:76::1'
    )/
    TCP(
        sport=179,
        dport=37339,
        seq=6601,
        ack=3046,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt741 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.54.66.74',
        dst='10.54.66.73'
    )/
    TCP(
        sport=39173,
        dport=179,
        seq=3777,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt742 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.54.66.73',
        dst='10.54.66.74'
    )/
    TCP(
        sport=179,
        dport=39173,
        seq=3472,
        ack=3778,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt743 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.54.66.74',
        dst='10.54.66.73'
    )/
    TCP(
        sport=39173,
        dport=179,
        seq=3778,
        ack=3473,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt744 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.54.66.74',
        dst='10.54.66.73'
    )/
    TCP(
        sport=39173,
        dport=179,
        seq=3778,
        ack=3473,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt745 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.54.66.73',
        dst='10.54.66.74'
    )/
    TCP(
        sport=179,
        dport=39173,
        seq=3473,
        ack=3842,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=35152,
        hold_time=180,
        bgp_id='192.168.158.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=35152 |>)
        ]
    )
)

pkt746 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.54.66.74',
        dst='10.54.66.73'
    )/
    TCP(
        sport=39173,
        dport=179,
        seq=3842,
        ack=3537,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt747 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.54.66.73',
        dst='10.54.66.74'
    )/
    TCP(
        sport=179,
        dport=39173,
        seq=3537,
        ack=3861,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt748 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.54.66.74',
        dst='10.54.66.73'
    )/
    TCP(
        sport=39173,
        dport=179,
        seq=3861,
        ack=3556,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[52064] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.54.66.74 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.18.220.0'))
        ]
    )
)

pkt749 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.54.66.73',
        dst='10.54.66.74'
    )/
    TCP(
        sport=179,
        dport=39173,
        seq=3556,
        ack=3927,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt750 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:42:4a::1',
        dst='2001:db8:42:49::2'
    )/
    TCP(
        sport=39174,
        dport=179,
        seq=2487,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt751 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:42:49::2',
        dst='2001:db8:42:4a::1'
    )/
    TCP(
        sport=179,
        dport=39174,
        seq=6877,
        ack=2488,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt752 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:42:4a::1',
        dst='2001:db8:42:49::2'
    )/
    TCP(
        sport=39174,
        dport=179,
        seq=2488,
        ack=6878,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt753 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:42:4a::1',
        dst='2001:db8:42:49::2'
    )/
    TCP(
        sport=39174,
        dport=179,
        seq=2488,
        ack=6878,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=52064,
        hold_time=180,
        bgp_id='10.66.16.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=52064 |>)
        ]
    )
)

pkt754 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:42:49::2',
        dst='2001:db8:42:4a::1'
    )/
    TCP(
        sport=179,
        dport=39174,
        seq=6878,
        ack=2552,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=35152,
        hold_time=180,
        bgp_id='192.168.158.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=35152 |>)
        ]
    )
)

pkt755 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:42:4a::1',
        dst='2001:db8:42:49::2'
    )/
    TCP(
        sport=39174,
        dport=179,
        seq=2552,
        ack=6942,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt756 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:42:49::2',
        dst='2001:db8:42:4a::1'
    )/
    TCP(
        sport=179,
        dport=39174,
        seq=6942,
        ack=2571,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt757 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:42:4a::1',
        dst='2001:db8:42:49::2'
    )/
    TCP(
        sport=39174,
        dport=179,
        seq=2571,
        ack=6961,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[52064] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:42:4a::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:dc::/64 |>] |>)
        ]
    )
)

pkt758 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:42:49::2',
        dst='2001:db8:42:4a::1'
    )/
    TCP(
        sport=179,
        dport=39174,
        seq=6961,
        ack=2659,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt759 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.109.42.74',
        dst='10.109.42.73'
    )/
    TCP(
        sport=30010,
        dport=179,
        seq=4333,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt760 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.109.42.73',
        dst='10.109.42.74'
    )/
    TCP(
        sport=179,
        dport=30010,
        seq=3082,
        ack=4334,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt761 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.109.42.74',
        dst='10.109.42.73'
    )/
    TCP(
        sport=30010,
        dport=179,
        seq=4334,
        ack=3083,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt762 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.109.42.74',
        dst='10.109.42.73'
    )/
    TCP(
        sport=30010,
        dport=179,
        seq=4334,
        ack=3083,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=56054,
        hold_time=180,
        bgp_id='10.130.43.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=56054 |>)
        ]
    )
)

pkt763 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.109.42.73',
        dst='10.109.42.74'
    )/
    TCP(
        sport=179,
        dport=30010,
        seq=3083,
        ack=4398,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt764 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.109.42.74',
        dst='10.109.42.73'
    )/
    TCP(
        sport=30010,
        dport=179,
        seq=4398,
        ack=3147,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt765 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.109.42.73',
        dst='10.109.42.74'
    )/
    TCP(
        sport=179,
        dport=30010,
        seq=3147,
        ack=4417,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt766 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.109.42.74',
        dst='10.109.42.73'
    )/
    TCP(
        sport=30010,
        dport=179,
        seq=4417,
        ack=3166,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[56054] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.109.42.74 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.18.94.0'))
        ]
    )
)

pkt767 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.109.42.73',
        dst='10.109.42.74'
    )/
    TCP(
        sport=179,
        dport=30010,
        seq=3166,
        ack=4483,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt768 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:2a:4a::1',
        dst='2001:db8:2a:49::2'
    )/
    TCP(
        sport=30011,
        dport=179,
        seq=2959,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt769 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:2a:49::2',
        dst='2001:db8:2a:4a::1'
    )/
    TCP(
        sport=179,
        dport=30011,
        seq=6974,
        ack=2960,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt770 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:2a:4a::1',
        dst='2001:db8:2a:49::2'
    )/
    TCP(
        sport=30011,
        dport=179,
        seq=2960,
        ack=6975,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt771 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:2a:4a::1',
        dst='2001:db8:2a:49::2'
    )/
    TCP(
        sport=30011,
        dport=179,
        seq=2960,
        ack=6975,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=56054,
        hold_time=180,
        bgp_id='10.130.43.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=56054 |>)
        ]
    )
)

pkt772 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:2a:49::2',
        dst='2001:db8:2a:4a::1'
    )/
    TCP(
        sport=179,
        dport=30011,
        seq=6975,
        ack=3024,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=2147,
        hold_time=180,
        bgp_id='100.106.91.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=2147 |>)
        ]
    )
)

pkt773 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:2a:4a::1',
        dst='2001:db8:2a:49::2'
    )/
    TCP(
        sport=30011,
        dport=179,
        seq=3024,
        ack=7039,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt774 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:2a:49::2',
        dst='2001:db8:2a:4a::1'
    )/
    TCP(
        sport=179,
        dport=30011,
        seq=7039,
        ack=3043,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt775 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:2a:4a::1',
        dst='2001:db8:2a:49::2'
    )/
    TCP(
        sport=30011,
        dport=179,
        seq=3043,
        ack=7058,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[56054] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:2a:4a::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:5e::/64 |>] |>)
        ]
    )
)

pkt776 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:2a:49::2',
        dst='2001:db8:2a:4a::1'
    )/
    TCP(
        sport=179,
        dport=30011,
        seq=7058,
        ack=3131,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt777 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.158.241.234',
        dst='10.158.241.233'
    )/
    TCP(
        sport=31307,
        dport=179,
        seq=2192,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt778 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.158.241.233',
        dst='10.158.241.234'
    )/
    TCP(
        sport=179,
        dport=31307,
        seq=4809,
        ack=2193,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt779 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.158.241.234',
        dst='10.158.241.233'
    )/
    TCP(
        sport=31307,
        dport=179,
        seq=2193,
        ack=4810,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt780 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.158.241.234',
        dst='10.158.241.233'
    )/
    TCP(
        sport=31307,
        dport=179,
        seq=2193,
        ack=4810,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=56054,
        hold_time=180,
        bgp_id='10.130.43.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=56054 |>)
        ]
    )
)

pkt781 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.158.241.233',
        dst='10.158.241.234'
    )/
    TCP(
        sport=179,
        dport=31307,
        seq=4810,
        ack=2257,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt782 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.158.241.234',
        dst='10.158.241.233'
    )/
    TCP(
        sport=31307,
        dport=179,
        seq=2257,
        ack=4874,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt783 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.158.241.233',
        dst='10.158.241.234'
    )/
    TCP(
        sport=179,
        dport=31307,
        seq=4874,
        ack=2276,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt784 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.158.241.234',
        dst='10.158.241.233'
    )/
    TCP(
        sport=31307,
        dport=179,
        seq=2276,
        ack=4893,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[56054] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.158.241.234 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.18.94.0'))
        ]
    )
)

pkt785 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.158.241.233',
        dst='10.158.241.234'
    )/
    TCP(
        sport=179,
        dport=31307,
        seq=4893,
        ack=2342,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt786 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:f1:ea::1',
        dst='2001:db8:f1:e9::2'
    )/
    TCP(
        sport=31308,
        dport=179,
        seq=2871,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt787 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:f1:e9::2',
        dst='2001:db8:f1:ea::1'
    )/
    TCP(
        sport=179,
        dport=31308,
        seq=6065,
        ack=2872,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt788 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:f1:ea::1',
        dst='2001:db8:f1:e9::2'
    )/
    TCP(
        sport=31308,
        dport=179,
        seq=2872,
        ack=6066,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt789 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:f1:ea::1',
        dst='2001:db8:f1:e9::2'
    )/
    TCP(
        sport=31308,
        dport=179,
        seq=2872,
        ack=6066,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=56054,
        hold_time=180,
        bgp_id='10.130.43.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=56054 |>)
        ]
    )
)

pkt790 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:f1:e9::2',
        dst='2001:db8:f1:ea::1'
    )/
    TCP(
        sport=179,
        dport=31308,
        seq=6066,
        ack=2936,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=14710,
        hold_time=180,
        bgp_id='172.19.178.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=14710 |>)
        ]
    )
)

pkt791 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:f1:ea::1',
        dst='2001:db8:f1:e9::2'
    )/
    TCP(
        sport=31308,
        dport=179,
        seq=2936,
        ack=6130,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt792 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:f1:e9::2',
        dst='2001:db8:f1:ea::1'
    )/
    TCP(
        sport=179,
        dport=31308,
        seq=6130,
        ack=2955,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt793 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:f1:ea::1',
        dst='2001:db8:f1:e9::2'
    )/
    TCP(
        sport=31308,
        dport=179,
        seq=2955,
        ack=6149,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[56054] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:f1:ea::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:5e::/64 |>] |>)
        ]
    )
)

pkt794 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:f1:e9::2',
        dst='2001:db8:f1:ea::1'
    )/
    TCP(
        sport=179,
        dport=31308,
        seq=6149,
        ack=3043,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt795 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.86.228.2',
        dst='10.86.228.1'
    )/
    TCP(
        sport=39890,
        dport=179,
        seq=2035,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt796 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.86.228.1',
        dst='10.86.228.2'
    )/
    TCP(
        sport=179,
        dport=39890,
        seq=1624,
        ack=2036,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt797 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.86.228.2',
        dst='10.86.228.1'
    )/
    TCP(
        sport=39890,
        dport=179,
        seq=2036,
        ack=1625,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt798 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.86.228.2',
        dst='10.86.228.1'
    )/
    TCP(
        sport=39890,
        dport=179,
        seq=2036,
        ack=1625,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=56054,
        hold_time=180,
        bgp_id='10.130.43.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=56054 |>)
        ]
    )
)

pkt799 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.86.228.1',
        dst='10.86.228.2'
    )/
    TCP(
        sport=179,
        dport=39890,
        seq=1625,
        ack=2100,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt800 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.86.228.2',
        dst='10.86.228.1'
    )/
    TCP(
        sport=39890,
        dport=179,
        seq=2100,
        ack=1689,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt801 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.86.228.1',
        dst='10.86.228.2'
    )/
    TCP(
        sport=179,
        dport=39890,
        seq=1689,
        ack=2119,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt802 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.86.228.2',
        dst='10.86.228.1'
    )/
    TCP(
        sport=39890,
        dport=179,
        seq=2119,
        ack=1708,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[56054] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.86.228.2 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.18.94.0'))
        ]
    )
)

pkt803 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.86.228.1',
        dst='10.86.228.2'
    )/
    TCP(
        sport=179,
        dport=39890,
        seq=1708,
        ack=2185,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt804 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:e4:2::1',
        dst='2001:db8:e4:1::2'
    )/
    TCP(
        sport=39891,
        dport=179,
        seq=2081,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt805 = (
    Ether()/
    IPv6(
        plen=24,
        nh=6,
        src='2001:db8:e4:1::2',
        dst='2001:db8:e4:2::1'
    )/
    TCP(
        sport=179,
        dport=39891,
        seq=6489,
        ack=2082,
        flags=<Flag 18 (SA)>,
        window=16384,
        options=[
            ('MSS', 1460)
        ]
    )
)

pkt806 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:e4:2::1',
        dst='2001:db8:e4:1::2'
    )/
    TCP(
        sport=39891,
        dport=179,
        seq=2082,
        ack=6490,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt807 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:e4:2::1',
        dst='2001:db8:e4:1::2'
    )/
    TCP(
        sport=39891,
        dport=179,
        seq=2082,
        ack=6490,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=56054,
        hold_time=180,
        bgp_id='10.130.43.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=56054 |>)
        ]
    )
)

pkt808 = (
    Ether()/
    IPv6(
        plen=85,
        nh=6,
        src='2001:db8:e4:1::2',
        dst='2001:db8:e4:2::1'
    )/
    TCP(
        sport=179,
        dport=39891,
        seq=6490,
        ack=2146,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=65,
        type=1
    )/
    BGPOpen(
        my_as=15500,
        hold_time=180,
        bgp_id='172.21.231.1',
        opt_params=[
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP (IP version 4) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=6, param_value=<BGPCapMultiprotocol  code=Multiprotocol Extensions for BGP-4 length=4 afi=IP6 (IP version 6) reserved=0 safi=Network Layer Reachability Information used for unicast forwarding |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 (Cisco) length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Route Refresh Capability for BGP-4 length=0 cap_data=b'' |>),
            BGPOptParam(param_length=2, param_value=<BGPCapGeneric  code=Enhanced Route Refresh Capability length=0 cap_data=b'' |>),
            BGPOptParam(param_length=6, param_value=<BGPCapFourBytesASN  code=Support for 4-octet AS number capability length=4 asn=15500 |>)
        ]
    )
)

pkt809 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:e4:2::1',
        dst='2001:db8:e4:1::2'
    )/
    TCP(
        sport=39891,
        dport=179,
        seq=2146,
        ack=6554,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt810 = (
    Ether()/
    IPv6(
        plen=39,
        nh=6,
        src='2001:db8:e4:1::2',
        dst='2001:db8:e4:2::1'
    )/
    TCP(
        sport=179,
        dport=39891,
        seq=6554,
        ack=2165,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt811 = (
    Ether()/
    IPv6(
        plen=108,
        nh=6,
        src='2001:db8:e4:2::1',
        dst='2001:db8:e4:1::2'
    )/
    TCP(
        sport=39891,
        dport=179,
        seq=2165,
        ack=6573,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[56054] |>] |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>),
            BGPPathAttr(type_code=14, attr_len=30, attribute=<BGPPAMPReachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding nh_addr_len=16 nh_v6_addr=2001:db8:e4:2::1 reserved=0 nlri=[<BGPNLRI_IPv6  prefix=2001:db8:5e::/64 |>] |>)
        ]
    )
)

pkt812 = (
    Ether()/
    IPv6(
        plen=20,
        nh=6,
        src='2001:db8:e4:1::2',
        dst='2001:db8:e4:2::1'
    )/
    TCP(
        sport=179,
        dport=39891,
        seq=6573,
        ack=2253,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt813 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=48173,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=INCOMPLETE |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt814 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=48239,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt815 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=48239,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt816 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=48305,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt817 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=48305,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=70,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=8, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=3 segment_value=[35152, 35152, 35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt818 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=48375,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt819 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=48375,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=14, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=2 segment_value=[35152, 35252] |>, <ASPathSegment  segment_type=AS_SET segment_length=3 segment_value=[35352, 35353, 35354] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=6, attr_len=0, attribute=<BGPPAAtomicAggregate  |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=7, attr_len=6, attribute=<BGPPAAggregator  aggregator_asn=35152 speaker_address=192.168.158.1 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt820 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=48463,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt821 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=48463,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=59,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=192.168.158.1 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.2.0'))
        ]
    )
)

pkt822 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=48522,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt823 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=48522,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=59,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=100.106.91.1 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.2.0'))
        ]
    )
)

pkt824 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=48581,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt825 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=48581,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=300 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt826 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=48647,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt827 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=48647,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=50 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt828 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=48713,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt829 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=48713,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_ADVERTISE |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.2.0'))
        ]
    )
)

pkt830 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=48779,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt831 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=48779,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=2303722472 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.2.0'))
        ]
    )
)

pkt832 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=48845,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt833 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=48845,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.100.0'))
        ]
    )
)

pkt834 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=48911,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt835 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=48911,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.100.0'))
        ]
    )
)

pkt836 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=48977,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt837 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=48977,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.2.0'))
        ]
    )
)

pkt838 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=49043,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt839 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49043,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.2.0'))
        ]
    )
)

pkt840 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=49109,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt841 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49109,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt842 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=49175,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt843 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49175,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt844 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=49241,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt845 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49241,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=67,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=12, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=5 segment_value=[35152, 18497, 41273, 2147, 14710] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.100.0'))
        ]
    )
)

pkt846 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=49308,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt847 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49308,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=59,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.100.0'))
        ]
    )
)

pkt848 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=49367,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt849 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49367,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt850 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=49433,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt851 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49433,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=71,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=6, attr_len=0, attribute=<BGPPAAtomicAggregate  |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=7, attr_len=6, attribute=<BGPPAAggregator  aggregator_asn=35152 speaker_address=192.168.158.1 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt852 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=49504,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt853 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49504,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=31,
        type=2
    )/
    BGPUpdate(
        withdrawn_routes=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0')),
            BGPNLRI_IPv4(prefix=(24, '192.0.2.0'))
        ]
    )
)

pkt854 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=49535,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt855 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49535,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=47,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_code=15, attr_len=21, attribute=<BGPPAMPUnreachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding afi_safi_specific=<BGPPAMPUnreachNLRI_IPv6  withdrawn_routes=[<BGPNLRI_IPv6  prefix=2001:db8:71::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:2::/64 |>] |> |>)
        ]
    )
)

pkt856 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=49582,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt857 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49582,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=21,
        type=3
    )/
    BGPNotification(
        error_code=1,
        error_subcode=2,
        data=b''
    )
)

pkt858 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=49603,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt859 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49603,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=21,
        type=3
    )/
    BGPNotification(
        error_code=2,
        error_subcode=2,
        data=b''
    )
)

pkt860 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=49624,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt861 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49624,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=21,
        type=3
    )/
    BGPNotification(
        error_code=3,
        error_subcode=1,
        data=b''
    )
)

pkt862 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=49645,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt863 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49645,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=21,
        type=3
    )/
    BGPNotification(
        error_code=4,
        data=b''
    )
)

pkt864 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=49666,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt865 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49666,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=21,
        type=3
    )/
    BGPNotification(
        error_code=5,
        data=b''
    )
)

pkt866 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=49687,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt867 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49687,
        ack=7314,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt868 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=49725,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt869 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7314,
        ack=49725,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt870 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49725,
        ack=7352,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt871 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49725,
        ack=7352,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt872 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7352,
        ack=49791,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt873 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49791,
        ack=7352,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.100.0'))
        ]
    )
)

pkt874 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7352,
        ack=49857,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt875 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49857,
        ack=7352,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.2.0'))
        ]
    )
)

pkt876 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7352,
        ack=49923,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt877 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7352,
        ack=49923,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[39479] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.206 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.246.0'))
        ]
    )
)

pkt878 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49923,
        ack=7418,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt879 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7418,
        ack=49923,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[39479] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.206 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.5.0'))
        ]
    )
)

pkt880 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49923,
        ack=7484,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt881 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49923,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt882 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=49961,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt883 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=2071,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=73,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(16, '203.112.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.1.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.1.2.0'))
        ]
    )
)

pkt884 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=2144,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt885 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=2144,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.1.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.1.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.1.8.0'))
        ]
    )
)

pkt886 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=2218,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt887 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=2218,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.2.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.2.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.2.4.0'))
        ]
    )
)

pkt888 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=2292,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt889 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=2292,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.2.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.2.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.3.0.0'))
        ]
    )
)

pkt890 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=2366,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt891 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=2366,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.3.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.3.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.3.6.0'))
        ]
    )
)

pkt892 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=2440,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt893 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=2440,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.3.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.4.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.4.2.0'))
        ]
    )
)

pkt894 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=2514,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt895 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=2514,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.4.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.4.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.4.8.0'))
        ]
    )
)

pkt896 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=2588,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt897 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=2588,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.5.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.5.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.5.4.0'))
        ]
    )
)

pkt898 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=2662,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt899 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=2662,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.5.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.5.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.6.0.0'))
        ]
    )
)

pkt900 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=2736,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt901 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=2736,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.6.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.6.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.6.6.0'))
        ]
    )
)

pkt902 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=2810,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt903 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=2810,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.6.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.7.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.7.2.0'))
        ]
    )
)

pkt904 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=2884,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt905 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=2884,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.7.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.7.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.7.8.0'))
        ]
    )
)

pkt906 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=2958,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt907 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=2958,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.8.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.8.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.8.4.0'))
        ]
    )
)

pkt908 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=3032,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt909 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=3032,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.8.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.8.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.9.0.0'))
        ]
    )
)

pkt910 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=3106,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt911 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=3106,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.9.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.9.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.9.6.0'))
        ]
    )
)

pkt912 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=3180,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt913 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=3180,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.9.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.10.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.10.2.0'))
        ]
    )
)

pkt914 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=3254,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt915 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=3254,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.10.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.10.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.10.8.0'))
        ]
    )
)

pkt916 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=3328,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt917 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=3328,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.11.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.11.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.11.4.0'))
        ]
    )
)

pkt918 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=3402,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt919 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=3402,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.11.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.11.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.12.0.0'))
        ]
    )
)

pkt920 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=3476,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt921 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=3476,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.12.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.12.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.12.6.0'))
        ]
    )
)

pkt922 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=3550,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt923 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=3550,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.12.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.13.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.13.2.0'))
        ]
    )
)

pkt924 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=3624,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt925 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=3624,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.13.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.13.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.13.8.0'))
        ]
    )
)

pkt926 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=3698,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt927 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=3698,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.14.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.14.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.14.4.0'))
        ]
    )
)

pkt928 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=3772,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt929 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=3772,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.14.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.14.8.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.1.0'))
        ]
    )
)

pkt930 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=3846,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt931 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=3846,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.168.2.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.3.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.4.0'))
        ]
    )
)

pkt932 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=3920,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt933 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=3920,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.168.5.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.6.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.7.0'))
        ]
    )
)

pkt934 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=3994,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt935 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=3994,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.168.8.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.9.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.10.0'))
        ]
    )
)

pkt936 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4068,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt937 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=4068,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.168.11.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.12.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.13.0'))
        ]
    )
)

pkt938 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4142,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt939 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=4142,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.168.14.0'))
        ]
    )
)

pkt940 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4208,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt941 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=4208,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=35,
        type=2
    )/
    BGPUpdate(
        withdrawn_routes=[
            BGPNLRI_IPv4(prefix=(24, '10.4.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.4.0.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.3.0'))
        ]
    )
)

pkt942 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4243,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt943 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=4243,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=35,
        type=2
    )/
    BGPUpdate(
        withdrawn_routes=[
            BGPNLRI_IPv4(prefix=(24, '10.9.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.6.0.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.1.0'))
        ]
    )
)

pkt944 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4278,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt945 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=4278,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=34,
        type=2
    )/
    BGPUpdate(
        withdrawn_routes=[
            BGPNLRI_IPv4(prefix=(24, '192.168.4.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.11.0')),
            BGPNLRI_IPv4(prefix=(16, '203.112.0.0'))
        ]
    )
)

pkt946 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4312,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt947 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=4312,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=35,
        type=2
    )/
    BGPUpdate(
        withdrawn_routes=[
            BGPNLRI_IPv4(prefix=(24, '10.7.0.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.10.0')),
            BGPNLRI_IPv4(prefix=(24, '10.2.2.0'))
        ]
    )
)

pkt948 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4347,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt949 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=4347,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=35,
        type=2
    )/
    BGPUpdate(
        withdrawn_routes=[
            BGPNLRI_IPv4(prefix=(24, '10.8.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.5.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.14.4.0'))
        ]
    )
)

pkt950 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4382,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt951 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=4382,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=31,
        type=2
    )/
    BGPUpdate(
        withdrawn_routes=[
            BGPNLRI_IPv4(prefix=(24, '10.6.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.1.6.0'))
        ]
    )
)

pkt952 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4413,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt953 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=4413,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt954 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4451,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt955 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=4451,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt956 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4489,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt957 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=4489,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt958 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4527,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt959 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=4527,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt960 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4565,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt961 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=4565,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt962 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4603,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt963 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=4603,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt964 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4641,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt965 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=4641,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt966 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4679,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt967 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=4679,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt968 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4717,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt969 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=4717,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt970 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4755,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt971 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=59362,
        dport=179,
        seq=4755,
        ack=7550,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt972 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=59362,
        seq=7550,
        ack=4793,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt973 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=49961,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=INCOMPLETE |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.100.0'))
        ]
    )
)

pkt974 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=50027,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt975 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=50027,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.100.0'))
        ]
    )
)

pkt976 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=50093,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt977 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=50093,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=70,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=8, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=3 segment_value=[35152, 35152, 35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.100.0'))
        ]
    )
)

pkt978 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=50163,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt979 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=50163,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=88,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=14, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=2 segment_value=[35152, 35252] |>, <ASPathSegment  segment_type=AS_SET segment_length=3 segment_value=[35352, 35353, 35354] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=6, attr_len=0, attribute=<BGPPAAtomicAggregate  |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=7, attr_len=6, attribute=<BGPPAAggregator  aggregator_asn=35152 speaker_address=192.168.158.1 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.100.0'))
        ]
    )
)

pkt980 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=50251,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt981 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=50251,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=59,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=192.168.158.1 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.100.0'))
        ]
    )
)

pkt982 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=50310,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt983 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=50310,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=59,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=100.106.91.1 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.100.0'))
        ]
    )
)

pkt984 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=50369,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt985 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=50369,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=300 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.2.0'))
        ]
    )
)

pkt986 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=50435,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt987 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=50435,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=50 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.2.0'))
        ]
    )
)

pkt988 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=50501,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt989 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=50501,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_ADVERTISE |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt990 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=50567,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt991 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=50567,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=2303722472 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt992 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=50633,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt993 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=50633,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt994 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=50699,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt995 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=50699,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt996 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=50765,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt997 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=50765,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.100.0'))
        ]
    )
)

pkt998 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=50831,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt999 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=50831,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.100.0'))
        ]
    )
)

pkt1000 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=50897,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1001 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=50897,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.2.0'))
        ]
    )
)

pkt1002 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=50963,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1003 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=50963,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.2.0'))
        ]
    )
)

pkt1004 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=51029,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1005 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51029,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=67,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=12, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=5 segment_value=[35152, 37466, 2147, 52064, 56054] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt1006 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=51096,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1007 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51096,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=59,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt1008 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=51155,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1009 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51155,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt1010 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=51221,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1011 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51221,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=71,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=6, attr_len=0, attribute=<BGPPAAtomicAggregate  |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=7, attr_len=6, attribute=<BGPPAAggregator  aggregator_asn=35152 speaker_address=192.168.158.1 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt1012 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=51292,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1013 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51292,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=31,
        type=2
    )/
    BGPUpdate(
        withdrawn_routes=[
            BGPNLRI_IPv4(prefix=(24, '192.0.2.0')),
            BGPNLRI_IPv4(prefix=(24, '198.51.100.0'))
        ]
    )
)

pkt1014 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=51323,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1015 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51323,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=47,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_code=15, attr_len=21, attribute=<BGPPAMPUnreachNLRI  afi=IP6 (IP version 6) safi=Network Layer Reachability Information used for unicast forwarding afi_safi_specific=<BGPPAMPUnreachNLRI_IPv6  withdrawn_routes=[<BGPNLRI_IPv6  prefix=2001:db8:2::/64 |>, <BGPNLRI_IPv6  prefix=2001:db8:64::/64 |>] |> |>)
        ]
    )
)

pkt1016 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=51370,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1017 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51370,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=21,
        type=3
    )/
    BGPNotification(
        error_code=1,
        error_subcode=2,
        data=b''
    )
)

pkt1018 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=51391,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1019 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51391,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=21,
        type=3
    )/
    BGPNotification(
        error_code=2,
        error_subcode=2,
        data=b''
    )
)

pkt1020 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=51412,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1021 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51412,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=21,
        type=3
    )/
    BGPNotification(
        error_code=3,
        error_subcode=1,
        data=b''
    )
)

pkt1022 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=51433,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1023 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51433,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=21,
        type=3
    )/
    BGPNotification(
        error_code=4,
        data=b''
    )
)

pkt1024 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=51454,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1025 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51454,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=21,
        type=3
    )/
    BGPNotification(
        error_code=5,
        data=b''
    )
)

pkt1026 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=51475,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1027 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51475,
        ack=7484,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt1028 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=51513,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1029 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7484,
        ack=51513,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt1030 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51513,
        ack=7522,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1031 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51513,
        ack=7522,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '203.0.113.0'))
        ]
    )
)

pkt1032 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7522,
        ack=51579,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1033 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51579,
        ack=7522,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '198.51.100.0'))
        ]
    )
)

pkt1034 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7522,
        ack=51645,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1035 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51645,
        ack=7522,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[35152] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.205 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.2.0'))
        ]
    )
)

pkt1036 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7522,
        ack=51711,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1037 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7522,
        ack=51711,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[39479] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.206 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.246.0'))
        ]
    )
)

pkt1038 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51711,
        ack=7588,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1039 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7588,
        ack=51711,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[39479] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.65.163.206 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=NO_EXPORT |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.0.5.0'))
        ]
    )
)

pkt1040 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51711,
        ack=7654,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1041 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.65.163.205',
        dst='10.65.163.206'
    )/
    TCP(
        sport=43240,
        dport=179,
        seq=51711,
        ack=7654,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt1042 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.65.163.206',
        dst='10.65.163.205'
    )/
    TCP(
        sport=179,
        dport=43240,
        seq=7654,
        ack=51749,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1043 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=7556,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=73,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(16, '203.112.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.1.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.1.2.0'))
        ]
    )
)

pkt1044 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=7629,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1045 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=7629,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.1.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.1.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.1.8.0'))
        ]
    )
)

pkt1046 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=7703,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1047 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=7703,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.2.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.2.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.2.4.0'))
        ]
    )
)

pkt1048 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=7777,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1049 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=7777,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.2.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.2.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.3.0.0'))
        ]
    )
)

pkt1050 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=7851,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1051 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=7851,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.3.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.3.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.3.6.0'))
        ]
    )
)

pkt1052 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=7925,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1053 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=7925,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.3.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.4.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.4.2.0'))
        ]
    )
)

pkt1054 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=7999,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1055 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=7999,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.4.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.4.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.4.8.0'))
        ]
    )
)

pkt1056 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=8073,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1057 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=8073,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.5.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.5.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.5.4.0'))
        ]
    )
)

pkt1058 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=8147,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1059 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=8147,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.5.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.5.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.6.0.0'))
        ]
    )
)

pkt1060 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=8221,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1061 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=8221,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.6.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.6.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.6.6.0'))
        ]
    )
)

pkt1062 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=8295,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1063 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=8295,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.6.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.7.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.7.2.0'))
        ]
    )
)

pkt1064 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=8369,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1065 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=8369,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.7.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.7.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.7.8.0'))
        ]
    )
)

pkt1066 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=8443,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1067 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=8443,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.8.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.8.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.8.4.0'))
        ]
    )
)

pkt1068 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=8517,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1069 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=8517,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.8.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.8.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.9.0.0'))
        ]
    )
)

pkt1070 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=8591,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1071 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=8591,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.9.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.9.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.9.6.0'))
        ]
    )
)

pkt1072 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=8665,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1073 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=8665,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.9.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.10.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.10.2.0'))
        ]
    )
)

pkt1074 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=8739,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1075 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=8739,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.10.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.10.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.10.8.0'))
        ]
    )
)

pkt1076 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=8813,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1077 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=8813,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.11.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.11.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.11.4.0'))
        ]
    )
)

pkt1078 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=8887,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1079 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=8887,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.11.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.11.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.12.0.0'))
        ]
    )
)

pkt1080 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=8961,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1081 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=8961,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.12.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.12.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.12.6.0'))
        ]
    )
)

pkt1082 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=9035,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1083 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=9035,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.12.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.13.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.13.2.0'))
        ]
    )
)

pkt1084 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=9109,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1085 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=9109,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.13.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.13.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.13.8.0'))
        ]
    )
)

pkt1086 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=9183,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1087 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=9183,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.14.0.0')),
            BGPNLRI_IPv4(prefix=(24, '10.14.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.14.4.0'))
        ]
    )
)

pkt1088 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=9257,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1089 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=9257,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '10.14.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.14.8.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.1.0'))
        ]
    )
)

pkt1090 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=9331,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1091 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=9331,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.168.2.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.3.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.4.0'))
        ]
    )
)

pkt1092 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=9405,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1093 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=9405,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.168.5.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.6.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.7.0'))
        ]
    )
)

pkt1094 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=9479,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1095 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=9479,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.168.8.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.9.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.10.0'))
        ]
    )
)

pkt1096 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=9553,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1097 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=9553,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=74,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.168.11.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.12.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.13.0'))
        ]
    )
)

pkt1098 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=9627,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1099 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=9627,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=66,
        type=2
    )/
    BGPUpdate(
        path_attr=[
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=1, attr_len=1, attribute=<BGPPAOrigin  origin=IGP |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=2, attr_len=4, attribute=<BGPPAASPath  segments=[<ASPathSegment  segment_type=AS_SEQUENCE segment_length=1 segment_value=[2147] |>] |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=3, attr_len=4, attribute=<BGPPANextHop  next_hop=10.125.216.9 |>),
            BGPPathAttr(type_code=4, attr_len=4, attribute=<BGPPAMultiExitDisc  med=100 |>),
            BGPPathAttr(type_flags=<Flag 64 (Transitive)>, type_code=5, attr_len=4, attribute=<BGPPALocalPref  local_pref=200 |>),
            BGPPathAttr(type_flags=<Flag 192 (Transitive+Optional)>, type_code=8, attr_len=4, attribute=<BGPPACommunity  community=140705892 |>)
        ],
        nlri=[
            BGPNLRI_IPv4(prefix=(24, '192.168.14.0'))
        ]
    )
)

pkt1100 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=9693,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1101 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=9693,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=35,
        type=2
    )/
    BGPUpdate(
        withdrawn_routes=[
            BGPNLRI_IPv4(prefix=(24, '10.6.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.10.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.6.0.0'))
        ]
    )
)

pkt1102 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=9728,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1103 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=9728,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=35,
        type=2
    )/
    BGPUpdate(
        withdrawn_routes=[
            BGPNLRI_IPv4(prefix=(24, '10.7.2.0')),
            BGPNLRI_IPv4(prefix=(24, '10.14.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.14.8.0'))
        ]
    )
)

pkt1104 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=9763,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1105 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=9763,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=35,
        type=2
    )/
    BGPUpdate(
        withdrawn_routes=[
            BGPNLRI_IPv4(prefix=(24, '192.168.9.0')),
            BGPNLRI_IPv4(prefix=(24, '10.3.4.0')),
            BGPNLRI_IPv4(prefix=(24, '10.13.4.0'))
        ]
    )
)

pkt1106 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=9798,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1107 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=9798,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=35,
        type=2
    )/
    BGPUpdate(
        withdrawn_routes=[
            BGPNLRI_IPv4(prefix=(24, '192.168.1.0')),
            BGPNLRI_IPv4(prefix=(24, '10.8.0.0')),
            BGPNLRI_IPv4(prefix=(24, '192.168.14.0'))
        ]
    )
)

pkt1108 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=9833,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1109 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=9833,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=35,
        type=2
    )/
    BGPUpdate(
        withdrawn_routes=[
            BGPNLRI_IPv4(prefix=(24, '10.11.8.0')),
            BGPNLRI_IPv4(prefix=(24, '10.11.6.0')),
            BGPNLRI_IPv4(prefix=(24, '10.10.0.0'))
        ]
    )
)

pkt1110 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=9868,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1111 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=9868,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPHeader(
        len=31,
        type=2
    )/
    BGPUpdate(
        withdrawn_routes=[
            BGPNLRI_IPv4(prefix=(24, '192.168.12.0')),
            BGPNLRI_IPv4(prefix=(24, '10.14.2.0'))
        ]
    )
)

pkt1112 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=9899,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1113 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=9899,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt1114 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=9937,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1115 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=9937,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt1116 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=9975,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1117 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=9975,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt1118 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=10013,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1119 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=10013,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt1120 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=10051,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1121 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=10051,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt1122 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=10089,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1123 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=10089,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt1124 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=10127,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1125 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=10127,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt1126 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=10165,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1127 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=10165,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt1128 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=10203,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1129 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=10203,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt1130 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=10241,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

pkt1131 = (
    Ether()/
    IP(
        tos=192,
        flags=<Flag 2 (DF)>,
        ttl=1,
        src='10.125.216.9',
        dst='10.125.216.10'
    )/
    TCP(
        sport=37757,
        dport=179,
        seq=10241,
        ack=3658,
        flags=<Flag 24 (PA)>,
        window=16384
    )/
    BGPKeepAlive(
        len=38
    )/
    BGPKeepAlive(
        len=19
    )
)

pkt1132 = (
    Ether()/
    IP(
        tos=192,
        ttl=1,
        src='10.125.216.10',
        dst='10.125.216.9'
    )/
    TCP(
        sport=179,
        dport=37757,
        seq=3658,
        ack=10279,
        flags=<Flag 16 (A)>,
        window=16384
    )
)

PKTS = [pkt1, pkt2, pkt3, pkt4, pkt5, pkt6, pkt7, pkt8, pkt9, pkt10, pkt11, pkt12, pkt13, pkt14, pkt15, pkt16, pkt17, pkt18, pkt19, pkt20, pkt21, pkt22, pkt23, pkt24, pkt25, pkt26, pkt27, pkt28, pkt29, pkt30, pkt31, pkt32, pkt33, pkt34, pkt35, pkt36, pkt37, pkt38, pkt39, pkt40, pkt41, pkt42, pkt43, pkt44, pkt45, pkt46, pkt47, pkt48, pkt49, pkt50, pkt51, pkt52, pkt53, pkt54, pkt55, pkt56, pkt57, pkt58, pkt59, pkt60, pkt61, pkt62, pkt63, pkt64, pkt65, pkt66, pkt67, pkt68, pkt69, pkt70, pkt71, pkt72, pkt73, pkt74, pkt75, pkt76, pkt77, pkt78, pkt79, pkt80, pkt81, pkt82, pkt83, pkt84, pkt85, pkt86, pkt87, pkt88, pkt89, pkt90, pkt91, pkt92, pkt93, pkt94, pkt95, pkt96, pkt97, pkt98, pkt99, pkt100, pkt101, pkt102, pkt103, pkt104, pkt105, pkt106, pkt107, pkt108, pkt109, pkt110, pkt111, pkt112, pkt113, pkt114, pkt115, pkt116, pkt117, pkt118, pkt119, pkt120, pkt121, pkt122, pkt123, pkt124, pkt125, pkt126, pkt127, pkt128, pkt129, pkt130, pkt131, pkt132, pkt133, pkt134, pkt135, pkt136, pkt137, pkt138, pkt139, pkt140, pkt141, pkt142, pkt143, pkt144, pkt145, pkt146, pkt147, pkt148, pkt149, pkt150, pkt151, pkt152, pkt153, pkt154, pkt155, pkt156, pkt157, pkt158, pkt159, pkt160, pkt161, pkt162, pkt163, pkt164, pkt165, pkt166, pkt167, pkt168, pkt169, pkt170, pkt171, pkt172, pkt173, pkt174, pkt175, pkt176, pkt177, pkt178, pkt179, pkt180, pkt181, pkt182, pkt183, pkt184, pkt185, pkt186, pkt187, pkt188, pkt189, pkt190, pkt191, pkt192, pkt193, pkt194, pkt195, pkt196, pkt197, pkt198, pkt199, pkt200, pkt201, pkt202, pkt203, pkt204, pkt205, pkt206, pkt207, pkt208, pkt209, pkt210, pkt211, pkt212, pkt213, pkt214, pkt215, pkt216, pkt217, pkt218, pkt219, pkt220, pkt221, pkt222, pkt223, pkt224, pkt225, pkt226, pkt227, pkt228, pkt229, pkt230, pkt231, pkt232, pkt233, pkt234, pkt235, pkt236, pkt237, pkt238, pkt239, pkt240, pkt241, pkt242, pkt243, pkt244, pkt245, pkt246, pkt247, pkt248, pkt249, pkt250, pkt251, pkt252, pkt253, pkt254, pkt255, pkt256, pkt257, pkt258, pkt259, pkt260, pkt261, pkt262, pkt263, pkt264, pkt265, pkt266, pkt267, pkt268, pkt269, pkt270, pkt271, pkt272, pkt273, pkt274, pkt275, pkt276, pkt277, pkt278, pkt279, pkt280, pkt281, pkt282, pkt283, pkt284, pkt285, pkt286, pkt287, pkt288, pkt289, pkt290, pkt291, pkt292, pkt293, pkt294, pkt295, pkt296, pkt297, pkt298, pkt299, pkt300, pkt301, pkt302, pkt303, pkt304, pkt305, pkt306, pkt307, pkt308, pkt309, pkt310, pkt311, pkt312, pkt313, pkt314, pkt315, pkt316, pkt317, pkt318, pkt319, pkt320, pkt321, pkt322, pkt323, pkt324, pkt325, pkt326, pkt327, pkt328, pkt329, pkt330, pkt331, pkt332, pkt333, pkt334, pkt335, pkt336, pkt337, pkt338, pkt339, pkt340, pkt341, pkt342, pkt343, pkt344, pkt345, pkt346, pkt347, pkt348, pkt349, pkt350, pkt351, pkt352, pkt353, pkt354, pkt355, pkt356, pkt357, pkt358, pkt359, pkt360, pkt361, pkt362, pkt363, pkt364, pkt365, pkt366, pkt367, pkt368, pkt369, pkt370, pkt371, pkt372, pkt373, pkt374, pkt375, pkt376, pkt377, pkt378, pkt379, pkt380, pkt381, pkt382, pkt383, pkt384, pkt385, pkt386, pkt387, pkt388, pkt389, pkt390, pkt391, pkt392, pkt393, pkt394, pkt395, pkt396, pkt397, pkt398, pkt399, pkt400, pkt401, pkt402, pkt403, pkt404, pkt405, pkt406, pkt407, pkt408, pkt409, pkt410, pkt411, pkt412, pkt413, pkt414, pkt415, pkt416, pkt417, pkt418, pkt419, pkt420, pkt421, pkt422, pkt423, pkt424, pkt425, pkt426, pkt427, pkt428, pkt429, pkt430, pkt431, pkt432, pkt433, pkt434, pkt435, pkt436, pkt437, pkt438, pkt439, pkt440, pkt441, pkt442, pkt443, pkt444, pkt445, pkt446, pkt447, pkt448, pkt449, pkt450, pkt451, pkt452, pkt453, pkt454, pkt455, pkt456, pkt457, pkt458, pkt459, pkt460, pkt461, pkt462, pkt463, pkt464, pkt465, pkt466, pkt467, pkt468, pkt469, pkt470, pkt471, pkt472, pkt473, pkt474, pkt475, pkt476, pkt477, pkt478, pkt479, pkt480, pkt481, pkt482, pkt483, pkt484, pkt485, pkt486, pkt487, pkt488, pkt489, pkt490, pkt491, pkt492, pkt493, pkt494, pkt495, pkt496, pkt497, pkt498, pkt499, pkt500, pkt501, pkt502, pkt503, pkt504, pkt505, pkt506, pkt507, pkt508, pkt509, pkt510, pkt511, pkt512, pkt513, pkt514, pkt515, pkt516, pkt517, pkt518, pkt519, pkt520, pkt521, pkt522, pkt523, pkt524, pkt525, pkt526, pkt527, pkt528, pkt529, pkt530, pkt531, pkt532, pkt533, pkt534, pkt535, pkt536, pkt537, pkt538, pkt539, pkt540, pkt541, pkt542, pkt543, pkt544, pkt545, pkt546, pkt547, pkt548, pkt549, pkt550, pkt551, pkt552, pkt553, pkt554, pkt555, pkt556, pkt557, pkt558, pkt559, pkt560, pkt561, pkt562, pkt563, pkt564, pkt565, pkt566, pkt567, pkt568, pkt569, pkt570, pkt571, pkt572, pkt573, pkt574, pkt575, pkt576, pkt577, pkt578, pkt579, pkt580, pkt581, pkt582, pkt583, pkt584, pkt585, pkt586, pkt587, pkt588, pkt589, pkt590, pkt591, pkt592, pkt593, pkt594, pkt595, pkt596, pkt597, pkt598, pkt599, pkt600, pkt601, pkt602, pkt603, pkt604, pkt605, pkt606, pkt607, pkt608, pkt609, pkt610, pkt611, pkt612, pkt613, pkt614, pkt615, pkt616, pkt617, pkt618, pkt619, pkt620, pkt621, pkt622, pkt623, pkt624, pkt625, pkt626, pkt627, pkt628, pkt629, pkt630, pkt631, pkt632, pkt633, pkt634, pkt635, pkt636, pkt637, pkt638, pkt639, pkt640, pkt641, pkt642, pkt643, pkt644, pkt645, pkt646, pkt647, pkt648, pkt649, pkt650, pkt651, pkt652, pkt653, pkt654, pkt655, pkt656, pkt657, pkt658, pkt659, pkt660, pkt661, pkt662, pkt663, pkt664, pkt665, pkt666, pkt667, pkt668, pkt669, pkt670, pkt671, pkt672, pkt673, pkt674, pkt675, pkt676, pkt677, pkt678, pkt679, pkt680, pkt681, pkt682, pkt683, pkt684, pkt685, pkt686, pkt687, pkt688, pkt689, pkt690, pkt691, pkt692, pkt693, pkt694, pkt695, pkt696, pkt697, pkt698, pkt699, pkt700, pkt701, pkt702, pkt703, pkt704, pkt705, pkt706, pkt707, pkt708, pkt709, pkt710, pkt711, pkt712, pkt713, pkt714, pkt715, pkt716, pkt717, pkt718, pkt719, pkt720, pkt721, pkt722, pkt723, pkt724, pkt725, pkt726, pkt727, pkt728, pkt729, pkt730, pkt731, pkt732, pkt733, pkt734, pkt735, pkt736, pkt737, pkt738, pkt739, pkt740, pkt741, pkt742, pkt743, pkt744, pkt745, pkt746, pkt747, pkt748, pkt749, pkt750, pkt751, pkt752, pkt753, pkt754, pkt755, pkt756, pkt757, pkt758, pkt759, pkt760, pkt761, pkt762, pkt763, pkt764, pkt765, pkt766, pkt767, pkt768, pkt769, pkt770, pkt771, pkt772, pkt773, pkt774, pkt775, pkt776, pkt777, pkt778, pkt779, pkt780, pkt781, pkt782, pkt783, pkt784, pkt785, pkt786, pkt787, pkt788, pkt789, pkt790, pkt791, pkt792, pkt793, pkt794, pkt795, pkt796, pkt797, pkt798, pkt799, pkt800, pkt801, pkt802, pkt803, pkt804, pkt805, pkt806, pkt807, pkt808, pkt809, pkt810, pkt811, pkt812, pkt813, pkt814, pkt815, pkt816, pkt817, pkt818, pkt819, pkt820, pkt821, pkt822, pkt823, pkt824, pkt825, pkt826, pkt827, pkt828, pkt829, pkt830, pkt831, pkt832, pkt833, pkt834, pkt835, pkt836, pkt837, pkt838, pkt839, pkt840, pkt841, pkt842, pkt843, pkt844, pkt845, pkt846, pkt847, pkt848, pkt849, pkt850, pkt851, pkt852, pkt853, pkt854, pkt855, pkt856, pkt857, pkt858, pkt859, pkt860, pkt861, pkt862, pkt863, pkt864, pkt865, pkt866, pkt867, pkt868, pkt869, pkt870, pkt871, pkt872, pkt873, pkt874, pkt875, pkt876, pkt877, pkt878, pkt879, pkt880, pkt881, pkt882, pkt883, pkt884, pkt885, pkt886, pkt887, pkt888, pkt889, pkt890, pkt891, pkt892, pkt893, pkt894, pkt895, pkt896, pkt897, pkt898, pkt899, pkt900, pkt901, pkt902, pkt903, pkt904, pkt905, pkt906, pkt907, pkt908, pkt909, pkt910, pkt911, pkt912, pkt913, pkt914, pkt915, pkt916, pkt917, pkt918, pkt919, pkt920, pkt921, pkt922, pkt923, pkt924, pkt925, pkt926, pkt927, pkt928, pkt929, pkt930, pkt931, pkt932, pkt933, pkt934, pkt935, pkt936, pkt937, pkt938, pkt939, pkt940, pkt941, pkt942, pkt943, pkt944, pkt945, pkt946, pkt947, pkt948, pkt949, pkt950, pkt951, pkt952, pkt953, pkt954, pkt955, pkt956, pkt957, pkt958, pkt959, pkt960, pkt961, pkt962, pkt963, pkt964, pkt965, pkt966, pkt967, pkt968, pkt969, pkt970, pkt971, pkt972, pkt973, pkt974, pkt975, pkt976, pkt977, pkt978, pkt979, pkt980, pkt981, pkt982, pkt983, pkt984, pkt985, pkt986, pkt987, pkt988, pkt989, pkt990, pkt991, pkt992, pkt993, pkt994, pkt995, pkt996, pkt997, pkt998, pkt999, pkt1000, pkt1001, pkt1002, pkt1003, pkt1004, pkt1005, pkt1006, pkt1007, pkt1008, pkt1009, pkt1010, pkt1011, pkt1012, pkt1013, pkt1014, pkt1015, pkt1016, pkt1017, pkt1018, pkt1019, pkt1020, pkt1021, pkt1022, pkt1023, pkt1024, pkt1025, pkt1026, pkt1027, pkt1028, pkt1029, pkt1030, pkt1031, pkt1032, pkt1033, pkt1034, pkt1035, pkt1036, pkt1037, pkt1038, pkt1039, pkt1040, pkt1041, pkt1042, pkt1043, pkt1044, pkt1045, pkt1046, pkt1047, pkt1048, pkt1049, pkt1050, pkt1051, pkt1052, pkt1053, pkt1054, pkt1055, pkt1056, pkt1057, pkt1058, pkt1059, pkt1060, pkt1061, pkt1062, pkt1063, pkt1064, pkt1065, pkt1066, pkt1067, pkt1068, pkt1069, pkt1070, pkt1071, pkt1072, pkt1073, pkt1074, pkt1075, pkt1076, pkt1077, pkt1078, pkt1079, pkt1080, pkt1081, pkt1082, pkt1083, pkt1084, pkt1085, pkt1086, pkt1087, pkt1088, pkt1089, pkt1090, pkt1091, pkt1092, pkt1093, pkt1094, pkt1095, pkt1096, pkt1097, pkt1098, pkt1099, pkt1100, pkt1101, pkt1102, pkt1103, pkt1104, pkt1105, pkt1106, pkt1107, pkt1108, pkt1109, pkt1110, pkt1111, pkt1112, pkt1113, pkt1114, pkt1115, pkt1116, pkt1117, pkt1118, pkt1119, pkt1120, pkt1121, pkt1122, pkt1123, pkt1124, pkt1125, pkt1126, pkt1127, pkt1128, pkt1129, pkt1130, pkt1131, pkt1132]
TIMES = [1761416561.577484, 1761416561.588376, 1761416561.600340, 1761416561.620103, 1761416561.632742, 1761416561.645061, 1761416561.658619, 1761416561.670056, 1761416561.684341, 1761416561.702808, 1761416561.716156, 1761416561.727604, 1761416561.737365, 1761416561.754681, 1761416561.776338, 1761416561.793164, 1761416561.808979, 1761416561.828883, 1761416561.845211, 1761416561.855991, 1761416561.865921, 1761416561.892084, 1761416561.922756, 1761416561.936882, 1761416561.948509, 1761416561.962477, 1761416561.982022, 1761416562.003148, 1761416562.037767, 1761416562.054112, 1761416562.084941, 1761416562.118168, 1761416562.135154, 1761416562.155224, 1761416562.169977, 1761416562.190486, 1761416562.203223, 1761416562.213427, 1761416562.225857, 1761416562.250357, 1761416562.263300, 1761416562.276963, 1761416562.295071, 1761416562.308045, 1761416562.327846, 1761416562.347547, 1761416562.365078, 1761416562.375458, 1761416562.388138, 1761416562.417846, 1761416562.430591, 1761416562.444226, 1761416562.462521, 1761416562.477492, 1761416562.498063, 1761416562.513748, 1761416562.530637, 1761416562.544029, 1761416562.567985, 1761416562.580369, 1761416562.593346, 1761416562.607974, 1761416562.679639, 1761416562.702402, 1761416562.716177, 1761416562.729197, 1761416562.740108, 1761416562.765381, 1761416562.777627, 1761416562.789476, 1761416562.799624, 1761416562.817807, 1761416562.830987, 1761416562.849524, 1761416562.874909, 1761416562.889877, 1761416562.905528, 1761416562.934396, 1761416562.948906, 1761416562.959699, 1761416562.974774, 1761416563.015075, 1761416563.024561, 1761416563.039984, 1761416563.052142, 1761416563.069004, 1761416563.081537, 1761416563.099175, 1761416563.114781, 1761416563.132299, 1761416563.149132, 1761416563.160275, 1761416563.173249, 1761416563.207632, 1761416563.223437, 1761416563.236015, 1761416563.248977, 1761416563.259938, 1761416563.287306, 1761416563.301328, 1761416563.311903, 1761416563.328607, 1761416563.348980, 1761416563.364882, 1761416563.381947, 1761416563.392177, 1761416563.405245, 1761416563.434993, 1761416563.447835, 1761416563.464948, 1761416563.483265, 1761416563.493856, 1761416563.526222, 1761416563.539661, 1761416563.567503, 1761416563.580562, 1761416563.597757, 1761416563.608336, 1761416563.620703, 1761416563.648692, 1761416563.660958, 1761416563.678007, 1761416563.695981, 1761416563.716381, 1761416563.729153, 1761416563.754569, 1761416563.773054, 1761416563.786434, 1761416563.798989, 1761416563.812748, 1761416563.844019, 1761416563.860399, 1761416563.880519, 1761416563.891703, 1761416563.934598, 1761416563.950894, 1761416563.962672, 1761416563.986243, 1761416564.001449, 1761416564.013806, 1761416564.049239, 1761416564.062845, 1761416564.074428, 1761416564.091208, 1761416564.105296, 1761416564.123277, 1761416564.138223, 1761416564.158820, 1761416564.173234, 1761416564.191186, 1761416564.250617, 1761416564.267982, 1761416564.293686, 1761416564.305211, 1761416564.325251, 1761416564.339005, 1761416564.361385, 1761416564.373052, 1761416564.386696, 1761416564.404166, 1761416564.446660, 1761416564.475170, 1761416564.490744, 1761416564.510890, 1761416564.521987, 1761416564.534706, 1761416564.548092, 1761416564.569938, 1761416564.589046, 1761416564.604158, 1761416564.644598, 1761416564.658845, 1761416564.686146, 1761416564.718386, 1761416564.739473, 1761416564.756775, 1761416564.769553, 1761416564.788006, 1761416564.805875, 1761416564.826128, 1761416564.841914, 1761416564.854634, 1761416564.868307, 1761416564.908694, 1761416564.920389, 1761416564.933123, 1761416564.946499, 1761416564.961221, 1761416564.977795, 1761416564.999475, 1761416565.013499, 1761416565.031350, 1761416565.053913, 1761416565.067300, 1761416565.088828, 1761416565.102485, 1761416565.119305, 1761416565.131686, 1761416565.143734, 1761416565.161295, 1761416565.178012, 1761416565.192345, 1761416565.205035, 1761416565.229801, 1761416565.250407, 1761416565.263435, 1761416565.282838, 1761416565.298629, 1761416565.318801, 1761416565.335271, 1761416565.362988, 1761416565.376361, 1761416565.398218, 1761416565.420205, 1761416565.439744, 1761416565.458752, 1761416565.473885, 1761416565.486960, 1761416565.499563, 1761416565.518064, 1761416565.535198, 1761416565.551387, 1761416565.566246, 1761416565.588390, 1761416565.605412, 1761416565.623427, 1761416565.636551, 1761416565.651840, 1761416565.670498, 1761416565.689723, 1761416565.717457, 1761416565.730206, 1761416565.752210, 1761416565.788016, 1761416565.811075, 1761416565.822581, 1761416565.834941, 1761416565.849901, 1761416565.864330, 1761416565.882379, 1761416565.910815, 1761416565.922255, 1761416565.934689, 1761416565.955364, 1761416565.988298, 1761416566.003694, 1761416566.017484, 1761416566.033437, 1761416566.052607, 1761416566.068713, 1761416566.080575, 1761416566.099852, 1761416566.124478, 1761416566.134814, 1761416566.160311, 1761416566.175502, 1761416566.187538, 1761416566.200433, 1761416566.218528, 1761416566.234613, 1761416566.259314, 1761416566.290531, 1761416566.306195, 1761416566.329307, 1761416566.343312, 1761416566.355587, 1761416566.375396, 1761416566.400455, 1761416566.419831, 1761416566.452651, 1761416566.482323, 1761416566.498891, 1761416566.522773, 1761416566.541611, 1761416566.560867, 1761416566.573247, 1761416566.603385, 1761416566.627860, 1761416566.638058, 1761416566.650014, 1761416566.663335, 1761416566.697418, 1761416566.723851, 1761416566.735436, 1761416566.753108, 1761416566.777642, 1761416566.792513, 1761416566.814191, 1761416566.830105, 1761416566.848531, 1761416566.868809, 1761416566.885646, 1761416566.901243, 1761416566.918715, 1761416566.949575, 1761416566.984335, 1761416567.011194, 1761416567.027056, 1761416567.071511, 1761416567.084980, 1761416567.095957, 1761416567.107829, 1761416567.125630, 1761416567.146898, 1761416567.161346, 1761416567.218043, 1761416567.231416, 1761416567.256820, 1761416567.271473, 1761416567.345360, 1761416567.367421, 1761416567.385896, 1761416567.406991, 1761416567.422349, 1761416567.455343, 1761416567.469968, 1761416567.491785, 1761416567.505667, 1761416567.523809, 1761416567.542204, 1761416567.561734, 1761416567.579811, 1761416567.595432, 1761416567.610091, 1761416567.632646, 1761416567.653312, 1761416567.670225, 1761416567.695731, 1761416567.710204, 1761416567.736903, 1761416567.757160, 1761416567.779866, 1761416567.796128, 1761416567.819706, 1761416567.844117, 1761416567.861363, 1761416567.883440, 1761416567.896463, 1761416567.920022, 1761416567.934123, 1761416567.954270, 1761416567.969721, 1761416567.998728, 1761416568.016131, 1761416568.030273, 1761416568.047956, 1761416568.065251, 1761416568.077282, 1761416568.089289, 1761416568.111456, 1761416568.136693, 1761416568.151406, 1761416568.181593, 1761416568.199554, 1761416568.219720, 1761416568.240989, 1761416568.253126, 1761416568.265814, 1761416568.288792, 1761416568.300033, 1761416568.321308, 1761416568.334681, 1761416568.344602, 1761416568.355410, 1761416568.370374, 1761416568.386530, 1761416568.404041, 1761416568.416298, 1761416568.431430, 1761416568.460077, 1761416568.475547, 1761416568.494697, 1761416568.508697, 1761416568.524887, 1761416568.542128, 1761416568.560975, 1761416568.583121, 1761416568.601692, 1761416568.630028, 1761416568.645211, 1761416568.666404, 1761416568.697721, 1761416568.709961, 1761416568.729335, 1761416568.748276, 1761416568.768624, 1761416568.794227, 1761416568.806863, 1761416568.818635, 1761416568.844701, 1761416568.857948, 1761416568.871270, 1761416568.889520, 1761416568.907017, 1761416568.924840, 1761416568.941040, 1761416568.953909, 1761416568.970707, 1761416568.994285, 1761416569.009522, 1761416569.028388, 1761416569.040717, 1761416569.055902, 1761416569.070689, 1761416569.091279, 1761416569.109568, 1761416569.127008, 1761416569.138239, 1761416569.151097, 1761416569.174298, 1761416569.196072, 1761416569.219310, 1761416569.236161, 1761416569.265789, 1761416569.284474, 1761416569.301111, 1761416569.324060, 1761416569.338610, 1761416569.359364, 1761416569.374911, 1761416569.404227, 1761416569.417356, 1761416569.435521, 1761416569.446534, 1761416569.463867, 1761416569.482833, 1761416569.510161, 1761416569.533128, 1761416569.555758, 1761416569.586129, 1761416569.600586, 1761416569.636371, 1761416569.650531, 1761416569.669842, 1761416569.690511, 1761416569.708126, 1761416569.721947, 1761416569.743483, 1761416569.798962, 1761416569.816939, 1761416569.836799, 1761416569.849494, 1761416569.861480, 1761416569.900055, 1761416569.913231, 1761416569.932220, 1761416569.953015, 1761416569.966161, 1761416569.985809, 1761416570.013547, 1761416570.025244, 1761416570.037416, 1761416570.052191, 1761416570.069088, 1761416570.088081, 1761416570.109825, 1761416570.120603, 1761416570.138771, 1761416570.162266, 1761416570.177267, 1761416570.196083, 1761416570.222307, 1761416570.236720, 1761416570.250276, 1761416570.263570, 1761416570.282272, 1761416570.303457, 1761416570.325797, 1761416570.338505, 1761416570.366249, 1761416570.383262, 1761416570.397023, 1761416570.410400, 1761416570.431616, 1761416570.452925, 1761416570.476344, 1761416570.493505, 1761416570.506614, 1761416570.563240, 1761416570.608065, 1761416570.628586, 1761416570.640543, 1761416570.659524, 1761416570.672766, 1761416570.687105, 1761416570.699624, 1761416570.713039, 1761416570.730611, 1761416570.747942, 1761416570.759538, 1761416570.770809, 1761416570.795073, 1761416570.806438, 1761416570.817290, 1761416570.831364, 1761416570.869564, 1761416570.889181, 1761416570.905777, 1761416570.917455, 1761416570.938147, 1761416570.962309, 1761416570.974496, 1761416570.995285, 1761416571.031217, 1761416571.050209, 1761416571.067113, 1761416571.085384, 1761416571.099127, 1761416571.115392, 1761416571.145969, 1761416571.162292, 1761416571.175567, 1761416571.188966, 1761416571.227480, 1761416571.255800, 1761416571.271404, 1761416571.283412, 1761416571.298746, 1761416571.326705, 1761416571.344620, 1761416571.357042, 1761416571.376110, 1761416571.403240, 1761416571.417033, 1761416571.444456, 1761416571.460301, 1761416571.502576, 1761416571.517335, 1761416571.540362, 1761416571.555369, 1761416571.569864, 1761416571.595121, 1761416571.610717, 1761416571.630568, 1761416571.647502, 1761416571.676243, 1761416571.687891, 1761416571.699913, 1761416571.712076, 1761416571.728365, 1761416571.744985, 1761416571.765293, 1761416571.778863, 1761416571.799004, 1761416571.821290, 1761416571.834277, 1761416571.853222, 1761416571.871324, 1761416571.885051, 1761416571.899961, 1761416571.934538, 1761416571.957112, 1761416571.981688, 1761416571.993345, 1761416572.017825, 1761416572.059430, 1761416572.071919, 1761416572.093868, 1761416572.124585, 1761416572.152627, 1761416572.171750, 1761416572.192623, 1761416572.209193, 1761416572.221594, 1761416572.245645, 1761416572.257741, 1761416572.277998, 1761416572.318800, 1761416572.332972, 1761416572.345282, 1761416572.362474, 1761416572.382404, 1761416572.416857, 1761416572.429472, 1761416572.444657, 1761416572.466442, 1761416572.486797, 1761416572.503566, 1761416572.516790, 1761416572.554503, 1761416572.573805, 1761416572.603115, 1761416572.617915, 1761416572.636070, 1761416572.667187, 1761416572.683878, 1761416572.705088, 1761416572.719284, 1761416572.733701, 1761416572.745374, 1761416572.766548, 1761416572.783820, 1761416572.802454, 1761416572.813348, 1761416572.825705, 1761416572.850493, 1761416572.863107, 1761416572.879164, 1761416572.891933, 1761416572.988672, 1761416573.007113, 1761416573.072806, 1761416573.095766, 1761416573.109632, 1761416573.133987, 1761416573.152312, 1761416573.166464, 1761416573.182942, 1761416573.197633, 1761416573.218676, 1761416573.236603, 1761416573.249866, 1761416573.263167, 1761416573.288812, 1761416573.306138, 1761416573.336197, 1761416573.360100, 1761416573.375744, 1761416573.394446, 1761416573.439745, 1761416573.453951, 1761416573.468272, 1761416573.520023, 1761416573.556928, 1761416573.570614, 1761416573.587038, 1761416573.602856, 1761416573.624378, 1761416573.671331, 1761416573.686635, 1761416573.701468, 1761416573.729833, 1761416573.742584, 1761416573.753728, 1761416573.769582, 1761416573.784101, 1761416573.806807, 1761416573.834708, 1761416573.858161, 1761416573.875802, 1761416573.905960, 1761416573.918906, 1761416573.929987, 1761416573.944770, 1761416573.963158, 1761416573.981791, 1761416574.000702, 1761416574.021142, 1761416574.051366, 1761416574.073849, 1761416574.088417, 1761416574.109541, 1761416574.122063, 1761416574.138548, 1761416574.170834, 1761416574.190079, 1761416574.201422, 1761416574.218068, 1761416574.242918, 1761416574.255280, 1761416574.267137, 1761416574.283314, 1761416574.295148, 1761416574.314070, 1761416574.353593, 1761416574.365017, 1761416574.378931, 1761416574.401572, 1761416574.435035, 1761416574.448320, 1761416574.466456, 1761416574.481711, 1761416574.505701, 1761416574.528521, 1761416574.558478, 1761416574.577449, 1761416574.597181, 1761416574.612414, 1761416574.627438, 1761416574.639823, 1761416574.652894, 1761416574.671761, 1761416574.693974, 1761416574.705354, 1761416574.719779, 1761416574.877395, 1761416574.892294, 1761416574.905784, 1761416574.916819, 1761416574.940367, 1761416574.960743, 1761416574.981520, 1761416575.005695, 1761416575.025629, 1761416575.041798, 1761416575.058310, 1761416575.069710, 1761416575.082705, 1761416575.094795, 1761416575.112064, 1761416575.126420, 1761416575.144431, 1761416575.157612, 1761416575.181668, 1761416575.194528, 1761416575.212027, 1761416575.228753, 1761416575.273857, 1761416575.292183, 1761416575.311288, 1761416575.350970, 1761416575.367280, 1761416575.392312, 1761416575.426315, 1761416575.446635, 1761416575.460071, 1761416575.476290, 1761416575.492152, 1761416575.507015, 1761416575.517161, 1761416575.530249, 1761416575.555732, 1761416575.575377, 1761416575.588710, 1761416575.600244, 1761416575.630712, 1761416575.654038, 1761416575.679317, 1761416575.691601, 1761416575.707498, 1761416575.728481, 1761416575.753523, 1761416575.791961, 1761416575.803291, 1761416575.818905, 1761416575.843134, 1761416575.858618, 1761416575.868085, 1761416575.885148, 1761416575.914056, 1761416575.925680, 1761416575.940563, 1761416575.958191, 1761416575.972862, 1761416575.994134, 1761416576.018664, 1761416576.062437, 1761416576.080834, 1761416576.101663, 1761416576.117119, 1761416576.128792, 1761416576.141024, 1761416576.154245, 1761416576.177305, 1761416576.195331, 1761416576.210588, 1761416576.226979, 1761416576.250211, 1761416576.259739, 1761416576.274530, 1761416576.294640, 1761416576.311375, 1761416576.332146, 1761416576.349918, 1761416576.362227, 1761416576.380288, 1761416576.399411, 1761416576.412780, 1761416576.425175, 1761416576.445398, 1761416576.463671, 1761416576.479909, 1761416576.522279, 1761416576.534697, 1761416576.546761, 1761416576.568763, 1761416576.580654, 1761416576.599808, 1761416576.614630, 1761416576.630647, 1761416576.653098, 1761416576.669755, 1761416576.681617, 1761416576.702226, 1761416576.722947, 1761416576.737798, 1761416576.747970, 1761416576.761468, 1761416576.776154, 1761416576.807537, 1761416576.826814, 1761416576.838856, 1761416576.851609, 1761416576.874256, 1761416576.887315, 1761416576.907850, 1761416576.926887, 1761416576.948094, 1761416576.987686, 1761416577.017100, 1761416577.027479, 1761416577.043146, 1761416577.063795, 1761416577.085305, 1761416577.101799, 1761416577.113391, 1761416577.127576, 1761416577.150840, 1761416577.165706, 1761416577.199568, 1761416577.214071, 1761416577.235417, 1761416577.365169, 1761416577.386854, 1761416577.400171, 1761416577.437132, 1761416577.452058, 1761416577.469833, 1761416577.485493, 1761416577.529894, 1761416577.545502, 1761416577.560853, 1761416577.572857, 1761416577.589016, 1761416577.601275, 1761416577.623376, 1761416577.634619, 1761416577.661121, 1761416577.683445, 1761416577.699129, 1761416577.721753, 1761416577.752659, 1761416577.764641, 1761416577.779138, 1761416577.788756, 1761416577.818263, 1761416577.834271, 1761416577.851850, 1761416577.883786, 1761416577.906020, 1761416577.934661, 1761416577.956914, 1761416577.969015, 1761416577.998096, 1761416578.011932, 1761416578.038090, 1761416578.051470, 1761416578.068626, 1761416578.082707, 1761416578.101586, 1761416578.113548, 1761416578.133925, 1761416578.182962, 1761416578.200612, 1761416578.219546, 1761416578.236165, 1761416578.248665, 1761416578.261470, 1761416578.277604, 1761416578.289635, 1761416578.306741, 1761416578.329295, 1761416578.345018, 1761416578.359377, 1761416578.373126, 1761416578.386945, 1761416578.406181, 1761416578.426761, 1761416578.442551, 1761416578.456732, 1761416578.477745, 1761416578.526054, 1761416578.538613, 1761416578.572655, 1761416578.584247, 1761416578.604224, 1761416578.618464, 1761416578.639785, 1761416578.652487, 1761416578.694271, 1761416578.707197, 1761416578.734132, 1761416578.752269, 1761416578.760866, 1761416578.775592, 1761416578.782316, 1761416578.798018, 1761416578.804504, 1761416578.816865, 1761416578.822593, 1761416578.834400, 1761416578.840244, 1761416578.850635, 1761416578.855918, 1761416578.872325, 1761416578.877810, 1761416578.888998, 1761416578.893965, 1761416578.906488, 1761416578.911458, 1761416578.933429, 1761416578.938899, 1761416578.950590, 1761416578.955499, 1761416578.969466, 1761416578.974425, 1761416578.984580, 1761416578.989507, 1761416579.002566, 1761416579.007493, 1761416579.025633, 1761416579.030714, 1761416579.044228, 1761416579.049250, 1761416579.060714, 1761416579.065679, 1761416579.077394, 1761416579.082304, 1761416579.094085, 1761416579.099092, 1761416579.125605, 1761416579.130999, 1761416579.145767, 1761416579.151111, 1761416579.163267, 1761416579.168448, 1761416579.188669, 1761416579.194012, 1761416579.207687, 1761416579.213052, 1761416579.236282, 1761416579.241877, 1761416579.258806, 1761416579.264318, 1761416579.277351, 1761416579.282808, 1761416579.324567, 1761416579.330719, 1761416579.366292, 1761416579.373079, 1761416579.399843, 1761416579.401911, 1761416579.415900, 1761416579.417897, 1761416579.437019, 1761416579.440410, 1761416579.452744, 1761416579.455421, 1761416579.476265, 1761416579.478939, 1761416579.511195, 1761416579.514853, 1761416579.537381, 1761416579.539845, 1761416579.553155, 1761416579.555177, 1761416579.567038, 1761416579.569028, 1761416579.587739, 1761416579.590230, 1761416579.604070, 1761416579.606741, 1761416579.622943, 1761416579.625856, 1761416579.653204, 1761416579.656056, 1761416579.671695, 1761416579.673755, 1761416579.687724, 1761416579.690194, 1761416579.701017, 1761416579.702636, 1761425766.182490, 1761425766.197331, 1761425766.217878, 1761425766.232132, 1761425766.245790, 1761425766.259001, 1761425766.270345, 1761425766.286153, 1761425766.301993, 1761425766.318218, 1761425766.335435, 1761425766.366761, 1761425766.408830, 1761425766.438465, 1761425766.461080, 1761425766.512464, 1761425766.524144, 1761425766.550514, 1761425766.563465, 1761425766.577065, 1761425766.600775, 1761425766.614915, 1761425766.627015, 1761425766.642252, 1761425766.655881, 1761425766.672853, 1761425766.709370, 1761425766.740382, 1761425766.770758, 1761425766.794738, 1761425766.808643, 1761425766.825480, 1761425766.853272, 1761425766.868044, 1761425766.885708, 1761425766.912851, 1761425766.926055, 1761425766.939225, 1761425766.949959, 1761425766.966483, 1761425767.006731, 1761425767.019899, 1761425767.033938, 1761425767.049004, 1761425767.064138, 1761425767.078264, 1761425767.089663, 1761425767.116317, 1761425767.128317, 1761425767.140462, 1761425767.153697, 1761425767.166983, 1761425767.179657, 1761425767.189809, 1761425767.243660, 1761425767.260329, 1761425767.272870, 1761425767.283669, 1761425767.301149, 1761425767.316281, 1761425767.326614, 1761425767.342493, 1761425767.353967, 1761425767.371379, 1761425767.384685, 1761425767.400183, 1761425767.415062, 1761425767.432474, 1761425767.448126, 1761425767.462179, 1761425767.477022, 1761425767.481984, 1761425767.495349, 1761425767.500952, 1761425767.511987, 1761425767.516585, 1761425767.533970, 1761425767.538535, 1761425767.552019, 1761425767.556701, 1761425767.569250, 1761425767.573168, 1761425767.588760, 1761425767.593151, 1761425767.604596, 1761425767.608425, 1761425767.620036, 1761425767.623721, 1761425767.638267, 1761425767.642337, 1761425767.654318, 1761425767.657901, 1761425767.671281, 1761425767.674876, 1761425767.691973, 1761425767.695718, 1761425767.706757, 1761425767.710964, 1761425767.723376, 1761425767.727736, 1761425767.742140, 1761425767.746074, 1761425767.758578, 1761425767.762392, 1761425767.772664, 1761425767.776601, 1761425767.791888, 1761425767.795908, 1761425767.808834, 1761425767.812915, 1761425767.822450, 1761425767.826787, 1761425767.869407, 1761425767.874429, 1761425767.886895, 1761425767.891420, 1761425767.903788, 1761425767.908436, 1761425767.919293, 1761425767.923488, 1761425767.937437, 1761425767.941890, 1761425767.962041, 1761425767.966575, 1761425767.978040, 1761425767.982559, 1761425767.994258, 1761425767.998746, 1761425768.019193, 1761425768.020507, 1761425768.037024, 1761425768.038326, 1761425768.052194, 1761425768.053844, 1761425768.066082, 1761425768.067652, 1761425768.085773, 1761425768.087733, 1761425768.100774, 1761425768.102289, 1761425768.114626, 1761425768.115585, 1761425768.128392, 1761425768.129407, 1761425768.141033, 1761425768.142090, 1761425768.157861, 1761425768.160664, 1761425768.174340, 1761425768.175433, 1761425768.189600, 1761425768.191388, 1761425768.206088, 1761425768.208622, 1761425768.224869, 1761425768.227198, 1761425768.247649, 1761425768.249027, 1761425768.266315, 1761425768.269259]

def _burst(iface: str, preserve_delta: bool):
    if preserve_delta and len(PKTS) > 1:
        t0 = TIMES[0]
        for p, t in zip(PKTS, TIMES):
            time.sleep(t - t0)
            t0 = t
            sendp(p, iface=iface, verbose=False)
    else:
        sendp(PKTS, iface=iface, inter=0, verbose=False)

def main():
    ap = argparse.ArgumentParser(description="Replay captured traffic once or in a loop")
    ap.add_argument("-i", "--iface", required=True, help="Interface to send on")
    ap.add_argument("--delta", action="store_true", help="Preserve original inter‑packet timing")
    ap.add_argument("--loop", action="store_true", help="Loop indefinitely")
    args = ap.parse_args()

    print(f"Sending {len(PKTS)} packets on {args.iface} …")
    if args.loop:
        while True:
            _burst(args.iface, args.delta)
    else:
        _burst(args.iface, args.delta)
    print("Done.")

if __name__ == "__main__":
    main()
