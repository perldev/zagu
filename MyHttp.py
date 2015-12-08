import httplib, urllib
import logging

def my_url(U):
    Index=0
    Length=len(U)
    try:
        Index=U.index("http://",0)
    except :
        Index=None

    if Index is None :
        try :
            Path=U.index("/",0)
            return [ U[0:Path ]  , U[ Path:  Length ] ]
        except :
            return [U,"/"]
    else :
        Index+=7
        try :
            Path=U.index("/",Index)
            return [ U[ Index:Path ]  , U[ Path:  Length ] ]
        except :
            return [U [ Index: Length ],"/"]


def my_connect(U,Data):
        [Domain,Path] = my_url(U)
        conn = httplib.HTTPConnection(Domain)
        params = urllib.urlencode(Data)
        conn.request("POST",Path,params)
        r = conn.getresponse()
        headers = r.getheaders()
        Data = r.read()
        #logging.debug("log web request " + Data)
        return Data