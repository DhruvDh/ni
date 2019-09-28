module.exports = {
    title: "Ni",
    description: "There's stuff in here",
    themeConfig: {
        nav: [
            { text: 'Home', link: '/' },
            { text: 'PWA', link: '/pwa/ ' },
        ],
        sidebar: [
            '/',
            '/PWA/',
            '/PWA/reactivity/'
        ],
        displayAllHeaders: true,
        sidebarDepth: 2
    },
    scripts: {
        "docs:build": "vuepress build docs"
    },
    base: "/ni/",
    dest: "docs/",
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