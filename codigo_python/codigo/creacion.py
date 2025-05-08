import grafo as gr


grafoMalla10=gr.Grafo()
grafoMalla10.generar_malla(filas=5,columnas=5)
grafoMalla10.archivo_grafo('malla_10')

arbolBFSGusano10 = grafoMalla10.BFS(inicio="1_1")
arbolBFSGusano10.archivo_grafo('ArbolBFS_Malla_10')

arbolDfsInteGusano10 = grafoMalla10.DfsIte(inicio="0_0")
arbolDfsInteGusano10.archivo_grafo('arbolDfsInte_Malla_10')

arbolDfsRecGusano1 = grafoMalla10.DfsR(inicio="0_0")
arbolDfsRecGusano1.archivo_grafo('arbolDfsRec_Malla_10')

grafoGusano1=gr.Grafo()
grafoGusano1.grafoErdosReny(30,100)
grafoGusano1.archivo_grafo('GrafoErdosReny1')

arbolBFSGusano1 = grafoGusano1.BFS(inicio=1)
arbolBFSGusano1.archivo_grafo('ArbolBFS1_ErdosReny_1')

arbolDfsInteGusano1 = grafoGusano1.DfsIte(inicio=1)
arbolDfsInteGusano1.archivo_grafo('arbolDfsInte_ErdosReny_1')

arbolDfsRecGusano1 = grafoGusano1.DfsR(inicio=1)
arbolDfsRecGusano1.archivo_grafo('arbolDfsRec_ErdosReny_1')

#2

grafoMalla2=gr.Grafo()
grafoMalla2.generar_malla(filas=20,columnas=20)
grafoMalla2.archivo_grafo('malla_20')

arbolBFSGusano2 = grafoMalla2.BFS(inicio="1_1")
arbolBFSGusano2.archivo_grafo('ArbolBFS_malla_20')

arbolDfsInteGusano2 = grafoMalla2.DfsIte(inicio="0_0")
arbolDfsInteGusano2.archivo_grafo('arbolDfsInte_malla_20')

arbolDfsRecGusano2 = grafoMalla2.DfsR(inicio="0_0")
arbolDfsRecGusano2.archivo_grafo('arbolDfsRec_malla_20')

grafoGusano2=gr.Grafo()
grafoGusano2.grafoErdosReny(30,100)
grafoGusano2.archivo_grafo('GrafoErdosReny2')

arbolBFSGusano2 = grafoGusano2.BFS(inicio=1)
arbolBFSGusano2.archivo_grafo('ArbolBFSErdosReny2')

arbolDfsInteGusano2 = grafoGusano2.DfsIte(inicio=1)
arbolDfsInteGusano2.archivo_grafo('arbolDfsErdosReny2')

arbolDfsRecGusano2 = grafoGusano2.DfsR(inicio=1)
arbolDfsRecGusano2.archivo_grafo('arbolDfsRecErdosReny2')

#3
grafoMalla3=gr.Grafo()
grafoMalla3.generar_malla(filas=30,columnas=30)
grafoMalla3.archivo_grafo('malla_30')

arbolBFSGusano3 = grafoMalla3.BFS(inicio="1_1")
arbolBFSGusano3.archivo_grafo('ArbolBFS_malla_30')

arbolDfsInteGusano3 = grafoMalla3.DfsIte(inicio="0_0")
arbolDfsInteGusano3.archivo_grafo('arbolDfsInte_malla_30')

arbolDfsRecGusano3 = grafoMalla3.DfsR(inicio="0_0")
arbolDfsRecGusano3.archivo_grafo('arbolDfsRec_malla_30')

grafoGusano3=gr.Grafo()
grafoGusano3.grafoErdosReny(500,1500)
grafoGusano3.archivo_grafo('GrafoErdosReny3')

arbolBFSGusano3 = grafoGusano3.BFS(inicio=1)
arbolBFSGusano3.archivo_grafo('ArbolBFSErdosReny3')

arbolDfsInteGusano3 = grafoGusano3.DfsIte(inicio=1)
arbolDfsInteGusano3.archivo_grafo('arbolDfsInteErdosReny3')

arbolDfsRecGusano3 = grafoGusano3.DfsR(inicio=1)
arbolDfsRecGusano3.archivo_grafo('arbolDfsRecErdosReny3')


















