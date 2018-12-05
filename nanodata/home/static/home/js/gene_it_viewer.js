function ajax(url) {
	return new Promise(
		function(resolve, reject) {
			var r = new XMLHttpRequest();
 
			r.onload = function() {
				if(this.status == 200) {
					console.log("Page " + url + " loaded successfully");
					resolve(this.responseText);
				} else {
					console.log("Error " + this.status + " loading " + url);
					reject();
				}
			};
			r.onerror = reject;
			r.open('GET', url);
			r.send();
		}
	);
};



function ajax_post(url, data, params = false) {
	return new Promise(
		function(resolve, reject) {
			var xhr = new XMLHttpRequest();
			if (params){ url += params; };

			var csrftoken = GLOBAL_csrf_token.match(/value="(.*)">/).pop()

			xhr.open('POST', url, true);
			xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");		        
			xhr.setRequestHeader("X-CSRFToken", csrftoken);

			xhr.onreadystatechange = function() {//Call a function when the state changes.
				if(xhr.readyState == 4 && xhr.status == 200) {
					resolve(this.responseText)
				}
			}

			xhr.onerror = reject;
			var json = JSON.stringify(data);
			xhr.send(json);
		}
	);
};



class GeneIT_viewer{
	constructor(id) {
		var that = this;

		var input_text_area = document.getElementById('geneit_input_text_area');
		
		this.output_text_area = document.getElementById('geneit_output_text_area');
		this.output_text = document.getElementById('output_text');
		this.gi_stats_input = document.getElementById('gi_stats_input');
		this.gi_stats_output = document.getElementById('gi_stats_output');
		this.text_input_value = document.getElementById('text_input_value');
		this.conv_selector = document.getElementById('conv_selector');

		var url = input_text_area.getAttribute('data-url');
		this.text_input_value.addEventListener("input", function(){ that.set_post(url); } );
		this.conv_selector.addEventListener("change", function(){ that.set_post(url); })

	};

	set_post(url){
		var that = this;

		var data = {
			'value': that.text_input_value.value, 
			'params': {'method': that.conv_selector.value}
		};

		ajax_post(url, data).then(function(response){
			var json = JSON.parse(response)
			var data = json.data;
			that.set_output_data(data);

		}).catch(function(error) {
			  console.log(error);
		});
	};

	set_output_data(data){
		var that = this;
		// console.log(data)
		that.output_text.innerHTML = data.output_text;
		var stats = data.stats
		that.gi_stats_input.innerHTML = stats.input_bsize;
		that.gi_stats_output.innerHTML = stats.output_bsize;
	};




	response_menu(action){
		var that = this;
	};

	render_all() {
		console.log('render_all_geneit')
	};
};