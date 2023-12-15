from argparse import ArgumentParser , FileType
from threading import Thread
from requests import get, exceptions
from time import time 

subdomains =[]
def prepare_words():
    """Generator function for words
    """
    words= arguments.wordlist.read().split()
    for word in words:
        yield word


def prepare_args():
    """Prepare Arguments 

         return: 
             args(argparse.Namespace)
    
    """

    parser = ArgumentParser(description="Python Based Fast Sub Domain Finder",usage="%(prog)s google.com",epilog="Example - %(prog)s -w /usr/share/wordlist.txt -t 500 -V google.com")
    parser.add_argument(metavar="Domain",dest="domain",help="Doamin Name")
    parser.add_argument("-w","--wordlist",dest="wordlist",metavar="",type=FileType("r"), help="wordlist of subdomains",default="wordlist.txt")
    parser.add_argument("-t","--threads",dest="threads",type=int,help="threads to use",default=500)
    parser.add_argument("-V","--verbose",action="store_true",help="verbose output")
    parser.add_argument("-v","--version",action="version",help="print version",version="%(prog)s 1.0")
    args=parser.parse_args()
    return args





def check_subdomain():
    """check subdomain for 200
    """

    while True:
        try:
            word=next(words)
            url= f"https://{word}.{arguments.domain}"
            request=get(url,timeout=5)
            if request.status_code==200:
                subdomains.append(url)
                if arguments.verbose:
                    print(url)
        except (exceptions.ConnectionError, exceptions.ReadTimeout):
            continue
        except StopIteration:
            break






def prepare_threads():
    """Create,start,join threads
    """
    thread_list=[]
    for _ in range(arguments.threads):
        thread_list.append(Thread(target=check_subdomain))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()










if __name__=="__main__":
    arguments = prepare_args()
    words= prepare_words()
    start_time = time()
    prepare_threads()
    end_time = time()
    print("Sub Domains Found - \n"+"\n".join(i for i in subdomains))
    print(f"Time taken - {round(end_time-start_time,2)}")



                                   



    