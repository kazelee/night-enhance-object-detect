import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router';
import { usePermissStore } from '../store/permiss';
import Home from '../views/home.vue';
import NProgress from 'nprogress'
import 'nprogress/nprogress.css'

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        redirect: '/dashboard',
    },
    {
        path: '/',
        name: 'Home',
        component: Home,
        children: [
            {
                path: '/dashboard',
                name: 'dashboard',
                meta: {
                    title: '系统首页',
                    permiss: '1',
                },
                component: () => import(/* webpackChunkName: "dashboard" */ '../views/dashboard.vue'),
            },
            {
                path: '/info',
                name: 'info',
                meta: {
                    title: '项目介绍',
                    permiss: '2',
                },
                component: () => import(/* webpackChunkName: "table" */ '../views/info.vue'),
            },
            {
                path: '/lolv1',
                name: 'lolv1',
                meta: {
                    title: 'LOL_v1',
                    permiss: '5',
                },
                component: () => import(/* webpackChunkName: "charts" */ '../views/dataset/lolv1.vue'),
            },
            {
                path: '/sid',
                name: 'sid',
                meta: {
                    title: 'SID',
                    permiss: '6',
                },
                component: () => import(/* webpackChunkName: "charts" */ '../views/dataset/sid.vue'),
            },
            {
                path: '/sdsd',
                name: 'sdsd',
                meta: {
                    title: 'SDSD',
                    permiss: '7',
                },
                component: () => import(/* webpackChunkName: "charts" */ '../views/dataset/sdsd.vue'),
            },
            {
                path: '/fivek',
                name: 'fivek',
                meta: {
                    title: 'FiveK',
                    permiss: '8',
                },
                component: () => import(/* webpackChunkName: "charts" */ '../views/dataset/fivek.vue'),
            },
            {
                path: '/bdd100k',
                name: 'bdd100k',
                meta: {
                    title: 'BDD100K',
                    permiss: '10',
                },
                component: () => import(/* webpackChunkName: "charts" */ '../views/dataset/bdd100k.vue'),
            },
            {
                path: '/exdark',
                name: 'exdark',
                meta: {
                    title: 'ExDark',
                    permiss: '11',
                },
                component: () => import(/* webpackChunkName: "charts" */ '../views/dataset/exdark.vue'),
            },
            {
                path: '/permission',
                name: 'permission',
                meta: {
                    title: '权限管理',
                    permiss: '13',
                },
                component: () => import(/* webpackChunkName: "permission" */ '../views/permission.vue'),
            },
            {
                path: '/donate',
                name: 'donate',
                meta: {
                    title: '鼓励作者',
                    permiss: '14',
                },
                component: () => import(/* webpackChunkName: "donate" */ '../views/donate.vue'),
            },
            {
                path: '/my-upload',
                name: 'my-upload',
                meta: {
                    title: '测试运行',
                    permiss: '15',
                },
                component: () => import(/* webpackChunkName: "donate" */ '../views/my-upload.vue'),
            },
            {
                path: '/user',
                name: 'user',
                meta: {
                    title: '个人中心',
                },
                component: () => import(/* webpackChunkName: "user" */ '../views/user.vue'),
            },
            
        ],
    },
    {
        path: '/login',
        name: 'Login',
        meta: {
            title: '登录',
        },
        component: () => import(/* webpackChunkName: "login" */ '../views/login.vue'),
    },
    {
        path: '/403',
        name: '403',
        meta: {
            title: '没有权限',
        },
        component: () => import(/* webpackChunkName: "403" */ '../views/403.vue'),
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
    NProgress.start();
    const role = localStorage.getItem('ms_username');
    const permiss = usePermissStore();
    if (!role && to.path !== '/login') {
        next('/login');
    } else if (to.meta.permiss && !permiss.key.includes(to.meta.permiss)) {
        // 如果没有权限，则进入403
        next('/403');
    } else {
        next();
    }
});

router.afterEach(() => {
    NProgress.done()
})

export default router;
