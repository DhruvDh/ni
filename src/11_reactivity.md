# Why JavaScript needs to be Reactive

Let's say that one fine afternoon we decide to create two variables `a` and `b`, both of which we set to `2`, and we make a third variable `c` which we decree should be equal to the sum of `a` and `b`. If we were doing all this in Javascript, what we write should end up looking like this -

```js
let a = 2;
let b = 2;

let c = a + b;
```

Now, on that fine afternoon, if we also decide to print out the value of `c` with `console.log(c)` and run this little script with a Javascript runtime like [Node](https://nodejs.org/en/), we would see what we expect to see printed out -

```sh
4
```

Which prints `a + b` or `2 + 2` and thusly `4`. At this point if, rather miraculously, we still want to play around with our variables and haven't opened Netflix in a new tab, then we might try changing the the value of either `a` or `b` - just for some mischief.

Doing and printing out `c` again all written down in code would look something like this -

```js
let a = 2;
let b = 2;

let c = a + b;
console.log(c);

a = 3;
console.log(c);
```

Which if we run, again in a Javascript runtime like Node, would leave us this output -

```js
4
4
```

Uhm, hold up. Yeah, this afternoon sucks but how is it that `c` prints out as `4` the second time around too? 

We did tell javascript that `c` is _equal_ to `a + b`, which should mean that `c` equals `5` when we log it to the console the second time, seeing as how `a + b` is now `3 + 2`?

But evidently that's not how Javascript works, as `c` is still `4`. We can only conclude that Javascript is a spoilt little brat that does not to what it's told. It is seemingly deceiving us into thinking that `c` is equal to `a + b` when it most certainly isn't. 

At this point, there maybe some of you whose brains were marred by an education in Computer Science thinking that, well, there's nothing particularly wrong here, and that Javascript is innocent because when we wrote `let c = a + b;`, we did not actually set `c` to be equal to `a + b`, we simply stored the _current_ value of `a + b` into `c` - which happened to be `4` at the time. And as such it remains to be `4` for the rest of `c`'s existence until we store a different value there. 

That being said, it is also very easy to imagine a parallel universe in which variables, once declared to be equal to something else (say `a + b`), actually stay equal to that something else (say `a + b`). That universe would much nicer to live in too and you probably need a little convincing to see why.

Let's think about websites for a moment, like the one you're on now. Almost all websites follow a simple pattern - you have some data, your intention is to show that data to users of that website, and you use HTML and CSS to make sure said data looks pretty when shown.

You'd be surprised how many website adhere to this simple pattern. Even something like Instagram ([it's not just an app!](https://www.instagram.com/)), the posts are data, the follower count is data, the comments on a post are data, the number of likes is data. Once you're on someone's profile page or someone's post, your browser asks for the relevant data, the server responds with said data, and then somewhere in the code for Instagram would be a line like this -

```js
document
    .getElementByID("NameOfPlaceWhereLikesAreShown")
    .text = "liked by " + randomLiker.name + " and " + noOfLikers + " others";
// generates the "liked by" message and makes the relevant part of the website display it
```

Here `"liked by " + randomLiker.name + " and " + noOfLikers + " others"` is what generates the messages like the following -

![Liked by message](/ni/img/liked_by_message.png)

While what `document.getElementByID("NameOfPlaceWhereLikesAreShown").text` does is that it finds the place whose text we need to set to be equal to the above message so that we can set it to be equal to the above message.

For the sake of simplicity, let's not worry about how we display the "liked by" message and simply assume that there is a `displayText` variable whose value will end up being shown where we need to show the "liked by" message. So we generate the message like so -

```js
let displayText = "liked by " + numberOfLikers + " others";
```

The interesting thing to note here is that this particular piece of code does do a rather similar job as the earlier `let c = a + b;` line - it sets a variable to be a certain value based on the values of other variables. And as such, it suffers from the same problems of javascript being dumb - when `a` or `b` changes, the value of `c` doesn't react to that change, and remains equal to the old, incorrect value. Similarly here, when people keep liking your post because of course they do, the value of `displayText` won't react and will remain equal to the old value.

At this point, people who make websites have 2 options, either they are okay with the data they show being old, and incorrect, and hope that the user would refresh or reload the page if he or she wants the newest values, or they have to do lots of javascript and client-server gymnastics to ensure that the data being shown is always the newest.

The way it works is that on the client-side, that is on your computer, they watch for people clicking the "like" button and then update the "numberOfLikes" variable whenever that happens, and then also update the "displayText" message whenever _that_ happens, and also at the same time send a message to the sever saying "yo, this dude likes this". Which might not seem like a whole lot of work, but when you have to do it for each and everything you are displaying on your application of website that is capable of changing it does add up to be a whole lot of work for us to do just to cover up for Javascript being dumb.

This is a frequent pain for everyone who develops websites and applications, not only do they have to instruct a computer or a phone about what data to display, how to display it in a pretty way, but also having to explain in tedious detail to said phone or computer on how to react if this data changes.

Which is exactly why a universe in which once you set `c` to be equal to `a + b`, it would actually stay equal to `a + b` forever, and not just until something changes the values of `a` and `b` be a much nicer universe to live in. You'd just have to explain how to display the data in a pretty way, and there would be no need to explain how to react to changes in data - it would do that on its own.

Next up we're going to have another amazing afternoon where we try to wrestle javascript into making good on it's promise of making something equal to something else.se.se.