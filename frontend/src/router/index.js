import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import DeliveryTracking from '../components/DeliveryTracking.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/delivery/:id', name: 'DeliveryTracking', component: DeliveryTracking, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
