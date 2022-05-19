import { useCssModule } from "vue";

class User {
  constructor(username = "", weight = null, height = null, bodyShape = null) {
    this.username = username;
    this.weight = weight;
    this.height = height;
    this.bodyShape = bodyShape;
  }
}

export default User;
