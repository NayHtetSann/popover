/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";
import { Dialog } from "@web/core/dialog/dialog";
import { _t } from "@web/core/l10n/translation";
import { useChildRef } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";

export class DynamicPopup extends Component {
    setup() {
        this.modalRef = useChildRef();
    }

    async _cancel() {
        return this.execButton(false);
    }

    async execButton(callback) {
        this.props.close();
    }

}

DynamicPopup.template = "dynamic_popover.DynamicPopOver";
DynamicPopup.components = { Dialog };

publicWidget.registry.DynamicPopOverForm = publicWidget.Widget.extend({
        selector: '.oe_empty',

        start: function(){
            var self=this;
            self.callDynamicPopover();
        },

        async callDynamicPopover(){
            var responses = await jsonrpc('/fetch/images', {})
            for (var response of responses){
                this.call("dialog", "add", DynamicPopup, {
                    title: _t(""),
                    size: response[0],
                    text: 'Dynamic Popover',
                    image: response[1],
                });
            }
        }
});

