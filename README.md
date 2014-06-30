sshd_stunnel
============
Script per l'installazione automatica di https://code.google.com/p/auditing-sshd/

Questo script imposterà automaticamente tutte le configurazioni o dipendenze necessarie

Testato su Centos 6.x

Come installare:
  $ wget https://raw.githubusercontent.com/trakons/sshd_stunnel/master/install
  $ chmod +x install
  $ ./install
  
##Component
To include as a [component](http://github.com/component/component), just run

    $ component install FortAwesome/Font-Awesome

Or add

    "FortAwesome/Font-Awesome": "*"

to the `dependencies` in your `component.json`.

## Hacking on Font Awesome

From the root of the repository, install the tools used to develop.

    $ bundle install
    $ npm install

Build the project and documentation:

    $ bundle exec jekyll build

Or serve it on a local server on http://localhost:7998/Font-Awesome/:

    $ bundle exec jekyll serve
