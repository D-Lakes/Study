package main

import "fmt"
// I dont really understand...
// Now I understand...https://stackoverflow.com/a/37511926/26854191

func intSeq() func() int {
  i := 0
  return func() int {
    i ++
    return i
  }
}

func main() {
  nextInt := intSeq()

  fmt.Println(nextInt())
  fmt.Println(nextInt())
  fmt.Println(nextInt())

  newInts := intSeq()
  fmt.Println(newInts())
}
