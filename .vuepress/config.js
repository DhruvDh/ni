module.exports = {
    title: "Blog",
    description: "Just playing around with a blog.",
    theme: 'local',
    themeConfig: {
        nav: [
            { text: 'Home', link: '/' },
            { text: 'External', link: 'https://google.com' },
        ]
    },
    scripts: {
        "docs:build": "vuepress build docs"
    },
    base: "/blog/",
    dest: "docs/",
    port: "8080",
    sidebar: [
        '/',
        '/reactivity',
        ['/page-b', 'Explicit link text']
    ],
    chainWebpack: (config, isServer) => {
        if (!isServer) {
            config.module
                .rule('fonts')
                .test(/\.(ttf|woff|woff2)$/)
                .use('file-loader')
                .loader('file?name=src/css/[name].[ext]')
                .end()
        }
    }
}