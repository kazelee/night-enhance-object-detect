<template>
    <div>
       <input type="file"  @change="handleFileChange"/>
     
          <button @click="uploadFile">上传</button>
          <br>
         <img :src="imageUrl" v-if="imageUrl">
     </div>
   </template>
   
   <script>
   import axios from "axios";
   
    
   export default {
     data() {
       return {
         imageUrl: '',
       };
     },
     methods: {
       handleFileChange(e) {
         this.file=e.target.files[0];
         const file = e.target.files[0];
         const reader = new FileReader();
         reader.readAsDataURL(file);
         reader.onload = () => {
           this.imageUrl = reader.result;
           this.uploadImage(file);
         };
       },
   
       uploadFile() {
         const formData = new FormData();
         formData.append('file', this.file);
    
         // 发送文件到后端
         axios.post('http://localhost:5000/upload', formData, {
           headers: {
             'Content-Type': 'multipart/form-data'
           }
         })
             .then(response => {
               console.log(response.data);
               // 在这里你可以处理上传成功的逻辑
               if ('error' in response.data) {
                 alert(response.data.error);
                 return
               }
               // 显示成功消息
               alert(response.data);
             })
             .catch(error => {
               console.error(error);
               // 在这里你可以处理上传失败的逻辑
    
               // 显示错误消息
               alert('文件上传失败');
             });
       }
     }
   };
   </script>
    
   <style scoped>
   /* Add your CSS styles here */
   div {
     margin: 20px;
   }
    
   input {
     margin-bottom: 10px;
   }
    
   button {
     padding: 10px;
     background-color: #4caf50;
     color: white;
     border: none;
     border-radius: 4px;
     cursor: pointer;
   }
    
   button:hover {
     background-color: #45a049;
   }
   </style>
    
   