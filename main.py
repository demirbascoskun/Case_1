
class ArrayProcess:

    @staticmethod
    def RemoveDuplicates(*args):
        cleaned_array = []
        for arr in args:
            cleaned_array += [x for x in arr]
        return set(cleaned_array)
    
    @staticmethod
    def SeperateEventOddNumbers(arr):
        if len(arr) == 0:
            raise ValueError('You can not seperate empyt array !')

        even_odd_dict = {'Even':[],"Odd":[]}
        for element in arr:
            if type(element) != int:
                continue
            if element % 2 == 0:
                even_odd_dict['Even'].append(element)
            else:
                even_odd_dict['Odd'].append(element)
        return even_odd_dict





       

array1= ["1","2",4,5,6,7,8,9,10,12,14,15,17,'3']




print((ArrayProcess.SeperateEventOddNumbers(array1)))
print((ArrayProcess.RemoveDuplicates(array1)))