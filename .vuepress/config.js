module.exports = {
    title: "Blog",
    description: "Just playing around with a blog.",
    themeConfig: {
        nav: [
            { text: 'Home', link: '/' },
            { text: 'External', link: 'https://google.com' },
        ]
    },
    scripts: {
        "docs:build": "vuepress build docs"
    },
    base: "/blog/"
    // sidebar: [
    //     '/',
    //     '/page-a',
    //     ['/page-b', 'Explicit link text']
    // ],
}