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

Which is `a + b` or `2 + 2` and thusly `4`. At this point if rather miraculously we still want to play around with our variables `a`, `b,`, `c`, and haven't opened Netflix in a new tab, then we might try changing the the value of either `a` or `b` - just for some mischief.

That and printing out `c` again after the change all written down in code would look something like this -

```js
let a = 2;
let b = 2;

let c = a + b;
console.log(c);

a = 3;
console.log(c);
```

Which if we run would leave us this output -
```js
4
4
```

Uhm, hold up. Yeah, this afternoon sucks but how is it that the value of `c` is still `4`? 

We did tell javascript that `c` is _equal_ to `a + b`, which should mean that `c` equals `5` when we log it to the console the second time around, seeing as how `a + b` is now `3 + 2`?

But evidently that's not how Javascript works, as `c` is still `4`. We can only conclude that Javascript is a spoilt little brat that does not to what it's told. Javascript nods in agreement when we tell it to _let_ `c` be equal to `a + b`, oh but it's just an _act_ and Javascript is merely waiting for its chance to makes us look like a fool.

At this point, there maybe some of you whose brains were marred by an education in Computer Science thinking that, well, there's nothing particularly wrong here, and that Javascript is innocent because when we wrote `let c = a + b;`, we did not actually set `c` to be equal to `a + b`, we simply stored the _current_ value of `a + b` into `c` - which happened to be `4` at the time. And as such it remains to be `4` for the rest of `c`'s existence until we store a different value there. 

That being said, wouldn't it be convenient if variables that were set to be equal to something actually stayed equal to that something?

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