function validate(val) {
    var v1 = document.getElementById("name");
    var v2 = document.getElementById("phone");
    var v3 = document.getElementById("address");
    // Add more variables for other input fields as needed
  
    var submitBtn = document.getElementById("submitBtn");
    
    var flag1 = v1.value.trim() !== "";
    var flag2 = v2.value.trim() !== "";
    var flag3 = v3.value.trim() !== "";
    // Add more flag variables for other input fields as needed
  
    var flag = flag1 && flag2 && flag3; // Combine flags for all required fields
  
    if (flag) {
      submitBtn.removeAttribute("disabled");
    } else {
      submitBtn.setAttribute("disabled", "disabled");
    }
}