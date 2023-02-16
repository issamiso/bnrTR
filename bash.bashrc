shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth
python3 .bnr.py
# Default command line prompt.
PROMPT_DIRTRIM=2
#PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '
PS1='\[\e[0;35m\]IssamIso4Root\[\e[0;32m\]:\[\e[0;31m\]\w \[\e[0;97m\]\$\[\e[0m\] '
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
	command_not_found_handle() {
		/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
	}
fi

[ -r /data/data/com.termux/files/usr/share/bash-completion/bash_completion ] && . /data/data/com.termux/files/usr/share/bash-completion/bash_completion
