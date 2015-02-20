import sys
from api import apiUrl,apiKey
from wordnik import swagger,WordApi

if len(sys.argv)<=1:
    print "No word given to search for. Usage 'define <word>'."
else:
    word = sys.argv[1];
    #Initialise client
    client = swagger.ApiClient(apiKey, apiUrl);

    wordApi = WordApi.WordApi(client);
    definitions = wordApi.getDefinitions(word,sourceDictionaries='wiktionary');
    if not definitions:
    	    print "Trying for "+word.lower();
	    definitions = wordApi.getDefinitions(word.lower(),sourceDictionaries='wiktionary');
    if definitions==None:
        print "No such word found. Check the spelling and try again"
    else:
        for definition in definitions:
	    print definition.partOfSpeech+": "+definition.text;
