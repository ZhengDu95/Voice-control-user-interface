/*
 * Translated default messages for the jQuery validation plugin.
 * Locale: ZH (Chinese, 中文 (Zhōngwén), 汉语, 漢語)
 */
$.extend( $.validator.messages, {
	required: "Cannot be empty",
	remote: "Please fix this field",
	email: "Invalid email address",
	url: "Invalid network address",
	date: "Invalid date format",
	dateISO: "Date format(YYYY-MM-DD)",
	number: "Invalid number",
	digits: "Digital only",
	creditcard: "Invalid Credit card number format",
	equalTo: "Two different inputs",
	extension: "Invalid suffix",
	maxlength: $.validator.format( "Enter up to {0} character" ),
	minlength: $.validator.format( "Enter at least to {0} character" ),
	rangelength: $.validator.format( "String length between {0} and {1}" ),
	range: $.validator.format( "Value range between {0} and {1}" ),
	max: $.validator.format( "The value should be no more than {0}" ),
	min: $.validator.format( "The value should be no less than {0}" )
} );
