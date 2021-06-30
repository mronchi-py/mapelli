# (Client Side) Web Languages 

## HTML
https://www.w3schools.com/html/


**div vs span**
`div` is a block element
`span` is an inline element.



## CSS

https://www.w3schools.com/css/

CSS can be added to HTML documents in 3 ways:
- Inline - by using the `style` Attribute inside HTML Elements
- Internal - by using a `<style>` Element in the `<head>` Section
- External - by using a `<link>` Element to link to an external CSS file

*External*
```html
<head>
  <link rel="stylesheet" href="styles.css">
</head>
```

All the styles in a page will "cascade" into a new "virtual" style sheet by the following rules, 
where number one has the highest priority:
1. Inline style (inside an HTML element)
2. External and internal style sheets (in the head section)
3. Browser default


### CSS (Simple) Selectors
*Selector by Element Name*
```css

body {
  color: red;
}
```

*Selector by Element id (HTML Attribute id)*
```css
#foo {
  color: blue;
}
```

*Selector by Element class (HTML Attribute class)*
```css
# Selector by Element class
.bar{
  color: green;
}

```

## JavaScript
https://www.w3schools.com/js/
