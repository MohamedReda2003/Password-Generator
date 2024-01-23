import random  

import flet as ft




class Password_Generator:
    
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "@#$&_-()=%*:/!?+."
    
    string_all = lower + upper + numbers + symbols
    string_except_number_symbols=lower+upper
    string_except_number=lower+upper+symbols
    string_except_symbol=lower+upper+numbers
    
    def __init__(self,page,length,add_number,add_symbol):
        self.page=page
        self.length=int(length)
        self.add_number=add_number
        self.add_symbol=add_symbol
    
    def psd_without_symbol(self):
        password = "".join(random.sample(self.string_except_symbol, self.length))
        while password[0] not in self.lower:
            if password[0] in self.upper :
                break
            # print(password)
            password = "".join(random.sample(self.string_except_symbol, self.length))
        return password
        
    def psd_without_number(self):
        password = "".join(random.sample(self.string_except_number, self.length))
        while password[0] not in self.lower:
            if password[0] in self.upper :
                break
            # print(password)
            password = "".join(random.sample(self.string_except_number, self.length))
        return password
    
    def psd_without_number_symbol(self):
        password = "".join(random.sample(self.string_except_number_symbols, self.length))
        while password[0] not in self.lower:
            if password[0] in self.upper :
                break
            # print(password)
            password = "".join(random.sample(self.string_except_number_symbols, self.length))
        return password
    
    def psd_with_all_possibilities(self):
        password = "".join(random.sample(self.string_all, self.length))
        while password[0] not in self.lower:
            if password[0] in self.upper :
                break
            password = "".join(random.sample(self.string_all, self.length))
        return password
    
    def generate(self,e):

        if self.add_number==True and self.add_symbol==True:
            psd=self.psd_with_all_possibilities()
        elif self.add_number==True and self.add_symbol==False:
            psd=self.psd_without_symbol()
        elif self.add_number==False and self.add_symbol==True:
            psd=self.psd_without_number()
        elif self.add_number==False and self.add_symbol==False:
            psd=self.psd_without_number_symbol()

        
        print('Password is: ',psd)
        return psd
        




def main(page):
    page.title = "Password Generator"
    page.bgcolor="DARK"
    
    
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    txt_number = ft.Text(value="Password Generator",size=70, text_align=ft.TextAlign.CENTER, width=300,bgcolor=ft.colors.RED,weight=ft.FontWeight.W_100)
    
    numbers = ft.Checkbox(label="Do you want to have numbers in the generated password?")
    symbols= ft.Checkbox(label="Do you want to have special characters in the generated password?")
    length=ft.TextField(label="legth of the password you want")
    print(length.value)
    
    execute_btn=ft.ElevatedButton(text="Generate a password")
    
    def execute(e):
        
        letter=False
        print(length)
        if length.value:
            for i in length.value :
                if not i.isdigit():
                    letter=True
                    print("This is not an integer")
                    break
            if letter==False:
                page.clean()
                # print('checked out')
                password_generator=Password_Generator(page,length.value, numbers.value, symbols.value).generate(e)
                txt_number = ft.Text(value=password_generator,size=35, text_align=ft.TextAlign.CENTER, width=500,bgcolor=ft.colors.GREEN,weight=ft.FontWeight.NORMAL)
                # page.add()
                return_btn=ft.ElevatedButton(text="Go back",on_click=home)
                page.add(ft.Row([txt_number],alignment=ft.MainAxisAlignment.CENTER),
                         ft.Row([return_btn],alignment=ft.MainAxisAlignment.CENTER)
                        )
        else :
            pass
        page.update()
        
        
    execute_btn.on_click=execute
        
        
    def home(e):   
        page.clean()
        page.add(ft.Row([txt_number],alignment=ft.MainAxisAlignment.CENTER),
                 ft.Row([numbers],alignment=ft.MainAxisAlignment.CENTER),
                 ft.Row([symbols],alignment=ft.MainAxisAlignment.CENTER),
                 ft.Row([length],alignment=ft.MainAxisAlignment.CENTER),
                 ft.Row([execute_btn],alignment=ft.MainAxisAlignment.CENTER)
                )
    page.add(ft.Row([txt_number],alignment=ft.MainAxisAlignment.CENTER),
             ft.Row([numbers],alignment=ft.MainAxisAlignment.CENTER),
             ft.Row([symbols],alignment=ft.MainAxisAlignment.CENTER),
             ft.Row([length],alignment=ft.MainAxisAlignment.CENTER),
             ft.Row([execute_btn],alignment=ft.MainAxisAlignment.CENTER)
            )






ft.app(target=main)




        
    
