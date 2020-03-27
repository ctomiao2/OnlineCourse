安装mysql步骤:
1. 解压OnlineCourse\database\mysql-8.0.19-winx64到文件夹mysql-8.0.19-winx64，拷贝该目录下的my.ini文件到mysql-8.0.19-winx64目录下
2. 修改my.ini中的basedir为mysql-8.0.19-winx64的绝对路径
3. 管理员身份打开cmd, cd到mysql-8.0.19-winx64\bin目录
4. 执行命令：mysqld --initialize --console
5. 执行完后会输出初始密码, 2018-04-20T02:35:05.464644Z 5 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: VTkcm#pUf1g<
其中APWCY5ws&hjQ就是mysql初始密码, 后续登录用到
6. 执行命令：mysqld install
7. 执行命令：net start mysql
8. 执行脚本OnlineCourse\database\login.bat, 第一次需要修改密码, 否则无法使用mysql, 使用第4步生成的密码登录
9. 修改mysql登录密码：ALTER USER "root"@"localhost" IDENTIFIED WITH mysql_native_password BY "Your password"; （注意末尾分号）
10. 修改密码成功后执行 flush privileges; （注意末尾分号）