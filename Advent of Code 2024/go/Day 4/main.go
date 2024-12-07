package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"regexp"
	"slices"
)

func main() {

	file, _ := os.Open("input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var matrix []string
	for scanner.Scan() {
		matrix = append(matrix, scanner.Text())
	}

	rHMF, _ := regexp.Compile(`XMAS`)
	rHMB, _ := regexp.Compile(`SAMX`)

	var Hsum int //Horizontal Matches
	var Vsum int // Vertical Matches
	var Dsum int // Diagonal Matches

	for idx := range matrix {
		Hsum += horzMatches(matrix[idx], rHMF)
		Hsum += horzMatches(matrix[idx], rHMB)
	}

	_, err := file.Seek(0, io.SeekStart)
	if err != nil {
		os.Exit(1)
	}

	reader := bufio.NewReader(file)

	var transposedMatrix [140][140]byte
	for i := 0; i < 140; i++ {
		for j := 0; j < 140; j++ {
			b, _ := reader.ReadByte()
			if b == 10 { // Newline character
				j--
			} else {
				transposedMatrix[j][i] = b
			}
		}
	}

	for _, byteArray := range transposedMatrix {
		byteSlice := byteArray[:]
		Vsum += horzMatches(string(byteSlice), rHMF)
		Vsum += horzMatches(string(byteSlice), rHMB)
	}

	for i := 0; i < len(matrix)-3; i++ {
		for j := 0; j < len(matrix)-3; j++ {
			var b []byte
			b = append(b, matrix[i][j], matrix[i+1][j+1], matrix[i+2][j+2], matrix[i+3][j+3])
			if rHMF.Match(b) {
				Dsum += 1
			}
			if rHMB.Match(b) {
				Dsum += 1
			}
		}
	}

	var reversedMatrix []string
	for idx := range matrix {
		line := []byte(matrix[idx])
		slices.Reverse(line)
		reversedMatrix = append(reversedMatrix, string(line))
	}

	for i := 0; i < len(reversedMatrix)-3; i++ {
		for j := 0; j < len(reversedMatrix)-3; j++ {
			var b []byte
			b = append(b, reversedMatrix[i][j], reversedMatrix[i+1][j+1], reversedMatrix[i+2][j+2], reversedMatrix[i+3][j+3])
			if rHMF.Match(b) {
				Dsum += 1
			}
			if rHMB.Match(b) {
				Dsum += 1
			}
		}
	}
	fmt.Println("Part 1:", Hsum+Vsum+Dsum)

	r1, _ := regexp.Compile(`MASMS`)
	r2, _ := regexp.Compile(`MASSM`)
	r3, _ := regexp.Compile(`SAMMS`)
	r4, _ := regexp.Compile(`SAMSM`)

	var sum2 int

	for j := 0; j < len(matrix)-2; j++ {
		for i := 0; i < len(matrix)-2; i++ {
			var b []byte
			b = append(b, matrix[j][i], matrix[j+1][i+1], matrix[j+2][i+2], matrix[j+2][i], matrix[j][i+2])
			if r1.Match(b) {
				sum2 += 1
			}
			if r2.Match(b) {
				sum2 += 1
			}
			if r3.Match(b) {
				sum2 += 1
			}
			if r4.Match(b) {
				sum2 += 1
			}
		}
	}
	fmt.Println("Part 2:", sum2)

}

func horzMatches(line string, pattern *regexp.Regexp) int {
	var matches int
	matches = len(pattern.FindAllString(line, -1))
	return matches
}
