<!-- ImageGrid.vue -->
<template>
    <div class="image-grid">
      <div v-for="image in images" :key="image.id" class="image-item">
        <img :src="image.url" alt="Image" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        images: [
          { id: 1, url: 'http://127.0.0.1:5678/static/img/15.jpg' }
          // Add more image objects here
        ],
      };
    },
  };
  </script>
  
  <style scoped>
  .image-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 16px;
  }
  
  .image-item {
    overflow: hidden;
    border-radius: 8px;
  }
  
  .image-item img {
    width: 100%;
    height: auto;
    object-fit: cover;
  }
  </style>
  