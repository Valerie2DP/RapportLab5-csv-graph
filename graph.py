import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

# Exemple du code pour le scope_0

# Load data, lire le fichier csv
df = pd.read_csv('scope_0.csv', header=[0,1])
df1 = pd.read_csv('scope_1.csv', header=[0,1])
df2 = pd.read_csv('scope_2.csv', header=[0,1])
df3 = pd.read_csv('scope_3.csv', header=[0,1])
df4 = pd.read_csv('scope_4.csv', header=[0,1])
df5 = pd.read_csv('scope_5.csv', header=[0,1])
df6 = pd.read_csv('scope_6.csv', header=[0,1])
df7 = pd.read_csv('scope_7.csv', header=[0,1])
df8 = pd.read_csv('scope_8.csv', header=[0,1])
df9 = pd.read_csv('scope_9.csv', header=[0,1])


# m = df[[('x-axis','second'), ('2','Volt')]] # a cause qu'on a 2 ligne dans le "header"
# m.plot(x=('x-axis','second'), y = ('2','Volt'))

# faire une matrice, un array d deux dimension contenant ce qui faut pour le graphique

def graphique(data,title):
    if ('1','Volt') in data.columns :
        m1 = data[[('x-axis','second'),('1','Volt')]]
        m1.plot(x=('x-axis','second'),y=('1','Volt'))
        # m1.plot(legend=None)
        

    if  ('2','Volt') in data.columns :
        m2 = data[[('x-axis','second'), ('2','Volt')]] # a cause qu'on a 2 ligne dans le "header"
        m2.plot(x=('x-axis','second'), y = ('2','Volt'))
        # m2.plot(legend=None)
    


    plt.legend('',frameon=False)
    plt.xlabel("Temps [s]")
    plt.ylabel("Tension [V]")
    plt.title(title)
    plt.show()

# Graphique par scope
# graphique(df, 'Signal de sortie (canal 2) avec impulsion parasite (min ou max)') # ** C'est bon
# graphique(df1, 'Signal de sortie wtf ?? pas sur que c\'est revelant') # **Affiche quelquechose de bizarre
# graphique(df2, 'Signal de sortie (canal 2) sans impulsion parasite') # ** C'est bon
# graphique(df3, 'Signal de soirte et d\'entrée (canal 1 et 2)\n utiliser pour calculer la vitesse de propagation') # ** weird car je veux 2 fig en un graphique
# graphique(df4, 'Signal d\'entrée (canal 1) 2 impulsion ') # C'est bon?
# graphique(df5, 'Signal d\'entrée (canal 1) utilisé pour calculer le coefficient de réflexion') # Meme graphique que df4 ??
# graphique(df6, 'Signal d\'entrée (canal 1) court circuit du canal 2?') # C'est bon différent graphique!
# graphique(df7, 'Signal d\'entrée (canal 1) avec l\'adaptation d\'impédance \npour pas avoir de réflexion') # meme bug que le df3, 2 fig s'affiche
# graphique(df8, 'Signal a letape du circuit ouvert??') # meme bug que le df3 et df7 2 fig s'affiche
# graphique(df9, 'allo') # même bug que le df3,df7 et df8.

#if (     '1',   'Volt') in df.columns:
#    print('fonctionne!')
#else:
#    print(':(')


