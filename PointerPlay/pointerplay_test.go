package pointerplay_test

import (
	"pointerplay"
	"testing"
)

func TestDouble(t *testing.T) {
	t.Parallel()
	x := pointerplay.MyInt(12)
	want := pointerplay.MyInt(24)
	(&x).Double()
	if want != x {
		t.Errorf("want %d, got %d", want, x)
	}
}
