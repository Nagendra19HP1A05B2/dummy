function onKeyUp(event) {
  Streamlit.setComponentValue(event.target.myParams)
}

const debounce = (callback, wait) => {
  let timeoutId = null;
  return (...args) => {
    window.clearTimeout(timeoutId);
    timeoutId = window.setTimeout(() => {
      callback.apply(null, args);
    }, wait);
  };
}

/**
 * The component's render function. This will be called immediately after
 * the component is initially loaded, and then again every time the
 * component gets new data from Python.
 */
function onRender(event) {
  // Get the RenderData from the event
  if (!window.rendered) {
    const {
      label,
      value
    } = event.detail.args;

    const input = document.getElementById("input_box");
    const label_el = document.getElementById("label")
    const root = document.getElementById("root")


    const user_button = document.getElementById("lbUserButton")
    user_button.myParams = 'projects'
    user_button.addEventListener('click', onKeyUp)

    const user_button1 = document.getElementById("lbUserButton1")
    user_button1.myParams = 'suites'
    user_button1.addEventListener('click', onKeyUp)

    if (label_el) {
      label_el.innerText = label
    }

    if (value && !input.value) {
      input.value = value
    }
    if (debounce_time > 0) { // is false if debounce_time is 0 or undefined
      input.onkeyup = debounce(onKeyUp, debounce_time)
    }
    else {
      input.onkeyup = onKeyUp
    }

    window.rendered = true
  }
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
// Render with the correct height
Streamlit.setFrameHeight(73)