from list.tad_lista.linked_list import LinkedList
from list.ex_01.cliente import Customer


class Company:
    def __init__(self, company_name: str, customer_list: LinkedList = None):
        self.__company_name = company_name
        if customer_list is None:
            self.__costumer_list = LinkedList()
        else:
            self.__costumer_list = customer_list

    @property
    def company_name(self):
        return self.__company_name

    def show_custumers(self):
        string = '[\n'
        for customer in self.__costumer_list:
            string += f'({customer.name}, {customer.cpf}), \n'
        string += ']'
        print(string)

    def insert_customer(self, name: str, cpf: str):
        if not self.contains(cpf):
            self.__costumer_list.append(Customer(name, cpf))
        else:
            print('Customer is already registered.')

    def contains(self, cpf: str):
        for customer in self.__costumer_list:
            if customer.cpf == cpf:
                return True
        return False

    def n_registered_customers(self):
        return self.__costumer_list.size()

