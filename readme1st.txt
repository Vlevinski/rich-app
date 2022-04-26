
# Run

$ ./demo.py
[1, 2, 3, 4]
(1, 2, 3, 4)
{'nums_list': [1, 2, 3, 4], 'nums_tuple': (1, 2, 3, 4)}
[True, False]
(env)  /rich-app$ 

## Install

 $ mkdir rich-app
 $ cd rich-app
 /rich-app$ python -m venv env
 /rich-app$ . env/bin/activate
(env)  /rich-app$ pip install Rich
Collecting Rich
  Downloading rich-12.2.0-py3-none-any.whl (229 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 229.8/229.8 KB 1.3 MB/s eta 0:00:00
Collecting pygments<3.0.0,>=2.6.0
  Downloading Pygments-2.12.0-py3-none-any.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 3.8 MB/s eta 0:00:00
Collecting commonmark<0.10.0,>=0.9.0
  Downloading commonmark-0.9.1-py2.py3-none-any.whl (51 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 51.1/51.1 KB 739.0 kB/s eta 0:00:00
Installing collected packages: commonmark, pygments, Rich
Successfully installed Rich-12.2.0 commonmark-0.9.1 pygments-2.12.0
(env)  /rich-app$ 

(env)  /rich-app$ python -m rich
                                 Rich features                                  
                                                                                
    Colors    ✓ 4-bit color                 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
              ✓ 8-bit color                 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
              ✓ Truecolor (16.7 million)    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
              ✓ Dumb terminals              ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
              ✓ Automatic color conversion  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
                                                                                
    Styles    All ansi styles: bold, dim, italic, underline, strikethrough,     
              reverse, and even blink.                                          
                                                                                
     Text     Word wrap text. Justify left, center, right or full.              
                                                                                
              Lorem ipsum       Lorem ipsum        Lorem ipsum Lorem      ipsum 
              dolor sit amet, dolor sit amet,  dolor sit amet, dolor sit  amet, 
              consectetur       consectetur        consectetur consectetur      
              adipiscing        adipiscing    adipiscing elit. adipiscing elit. 
              elit. Quisque    elit. Quisque  Quisque in metus Quisque in metus 
              in metus sed     in metus sed         sed sapien sed       sapien 
              sapien              sapien             ultricies ultricies        
              ultricies          ultricies        pretium a at pretium   a   at 
              pretium a at     pretium a at    justo. Maecenas justo.  Maecenas 
              justo. Maecenas justo. Maecenas  luctus velit et luctus velit  et 
              luctus velit et luctus velit et  auctor maximus. auctor maximus.  
              auctor maximus. auctor maximus.                                   
                                                                                
    Asian     🇨🇳  该库支持中文，日文和韩文文本！                                
   language   🇯🇵                                                                
   support    ライブラリは中国語、日本語、韓国語のテキストをサポートしています  
              🇰🇷  이 라이브러리는 중국어, 일본어 및 한국어 텍스트를 지원합니다  
                                                                                
    Markup    Rich supports a simple bbcode-like markup for color, style, and   
              emoji! 👍 🍎 🐜 🐻 🥖 🚌                                          
                                                                                
    Tables     Date           Title         Production Budget       Box Office  
              ───────────────────────────────────────────────────────────────── 
               Dec 20, 2019   Star Wars:         $275,000,000     $375,126,118  
                              The Rise of                                       
                              Skywalker                                         
               May 25, 2018   Solo: A            $275,000,000     $393,151,347  
                              Star Wars                                         
                              Story                                             
               Dec 15, 2017   Star Wars          $262,000,000   $1,332,539,889  
                              Ep. VIII:                                         
                              The Last                                          
                              Jedi                                              
               May 19, 1999   Star Wars          $115,000,000   $1,027,044,677  
                              Ep. I: The                                        
                              phantom                                           
                              Menace                                            
                                                                                
    Syntax       1 def iter_last(values: Itera  {                               
 highlighting    2 │   """Iterate and generate  │   'foo': [                    
      &          3 │   iter_values = iter(valu  │   │   3.1427,                 
    pretty       4 │   try:                     │   │   (                       
   printing      5 │   │   previous_value = ne  │   │   │   'Paul Atreides',    
                 6 │   except StopIteration:    │   │   │   'Vladimir           
                 7 │   │   return               Harkonnen',                     
                 8 │   for value in iter_value  │   │   │   'Thufir Hawat'      
                 9 │   │   yield False, previo  │   │   )                       
                10 │   │   previous_value = va  │   ],                          
                11 │   yield True, previous_va  │   'atomic': (                 
                                                │   │   False,                  
                                                │   │   True,                   
                                                │   │   None                    
                                                │   )                           
                                                }                               
                                                                                
   Markdown   # Markdown                        ╔═════════════════════════════╗ 
                                                ║          Markdown           ║ 
              Supports much of the *markdown*   ╚═════════════════════════════╝ 
              __syntax__!                                                       
                                                Supports much of the markdown   
              - Headers                         syntax!                         
              - Basic formatting: **bold**,                                     
              *italic*, `code`                   • Headers                      
              - Block quotes                     • Basic formatting: bold,      
              - Lists, and more...                 italic, code                 
                                                 • Block quotes                 
                                                 • Lists, and more...           
                                                                                
    +more!    Progress bars, columns, styled logging handler, tracebacks,       
              etc...                                                            
                                                                                
rendered in 83.6ms (cold cache)
rendered in 34.1ms (warm cache)
╭──────────────────────── Thanks for trying out Rich! ─────────────────────────╮
│                                                                              │
│  We hope you enjoy using         Textualize https://github.com/textualize    │
│  Rich!                                                                       │
│                               Buy devs a ☕ https://ko-fi.com/textualize     │
│  Rich is maintained with ❤                                                   │
│  by Textualize.io                   Twitter https://twitter.com/willmcgugan  │
│                                                                              │
│  - Will McGugan                                                              │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯
(env)  /rich-app$
