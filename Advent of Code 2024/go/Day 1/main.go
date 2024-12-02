package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
)

func main() {
	file, err := os.Open("input.txt")
	check(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanWords)

	var list1 []int
	var list2 []int
	var counter bool

	for scanner.Scan() {
		num, err := strconv.Atoi(scanner.Text())
		check(err)

		if counter == false {
			list1 = append(list1, num)
		} else {
			list2 = append(list2, num)
		}
		counter = !counter
	}

	slices.Sort(list1)
	slices.Sort(list2)

	list3 := comuputeDistance(list1, list2)
	fmt.Println(sumDistances(list3)) // Part 1 Answer

	list4 := make(map[int]int)

	for _, value := range list1 {
		for _, otherValue := range list2 {
			if value == otherValue {
				list4[value] += 1
			}
		}
	}

	var sum int
	for key, value := range list4 {
		sum += key * value
	}
	fmt.Println(sum) // Part2 Answer

}

func check(e error) {
	if e != nil {
		os.Exit(1)
	}
}

func comuputeDistance(list1, list2 []int) []int {
	var distanceList []int

	for idx := range list1 {
		diff := list1[idx] - list2[idx]
		if diff < 0 {
			diff = -1 * diff
		}
		distanceList = append(distanceList, diff)
	}
	return distanceList
}

func sumDistances(distances []int) int {
	sum := 0
	for _, distance := range distances {
		sum = sum + distance
	}
	return sum
}
