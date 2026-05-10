<template>
  <div class="delivery-tracking">
    <h2>Delivery Tracking</h2>
    <p>Delivery ID: {{ deliveryId }}</p>
    <p>Status: {{ status }}</p>
    <p>Estimated Arrival: {{ eta }}</p>
    <div v-if="mapUrl">
      <iframe :src="mapUrl" width="100%" height="300" frameborder="0"></iframe>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const props = defineProps({
  id: { type: String, required: true },
});

const deliveryId = ref(props.id);
const status = ref('');
const eta = ref('');
const mapUrl = ref('');

const fetchDelivery = async () => {
  try {
    const res = await axios.get(`/api/delivery/${deliveryId.value}`);
    const data = res.data;
    status.value = data.status;
    eta.value = data.eta;
    // Example: Google Maps embed URL
    if (data.address) {
      const query = encodeURIComponent(data.address);
      mapUrl.value = `https://www.google.com/maps/embed/v1/place?key=YOUR_API_KEY&q=${query}`;
    }
  } catch (e) {
    console.error('Error fetching delivery', e);
  }
};

onMounted(fetchDelivery);
</script>

<style scoped>
.delivery-tracking {
  padding: 1rem;
}
</style>
