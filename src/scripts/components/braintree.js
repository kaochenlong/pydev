import Alpine from "alpinejs"
import dropin from "braintree-web-drop-in"

Alpine.data("braintree_drop_in", () => ({
  init: function () {
    const token = this.$el.dataset.token
    const dropin_obj = { container: this.$el, authorization: token }

    dropin
      .create(dropin_obj)
      .then((_instance) => {
        console.log("ok!")
      })
      .catch((err) => {
        console.log(err)
      })
  },
}))
