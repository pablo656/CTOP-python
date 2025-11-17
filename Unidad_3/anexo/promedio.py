def promedio(numeros):
    total = 0
    for n in numeros:
        total += n
    return total / len(numeros)

def main():
    nums = [2,4,6]
    print('Lista:', nums)
    print('Promedio:', promedio(nums))

if __name__ == '__main__':
    main()