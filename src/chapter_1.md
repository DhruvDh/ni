# The second page

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