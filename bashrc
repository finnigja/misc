GREP_OPTIONS="--color"
if grep --help | grep -- --exclude-dir &>/dev/null; then
    for PATTERN in .cvs .git .hg .svn; do
        GREP_OPTIONS="$GREP_OPTIONS --exclude-dir=$PATTERN"
    done
fi
export GREP_OPTIONS

