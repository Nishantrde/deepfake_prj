// loader animation
let tl = gsap.timeline();
tl.from('.loader h1', {
  x: 200,
  opacity: 0,
  duration: 1,
  stagger: 0.1,
})
tl.to(".loader h1", {
  opacity: 0,
  x: -40,
  duration: 1,
  stagger: 0.1,
})
tl.to(".loader", {
  opacity: 0,
})
tl.to(".loader", {
  display: "none",
})
tl.from("h3",{
    y:100,
    opacity: 0,
    stagger: 0.1
  })
  tl.from("p", {
    y: 100,
    opacity: 0,
    stagger: 0.1
  })

//cursor animation
let main = document.querySelector(".page");
let vidDiv=document.querySelector(".video");
main.addEventListener("mousemove", (item) => {
    gsap.to('.cursor', {
        x: item.x,
        y: item.y,
        duration: 1,
        ease: "back.out",
    })
    vidDiv.addEventListener("mouseenter",()=>[
       gsap.to('.cursor',{
        scale:5,
        background:"#80808078"
       })
    ])
    vidDiv.addEventListener("mouseleave",()=>[
       gsap.to('.cursor',{
        scale:1,
        background:"#A9A9A9"
       })
    ])
})
  

// features animation

let tl4=gsap.timeline({
  scrollTrigger:{
    trigger:".features",
    start:"50% 50%",
    end:"200% 50%",
    pin:true,
    markers:true,
    scrub:1,
  }
})

tl4.to(".c-one",{
  marginTop:"-25%",
  opacity:"1",

},'sct-1')

tl4.to(".c-two",{
  opacity:"1",

},'sct-2')

tl4.to(".c-one",{
  marginTop:"-100%",
  opacity:"0",

},'sct-2')

tl4.to(".c-three",{
  opacity:"1",

},'sct-2')

tl4.to(".c-two",{
  opacity:"0",

},'sct-3')

tl4.to(".c-one",{
  marginTop:"-145%",
},'sct-3')

tl4.to(".c-three",{
  opacity:"0",

},'sct-4')