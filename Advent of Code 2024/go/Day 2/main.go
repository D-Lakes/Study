package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		os.Exit(1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var count int

	for scanner.Scan() {
		reports := convert(scanner.Text())

		if !isConsistent(reports) || !isValidAsc(reports) || !isValidDes(reports) {
			permutations := createPermutations(reports)
			for _, report := range permutations {
				if !isConsistent(report) || !isValidAsc(report) || !isValidDes(report) {
					continue
				}
				count += 1
				break
			}

		} else {
			count += 1
		}
	}

	fmt.Println(count) //answer to part 1 and 2
}

func convert(line string) []int {
	nums := strToInt(strings.Fields(line))
	return nums
}

func strToInt(words []string) []int {
	var nums []int
	for _, value := range words {
		conv, _ := strconv.Atoi(value)
		nums = append(nums, conv)
	}
	return nums
}

func isConsistent(report []int) bool {
	if report[0] > report[1] {
		for i := 0; i < len(report)-1; i++ {
			if report[i] > report[i+1] {
				continue
			} else {
				return false
			}
		}
		return true
	}
	if report[0] < report[1] {
		for i := 0; i < len(report)-1; i++ {
			if report[i] < report[i+1] {
				continue
			} else {
				return false
			}
		}
		return true
	}
	// case where report[0] == report[1]
	return false
}

func isValidDes(report []int) bool {
	for i := 0; i < len(report)-1; i++ {
		if report[i]-report[i+1] > 3 {
			return false
		}
	}
	return true

}
func isValidAsc(report []int) bool {
	for i := 0; i < len(report)-1; i++ {
		if report[i]-report[i+1] < -3 {
			return false
		}
	}
	return true
}

func createPermutations(report []int) [][]int {
	var permutations [][]int
	for idx := range report {
		if idx == len(report)-1 {
			permutations = append(permutations, report[:len(report)-1])
		}
		data := slices.Clone(report)
		data = slices.Delete(data, idx, idx+1)
		permutations = append(permutations, data)
	}
	return permutations
}
