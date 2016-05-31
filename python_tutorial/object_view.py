import requests

class ObjectView(object):

    def __init__(self, d):
        self.__dict__ = d

    def check_kwargs(self, param, retry=3, **kwargs):
        chk = kwargs.pop("check",None)
        print "check value = %s " % chk
        print "retry value = %s " % retry
        print "param value = %s " % param

    def form_command(self, **kwargs):
        cmd = "file-server edit "
        for k in kwargs.keys():
            args = '%s=%s ' %(k, kwargs[k])
            cmd += args
        print cmd         

def sample_dict(d):

   print d

def main():

    d = {'a' : 'mine', 'b': 1}
    o = ObjectView(d)
    print "Property a = %s" %(o.a)
    setattr(o, 'name', 'Sab')
    print o.name
    kwargs = {"check" : "sab"}
    o.check_kwargs('save', 
                   **kwargs)
    c = 'b'
    sample_dict({'a' : c}) 
    t = '5' if 2<1 else '10'
    print t
    kwargs = {"memory": 5, "cpu_count" : 10}
    o.form_command(**kwargs) 
       


if __name__ == '__main__':
    main()
