# Preface

> This page lays out the reason this website exists, and how it attempts to help. If you're here just to learn, feel free to skip this page and go on to [the next one](1_introduction.html).

This is an [open-source website](https://github.com/DhruvDh/ni) that is written with the intention of getting an average student of Computer Science or the like getting them up to speed on the intricacies of modern web development.

I think that teaching something, particularly computer science, is not as easy of a task to accomplish as most teachers and professors tend to think of it as, and neither is learning it. And as a result of this many students find them in a situation where they diligently did all that tasks that lead to academic success in the program they were enrolled in and yet they do not feel like they have attained the required skills to perform or land the job that they are expected to land.

For many students, the cracks in the confidence they have in their own skills start appearing way before it is time to look for a job, and they have trouble doing coursework that others seem to be able to _just do_ without too much of a fuss. They start to think that there is something lacking within them, and that this lacking is the reason they can't perform as well as they wish to.

I happen to think that more often than not, this lacking is not within a student, but rather in the way they are taught and encouraged to think about things. And I also think this situation tends to be a reality more often in third world countries, where education systems tend to believe that they cannot afford to be idealistic and compromise on the education they provide.

As to what exactly I think it is that is lacking, I am not sure this is the best place to talk about such things. Instead, if you are curious, I would direct you towards a chapter in the book "Surely, you're joking Mr. Feynman" `[1]`, where Dr. Richard Feynman - a noble prize winning physicist who is considered by many to be one of the best teachers of his time - gives a speech about his experience teaching in a third-world country (Brazil), and what he thinks about the state of the education system there. I believe not much has changed since.

> [1] [*O Americana, Outra Vez!* - Surely You're Joking, Mr. Feynman! (Adventures of a Curious Character).](http://sistemas.fciencias.unam.mx/~compcuantica/RICHARD%20P.%20FEYNMAN-SURELY%20YOU%27RE%20JOKING%20MR.%20FEYNMAN.PDF)
> Relevant text available in full [Appendix A](appendix.A.html)

## Teaching Philosophy

There is no shortage of resources to teach yourself web development from. I do not like most of them though, they tend to be a little to algorithmic.

Consider [w3schools](https://www.w3schools.com/), they're the most popular resource for learning the fundamentals of web development (ranked `#143` among *all websites* globally by traffic, as of 10/29/2019 `[1]`), and most of their tutorials are of the form -

1. Imagine you are in this state,
2. Imagine you want to do this,
3. This is how you do it.

Looking at a [random page](https://www.w3schools.com/js/js_htmldom_html.asp) from their JavaScript material, it does seem to skip the first step, it goes -

1. Imagine you want to write to the HTML document,
2. Do `document.write()`

Later in the page they go -

1. Imagine you want to change the HTML content,
2. Do `document.getElementByID(id).innerHTML = newHTML`

What a student that learns this way ends up with is a large set of how-to's in their head which they attempt to recall when the appropriate situation arises.

```
  +-----------------------------------------------------------+    
  | Students's head                                           |
  |===========================================================|    
  |   +----------------------------------------------------+  |    
  |   | Making websites                                    |  |
  |   |----------------------------------------------------|  |    
  |   |  +----------------------------------------------+  |  |    
  |   |  | HTML/JavaScript                              |  |  |    
  |   |  |----------------------------------------------|  |  |
  |   |  |  +----------------------------------------+  |  |  |    
  |   |  |  |  Write to HTML                         |  |  |  |    
  |   |  |  |----------------------------------------|  |  |  |
  |   |  |  |           document.write()             |  |  |  |    
  |   |  |  |   o -------------------------------->o |  |  |  |    
  |   |  |  +----------------------------------------+  |  |  |    
  |   |  |  +----------------------------------------+  |  |  |    
  |   |  |  |  Change HTML content                   |  |  |  |    
  |   |  |  |----------------------------------------|  |  |  |
  |   |  |  |  document.getElementByID().innerHTML   |  |  |  |    
  |   |  |  | o ---------------------------------->o |  |  |  |    
  |   |  |  +----------------------------------------+  |  |  |    
  |   |  |      ...                                     |  |  |    
  |   |  |  +----------------------------------------+  |  |  |    
  |   |  |  |  (Misc. info)                          |  |  |  |    
  |   |  |  +----------------------------------------+  |  |  |
  |   |  |                                              |  |  |    
  |   |  +----------------------------------------------+  |  |
  |   |                                                    |  |    
  |   +----------------------------------------------------+  |
  |                                                           |    
  +-----------------------------------------------------------+    
```


The annoying part about these tutorials is how quickly they take you from not knowing much about something to being able to visibly make things happen and feel like you've accomplished something, while only giving you a very shallow understanding on things.

This is very much like how most elementary math teachers approach teaching -

1. Imagine you want to find the area of a rectangle.
2. Do `length * breath`


> [1] [Traffic Metrics - Alexa Rank of w3schools.com](https://www.alexa.com/siteinfo/w3schools.com).
> Wayback machine snapshot of the page as of 10/29/2019 [here](https://web.archive.org/web/20191029095310/https://www.alexa.com/siteinfo/w3schools.com).

## Teaching Philosophy

Most people tend to think of learning as being equivalent to going from a state of not being able to do something to a state where one is capable of doing something. Rather, I've always thought that the act of learning is to go from a state of not being able to figure out how to do something - and therefore being incapable of doing it - to a state of knowing enough to be able to figure out how to do something.

This is a small but important distinction, and the latter is also how this website will attempt to teach. Rather than

Both ways of thinking about learning do seem to end with one transitioning to a state of being able to do something, and as such there are many who think of them as being the same thing.

This is probably a direct consequence of how we choose to grade students during their schooling. Consider a child learning basic geometry.

Both ways of thinking about learning do seem to have similar consequences, and as such people tend to think of them as meaning the same thing. While it is true that both end up with one being in a state of being able to do something, the latter

I've always thought that learning something is not equivalent to going from a state of not being able to do something, to being able to do something _doing_ something, but rather to figure out _how_ to do that something.


I've always thought that most teaching is a bit too algorithmic in nature,For instance,

I've always imagined concepts and branches of study as these rooms in one's head, filled with everything one knows about them. For example, consider `Basic Geometry` -

```
     +------------------------------------------------------------------------------+
     |  Basic Geometry  |                                                           |
     +------------------+                                                           |
     |                                                                              |
     |          Pythagorean Theorem                                                 |
     |                                                  Shapes                      |
     |                                                                   Lines      |
     |                        Angles                                                |
     |                                       Area                                   |
     |      Volume                                        Coordinate planes         |
     +------------------------------------------------------------------------------+
```

And all those concepts in the room are another room themselves, consider `Area` -

```

       Basic Geometry

           Area









```

## WIP: Why web development?

Okay, so I don't like the current state of education - how does one go from there to writing about web development?

In the years following the first launch of the iPhone and the subsequent flurry of Android phones the value proposition of a smartphone application or a web application for any consumer-facing business and increased exponentially.

Now about a decade later there is an excess of job opportunities for someone who is capable developer of applications or 'apps`, and not enough trained talent. So much so that companies have had to start programs to train talent themselves so that they can fill available positions, such as Red Ventures' [Road to Hire](https://www.roadtohire.org/).

While I find the education imparted by most institutions to be lacking, it is not, obviously, entirely devoid of value. I think it is possible to take the nuggets of information gleaned over time spent in the education system and use them as a foundation for a solid, intuitive, understanding of the what, why, and how of web development; and thusly help readers find a suitable job for themselves.
