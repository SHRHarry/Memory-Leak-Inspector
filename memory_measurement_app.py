# -*- coding: utf-8 -*-

import time
import psutil
import socket
import webbrowser
from argparse import ArgumentParser
from DatabaseObj import postgreSQL

'''
This file is a memory measurement tool for other apps.
It will create a sub-process to find out the PID of apps,
then track the memory cost (both RAM & VRAM) from PID,
send data to postgreSQL and show on Grafana at last.
'''

def make_arg_parser():
    parser = ArgumentParser("App memory inspection.")
    parser.add_argument('--exe_name', type=str, default="LineLauncher.exe", help='Number of test times.')
    parser.add_argument('--del_table', type=str, choices=["yes", "no"], default="no", help='Number of test times.')
    args = parser.parse_args()
    
    return args

def find_PID(sw_text = "LineLauncher.exe"):
    filename = ""
    pid_list = []
    for pid in psutil.pids():
        try:
            process_ = psutil.Process(pid)
            filename = process_.name()
        except:
            pass
        if len(filename) > 0:
            if sw_text in filename:
                # print(f"filename = {filename}, pid = {pid}")
                pid_list.append(pid)
                #break
            else:
                pid = -1

        else:
            pid = -1

    return pid_list

def get_RAM_detail(process_, sw_text):
    pid = process_.pid
    percent = round(process_.memory_percent(), 1)
    private = process_.memory_info().private >> 20
    # vms = process_.memory_info().vms >> 20

    private_G = process_.memory_info().private >> 30
    # vms_G = process_.memory_info().vms >> 30
    return f"PROCESS({sw_text:16s}) | PID {pid:5d} | used({percent:5.1f}%) | Memory = {private:5d} MB ({private_G:2d} GB)", private

def get_sw_memory(sw_text):
    
    sw_pid_list = find_PID(sw_text)
    sw_RAM_used_list = []
    
    if len(sw_pid_list) > 0:
        try:
            sw_process = [psutil.Process(s_p_l) for s_p_l in sw_pid_list]
            # process_APP = psutil.Process(APP_pid_list[0])
        except Exception as e:
            print(e)
    else:
        sw_process = [None for _ in range(len(sw_pid_list))]

    try:
        if sw_process != None:
            for s_p in sw_process:
                sw_RAM_detail, sw_RAM_used = get_RAM_detail(s_p, sw_text)
                sw_RAM_used_list.append(sw_RAM_used)
                print(sw_RAM_detail)
        else:
            sw_RAM_used = 0
    except Exception as e:
        print(e)

    # print(f"{sw_text} RAM used: {sw_RAM_used} MB")
    return sw_RAM_used_list, sw_pid_list

def Check_port(SettlementTime, IP = "127.0.0.1", port = 8081):
    sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sc.settimeout(2)
    try:
        sc.connect((IP,port))
        sc.close()
        return 10000
    except Exception as e:
        print(e)
        
        sc.close()
        return 0

if __name__ == "__main__":
    
    grafana_url = "<path-to-your-dashboard>"
    webbrowser.open_new(grafana_url)
    
    args = make_arg_parser()
    
    ### postgreSQL Setting
    postgresql = postgreSQL()
    
    ### Create Memory Leak Table
    try:
        strMemoryLeakTable = '''CREATE TABLE MemoryLeak_app
        (APP_RAM INT    NOT NULL,
        '''
        strMemoryLeakTable += '''SettlementTime TIMESTAMPTZ);
        SET TIMEZONE = 'Asia/Taipei';
        '''
        postgresql.CreateTable(strMemoryLeakTable)
        
    except Exception as e:
        print(e)
        
        ### Determine whether to delete table or not
        if args.del_table == "yes":
            
            postgresql.DeteteTable("MemoryLeak_app")
            
            strMemoryLeakTable = '''CREATE TABLE MemoryLeak_app
            (APP_RAM INT    NOT NULL,
            '''
            strMemoryLeakTable += '''SettlementTime TIMESTAMPTZ);
            SET TIMEZONE = 'Asia/Taipei';
            '''
            postgresql.CreateTable(strMemoryLeakTable)
        else:
            pass
        
    # print(strMemoryLeakTable)
    
    ### start getting information
    while True:
        
        print(f"---------------------------- EXE Name : {args.exe_name} ----------------------------")

        ### Find APP RAM's PID
        APP_RAM_used_list, APP_pid_list = get_sw_memory(args.exe_name)
        
        ### Setting local time
        local_time = time.localtime()
        SettlementTime = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
        
        ### send to postgreSQL
        strMemoryLeakValue = '''INSERT INTO MemoryLeak_app (APP_RAM,
        '''

        strMemoryLeakValue += '''SettlementTime)
        '''
        
        if len(APP_RAM_used_list) > 0:
            for a_r_u in APP_RAM_used_list:
                strMemoryLeakValue += f'''VALUES ({a_r_u}, '''
        else:
            strMemoryLeakValue += '''VALUES (0, '''
        
        
        strMemoryLeakValue += f'''\'{SettlementTime}+08\')'''
        
        # print(strMemoryLeakValue)
        postgresql.Insert(strMemoryLeakValue)

        time.sleep(1)