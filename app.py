from flask import Flask, render_template, request, jsonify
from netmiko import ConnectHandler


app = Flask(__name__)


@app.route('/get-config/<ip_address>/', methods=['GET','POST'])
def show_run(ip_address):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        enable = request.form['enable']
        device = {'ip': ip_address,
                  'username': username,
                  'password': password,
                  'secret': enable,
                  'device_type': 'cisco_xe'}
        connection = ConnectHandler(**device)
        user_mode = connection.find_prompt()
        if '>' in user_mode:
            connection.enable()
        showrun = connection.send_command('show run')
        hostname= connection.find_prompt()[:-1]
        connection.disconnect()
        with open(hostname +'_ShowRun.txt', 'w') as file:
            file.write(showrun)
        return jsonify(showrun)
    else:
        return render_template('login.html', network_device='Network Controller')


@app.route('/neighbors/<ip_address>', methods=['GET', 'POST'])
def show_cpd_neighbor(ip_address):
    if request.method == 'POST':
        username= request.form['username']
        password= request.form['password']
        enable= request.form['enable']
        device = {'ip': ip_address,
                  'username': username,
                  'password': password,
                  'secret': enable,
                  'device_type': 'cisco_xe'}
        connection = ConnectHandler(**device)
        user_mode = connection.find_prompt()
        if '>' in user_mode:
            connection.enable()
        get_neighbor = connection.send_command('show cdp neighbor')
        connection.disconnect()
        with open(device['ip'] +'-neighbors.txt', 'w') as file:
            file.write(get_neighbor)
        return 'Config has been saved to the working directory'
    else:
        return render_template('login.html', network_device= 'Network Controller')


@app.route('/get-config/<ip_address>/ip_addresses', methods= ['GET', 'POST'])
def show_ip_int_brief(ip_address):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        enable = request.form['enable']
        device = {'ip': ip_address,
                  'username': username,
                  'password': password,
                  'secret': enable,
                  'device_type': 'cisco_xe'}
        connection = ConnectHandler(**device)
        user_mode = connection.find_prompt()
        if '>' in user_mode:
            connection.enable()
        get_ips = connection.send_command('show ip interface brief')
        connection.disconnect()
        with open(device['ip'] + '-ipaddress.txt', 'w') as file:
            file.write(get_ips)
        return 'Config has been saved to the working directory'
    else:
        return render_template('login.html', network_device='Network Controller')

@app.route('/get-config/<ip_address>/<iface>', methods=['GET','POST'])
def show_run_iface(ip_address, iface):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        enable = request.form['enable']
        device = {'ip': ip_address,
                  'username': username,
                  'password': password,
                  'secret': enable,
                  'device_type': 'cisco_xe'}
        connection = ConnectHandler(**device)
        user_mode = connection.find_prompt()
        if '>' in user_mode:
            connection.enable()
        get_L3_iface = connection.send_command('show run int ' + iface)
        connection.disconnect()
        return jsonify(get_L3_iface)
    else:
        return render_template('login.html', network_device='Network Controller')

@app.route('/get-config/<ip_address>/vlans', methods= ['GET', 'POST'])
def show_vlan_brief(ip_address):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        enable = request.form['enable']
        device = {'ip': ip_address,
                  'username': username,
                  'password': password,
                  'secret': enable,
                  'device_type': 'cisco_xe'}
        connection = ConnectHandler(**device)
        user_mode = connection.find_prompt()
        if '>' in user_mode:
            connection.enable()
        get_vlans = connection.send_command('show vlan brief')
        hostname= connection.find_prompt()[:-1]
        connection.disconnect()
        with open('_vlans.txt', 'w') as file:
            file.write(get_vlans)
        return jsonify(get_vlans)
    else:
        return render_template('login.html', network_device='Network Controller')

@app.route('/get-interface/<ip_address>/portstatus', methods= ['GET', 'POST'])
def show_int_status(ip_address):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        enable = request.form['enable']
        device = {'ip': ip_address,
                  'username': username,
                  'password': password,
                  'secret': enable,
                  'device_type': 'cisco_xe'}
        connection = ConnectHandler(**device)
        user_mode = connection.find_prompt()
        if '>' in user_mode:
            connection.enable()
        get_int_status = connection.send_command('show interface status')
        hostname= connection.find_prompt()[:-1]
        connection.disconnect()
        with open(hostname +'_ifacestatus.txt', 'w') as file:
            file.write(get_int_status)
        return jsonify(get_int_status)
    else:
        return render_template('login.html', network_device='Network Controller')


app.run(debug=True, port=9999)
