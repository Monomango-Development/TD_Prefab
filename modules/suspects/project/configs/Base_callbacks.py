'''Info Header Start
Name : Base_callbacks
Author : wieland@MONOMANGO
Saveorigin : Project.toe
Saveversion : 2022.32660
Info Header End'''
def GetConfigSchema(CollectionValue, CollectionDict, CollectionList):

	positiveValue = CollectionValue(default = 4, validator = lambda value : value > 0)

	return {
    	"Some_Integer" : CollectionValue( 
			default = -2, 
			validator = lambda value: value < 4,
			typecheck = (float, int)
		 ),
    	"Some_String"   : CollectionValue( default = "foo", validator= lambda value: isinstance( value, str)),
    	"Subdata" : CollectionDict({
        	"Sub" : CollectionValue( default = 13, validator= lambda value: value < 14 ),
			"SubDict" : CollectionDict({
				"SubSubValue" : CollectionValue( 
					default = "Foobar",
					typecheck = str,
					parser = lambda value: value.upper()
				)
			})
    		}),
    	"Sublist" : CollectionList( ),
	    "Prefilled_Sublist" : CollectionList(
			["Hello", "WOrld"]
		),
		"PositiveValue" : positiveValue(),
		"Prefilled_Validated" : CollectionList(
			items = [1,2,3],
			default_member = CollectionValue(default = -1, validator = lambda value: value < 3)
		)
		}
		
		
#def GetConfigData():
#	return a jsonString. Can be used to fetch API data or similiar.
#	return ""