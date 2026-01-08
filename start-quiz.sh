#!/usr/bin/env bash

set -euo pipefail

cd "$(dirname "$(readlink -f "$0")")"

cat <<EOF
########################################################################
SD212 Quiz Extractor

You should only run this program when you are in the lab room and
ready to start the quiz with your instructor present.

Remember that, while you are taking the quiz:
  * You may not visit any websites besides the course websites for
    SD211 and SD212.
  * No Googling, no AI (not even the official course Gemini Gem),
    no Copilot, no phone

IMPORTANT: Resist the urge to talk abou this quiz with your classmates
in other sections until everyone has taken it! Give everyone the same
fair chance.

When you are ready to get started, enter the name of the quiz
such as 'quiz01', and the exact passphrase your instructor provides you,
into the prompts below.

(The script will try to guess the correct quiz name for you.)

EOF

guess_name=''
for ef in $(ls .enc); do
  guess_name=${ef%.gpg}
  if [[ ! -e $guess_name ]]; then
    break
  fi
done

read -p "Which quiz? " -e -i "$guess_name" qname
efile=".enc/$qname.gpg"

if [[ ! -e $efile ]]; then
  echo "ERROR: no quiz '$qname' found. Ask your instructor for the right quiz name to use."
  exit 1
fi

qfold="$qname"
if [[ -e $qfold ]]; then
  echo "ERROR: folder '$qfold' already exists. Delete it or move it somewhere else."
  exit 1
fi

read -p "Enter passphrase: " pass
if ! ( echo "$pass" | gpg --quiet --batch --passphrase-fd 0 -d "$efile" | tar -xzv); then
  echo
  echo "ERROR: Decryption failure. Maybe you entered the wrong passphrase?"
  exit 2
fi

cat <<EOF

Files successfully extracted to $qfold

Time to get started!
Look at the $qfold/instructions.md file for the details.

GOOD LUCK.
########################################################################
EOF

:
