def XXLDOLL(func):
    print ("Opening XXLDOLL")

    def XLDOLL():
        print ("Opening XLDOLL")

        def LDOLL():
            print ("Opening LDOLL")

            def MDOLL():
                print ("Opening MDOLL")

                def SDOLL():
                    print ("Opening SDOLL")

                    def XSDOLL():
                        print ("Opening XSDOLL")
                        return func

                    return XSDOLL()

                return SDOLL()

            return MDOLL()

        return LDOLL()
    
    return XLDOLL()

                
@XXLDOLL
def RUSSIANDOLL():
    return "DOLL"

print(RUSSIANDOLL())
