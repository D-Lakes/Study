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
	file, _ := os.Open("rules.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)

	ruleSet := make(map[int][]int)
	reversedRuleSet := make(map[int][]int)

	for scanner.Scan() {
		b, a, _ := strings.Cut(scanner.Text(), "|")
		page, _ := strconv.Atoi(b)
		rule, _ := strconv.Atoi(a)
		ruleSet[page] = append(ruleSet[page], rule)
		reversedRuleSet[rule] = append(reversedRuleSet[rule], page)
	}

	file2, _ := os.Open("print_order.txt")
	defer file2.Close()
	scanner2 := bufio.NewScanner(file2)

	var tempStrings []string

	for scanner2.Scan() {
		tempStrings = append(tempStrings, scanner2.Text())
	}

	var prints [][]int
	for _, value := range tempStrings {
		prints = append(prints, strToInt(strings.Split(value, ",")))
	}

	var ruleSetKeys []int

	for k := range ruleSet {
		ruleSetKeys = append(ruleSetKeys, k)
	}

	var possiblyValidPrints [][]int
	var inValidPrints [][]int

	for _, printOrder := range prints {
		valid := true
		for idx := range printOrder {
			if slices.Contains(ruleSetKeys, printOrder[idx]) {
				for _, value := range printOrder[:idx] {
					if slices.Contains(ruleSet[printOrder[idx]], value) {
						valid = false
						break
					}
				}
			}
		}
		if valid {
			possiblyValidPrints = append(possiblyValidPrints, printOrder)
		} else {
			inValidPrints = append(inValidPrints, printOrder)
		}
	}

	var validPrints [][]int

	for _, printOrder := range possiblyValidPrints {
		valid := true
		for idx := range printOrder {
			for _, value := range printOrder[idx:] {
				if slices.Contains(reversedRuleSet[printOrder[idx]], value) {
					valid = false

				}
			}
		}
		if valid {
			validPrints = append(validPrints, printOrder)
		} else {
			inValidPrints = append(inValidPrints, printOrder)
		}
	}

	var sum int

	for _, v := range validPrints {
		sum += v[len(v)/2]
	}
	fmt.Println("part 1:", sum)

	for _, printOrder := range inValidPrints {
		for i, page := range printOrder {
			if slices.Contains(ruleSetKeys, page) {
				for j, v := range printOrder[i:] {
					if slices.Contains(ruleSet[page], v) {
						printOrder[i], printOrder[j] = printOrder[j], printOrder[i]

					}
				}
			}
		}
	}

	for _, printOrder := range inValidPrints {
		for i, page := range printOrder {
			if slices.Contains(ruleSetKeys, page) {
				for j, v := range printOrder[:i] {
					if slices.Contains(reversedRuleSet[page], v) {
						printOrder[i], printOrder[j] = printOrder[j], printOrder[i]

					}
				}
			}
		}
	}

	var sum2 int
	for _, v := range inValidPrints {
		sum2 += v[len(v)/2]
	}

	fmt.Println(sum2)
}

func strToInt(words []string) []int {
	var nums []int
	for _, value := range words {
		conv, err := strconv.Atoi(value)
		if err != nil {
			continue
		}
		nums = append(nums, conv)
	}
	return nums
}
