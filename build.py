import shutit

s = shutit.create_session(session_type='bash')
s.send('rm -rf /tmp/tf_build && mkdir -p /tmp/tf_build')
s.send('git clone https://github.com/hashicorp/terraform.git')
s.send('cd terraform')
s.send('git checkout v0.12-dev')
s.send('vagrant destroy -f')
s.send('vagrant up')
s.send('vagrant ssh')
s.send('cd /opt/gopath/src/github.com/hashicorp/terraform/')
s.send('make test')
s.send('make bin')
s.pause_point('')
