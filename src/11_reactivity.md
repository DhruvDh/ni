# Motivation for Reactivity

Let's say that one fine afternoon we decide to create two variables `a` and `b`, both of which we set to `2`, and we make a third variable `c` which we decree should be equal to the sum of `a` and `b`. If we were doing all this in Javascript, what we write should end up looking like this -

```js
let a = 2;
let b = 2;

let c = a + b;
```

Now, on that fine afternoon, if we also decide to print out the value of `c` with a function like `console.log(c)` and run this little script with a Javascript runtime like [Node](https://nodejs.org/en/), we would see the sum of `a` and `b` printed out -

![Output](/ni/img/aplusb_1.svg)


Which is `2 + 2` and thusly `4`. At this point if, rather miraculously, we still want to play around with our variables and haven't opened Netflix in a new tab, then we might try changing the the value of either `a` or `b` - just for some mischief.

Doing that and printing out `c` again all written down in code would look something like this -

```js
let a = 2;
let b = 2;

let c = a + b;
console.log(c);

a = 3;
console.log(c);
```

Which if we run, again in a Javascript runtime like Node, would leave us with this output -

![Output](/ni/img/aplusb_2.svg)

Uhm, hold up. Yeah, this afternoon sucks but how is it that `c` prints out as `4` the second time around too? 

We did tell javascript to let `c` be _equal_ to `a + b`; and seeing as how `a + b` is now `3 + 2`, shouldn't javascript be printing out `5` the second time we print `c`?

But evidently that's not what Javascript did, as `c` was still `4`. We can only conclude that Javascript is a spoilt little brat that does not to what it's told. It is seemingly deceiving us into thinking that `c` is equal to `a + b` when it most certainly isn't.

At this point there maybe some of you whose brains were marred by an education in Computer Science thinking that, well, there's nothing particularly wrong here, and that Javascript is innocent because when we wrote `let c = a + b;`, we did not actually set `c` to be equal to `a + b`; we simply stored the _current_ value of `a + b` into `c` - which happened to be `4` at the time. And as such it remains to be `4` for the rest of `c`'s existence until we store a different value there.

These are the same kinds of people that would tell you that \\( sin^2(x) \\) is equal to \\( (sin(x))^2 \\) but \\( sin^{-1}(x) \\) is not equal to \\( \frac{1}{sin(x)} \\); just haters of anything that's sound and sensible.

They would also say that this is just how it works and that we should follow it or face doom and gloom; and they're probably right. That being said, it is also very easy to imagine a parallel universe in which variables, once declared to be equal to something else (say `a + b`), actually stay equal to that something else. That universe, I think, would be much nicer to live in too but you probably need a little convincing to see why that is so.

Let's think about websites for a moment, like the one you're on now. Almost all websites follow a simple pattern - you have some data, your intention is to show that data to users of your website, and you use [HTML](https://www.w3schools.com/html/) and [CSS](https://www.w3schools.com/css/default.asp) to make sure said data looks pretty when shown. Let's take instagram ([it's not just an app!](https://www.instagram.com/)) as an example,the posts are data, the follower count is data, the comments on a post are data, the number of likes is data. Once you're on someone's profile page or someone's post, your computer or phone asks for the relevant data, instagram's servers responds with said data, and then somewhere in the code for Instagram the Instagram website would be a line that does something like this -

```js
document
    .getElementByID("NameOfPlaceWhereLikesAreShown")
    .text = "Liked by " + randomLiker.name + " and " + noOfLikers + " others";
// generates the "liked by" message and makes the relevant part of the website display it
```

Here `"Liked by " + randomLiker.name + " and " + noOfLikers + " others"` is what generates the messages like the following -

![Liked by message](/ni/img/liked_by_message.png)

While what `document.getElementByID("NameOfPlaceWhereLikesAreShown").text` does is that it finds the place where we need to display the "liked by" message and set's its text to be equal to the "liked by" message we just generated.

For the sake of simplicity, let's not worry about how we display the "liked by" message and simply assume that there is a `displayText` variable whose value will end up being shown where we need to show the "liked by" message. So we generate the message like so -

```js
let displayText = "Liked by " + numberOfLikers + " others";
```

The interesting thing to note here is that this particular piece of code does do a very similar job to the earlier `let c = a + b;` line - it sets a variable to be a certain value based on the values of other variables. There just happen to be 3 variables instead of 2, and they happen to be "adding" strings instead of numbers.

It also suffers from the same problems of javascript being dumb - when `a` or `b` changes, the value of `c` doesn't react to that change, and remains equal to the old, incorrect value. Similarly here, when people keep liking your post because of course they do, the value of `displayText` won't react, or change and will remain equal to the old value.

At this point, people who make websites have 2 options, either they are okay with the data they show being old, and incorrect, and hope that the user would refresh or reload the page if he or she wants the latest and greatest, or they have to do lots of javascript and client-server gymnastics to ensure that the data being shown is always the newest.

The way it works is that on the client-side, that is on your computer, they watch for people clicking the "like" button and then update the "numberOfLikes" variable whenever that happens, and then also update the "displayText" message whenever _that_ happens, and also at the same time send a message to the sever saying "yo, this dude likes this". Which might not seem like a whole lot of work, but when you have to do it for each and everything you are displaying on your application of website that is capable of changing it does add up to be a whole lot of work for us to do just to cover up for Javascript being dumb.

This is a frequent pain for everyone who develops websites and applications, not only do they have to instruct a computer or a phone about what data to display, how to display it in a pretty way, but also having to explain in tedious detail to said phone or computer on how to react to changes in data according to a users expectations.

Which is exactly why a universe in which once you set `c` to be equal to `a + b`, it would actually stay equal to `a + b` forever, and not just until something changes the values of `a` and `b` be a much nicer universe to live in. You'd just have to explain how to display the data in a pretty way, and there would be no need to explain how to react to changes in data - it would do that on its own.

Next up we're going to have another amazing afternoon where we try to wrestle javascript into making good on it's promise of making something equal to something else.
