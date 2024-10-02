# BitBucketBits
Scripts I've written for working with the Bitbucket Server api


create_pull_req.py 
I couldn't find an easy way out there to do a Pull Request to a locally hosted Bitbucket Server. I poked around at the API and found it was possible but poorly documented. I couldn't find a script out there that did this so I write one up in an afternoon.

It's not perfect, of course. You'll need to edit the code to input your username/password, URL you're working against, and the repository. I'll make that more easily configurable in the future. It does what I needed for now so good enough.
