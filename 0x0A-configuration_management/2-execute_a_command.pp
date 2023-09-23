#This code kills process && works together eith the killmenow file which has been provided
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
