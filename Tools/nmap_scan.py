import nmap




def port_scan(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments='-p 1-65535 -T4 -v')  # 扫描所有端口
    return scanner[target]['tcp'].keys()
logo = """
.........................................................................................................................................................
                                            ........................................................    ....                                             
...............................................................,]]]]OOOO@@@@@@@@@OOO]]]].................................................................
                                        . ............]]OO@@@O@@@OO@@@@@@@@@OOOO@@@@OO@@@O@@O@O]`..........                                              
.................................................]/@@@@@@O[[..............................,[\@@@@O@O]`...................................................
                            ................,/@@@@@O[[...........................*...............[O@@@@@@\`.................                             
........................................./@@@@@\\^..............................**.................*..@O@@@O@]`..........................................
                           ..........]/@O@@/`O...O..............*]*]]]]]]]]]]]]]]]]*]*...............,O`..OO@@@OO\`........                              
..................................]@@@@@\/**.O^..=^......]]O@O@@@@@@@@@@@@@@@@@@@@@@@@@@@@OO]`.......=^..=O...OO@@@@\`...................................
                  .... ......../@@@@OO`.*\`.*=\...\`]/O@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@O@@@@@@@@@@O]`=/...O`..=O..=@@@O@O]...............                 
............................/@@@O@^..=^..,O...=^,OO@@@@@@@@@@OO@@@@@@@@@@@@@@@OOo/ooOO@@@O@@@@@@@@@@@O\,O`*..=^.*=/..\@@O@@].............................
                ........./@@@@/`*[O...O...,\,/O@@@OOO@@@@@O@OO@O@@@@@@@@@@@@@@@OOOOoo^O@O@OO@@O@@@OOOO@@@O\`/^..,O...=^.,@@OOO].........                 
......................]@@@OO`/^...\`..,O`,OO@@OOoOOO@@@OOO@OOO@@@@@@@@@@@@@O@@@@OooOO@@@@O@OO@OO@@@OOOooOO@@@O`,@.*,.O*..O.[@O@OO`.......................
        ...........]O@@O/O`*..O....O`.]O@@OOoooooooO@@OOOOOOO@@@@@@@@@O@@@@@@@@@@@@@@@@@@@@OOOOOOO@@Ooooooo/OO@@O\`,@*..=^...//@O@@\`...........         
  ..............]O@OO@@.`.\^*.,O`.,/@@OO/^\oooooo^OOOOOOOOOOO@O@@@@@O@@@@@@@@@@@@@@@@@@@@@@OOOOOOOOOOoooooooooooOO@@O`.=/.../^..,@@O@@\..................
    . ......../@@O@/..=\...=\..,O@@OO`=/^*\[,`,\/oOOOOOOOOOOOO@@@@O@@@@@@@@@@@@@@@@@@@@@@@OOOOOOOOOOOO[/[*,[*`[[o*\\O@@\`.]O*...O`.,@@OO@\.......        
...........,O@O@/`=\...,O`..,/@@OO/***************OOOOOOOOOOOO@@@@O@@@@@@@@@@@@@@@@@@O@@@@OOOOOOOOOOOO****************\O@@\`..,O```,@.\O@@@\.............
 ......../@@OO^\^..,O`*..,@@OOO`******************OOOOOOoOOOOOOOOOO@@@@@@@^*]\@@@@@@@OOOOOOOOoOoOOOOOO*******************\OO@@^...=/..*.@OOO@@`.... .... 
.......,O@@@/`,,\@`*.[O/OOOO[*********************OOOOOO]OOOOOOOOOO@@@@@@@@\@@@@@@@@@OOOOOOOOoO/OOOOOo********************.*\OOO//`...//..,\@OO\.........
......,OOO/^\O/..*,\]OOOO`........................oOOO\OoOOOoOOOOOO@@@@@@@@@@@@@@@@@@OOOOOoO/OO/\oOoO^.......................,/OOOO/O[**./@`\O@O@........
......O@@O@**]*[@@@@OOOOO@`.......................=OO/o,o=o[OoOOOOOO@@@@@@@@@@@@@@@@OOOOOOoO[O]]*ooO^........................OOOOOOO@@@O`***]/@@OO.......
......OOO[\*.\@@@\/[\O@@@O`........................=OOo^/o\/=OOOOOOOOO@@@@@@@@@@@@OOOOOOOOO*O\/*oOOO`.......................,@@@@Oo[\`[@@@^..=OOO@...... 
......\OOOOO/\@@@@@@@OO@OOO]`.......................OOOo\=\[o]OoOOOOOOOOOO@O@OOOOOOOOOOOOO`/\/]ooOO^......................,]]OO@@@@@@@@@@@//@O@@O/.......
.......[O@@@@@@@@\o@\[@O[O@O@@@@O\]`.................\OOo\=O[\O[OOOOOOOOOOOOOOOOOOOOOoOO[O/\O]oOOO^................*]O@@@@@@O@/[\O=*@]/@@@@@@@@/`......  
...........,[[O@@@@@@@@@O/@,=O/\\@@@@@@O`*********.**.\OOOO]O\*O\oOOOOOOOOOOOOOOOOOOOO\/O*/oOoOOO`.********...,/@@O@O@@O`OO,=@O@@@@@@@@@@[[`.............
    ................,[[@@@@@@@@@OO,\/@@@@@@@O]*.****.*.,OOOoOO[oO[O\//OOOOOOOOOOO/\]OO[O/\OOOOO/.****.*.,]O@@@@@@O@O/`@@@@@@@@@@/[`.................     
............................[\@@@@@@@\\\@[OO@@@@@\\]*****,OOOOOOoOo]/\OOOoOOoOoO/O`/o\OOOOOOOO*****./@@@O@@@OOO@/oO@@@@@@@[..............................
       ........... .............,[O@@@@@@Oo@\ooO@@@@@@@O]`*,\OOOOOOO]O/OOOOOOOOOO\OOOOOOOOO/**]/@@@@@@O@Oo\OOo/@@@@@@/`.....................  ..         
.....................................[O@@@@@@OO@\OO@O@@@@@@@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOO@@@@@@@OO\@OOO@OO@@@@@@/`......................................
                        .................[@@@@@@@O@OOOOOOOO@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@OOOOOOOO/@O@@@@@@/`.............                             
............................................,\@@@@@@OOOOOOOOOOOOOOOO@@@@@@@@@@@@@@OOOOOOOOOOOOOOOOO@@@@@@@[..............................................
                        ....   .................[@@@@@@@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO@@@@@@@/..................                                
....................................................[@@@@@@@@@@@OOOOOOOOOOOOOOOOOOOOOOO@@@@@@@@@@@/`.....................................................
                                      ..................[\@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@[`................                                         
................................................................[[[[[@@@@@@@@@@@@[[[[[`.................................................................


                                          _   _   __  __      _      ____             ___    ____     ____  
                                         | \ | | |  \/  |    / \    |  _ \           / _ \  |  _ \   / ___| 
                                         |  \| | | |\/| |   / _ \   | |_) |         | | | | | |_) | | |  _  
                                         | |\  | | |  | |  / ___ \  |  __/     _    | |_| | |  _ <  | |_| | 
                                         |_| \_| |_|  |_| /_/   \_\ |_|       (_)    \___/  |_| \_\  \____| 

                                                                           """
print(logo)

import nmap

def scan(target_host, target_ports, options):
    nm = nmap.PortScanner()
    nm.scan(hosts=target_host, arguments=options)

    for host in nm.all_hosts():
        print(f"Host : {host}")
        print("State : %s" % nm[host].state())

        for proto in nm[host].all_protocols():
            print("Protocol : %s" % proto)

            port_info = nm[host][proto].items()
            for port, info in port_info:
                print(f"Port : {port} \tState : {info['state']}")
                if 'product' in info:
                    print(f"\tProduct: {info['product']}")
                if 'version' in info:
                    print(f"\tVersion: {info['version']}")
                if 'osclass' in info:
                    print("Operating System Information:")
                    for osclass in info['osclass']:
                        print(f"\tFingerprint : {osclass['osfamily']}")
                if 'script' in info:
                    print(f"\tScripts: {info['script']}")

def main():
    target_host = input("Enter target host IP address: ")
    target_ports = input("Enter port range (e.g., 1-100): ")
    options = input("Enter options (e.g., -sV -O): ")

    scan(target_host, target_ports, options)

if __name__ == "__main__":
    main()

