# Dont wanna deal with ipv6...no one does.

def possible_ip_addresses(num_str:str):
    '''
    Get all possible consecutive combinations of IP addresses from a string of numbers (<=12 digits long).
    '''
    size = len(num_str)
    ip_list = []
    if not num_str.isdigit() or size > 12: return ip_list
    s = num_str
    for a in range(1,size-2):
        for b in range(a+1,size-1):
            for c in range(b+1,size):
                s = [num_str[0:a],num_str[a:b],num_str[b:c],num_str[c:]]
                invalid = False
                for o in s:
                    d = len(o)
                    if (d > 3) or (int(o) > 255) or (o[0] == "0" and d > 1):
                        invalid = True
                        break
                if not invalid: ip_list.append(".".join(s))
    return ip_list

if __name__ == '__main__':
    i = input('Enter numbers:\n>')
    ips = possible_ip_addresses(i)
    print(*ips,sep='\n')