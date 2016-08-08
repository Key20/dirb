import sys, argparse, requests, validators


def arguments():
    param = argparse.ArgumentParser(description='Example: python dirb -u http://example.com/ -l list.txt')
    param.add_argument('-u', '--url')
    param.add_argument('-l', '--list')
    return  param

parser = arguments()
args = parser.parse_args(sys.argv[1:])
list_file = open(args.list, 'r')

if args.url == None or args.list == None:
    print('Example: python dirb -u http://example.com/ -l list.txt')

else:
    if validators.url(args.url) == True:
        url = args.url
        list = []
        dir_list = []
        for i in list_file:
            list.append(i.rstrip('\n'))
        for i in list:
            status_code = requests.get(url+i).status_code
            full_url = url + i
            if status_code == 200 or status_code == 403 and full_url.rfind('/') != len(full_url)-1:
                print('Code: ' + str(status_code) +  ', URL: ' + url+i)
            elif status_code == 200 and full_url.rfind('/') == len(full_url)-1:
                    dir_list.append(full_url)
        for i in dir_list:
            print('----- DIR: ' + i)


    else:
        print('Example: python dirb -u http://example.com/ -l list.txt')
        exit(2)