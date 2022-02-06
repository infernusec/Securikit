# IP Scrapers & Useful Scripts

## Sort IPv4 Addresses By numeric
```cat ip-list.txt | sort -t . -k 1,1n -k 2,2n -k 3,3n -k 4,4n```

## AbuseIPDB last 24 hour reports
```for i in {1..136}; do curl 'https://www.abuseipdb.com/sitemap?page='$i   -H 'authority: www.abuseipdb.com'   -H 'pragma: no-cache'   -H 'cache-control: no-cache'   -H 'sec-ch-ua: " Not;A Brand";v="99", "Microsoft Edge";v="97", "Chromium";v="97"'   -H 'sec-ch-ua-mobile: ?0'   -H 'sec-ch-ua-platform: "Windows"'   -H 'upgrade-insecure-requests: 1'   -H 'dnt: 1'   -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76'   -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'   -H 'sec-fetch-site: same-origin'   -H 'sec-fetch-mode: navigate'   -H 'sec-fetch-user: ?1'   -H 'sec-fetch-dest: document'   -H 'referer: https://www.abuseipdb.com/sitemap?page=133'   -H 'accept-language: en-US,en;q=0.9'   -H 'cookie: __cf_bm=o8b18oSIvQ7GNZHLy_z.IfAuvZg0AHzATcic8TQZ.hU-1643976784-0-AXlX1R5yxPi7VoV7brEyGkMWD0PkmcwfW1ZvpkS8zf1IithYLu90LLVDZG04Qhq2FG4V49sNkc66Wt71bZxA6V2gG+Eub7JeSfqvLqzHmtho38GHx9SkdRuZ/FbjySaqrA==; XSRF-TOKEN=eyJpdiI6IkZmZU9yNGEzUGFNOCtaSmJyMlcxOFE9PSIsInZhbHVlIjoibVc5WWVZTEJMcEczMWtpeG9QYTM0T1d3N2h3M0VXOHEydWZqTjU4dUIwa3NSV1ZZdGNRR3RvT1wvWE1vTlkwRk0iLCJtYWMiOiI1NDc3NTk2OGU4NjFmYzc4MGExNWU1Yzg4OWEzMDdjZTM3ZjdiZDQwZjY3NzdjYjVjMThlZmI0MGZkMjQxMWJhIn0%3D; abuseipdb_session=eyJpdiI6Ik9DeTRBSW5xOEsraVN6bVh4cjhROFE9PSIsInZhbHVlIjoiK0FuKzk2S2tpeXJiOFFGN0VWbmVzUGpzUmd4OEVcL2V2TnkrMVVXWU5uNkJoZ25qS3F5ODBXcklPTWt1NG8zY1YiLCJtYWMiOiJmNTY3NzNjNTc2ZGM1NjhjYTIxNjM3YTNhMTU0ZTdiNjdiYzZjOWE1YzJlZWQ4YzNiMTVjMGVmYmZiNGYwMjM3In0%3D'   --compressed | grep '<a href="https://www.abuseipdb.com/check/' | cut -d '/' -f5 | cut -d '"' -f1 >> ipdb.log; done```

## VPNGate IP Addresses 
```curl -s http://www.vpngate.net/api/iphone/ | cut -d ',' -f2 | tail -n +2 | head -n -1```

## VPNBook IP Addresses
##### hostnames
```curl https://www.vpnbook.com/freevpn | grep '<li><strong>' | cut -d '>' -f3 | cut -d '<' -f1```
##### ipv4 resovled
```curl https://www.vpnbook.com/freevpn | grep '<li><strong>' | cut -d '>' -f3 | cut -d '<' -f1 | while IFS= read -r line; do host "$line" | awk '{ print $4 }'; done```
