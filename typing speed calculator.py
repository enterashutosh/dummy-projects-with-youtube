import time

text_to_type = "a quick brown fox jumps over a lazy dog"
print(f"type the following text:-\n{text_to_type}\n")
input("press enter to start...\n\n")

start = time.time()
typer_input = input("type the text: ")
end = time.time()

typing_time = end - start
typing_speed = len(typer_input)/typing_time
words_per_minute = (len(typer_input.split())/typing_time)*60

def mistakes(master_text, copy_text):
    error = 0
    for i in range(len(master_text)):
        try:
            if master_text[i] != copy_text[i]:
                error += 1
        except:
            error += 1
    return error

print(f"\n\n\ntime taken: {typing_time:.3f}")
print(f"typing speed (characters per second): {typing_speed:.3f}")
print(f"typing speed (words pe minute): {words_per_minute:.3f}")

print("\nmistakes: ",mistakes(text_to_type, typer_input))