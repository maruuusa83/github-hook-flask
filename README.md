Github Webhook in Flask
#######################

This is a super-simple Github webhook handler in the Flask.

``on-update.sh`` will be called only when the master branch is pushed.
The on-update script will be taken updated repository name as first argument.
That is all of this application.

---

It will also verify that the request originated from your repository.  
If you added the Secret when you create a new webhook, the signeture will be attach to the request-header. This application will check it.

## Gettings started
This program have to be executed by a user who can clone a repository from Github.

### Installation Requirements
This application needs some another package or applicaton as follows. Please insall them.

 * Flask
 * expect

Perhaps, you can use ``install_requirements.sh`` script. (Please be careful. It is a careless work.)

### On-update Script Configration
Copy ``on-update.sh.sample`` and edit it.

```
$ cp on-update.sh.sample on-update.sh
```

This script will pull the master branch from the origin when it is called in the initial state.

It requires a full-path of a directory that used to store automatically-update-projects in ``REPOS_PATH``.  
Furthermore, it needs a full-path of the ssh secret file and its passphrase for ``git pull origin master`` command.

---

If you need execute more commands, add your commands after ``### Script ###``.

### Reciever Configration
You can configure about recieve server. If you need some changes, edit ``app.py``.

 * LISTEN\_PATH   : The path after the domain like "http://example.com/<LISTEN\_PATH>".
 * LISTEN\_PORT   : The number of listening port.
 * SECRET         : The key for signature.
 * UPDATE\_SCRIPT : The name of script that will be called when master is updated.

### Starting the Server
Start the server as next:

```
$ python app.py
```

When you want to continue to run, following command is better:

```
$ nohup python app.py &
```

### Hook Test
Clone the repository in REPOS\_PATH and add new webhook to the remote repository.  

And so, push some commits to master from local. If application was operating normally, repository in REPOS\_PATH will be updated automatically.

