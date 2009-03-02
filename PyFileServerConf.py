
# Note: This file is in python syntax and format


##################################################################################################
# INITIALIZATION - Do not modify this section
config_mapping = dict()
user_mapping = dict()
desc_mapping = dict()
resAL_mapping = dict()
resAL_library = dict()

def addAL(descriptor, resAL):
    resAL_library[descriptor] = resAL

def addrealm(realmname, localdir, resALdescriptor=None):
    config_mapping['/' + realmname] = localdir
    resAL_mapping['/' + realmname] = resALdescriptor

def adduser(realmname, user, password, description):
    realmname = '/' + realmname
    if realmname not in user_mapping:
        user_mapping[realmname] = dict([])
    user_mapping[realmname][user] = password
    if realmname not in desc_mapping:
        desc_mapping[realmname] = dict([])
    desc_mapping[realmname][user] = description

        
##################################################################################################
# SERVER OPTIONS

# Property Options

#propsmanager =  # uncomment this line to specify your own locks manager                    
                 # default: pyfileserver.propertylibrary.PropertyManager

#propsfile =     # uncomment this line to specify a storage file location 
                 # for pyfileserver.propertylibrary.PropertyManager
                 # default: PyFileServer.dat in current directory


# Locks Options

#locksmanager =  # uncomment this line to specify your own locks manager                    
                 # default: pyfileserver.propertylibrary.LockManager

#locksfile =     # uncomment this line to specify a storage file location 
                 # for pyfileserver.propertylibrary.LockManager
                 # default: PyFileServer.locks in current directory

# Domain Controller

#domaincontroller =   # uncomment this line to specify your own domain controller
                      # default: pyfileserver.pyfiledomaincontroller
                      #          uses USERS section below

# HTTP Authentication Options

acceptbasic = True        # Allow basic authentication, True or False
acceptdigest = True       # Allow digest authenticatoin, True or False
defaultdigest = True      # True (default digest) or False (default basic)

# Verbose Output

verbose = 2          # 0 - no output (excepting application exceptions)         
                     # 1 - show single line request summaries (for logging)
                     # 2 - show full request/response header info (HTTP Logging)
                     #     request body and GET response bodies not shown
           
# Organizational Information - printed as a footer on html output

Info_AdminEmail = 'divinekid@gmail.com'
Info_Organization = 'Haoyu Bai'



##################################################################################################
# RESOURCE ABSTRACTION LAYERS
# To register a resource abstraction layer (for use in the next section REALMS):
# addAL(registered_name, resource_abstraction_layer_instance)
#

#from pyfileserver.fileabstractionlayer import ReadOnlyFilesystemAbstractionLayer, FilesystemAbstractionLayer
#addAL("readonlyfs", ReadOnlyFilesystemAbstractionLayer())
#addAL("fs", FilesystemAbstractionLayer())

from pyfileserver.btfs.abstraction_layer import AbstractionLayer
addAL("btfs", AbstractionLayer())


##################################################################################################
# REALMS
# if you would like to access files in the location 'c:\v_root' through PyFileServer as
# http://server:port/v_root, insert the following:
#   addrealm('vroot', 'c:\v_root', '')
#
# The last field refers to the registered name of the abstraction layer to use (register
# in the above section RESOURCE ABSTRACTION LAYERS). 
#   addAL('myowndatabase', MyOwnDatabaseAbstractionLayer()) 
#   addrealm('db', 'database:\UserDB', 'myowndatabase')
#  
# If you wish to share files using the default resource abstraction layer provided by
# PyFileServer, simply omit the field.
#   addrealm('file', 'C:\files')
#

addrealm('file', '/', 'btfs')


##################################################################################################
# USERS
# adduser('v_root' , 'user', 'password', 'description')  
# If no users are specified for a realm, no authentication is required to fully access the realm 
#
# Note: If you wish to use Windows WebDAV support (such as Windows XP's My Network Places),
# you need to include the domain of the user as part of the username (note the DOUBLE slash), 
# such as:
# adduser('v_root', 'domain\\user', 'password', 'description')

