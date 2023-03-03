import streamlit as st
st.title(':orange[Y]:green[KK]:orange[O] :blue[(City Mart Supermarket)]')
st.subheader(':blue[Thamine Branch]')

title = st.text_input('Enter your name or member ID.', 'Ma Khaing Thuzar Wai')
st.write('Your name or ID is :',title)

count = 0
st.header(':green[Select] :orange[Menu]')

st.subheader(':orange[Kyay Oh]')
genre = st.radio('With',('Pork', 'Beef', 'Chicken','Ngar phal','None'))
if genre == 'Pork':
    count += 5000
    st.write('Kyay Oh with pork is 5000.')
        
if genre == 'Beef':
    count += 5500
    st.write('Kyay Oh with beef is 5500.')
        
if genre == 'Chicken':
    count += 5000
    st.write('Kyay Oh with chicken is 5000.')
          
if genre == 'Ngar phal':
    count += 5500
    st.write("Kyay Oh with Ngar phal is 5500.")
    
if genre == 'None':
    count += 0
    st.write('None')
    
    
st.subheader(':orange[Kyay Oh Si Chet]')
sichet = st.radio('With',('pork_', 'beef_', 'chicken_','ngar phal_','None'))
if sichet == 'pork_':
    count += 5500
    st.write('Kyay Oh Si Chet with pork is 5500.')
        
if sichet == 'beef_':
    count += 6000
    st.write('Kyay Oh Si Chet with beef is 6000.')
        
if sichet == 'chicken_':
    count += 5500
    st.write('Kyay Oh Si Chet with chicken is 5500.')
          
if sichet == 'ngar phal_':
    count += 6000
    st.write("Kyay Oh Si Chet with Ngar phal is 6000.")
    
if sichet == 'None':
    count += 0
    st.write('None')
    
    
    
st.subheader(':orange[Drink]')
drink = st.radio('juice',('Stawberry', 'Avogado', 'Lime','Coca Cola','None'))
if drink == 'Stawberry':
    count += 3500
    st.write('Stawberry juice is 3500.')
        
if drink == 'Avogado':
    count += 3500
    st.write('Avogado juice is 3500.')
        
if drink == 'Lime':
    count += 3500
    st.write('Lime soda is 3500.')
          
if drink == 'Coca Cola':
    count += 2000
    st.write("Coca Cola is 2000.")
    
    
if drink == 'None':
    count += 0
    st.write('None')
    
    
    
st.subheader(':orange[Others]')
others = st.radio('special',('Phat Htoke', 'Pork Hmoe lone','None'))
if others == 'Phat Htoke':
    count += 5000
    st.write('Phat Htoke is 5000.')
        
if others == 'Pork Hmoe lone':
    count += 5000
    st.write('Pork Hmoe lone is 5000.')
    
    
if others == 'None':
    count += 0
    st.write('None')
    
    
st.subheader(':blue[Your balance is:]',str(count))
st.subheader(str(count))
    

    
rate = st.slider('Rate Our Service', 0, 10, 7)
st.write("You give us rating ", rate,'.')

text = st.text_input('Enter Your Feedback!!!', 'So good and great')
st.write('Your feedback is :',text)

st.header(' _:orange[THANK YOU ] :green[SO MUCH!!!]_ ')
