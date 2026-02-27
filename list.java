// # middle element
// # import java.util.*;
// # class ListNode {
// #     int val;
// #     ListNode next;
// #     ListNode(int val) {
// #         this.val = val;
// #         this.next = null;
// #     }
// # 
// # public class list {
// #     public ListNode findMiddle(ListNode head) {
// #         if (head == null) return null;
// #         ListNode slow = head;
// #         ListNode fast = head;
// #         while (fast != null && fast.next != null) {
// #             slow = slow.next;
// #             fast = fast.next.next;
// #         }
// #         return slow; // middle node
// #     }
// # }

// # delete last occurence of a target
// # public class list {
// #     public ListNode deleteLastOccurrence(ListNode head, int target) {
// #         if (head == null) return null;
// #         ListNode curr = head;
// #         ListNode prev = null;
// #         ListNode lastPrev = null;
// #         ListNode lastCurr = null;
// #         while (curr != null) {
// #             if (curr.val == target) {
// #                 lastPrev = prev;
// #                 lastCurr = curr;
// #             }
// #             prev = curr;
// #             curr = curr.next;
// #         }
// #         if (lastCurr == null) return head;
// #         if (lastPrev == null) {
// #             head = head.next;
// #         } else {
// #             lastPrev.next = lastCurr.next;
// #         }
// #         return head;
// #     }
// # }

// pair swapping in linkedlist
// import java.util.*;
// class ListNode {
//     int val;
//     ListNode next;
//     ListNode(int val) {
//         this.val = val;
//         this.next = null;
//     }
// }
// class list {
//     public ListNode swapPairs(ListNode head) {
//         if (head == null || head.next == null) return head;
//         ListNode first = head;
//         ListNode second = head.next;
//         first.next = swapPairs(second.next);
//         second.next = first;
//         return second; // new head
//     }
//     public static void main(String[] args) {
//         list l = new list();
//         ListNode head = new ListNode(1);
//         head.next = new ListNode(2);
//         head.next.next = new ListNode(3);
//         head.next.next.next = new ListNode(4);
//         head = l.swapPairs(head);
//         // Print 
//         ListNode curr = head;
//         while (curr != null) {
//             System.out.print(curr.val + " ");
//             curr = curr.next;
//         }
//     }
// }

// maximum sum of subarray of length k
// import java.util.*;
// class ListNode {
//     int val;
//     ListNode next;
//     ListNode(int val) {
//         this.val = val;
//         this.next = null;
//     }
// }
// class list {
//     public int maxSumSubarray(int[] arr, int k) {
//         if (arr.length < k) return -1; // not enough elements
//         int maxSum = 0;
//         for (int i = 0; i < k; i++) {
//             maxSum += arr[i];
//         }
//         int currentSum = maxSum;
//         for (int i = k; i < arr.length; i++) {
//             currentSum += arr[i] - arr[i - k];
//             maxSum = Math.max(maxSum, currentSum);
//         }
//         return maxSum;
//     }
//     public static void main(String[] args) {
//         list l = new list();
//         int[] arr = {1, 2, 3, 4, 5};
//         int k = 2;
//         System.out.println(l.maxSumSubarray(arr, k)); // Output: 9 (4 + 5)
//     }
// }

// return the max possible frequency of element after performing atmost k operation
import java.util.*;
class ListNode {
    int val;
    ListNode next;
    ListNode(int val) {
        this.val = val;
        this.next = null;
    }
}
class list {
    public int maxFrequency(int[] arr, int k) {
        Arrays.sort(arr);
        int left = 0;
        int maxFreq = 1;        
        for (int right = 1; right < arr.length; right++) {
            k += arr[right - 1]; // add previous element to k
            while (arr[right] * (right - left) > k) { // if current element can't be made equal to arr[right]
                k -= arr[left]; // remove left element from k
                left++; // move left pointer
            }
            maxFreq = Math.max(maxFreq, right - left + 1); // update max frequency
        }
        return maxFreq;
    }
    public static void main(String[] args) {
        list l = new list();
        int[] arr = {1,8,1,1,1,1,1};
        int k = 4;
        System.out.println(l.maxFrequency(arr, k)); // Output: 3 (all elements  can be made 4)
    }
}

