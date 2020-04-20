## Unlocking Your Tinder Likes (first 10) Without Gold

***
As I'm sure most of us know, Tinder doesn't allow you to see who has swiped right on you unless you purchase a subscription from them.

Of course there are ways of bypassing this that already exist such as opening up the developer console & using inspect element to change the value of the blur to 0px instead of the usual 12px value:
![](https://github.com/1d8/GettingLikesPics/blob/master/tinder/devconsole.png) 
But this still only gets us a partially unblurred image:

![](https://github.com/1d8/GettingLikesPics/blob/master/tinder/blurredimg.png)
BUT, if we open up developer console again and go to the network tab and click on our likes, we see some new events, but only 2 are of interest to us:
![](https://github.com/1d8/GettingLikesPics/blob/master/tinder/teaser.png)
These two teaser objects are what brings us the blurred images, going into the larger one (in my case 3.4kb), and then going into the response, we see JSON output:
![](https://github.com/1d8/GettingLikesPics/blob/master/tinder/json.png)
You can choose to [beautify](https://gchq.github.io/CyberChef/#recipe=JSON_Beautify('%20%20%20%20',false)) this to make it easier to read, but I just copied it all & threw it in a text editor.

The output we are most interested in, are .jpgs since that's where we will find images of the people who swiped right on us.

In my text editor (MousePad), I hit ctrl + f to find the instance of ".jpg" or ".jpeg" then hit highlight all to find all instances:
![](https://github.com/1d8/GettingLikesPics/blob/master/tinder/mpad.png)

Then browsing to these .jpeg URLs, we see the full unblurred image:
![](https://github.com/1d8/GettingLikesPics/blob/master/tinder/fullimg.png)

Please note, these aren't all of your matches, simply the select 10 that pop up when you click on the likes section but theoretically speaking, it would be possible to simply collect all the image links, refresh the page, and repeat and get different image links.
