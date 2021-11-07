$ipPublica = Invoke - RestMethodifconfig.me
$ipLocal = Get - NetIPAddress - AddressFamily IPV4
$nmapPriv = nmap 192.168.56.1
$nmapPublica = nmap 192.168.56.1
$nmapLocal = nmap - -script = http - auth - finder192.168.56.1
$info = """IP publica:n$ipPublican IP privadas:n$ipLocal
              nIP local nmap: 192.168.1.71, resultado:n$nmapPriv
              nIP publica nmap :n$nmapPublica
              nY IP privada nmap: 192.168.1.71 resultado:`n$nampLocal """


$codificado = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($info))
Set - Content - Value
"$codificado" - Path
C:\Users\Noe Rivera\Documents\LCP Practicas
