# bejaye copy paste kardane function ha mitonim dar yek function benevisim

class logger:

    # vaghti obj logger farakhani mishe function init ham bash farakhani mishe va yek filename
    # ro migire 
    def __init__(self, filename):
        self.file_name = filename

    def __s(self, msg):
        print(msg)


    def _write_log(self, level, msg):
        with open(self.file_name, 'a') as log_file:
            log_file.write("[{0}]{1}\n".format(level, msg))


    # on obj ke misazim dar asl on obj miad ja self 
    def critical(self, msg):
        self.write_log("CRITICAL", msg)

    def error(self, msg):
        self.write_log("ERROR", msg)

    def warning(self, msg):
        self.write_log("WARNING", msg)

    def debug(self, msg):
        self.write_log("DEBUG", msg)


    def info(self, msg):
        self.write_log("INFO", msg)

    def __str__(self):
        return "this is logger object"





# 2

class SingltonObject(object):

    class __SingletonObject():

        def __init__(self):
            self.val = None



        def __str__(self):
            pass




