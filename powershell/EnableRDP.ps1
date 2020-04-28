Start-Service Termservice
Set-NetFirewallRule RemoteDesktop-UserMode-In-TCP -Enabled True
Set-NetFirewallRule RemoteDesktop-UserMode-In-UDP -Enabled True
