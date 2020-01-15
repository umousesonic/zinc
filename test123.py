from runner import runner

if __name__ == '__main__':
    r = runner()
    p = 'public class main{public static void main (String[] args){System.out.println("hello world!");}}'
    print (r.sendCode(p, ''))