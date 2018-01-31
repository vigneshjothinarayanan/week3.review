#class Subnet_calculator:






def net_id(ip_addr):













def ip_address(ip,netmask):
    ip_addr=ip.split(".")
    dict_of_dotted={128:1,192:2,224:3,240:4,248:5,252:6,254:7,255:8}
    dict_of_cidr={1:128,2:192,3:224,4:240,5:252,6:252,7:254,8:255}

    if netmask>24 and netmask<32:
        key_value=32-netmask
        key_for_dict=8-key_value
        netmask_in_dotted_list=["255","255","255",str(dict_of_cidr.get(key_for_dict))]
        netmask_in_dotted=".".join(netmask_in_dotted_list)
        print("ip address: " ,ip,"\nnetmask(dotted decimal) :",netmask_in_dotted)

    elif netmask>16 and netmask<25:
        key_value=24-netmask
        key_for_dict=8-key_value
        netmask_in_dotted_list=["255","255",str(dict_of_cidr.get(key_for_dict)),"0"]
        netmask_in_dotted=".".join(netmask_in_dotted_list)
        print("ip address: " ,ip,"\nnetmask(dotted decimal) :",netmask_in_dotted)

    elif netmask>8 and netmask<17:
        key_value=16-netmask
        key_for_dict=8-key_value
        netmask_in_dotted_list=["255",str(dict_of_cidr.get(key_for_dict)),"0","0"]
        netmask_in_dotted=".".join(netmask_in_dotted_list)
        print("ip address: " ,ip,"\nnetmask(dotted decimal) :",netmask_in_dotted)

    elif netmask>0 and netmask<9:
        key_value=8-netmask
        key_for_dict=key_value
        netmask_in_dotted_list=[str(dict_of_cidr.get(key_for_dict)),"0","0","0"]
        netmask_in_dotted=".".join(netmask_in_dotted_list)
        print("ip address: " ,ip,"\nnetmask(dotted decimal) :",netmask_in_dotted)

    elif netmask<=0 or netmask>=32:
        print("invalid netmask")


ip_address("192.168.0.10",31)
