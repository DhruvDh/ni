let data = {
	'_a': 2,
	'b': 2,
	get a() {
		console.log("used a!")
		return this._a;
	},
	set a(val) {
		console.log(`changed a from ${this._a} to ${val}`);
		this._a = val;
		c = this._a + this.b;
	}
}


c = data.a + data.b;

console.log(c)



data.a = 5;

console.log(c)
