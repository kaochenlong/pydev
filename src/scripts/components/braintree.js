import Alpine from "alpinejs"
import dropin from "braintree-web-drop-in"

Alpine.data("braintree_drop_in", () => ({
  init() {
    const token = this.$el.dataset.token

    if (token) {
      dropin
        .create({ container: this.$el, authorization: token })
        .then((instance) => {
          const form = this.$el.closest("form")

          if (form) {
            form.addEventListener("submit", (e) => {
              e.preventDefault()

              instance
                .requestPaymentMethod()
                .then(({ nonce }) => {
                  if (nonce) {
                    this.createNonceField(nonce)

                    form.submit()
                  }
                })
                .catch((err) => {
                  console.log("error", err)
                })
            })
          } else {
            console.log("Form is missing")
          }

          console.log("ok!")
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },

  createNonceField(nonce) {
    const field = document.createElement("input")
    field.setAttribute("type", "hidden")
    field.setAttribute("name", "nonce")
    field.setAttribute("value", nonce)

    const form = this.$el.closest("form")
    form.appendChild(field)
  },
}))
