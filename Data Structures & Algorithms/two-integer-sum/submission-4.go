func twoSum(nums []int, target int) []int {
    hashmap := make(map[int] int)
	for i,n := range nums{
		need := target - n
		if j,ok := hashmap[need]; ok{
			return []int{j, i}
		}
		hashmap[n] = i
	}
	return nil
}
