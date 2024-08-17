import Alpine from "alpinejs"

Alpine.data("resume_comment", () => ({
  canSubmit: false,
  content: "",

  init() {
    this.$watch("content", (value) => {
      this.canSubmit = value.trim() !== ""
    })
  },
}))
