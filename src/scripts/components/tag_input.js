import Alpine from "alpinejs"
import Tagify from "@yaireo/tagify"

Alpine.data("tag_input", () => ({
  init() {
    new Tagify(this.$el)
  },
}))
