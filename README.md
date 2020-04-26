# Unlocking Your Tinder Likes' Photos (first 10) Without Gold

***
As I'm sure most of us know, Tinder doesn't allow you to see who has swiped right on you unless you purchase a subscription from them.

Of course there are ways of bypassing this that already exist such as opening up the developer console & using inspect element to change the value of the blur to 0px instead of the usual 12px value:
![](https://github.com/1d8/GettingLikesPics/blob/master/tinder/devconsole.png) 
But this still only gets us a partially unblurred image:

![](https://github.com/1d8/GettingLikesPics/blob/master/tinder/blurredimg.png)

BUT, if we open up developer console again and go to the network tab and click on our likes, we see some new events, but only 2 are of interest to us:
![](https://github.com/1d8/GettingLikesPics/blob/master/tinder/teaser.png)
These two teaser objects are what brings us the blurred images, going into the larger one (in my case 3.4KB), and then going into the response, we see JSON output:
![](https://github.com/1d8/GettingLikesPics/blob/master/tinder/json.png)
You can choose to [beautify](https://gchq.github.io/CyberChef/#recipe=JSON_Beautify('%20%20%20%20',false)) this to make it easier to read, but I just copied it all & threw it in a text editor.

The output we are most interested in, are .jpgs since that's where we will find images of the people who swiped right on us.

In my text editor (MousePad), I hit ctrl + f to find the instance of ".jpg" or ".jpeg" then hit highlight all to find all instances:
![](https://github.com/1d8/GettingLikesPics/blob/master/tinder/mpad.png)

Then browsing to these .jpeg URLs, we see the full unblurred image:
![](https://github.com/1d8/GettingLikesPics/blob/master/tinder/fullimg.png)

Please note, these aren't all of your matches, simply the select 10 that pop up when you click on the likes section but theoretically speaking, it would be possible to simply collect all the image links, refresh the page, and repeat and get different image links.


# Enumerating Before Swiping

***
This method is a way to see who's in your Tinder "time-line(?)" (for lack of a better term) before they even appear, this will gather their images, their birth year, their bio, and their Tinder ID number (as of now, I don't think the ID number is very useful)

* Open up the dev console
* Refresh the page (make sure you're on the main page before refreshing)
* Navigate to the **core?locale=en** object:
![](https://github.com/1d8/GettingLikesPics/blob/master/more-imgs/devcons.png)
* Copy the JSON output, paste it in your fav text edito
* Congrats!

# Diving Deeper Into The JSON:
Throwing our JSON into [Cyberchef's beautifier](https://gchq.github.io/CyberChef/#recipe=JSON_Beautify('%20%20%20%20',false)), we get this:

![](https://github.com/1d8/GettingLikesPics/blob/master/more-imgs/info1.png)

As we can see, we are hit with their ID, name, the year they were born (the date & the month remain the same for all users for some reason), as well as all their photos they have on their profile!

Scrolling down...

![](https://github.com/1d8/GettingLikesPics/blob/master/more-imgs/info2.png)

As we can see, we get even more info!

Here's more proof the birth month & day remain static for all users:

![](https://github.com/1d8/GettingLikesPics/blob/master/more-imgs/info3.png)

And here are the links to all the user's images in their profile:

![](https://github.com/1d8/GettingLikesPics/blob/master/more-imgs/userimgs.png)

And here's what the type of info you'd see if a person has their spotify connected to their account:

![](/home/n9/study/cybernotes/tinder/spotify.png)
![](https://github.com/1d8/GettingLikesPics/blob/master/more-imgs/spotify.png)

And if the person has their instagram connected...

![](https://github.com/1d8/GettingLikesPics/blob/master/more-imgs/insta.png)


# A More Automated Approach To Grabbing Imgs Of Likes

The extract jpeg script is meant to extract only unique img links to those who swiped right on you.

How this works is using regular expressions to extract the image URL & ensuring each URL ends with the .jpeg extension for the full image (since Tinder offers .jpg images with a variety of sizes)

Unfortunately, you still need to manually grab the JSON output which is detailed [here](https://github.com/1d8/PlayingAroundwTinder), after manually grabbing the JSON output, you beautify it [here](https://codebeautify.org/jsonviewer) then input the beautified json into the *string* variable in the code.

**NOTE:** This needs to be done multiple times over & over if you wish to grab the images of all your likes. Refresh, go back to dev console, grab JSON output, beautify it, paste it into script. Before pasting it into the *string* variable, drop down two spaces & ensure you stay within the triple quotes.

# Demo 
***

This is how it should look when inputting it into the script:

![](https://github.com/1d8/PlayingAroundwTinder/blob/master/script-imgs/input.png)

This is what I mean by dropping down a few spaces before pasting the 2nd piece of JSON:

![](https://github.com/1d8/PlayingAroundwTinder/blob/master/script-imgs/spaces.png)

![](https://github.com/1d8/PlayingAroundwTinder/blob/master/script-imgs/spaces2.png)

Here is the output after running the script:

![](https://github.com/1d8/PlayingAroundwTinder/blob/master/script-imgs/output.png)
