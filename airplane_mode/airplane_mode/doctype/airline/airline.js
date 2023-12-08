frappe.ui.form.on('Airline', {
    refresh: function(frm) { 
        if (frm.doc.website) {
         cur_frm.add_web_link("https://www.airbus.com/en", "Website")
        }
    }
});

