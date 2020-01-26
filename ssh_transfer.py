#-*- coding: utf-8 -*-
 
#!/usr/bin/python 
import paramiko
# 实例化一个trans对象# 实例化一个transport对象
transport = paramiko.Transport(('', 22))
# 建立连接
transport.connect(username='root', password='')
# 实例化一个 sftp对象,指定连接的通道
sftp = paramiko.SFTPClient.from_transport(transport)
 
# LocalFile.txt 上传至服务器 /home/fishman/test/remote.txt
#sftp.put('/root/upload.zip', '/web-server.py')
# 将LinuxFile.txt 下载到本地 fromlinux.txt文件中
sftp.get('/root/upload.zip', 'zsw.zip')
transport.close()
