import pocket_constants
from pocket_retrieve import PocketRetrieve

class Pocket:

    def __init__(self):
        self.pocketRetriever = PocketRetrieve()

    def mapInitialInput(self,x):
        return {
            'R': self.preRetrieve,
            'A': self.fakeNews,
            'M': self.fakeNews
        }.get(x, self.whatDoesTheUserWantToDo)

    def fakeNews(self):
        print 'fake news'

    def mapRetrieveInput(self,x):
        return {
            'T': pocket_constants.tag,
            'U': pocket_constants.untagged,
        }.get(x, "No match")

    def preRetrieve(self):
        optionParams = []
        print "Provide options"
        choices = raw_input("Please input your choices, separated by comma: ").upper()
        choiceslist = choices.replace(' ', '').split(',')
        print choiceslist
        for choice in choiceslist:
            response = self.mapRetrieveInput(choice)
            if response != 'No match':
                optionParams.append(response)
                for param in optionParams:
                    for key in param:
                        if param[key] == '_to_be_replaced_':
                            param[key] = raw_input('pls enter a value for ' + key + ':')
        self.pocketRetriever.retrieve(optionParams)

        def postRetrieve():
            pass

    def whatDoesTheUserWantToDo(self):
        print pocket_constants.retrieveText
        print pocket_constants.addText
        print pocket_constants.modifyText
        selectedOption = raw_input("Please select one of the above options: ").upper()
        self.mapInitialInput(selectedOption)()

if __name__ == '__main__':
    Pocket().whatDoesTheUserWantToDo()
