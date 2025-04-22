# Data Manipulation Concepts

This guide covers the **core Python concepts** you need to master for Data Manipulation.

---

## ✅ 1. Dictionary Manipulation

### Count Frequency
```python
count = {}
for item in items:
    count[item] = count.get(item, 0) + 1
```

["apple", "apple", "banana", "orange", "apple"]
- count['apple'] = 3
- count['banana'] = 1
- count['orange'] = 1
    - ('apple', 3), ('banana', 1), ('orange', 1)

### Track Min/Max per Key
```python
if key not in d:
    d[key] = [value, value]
else:
    d[key][0] = min(d[key][0], value)
    d[key][1] = max(d[key][1], value)
```

---

## ✅ 2. Sorting

### Sort by Value (Descending), then Key (Ascending)
```python
sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
```

---

## ✅ 3. String Manipulation

```python
user_id, ts = log.strip().split()
```

---

## ✅ 4. List Comprehension

```python
return [f"{item} {count}" for item, count in sorted_items]
```

---

## ✅ 5. Sets (for Deduplication)

```python
seen = set()
for log in logs:
    if log not in seen:
        seen.add(log)
```

---

## ✅ 6. Range Filtering (e.g. time span)

```python
if (max_ts - min_ts) <= maxSpan:
    result.append(user_id)
```