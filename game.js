var C;
function preload(){
	C = loadSound('Piano.ff.C4');
}
function setup(){

}

function draw(){

}
function keyPressed(){
	console.log(keyCode);
	if (keyCode == 65) {
		C.setVolume(0.1);
		C.play();
	}
	if (keyCode == 87) {
		cSharp = loadSound('Piano.ff.Db4.mp3');
	}
	if (keyCode == 68) {
		D = loadSound('Piano.ff.D4.mp3');
	}
	if (keyCode == 82) {
		dSharp = loadSound('Piano.ff.Eb4.mp3');
	}
	if (keyCode == 71) {
		E = loadSound('Piano.ff.E4.mp3');
	}
	if (keyCode == 72) {
		F = loadSound('Piano.ff.F4.mp3');
	}
	if (keyCode == 85) {
		fSharp = loadSound('Piano.ff.Gb4.mp3')
	}
	if (keyCode == 75) {
		G = loadSound('Piano.ff.Gf.mp3')
	}
	if (keyCode == 79) {
		gSharp = loadSound('Piano.ff.Ab4.mp3')
	}
	if (keyCode == 90) {
		A = loadSound('Piano.ff.A4.mp3')
	}
	if (keyCode == 83) {
		aSharp = loadSound('Piano.ff.Bb4.mp3')
	}
	if (keyCode == 67) {
		B = loadSound('Piano.ff.B4.mp3')
	}
	if (keyCode == 86) {
		bSharp = loadSound('Piano.ff.C5.mp3')
	}
}
