# ZeroTrust
ZeroTrust is a project with many information to secure Networks, Servers, IOT and more..
with this project you can able to reduce cyber attacks on your site, your servers, and your network.

The project containts:
1. Bad hosts (with ASN numbers) that can be potentially to cyber attacks.
2. Bad User agents (Like crawlers and scanners)
3. VPN / Proxy Providers that attackers use.
4. Internet scanner blocking (like shodan, censys, etc..)
5. TOR exit-nodes blocking. (Prevent access to your network from TOR network).



## List of hosts that can be potentially to cyber attacks..

### which attacks? Injections, Spams, Scams, Brute force, DDoS, Proxys, VPN etc...


| ISP | Countries / Regions | ASN | Links |
| ------ | ------ | ------ | ------ |
| AWS (Amazon Cloud) | [Click to view](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html) | 64512 | https://ip-ranges.amazonaws.com/ip-ranges.json https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html|
| GCP (Google Cloud) || 36040 ||
| DigitalOcean | US (NY,SF), EU, CA, DE, NL | 14061 ||
| Hetzner | DE,SF,US (W-D.C) | 24940 ||
| Zare || 25369, 200039 ||
| Kamatera || 210329, 36007, 64022, 204548 ||
| Hostinger || 47583 ||
| Unified Layer || 46606 | |
| OVH || 16276 ||
| Alibaba Cloud || 45102 ||
| Heficed || 61317 ||
| Contabo | [Click to view](https://contabo.com/en/locations/) | 51167, 40021 ||
| ChinaNet Jiangsu | CN | 23650 ||
| ACEVILLE PTE.LTD | HK | 139341 ||
| Private Layer INC | PA | 51852 ||
| Tencent Cloud Computing (Beijing) Co., Ltd | CN | 133478 ||
| The Calyx Institute | US | 4224 ||
| Censys | US | 398324 ||
| LG DACOM Corporation | KR | 3786 ||
| Linode | US | 63949 ||
| CHINA UNICOM China169 Backbone | CN | 4837 ||
| Chinanet | CN | 4134 ||
| TE-AS | EG | 8452 ||
| Axtel, S.A.B. de C.V. | MX | 6503 ||





# Block VPN Providers
https://www.vpngate.net/en/


# Block Auto Scanners (Shodan, Censys,)

More at Checkpoint - https://community.checkpoint.com/t5/Management/HowTo-Block-IoT-scanners-like-Shodan-Censys-Shadowserver-PAN/td-p/124612

Censys - https://support.censys.io/hc/en-us/articles/360043177092-Opt-Out-of-Scanning

Shodan - https://wiki.ipfire.org/configuration/firewall/blockshodan

BinaryEdge - https://api.binaryedge.io/v1/minions 


# Block Bad Useragents

[Click here](https://udger.com/resources/ua-list/crawlers) to find out more crawlers.

| Useragent  | String |
| ------ | ------ |
| Censys Scanner | ```Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)``` |


# Block TOR Exit nodes

https://www.dan.me.uk/torlist/

