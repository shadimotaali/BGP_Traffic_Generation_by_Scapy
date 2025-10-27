# BGP_Traffic_Generation_by_Scapy
Python-based BGP traffic generator using Scapy. Produces RFC 4271-compliant, labeled datasets with balanced normal/anomalous traffic for ML training. Supports IPv4/IPv6, multiple attack types, and exports to PCAP/CSV formats.
A systematic methodology for generating **balanced and realistic BGP traffic** specifically designed for training machine learning-based anomaly detection systems. This tool addresses critical limitations in existing BGP datasets: severe class imbalance, ambiguous labeling, and insufficient anomalous traffic.

## 🎯 Key Features

- **RFC-Compliant Traffic Generation**: Full compliance with BGP-4 (RFC 4271), Multiprotocol BGP (RFC 4760), and related specifications
- **Balanced Datasets**: Generate controllable ratios of normal to anomalous traffic (default 50-50, customizable)
- **Perfect Ground-Truth Labels**: IP ID-based labeling provides unambiguous classification of normal vs. attack traffic
- **Multiple Attack Scenarios**: Prefix hijacking, AS path manipulation, UPDATE flooding (DoS attacks)
- **Dual-Stack Support**: Complete IPv4 and IPv6 BGP session generation
- **Realistic Temporal Characteristics**: Pareto-distributed inter-packet delays matching real BGP traffic patterns
- **Multiple Export Formats**: 
  - PCAP files for Wireshark analysis
  - CSV files with extracted BGP attributes for ML feature engineering
- **Validated Traffic**: Cross-validated with GNS3 simulations, Cisco packet traces, and PCAP-to-Scapy reverse engineering


## 🚀 Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/BGP_Traffic_Generation_by_Scapy.git
