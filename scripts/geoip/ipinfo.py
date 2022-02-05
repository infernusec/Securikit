import geoip2.database
import sys
import multiprocessing

db_path = './geoipdb'
asn_reader = geoip2.database.Reader(db_path+'/GeoLite2-ASN.mmdb')
city_reader = geoip2.database.Reader(db_path+'/GeoLite2-City.mmdb')

def ipInfo(ip,save_as=None):
        try:
                asn_response = asn_reader.asn(ip)
                city_response = city_reader.city(ip)
                content = str(asn_response.autonomous_system_number)+" | "+ip+" | "+city_response.country.iso_code+" | "+asn_response.autonomous_system_organization
                if save_as is not None:
                    results_file = open(save_as,'a')
                    results_file.write(content+"\n")
                    results_file.close()
                else:
                    print(content)
        except:
                print("[Skipping]: IP {} is not in Database".format(ip))
                pass

if __name__ == '__main__':
    if not sys.stdin.isatty():
        ip=sys.stdin.read().rstrip()
        ipInfo(ip)
    else:
        filename = 'sorted-ipdb.txt'
        save_as = 'sorted-ipdb-results.txt'
        with open(filename,'r') as file:
            for line in file:
                flines = line.rstrip()
                p = multiprocessing.Process(target=ipInfo, args=(flines,save_as))
                p.start()
    print("Done!")
