# Reactive Programming

Let's say that one fine afternoon we decide to create two variables `a` and `b`, both of which we set to `2`, and we make a third variable `c` which we decree should be equal to `a + b`. If we were doing all this in Javascript, what we write should end up looking like this -

```js
let a = 2;
let b = 2;

let c = a + b;
```

Now, on that fine afternoon, if we also decide to print out the value of `c` with `console.log(c)` and run this little script with a Javascript runtime like [Node](https://nodejs.org/en/), we would see what we expect to see printed out -

```js
4
```

Which is `a + b` or `2 + 2` and thusly `4`. At this point if rather miraculously we still want to play around with our variables and haven't opened Netflix in a new tab, then we might try changing the the value of either `a` or `b` - just for some mischief.

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

But evidently that's not how Javascript works, as `c` is still `4`. We can only conclude that Javascript is a spoilt little brat that does not to what it's told. It deceives us into thinking that `c` is equal to `a + b` when it most certainly isn't. 

At this point, there maybe some of you whose brains were marred by an education in Computer Science thinking that, well, there's nothing particularly wrong here, and that Javascript is innocent because when we wrote `let c = a + b;`, we did not actually set `c` to be equal to `a + b`, we simply stored the _current_ value of `a + b` into `c` - which happened to be `4` at the time. And as such it remains to be `4` for the rest of `c`'s existence until we store a different value there. 

That being said, it is also very easy to imagine a parallel universe in which variables, once declared to be equal to something else (say `a + b`), actually stay equal to that something else (say `a + b`). That universe would much nicer to live in too and you probably need a little convincing to see why.

Let's think about websites for a moment, like the one you're on now. Almost all websites follow a simple pattern - you have some data, your intention is to show that data to the user of the website, and you use HTML and CSS to make sure said data looks pretty when shown.

You'd be surprised how many website adhere to this simple pattern. Even something like Instagram ([it's not just an app!](https://www.instagram.com/)), the posts are data, the follower count is data, the comments on a post are data, the number of likes is data. Once you're on someone's profile page or someone's post, your browser asks for the relevant data, the server responds with said data, and then somewhere in the code for Instagram would be a line like this -

```js
document
    .getElementByID("NameOfPlaceWhereLikesAreShown")
    .text = "liked by " + randomLiker.name + " and " + noOfLikers + " others";
```

Here `"liked by " + randomLiker.name + " and " + noOfLikers + " others"` is what generates the messages like the following -

![Liked by message](https://dhruvdh.github.io/blog/img/reactivity/liked_by_message.png)

While what `document.getElementByID("NameOfPlaceWhereLikesAreShown").text` does is that it finds the place whose text we need to set to be equal to the above message so that we can set it to be equal to the above message.

The interesting thing to note here is that this particular piece of code is basically the same as the above `let c = a + b;` line, and as such it suffers from the same brattiness 
of Javascript; it doesn't _stay_ equal to the message we really want it to be equal to. For the sake of simplicity let's consider that line to be -

```js
let displayText = "liked by " + numberOfLikers + " others";
```

But, just like we saw on that fine afternoon, where when `c` was equal to `a + b` initially, but didn't stay equal to `a + b` when either `a or b` was changed - `displayText` also won't show the correct number of people who've liked your post if someone "likes" the post _after_ you're set the value of `displayText`.

Which is exactly why the parallel universe in which Javascript is not scummy and variables that once told to be equal to something actually _stay equal_ would be a much nicer universe to live in. 

- The us
I'll give you an example, a rather plain one -

So what now? Are we just going to sit here and take it? Are we going to let javascript disrespect us like that?

No.

Javascript is a tool, our tool. We will not bow down to it. We will make it do our bidding.

But how?

Well the first thing that pops up in my mind is to make `c` a function instead - what if we do this:

```js
let a = 2;
let b = 2;

// instead of let c = a + b;
let c = () => a + b;

console.log(c);

a = 3;
console.log(c);
```

Here, we made use of [arrow functions](https://www.developerdrive.com/arrow-functions-javascript/) to make `c` a function that calculates and returns `a + b` instead of just storing the value `a + b` inside `c`. This should mean that it won't just print the stored value it had for `a + b`, rather it would calculate `a + b` again.

Output:

```js
[Function: c]
[Function: c]
```

Oh yeah, we're logging the function itself in console instead of calling the function and logging it's return value. So let's actually call it, like so -

```js
let a = 2;
let b = 2;

// instead of let c = a + b;
let c = () => a + b;

console.log( c() );

a = 3;
console.log( c() );
```

Which gives us the output we'd expect -

```js
4
5
```

But not only did we have to write `c()` instead of just `c`, which suspiciously seems like us bowing down to javascript, even if just a little; it also won't actually work for the search case I was describing earlier.