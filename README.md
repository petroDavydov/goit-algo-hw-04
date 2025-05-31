# goit-algo-hw-04
# Алгоритми сортування
## Аналіз наявних даних

__Висновки порівняльного аналізу сортувань__

1. Порівняльний аналіз алгоритмів за часом виконання
  - Insertion Sort - час виконання зростає квадратично (O(n²)) - повільний
  - Merge Sort (O(n log n)) ефективний навіть на великих масивах - швидший
  - Timsort (sorted())  - продуктивність значно перевищує Insertion Sort та Merge Sort - найшвидший

  * Чим більше number, тим більша різниця між алгоритмами:


<table>
    <tr>
        <th> number </th>
        <th> insertion sort </th>
        <th> merge sort </th>
        <th> timsort sort </th>
    </tr>
    <tr>
        <td> 1 </td>
        <td> 3.008 s </td>
        <td> 0.030 s </td>
        <td> 0.01 s </td>
    </tr>
    <tr>
        <td> 10 </td>
        <td> 31.220 s </td>
        <td> 0.309 s </td>
        <td> 0.022 s</td>
    </tr>
    <tr>
        <td> 100 </td>
        <td> 313.315 s </td>
        <td> 3.110 s </td>
        <td> 0.191 s </td>
    </tr>
    <tr>
        <td> 1000 </td>
        <td> 2555.278 s </td>
        <td> 19.980 s </td>
        <td> 1.092 s </td>
    </tr>
    <tr>
        <td> 10000 </td>
        <td> 19992.756 s </td>
        <td> 200.053 s </td>
        <td> 10.811 s </td>        
    </tr>
</table>