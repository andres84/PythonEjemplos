class continuarenfor(object):
    
    def contienfor(self):
        coleccion = [2, 4, 5, 7, 8, 9, 3, 4]
        for e in coleccion:
            if e % 2 != 0:
                continue
            print(e)

objeto = continuarenfor()
objeto.contienfor()




