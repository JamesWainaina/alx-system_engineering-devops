# Installing Nginx server

exec {'install':
  provider => shell,
  command  => 'sudo apt-get  -y update ; sudo apt-get install nginx ; echo "Hello World!" | sudo tee /
}
