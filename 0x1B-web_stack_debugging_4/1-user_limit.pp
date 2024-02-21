#increasing the hard ans soft file config file for holberto user.
exec { 'increase-hard-file-limit-for-holberton-user.
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => 'usr/local/bin/:bin/'
}
exec { 'increase-soft-file-limit-for-holberton-user.
  command => 'sed -i "/hoberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => 'usr/local/bin/:/bin/'
}
