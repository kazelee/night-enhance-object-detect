<template>
    <div class="sidebar">
        <el-menu
            class="sidebar-el-menu"
            :default-active="onRoutes"
            :collapse="sidebar.collapse"
            background-color="#324157"
            text-color="#bfcbd9"
            active-text-color="#20a0ff"
            unique-opened
            router
        >
            <template v-for="item in items">
                <template v-if="item.subs">
                    <el-sub-menu :index="item.index" :key="item.index" v-permiss="item.permiss">
                        <template #title>
                            <el-icon>
                                <component :is="item.icon"></component>
                            </el-icon>
                            <span>{{ item.title }}</span>
                        </template>
                        <template v-for="subItem in item.subs">
                            <el-sub-menu
                                v-if="subItem.subs"
                                :index="subItem.index"
                                :key="subItem.index"
                                v-permiss="item.permiss"
                            >
                                <template #title>{{ subItem.title }}</template>
                                <el-menu-item v-for="(threeItem, i) in subItem.subs" :key="i" :index="threeItem.index">
                                    {{ threeItem.title }}
                                </el-menu-item>
                            </el-sub-menu>
                            <el-menu-item v-else :index="subItem.index" v-permiss="item.permiss">
                                {{ subItem.title }}
                            </el-menu-item>
                        </template>
                    </el-sub-menu>
                </template>
                <template v-else>
                    <el-menu-item :index="item.index" :key="item.index" v-permiss="item.permiss">
                        <el-icon>
                            <component :is="item.icon"></component>
                        </el-icon>
                        <template #title>{{ item.title }}</template>
                    </el-menu-item>
                </template>
            </template>
        </el-menu>
    </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useSidebarStore } from '../store/sidebar';
import { useRoute } from 'vue-router';

const items = [
    {
        icon: 'Odometer',
        index: '/dashboard',
        title: '系统首页',
        permiss: '1',
    },
    {
        icon: 'DocumentCopy',
        index: '/info',
        title: '项目介绍',
        permiss: '2',
    },
    {
        icon: 'Folder',
        index: '3',
        title: '数据集介绍',
        permiss: '3',
        subs: [
            {
                index: '4',
                title: '训练集',
                permiss: '4',
                subs: [
                    {
                        index: '/lolv1',
                        title: 'LOL 系列',
                        permiss: '5'
                    },
                    {
                        index: '/sid',
                        title: 'SID SMID',
                        permiss: '6'
                    },
                    {
                        index: '/sdsd',
                        title: 'SDSD 系列',
                        permiss: '7'
                    },
                    {
                        index: '/fivek',
                        title: 'FiveK',
                        permiss: '8'
                    }
                ]
            },
            {
                index: '5',
                title: '测试集',
                permiss: '9',
                subs: [
                {
                        index: '/bdd100k',
                        title: 'BDD100K',
                        permiss: '10'
                    },
                    {
                        index: '/exdark',
                        title: 'ExDark',
                        permiss: '11'
                    },
                ],
            },
        ],
    },
    {
        icon: 'Picture',
        index: '/my-upload',
        title: '测试运行',
        permiss: '15',
    }
];

const route = useRoute();
const onRoutes = computed(() => {
    return route.path;
});

const sidebar = useSidebarStore();
</script>

<style scoped>
.sidebar {
    display: block;
    position: absolute;
    left: 0;
    top: 70px;
    bottom: 0;
    overflow-y: scroll;
}
.sidebar::-webkit-scrollbar {
    width: 0;
}
.sidebar-el-menu:not(.el-menu--collapse) {
    width: 250px;
}
.sidebar > ul {
    height: 100%;
}
</style>
