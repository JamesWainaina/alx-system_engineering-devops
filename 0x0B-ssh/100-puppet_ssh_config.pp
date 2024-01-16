# make changes to configuration file using Puppet

exec { 'echo':
    path    => 'usr/bin:bin',
    command => 'echo " IdentifyFile ~/.ssh/school\n
    PasswordAuthentication no" >> /etc/ssh/ssh_config',
    returns => [0,1],  
}
