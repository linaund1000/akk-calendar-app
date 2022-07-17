import tkinter as tk
import datetime as dt
'''A calendar for teachers to follow lessons with their students 
'''

class App():
    
    def __init__(self,root):
        '''root is created windows(our gui) with tkinter tk.TK() everything we write here will occur in that window '''
        

        
        root.geometry('1020x540+100+200')
        #not to allow resize for having a good size of button (just for now)



                                                       ###FRAMES

        #configuration frames
        root.rowconfigure(0,weight=1)
        root.rowconfigure(1,weight=10)
        root.columnconfigure(0,weight=9)#calendars
        root.columnconfigure(1,weight=1)#students
    
        
        #creating_frames
        calendar_info_frame = tk.Frame(root,highlightbackground="white", highlightthickness=5,bg='#d2cef5')#up side
        students_info_frame = tk.Frame(root,highlightbackground='white',highlightthickness=5,bg='#d2cef5')
  
        calendar_frame = tk.Frame(root,highlightbackground="white", highlightthickness=5,bg='#d2cef5')#down side
        students_list_frame = tk.Frame(root,highlightbackground="white",highlightthickness=5,bg = '#d2cef5',) 

        
        ##replacing the frames
        calendar_info_frame.grid(row=0,column=0,sticky='news')
        students_info_frame.grid(row=0,column=1,sticky='news')
        
        calendar_frame.grid(row=1,column=0,sticky='news')
        students_list_frame.grid(row=1,column=1,sticky='news')
        

        ####Creating the widgets through classes into frames
        self.student_part = Students_widget_maker(students_list_frame)#row = 1 / column = 1
        self.calendar_part = Calendar_widget_maker(calendar_frame) #row = 1 / column= 0  
        
        self.student_info_widget = Students_info_widget_maker(students_info_frame) #row = 0 / column = 1       
        self.calendar_info_widget = Calendar_info_widget_maker(calendar_info_frame,self.calendar_part) #row = 0 / column = 0
        
        
        root.mainloop()
        
        
class Students_info_widget_maker:
    #row = 0 , column = 1
    def __init__(self,frame):
        self.stud_name = 'all'
        self.label = tk.Label(frame,text='STUDENTS NAME!!')
        self.label.grid()

        
class Calendar_info_widget_maker:
    def __init__(self,frame,calendar_part):
        '''Controll only calendar part not students'''
        
        
        self.calendar_part = calendar_part
        self.frame = frame
        
        self.calendar_format = 'Week' #shows days and day information
        

        self.button = tk.Button(self.frame,text = self.calendar_format,width=10,height=3,command=self.change_calendar_format)      
        self.button.grid()
    
    def change_calendar_format(self):
        if self.calendar_format == 'Week':
            
            self.calendar_format = 'Day' #transform calendar into =day= format
            self.calendar_part.lectures_of_spesific_day()
            
        elif self.calendar_format == 'Day':
            
            self.calendar_format = 'Week' #transform calendar into =week= format
            self.calendar_part.days_of_week()
            
        else:
            self.calendar_format = 'Week'
        
        
        self.informatic_widget_maker()      

    def informatic_widget_maker(self):
        #refresh buttons format and condition week|day
        self.button.destroy()
        self.button = tk.Button(self.frame,width=10,height=3,text = self.calendar_format,command=self.change_calendar_format)      
        self.button.grid()
            
        
class Students_widget_maker():
    ''''''
    def __init__(self,Frame):
        '''this frames position is on the right side of app row=1,column=1'''
        control_frame = tk.Frame(Frame)
        

        st_number = 0
        student_list=['tugba','ata','seyma']#students_info.student_list will be here in the future
        '''instead of using for loop i can use something else like radiobutton'''
        for i in student_list:
            
            tk.Button(Frame,text=i).grid(column=0,row=st_number,padx=5,pady=3,ipady=10,ipadx=10,sticky='w')
            st_number +=1
   
class Calendar_widget_maker():
    def __init__(self,frame):
        '''calendar_ class will occur in frame that we add as a parameter,left side row=1 ,column=0'''
        self.today = dt.date.today()#'2022-19-7-16:30' 
        self.frame = frame
        self.days_of_week()#shows buttons
        
        
        #INFORMATION will COME hHERE FROM STUDENTS LECTURE INFO$$$
    def days_of_week(self):#which week we need to know
        ##this section shows week on the screen as button
        for widget in self.frame.winfo_children():
            widget.destroy()
        buttons_day = self.today
        for day in range(7):#days of week
    
            tk.Button(self.frame,text=f'{buttons_day}', width=9 , height=2 ,borderwidth=2, bg='white',fg='black').grid(row=day , column=1, padx=5,pady=3,ipady=10,ipadx=10,sticky='n')
            #all the buttons in frame created
            
            buttons_day = buttons_day + dt.timedelta(days=1)
              
    def  lectures_of_spesific_day(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        lecture_list = ['15:00','16:30']
        n = 0
        for lecture in lecture_list:
            
            tk.Button(self.frame,text=f'{lecture}',width=9 , height=2 ,borderwidth=2, bg='white',fg='black').grid(row=n, column=1, padx=5,pady=3,ipady=10,ipadx=10,sticky='n')
            n = n+1
    
    
    def lecture_informations(self):#lecture
            for widget in self.frame.winfo_children():
                widget.destroy()
      
if __name__ == '__main__':
    root = tk.Tk()#creating window
    app=App(root) #writing with classes give us more control
           
        
        
        
