module.exports = {
    title: "Ni",
    description: "There's stuff in here",
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
    base: "/ni/",
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
                .loader('file?name=/fonts/[name].[ext]')
                .end()
        }
    }
}