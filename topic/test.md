##Saida mak Test ?
Test mak parte ida nebe ita uza atu prova ita nia projektu nebe ita halo hodi hare katak ita nia projektu lao 
ho los ka lae, Ho Django iha Python jerál iha dalan prinsipál rua atu hakerek teste ba projetu mak  
test doctests no unittest.
**1. Doctests hakerek tiha ona iha Python docstrings ne'ebe ita teste iha ligasaun maka'as ho ita-nia funsaun 
docstrings no hakerek tiha ona iha maneira ida-ne ' ebé emulates sesaun ida hosi durubasa/interprete interativu Python nian. Ezemplu**

    def my_func(a_list, idx):
        """
        >>> a = ['larry', 'curly', 'moe']
        >>> my_func(a, 0)
        'larry'
        >>> my_func(a, 1)
        'curly'
        """
        return a_list[idx]

**2. unit teste defini ho klase.
unit teste – teste ne ' ebé mak hato'o nu'udar métodu ida iha Python nian class unittest no subclasses. 
Unitteat.TestCase ka Django nian liu TestCase. Ezemplu:** 
    import unittest
    from BankAccount import BankAccount


    class TestBankAccount(unittest.TestCase):
         
         def test(self):
             self.assertEqual('a', 'a')
             self.assertNotEqual('a', 'b')
             
             self.assertTrue(True)    
             self.assertFalse(False) 
         
         def test_add(self):
             account = BankAccount()
             amount = account.add(100) 
             
             self.assertEqual(account.amount, 100)
         self.assertEqual(amount, 100) 


###Oinsa mak atu run test ba ita nia projektu nebe mak ita halo hanesan Test ambiente (environment)

Molok ita atu test ita nia projektu ba dahuluk ita presiza tama ba diretóriu site nebe mak ita kria ona iha environment
no ita loke tuir command python nian mak hanesan 

    python manage.py test
 
Ita sei haree rezultadu ne ' ebé hanesan ho ida-ne'e:

    ----------------------------------------------------------------------
    Ran 22 tests in 0.221s

    OK