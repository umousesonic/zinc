from runner import runner

if __name__ == '__main__':
    r = runner()
    p = 'public class main{public static void main (String[] args){' \
        'public String StudentAnswer(String myInput){' \
        'return "myOutput"; ' \
        '}System.out.println("hello world!");}}'
    print (r.sendCode(p, ''))