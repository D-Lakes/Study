package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {

	file, _ := os.Open("input.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)

	r1, _ := regexp.Compile(`mul\(\d{1,3},\d{1,3}\)`)
	var matches [][]string

	for scanner.Scan() {
		matches = append(matches, r1.FindAllString(scanner.Text(), -1))
	}

	r2, _ := regexp.Compile(`\d{1,3}`)

	var pairs [][]string

	for _, match := range matches {
		for _, list := range match {
			pairs = append(pairs, (r2.FindAllString(list, -1)))
		}
	}

	var sum int

	for _, value := range pairs {
		nums := strToInt(value)
		sum += nums[0] * nums[1]

	}

	fmt.Println(sum) //part 1 answer
	file.Close()

	data, _ := os.ReadFile("input.txt")
	line := string(data)
	before, after, _ := strings.Cut(line, "don't()")

	donts := strings.Split(after, "don't()")
	var dos []string
	dos = append(dos, before)

	for _, value := range donts {
		_, a, _ := strings.Cut(value, "do()")
		dos = append(dos, a)
	}

	var matches2 [][]string
	for _, match2 := range dos {
		matches2 = append(matches2, r1.FindAllString(match2, -1))
	}

	var pairs2 [][]string
	for _, pair2 := range matches2 {
		for _, pair3 := range pair2 {

			pairs2 = append(pairs2, r2.FindAllString(pair3, -1))
		}
	}

	var sum2 int
	for _, value := range pairs2 {
		nums := strToInt(value)
		sum2 += nums[0] * nums[1]
	}
	fmt.Println(sum2)
}

func strToInt(words []string) []int {
	var nums []int
	for _, value := range words {
		conv, _ := strconv.Atoi(value)
		nums = append(nums, conv)
	}
	return nums
}
