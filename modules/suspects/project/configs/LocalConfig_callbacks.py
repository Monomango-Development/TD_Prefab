'''Info Header Start
Name : LocalConfig_callbacks
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2022.32660
Info Header End'''
from typing import Type

def GetConfigSchema(configValue:Type["ConfigValue"], collectionDict:Type["CollectionDict"], collectionList:Type["CollectionList"]) -> dict:

	positiveValue = configValue(default = 4, validator = lambda value : value > 0)
	
	return {
    	"Some_Integer" : configValue( 
			default = -2, 
			validator = lambda value: value < 4,
			typecheck = (float, int)
		 ),
    	"Some_String"   : configValue( default = "foo", validator= lambda value: isinstance( value, str)),
    	"Subdata" : collectionDict({
        	"Sub" : configValue( default = 13, validator= lambda value: value < 14 ),
			"SubDict" : collectionDict({
				"SubSubValue" : configValue( 
					default = "Foobar",
					typecheck = str,
					parser = lambda value: value.upper()
				)
			})
    		}),
    	"Sublist" : collectionList( ),
	    "Prefilled_Sublist" : collectionList(
			["Hello", "WOrld"]
		),
		"PositiveValue" : positiveValue(),
		"Prefilled_Validated" : collectionList(
			items = [1,2,3],
			default_member = configValue(default = -1, validator = lambda value: value < 3)
		)
		}
		
		
#def GetConfigData():
#	return a jsonString. Can be used to fetch API data or similiar.
#	return ""