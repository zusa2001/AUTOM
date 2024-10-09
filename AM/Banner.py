import time
from datetime import datetime
# ANSI escape sequence for colors
green_color = "\033[92m"
blue_color = "\033[94m"
reset_color = "\033[0m"

def print_welcome_banner():
    ascii_art = f"""
    {blue_color}                                                

                  ⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⣛⣉⣙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⠀⣾⠋⠁⠀⠀⠀⠑⣿⣆⠀⢠⡤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⢸⡇⠀⡴⠋⠑⣄⢤⡤⠧⣤⣬⣦⢤⣵⣤⣀⣠⢴⣶⡶⠶⠿⠿⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⣘⣤⠿⠛⠛⠅⠀⠀⠀⠈⠉⠙⢿⣧⡀⠀⣀⣀⣀⠀⠙⢿⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⢸⡇⠀⣲⡟⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡿⡍⠁⠀⠙⡗⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⢸⡇⠊⣷⠋⠰⠒⠄⠀⠀⠀⠀⠀⠀⠀⡖⡆⠀⠀⠀⠀⠈⢇⢧⠀⠀⠀⠁⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⠘⡇⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡎⣾⣛⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⠀⣯⠇⡴⣫⣳⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡤⣄⠀⠀⠀⠀⠀⡇⡟⠃⠀⠀⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⡞⡎⣸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣯⣷⣷⠀⠀⠀⠀⡇⡧⠤⠶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⢰⢱⠃⡿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣼⡟⡷⣷⣯⡇⡇⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⢀⡤⣞⣉⡍⢏⡼⠀⠘⠷⠃⠁⣀⣀⣀⠀⠀⠀⠀⣇⢿⣿⡿⢼⡾⠁⠀⠀⠀⣿⣒⡲⠶⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠉⢁⠖⠉⢀⡜⣷⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠛⠉⠙⠉⠉⠀⠀⠀⠀⣾⠳⢤⣄⠑⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⣎⡤⢺⠋⠀⠘⡧⡀⠀⠸⠤⠞⢧⣀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠟⡜⢹⡧⢄⡘⢌⠑⠦⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠘⠁⢠⠃⠀⡠⠔⠉⠻⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠡⠖⡡⠊⣿⠀⠀⠈⠳⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                  ⠀⠀⠘⠛⠉⠀⠀⠀⠀⠀⠈⣷⣍⠛⠛⠭⠭⠭⠭⠟⢋⡥⠞⠁⠀⠀⠉⠀⠀⣷⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  
                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣯⠢⣝⠒⠒⠒⠒⡉⠉⠀⠀⠀⠀⠀⠀⠀⢀⠎⠀⠀⡏⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  
                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⢆⡀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠊⠁⠀⠀⠘⣼⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⣽⠇⠓⠤⠥⠭⠭⠭⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⡤⠊⢱⡘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⣿⡶⣒⣶⡀⠀⠀⣠⡶⠶⠒⠒⠖⠋⠀⠀⠀⡀⠀⠀⠀⣀⠔⠻⡼⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⣼⠃⠚⢁⣼⡇⠀⢰⣇⡒⠒⠂⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠁⠀⠀⣸⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠁⠀⠀⠈⣝⠇⠀⠀⢳⡄⠉⠁⠀⠀⠀⢀⡴⠓⠋⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⠀⠀⠧⣀⣀⡠⠶⠋⠁⠀⠀⠀⠀⠉⠉⠙⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                          
    {reset_color}
    {green_color}                                                                        
          AAA        UUU   UUU  TTTTTTTTTTTTT   OOOOOOO    MMMMM   MMMMMM     
         AAAAA       UUU   UUU  TTTTTTTTTTTTT  OOO   OOO  MMMMMMM MMMMMMMM    
        AAAAAAA      UUU   UUU      TTTTT      OOO   OOO  MMMMMMMMMMMMMMMM    
       AAA   AAA     UUU   UUU      TTTTT      OOO   OOO  MMM   MMMM   MMM   
      AAAAAAAAAAA    UUU   UUU      TTTTT      OOO   OOO  MMM   MMMM   MMM   
     AAAAAAAAAAAAA   UUU   UUU      TTTTT      OOO   OOO  MMM   MMMM   MMM   
    AAA         AAA   UUUUUUU       TTTTT       OOOOOOO   MMM   MMMM   MMM   
    {blue_color}
    ========================================================================
                      W E L C O M E   T O   A U T O M                           
    ========================================================================
    {reset_color}
    """
    print(ascii_art)

def print_schedule():
    scheduleP = f"""
    {green_color}                                                                        
    ========================================================================
                           Y O U R    S C H E D U L E                           
    ========================================================================
    {reset_color}
    """
    print(scheduleP)

def print_change(old_status, new_status):
    scheduleP = f"""
    {blue_color}                                                                        
    Time: {datetime.now().time()}
    Change: {old_status} =========>>>> {new_status}
    {reset_color}
    """
    print(scheduleP)