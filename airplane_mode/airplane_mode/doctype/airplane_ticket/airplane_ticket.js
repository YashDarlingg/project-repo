frappe.ui.form.on('Airplane ticket', {
    refresh: function (frm) {
        frm.add_custom_button("Assign Seat", function () {
            var dialog = new frappe.ui.Dialog({
                title: "Select Seat",
                fields: [
                    {
                        label: __("Seat Number"),
                        fieldname: "seat_number",
                        fieldtype: "Data",
                        reqd: true
                    }
                ],
                primary_action: function () {
                    var seatNumber = dialog.get_value("seat_number");
                    frm.set_value("seat", seatNumber);
                    dialog.hide();
                }
            });
            dialog.show();
        });
    }
});
