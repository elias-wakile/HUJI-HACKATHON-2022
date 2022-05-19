<template>
  <div class="manage-closet">
    <Nav />

    <div class="card">
      <Carousel
        :value="products"
        :numVisible="3"
        :numScroll="3"
        :responsiveOptions="responsiveOptions"
      >
        <template #header>
          <h5>Basic</h5>
        </template>
        <template #item="slotProps">
          <div class="product-item">
            <div class="product-item-content">
              <div class="mb-3">
                <img
                  :src="slotProps.data.image"
                  :alt="slotProps.data.name"
                  class="product-image"
                />
              </div>
              <div>
                <h4 class="mb-1">{{ slotProps.data.name }}</h4>
                <div class="car-buttons mt-5">
                  <Button
                    icon="pi pi-search"
                    class="p-button p-button-rounded mr-2"
                  />
                  <Button
                    icon="pi pi-star-fill"
                    class="p-button-success p-button-rounded mr-2"
                  />
                  <Button
                    icon="pi pi-cog"
                    class="p-button-help p-button-rounded"
                  />
                </div>
              </div>
            </div>
          </div>
        </template>
      </Carousel>
    </div>
    <h5>Basic</h5>
    <FileUpload
      mode="basic"
      name="file[]"
      url="http://localhost:8080/"
      accept="image/*"
      :maxFileSize="1000000"
      @upload="onUpload"
      ref="file"
    />
  </div>
</template>

<script>
import { useUserStore } from "@/stores/userStore";
import InputText from "primevue/inputtext";
import Password from "primevue/password";
import Image from "primevue/image";
import TabMenu from "primevue/tabmenu";
import Button from "primevue/button";
import Dropdown from "primevue/dropdown";
import InputNumber from "primevue/inputnumber";
import Slider from "primevue/slider";
import { ref } from "vue";
import FileUpload from "primevue/fileupload";
import Galleria from "primevue/galleria";
import PhotoService from "../../src/service/PhotoService";
import ProductService from "../../src/service/ProductService";
import Nav from "@/components/Nav.vue";
import Carousel from "primevue/carousel";

export default {
  name: "ManageCloset",
  components: {
    InputText,
    Password,
    Image,
    TabMenu,
    Button,
    Dropdown,
    InputNumber,
    Slider,
    FileUpload,
    Galleria,
    Carousel,
    Nav,
  },
  setup() {
    const file = ref(null);
    return { file };
  },
  data() {
    return {
      clothes: [],
      images: null,
      activeIndex: 0,
      products: null,
      responsiveOptions: [
        {
          breakpoint: "1024px",
          numVisible: 3,
          numScroll: 3,
        },
        {
          breakpoint: "600px",
          numVisible: 2,
          numScroll: 2,
        },
        {
          breakpoint: "480px",
          numVisible: 1,
          numScroll: 1,
        },
      ],
    };
  },
  galleriaService: null,
  created() {
    this.galleriaService = new PhotoService();
    this.productService = new ProductService();
  },
  mounted() {
    this.loadClothes();
    this.galleriaService.getImages().then((data) => (this.images = data));
    this.productService
      .getProductsSmall()
      .then((data) => (this.products = data.slice(0, 9)));
  },
  methods: {
    loadClothes() {
      this.clothes = [
        {
          img_url:
            "https://media.dior.com/couture/ecommerce/media/catalog/product/9/e/1594849779_043J615A0589_C980_E08_GHC.jpg?imwidth=800",
          cloth_type: "shirt",
        },
      ];
    },
    imageClick(index) {
      this.activeIndex = index;
      this.displayCustom = true;
    },
    onUpload(event) {
      var formData = new FormData();
      let file = event.target.files[0];
      formData.append("fileName", file.name);
      formData.append();
    },
  },
};
</script>

<style scoped>
.product-item .product-item-content {
  border: 1px solid var(--surface-border);
  border-radius: 3px;
  margin: 0.3rem;
  text-align: center;
  padding: 2rem 0;
}

.product-item .product-image {
  width: 50%;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
}
</style>
