from filtros import construir_url
from buscador import buscar_empleos
from exportador import exportar_csv

def main():
    area = "informatica-y-telecom"
    ciudad = "bogota-dc"
    salario = 4
    experiencia = 4
    contrato = 5

    url = construir_url(area, ciudad, salario, experiencia, contrato)
    print(f"Buscando en: {url}")
    
    resultados = buscar_empleos(url)
    print(f"Se encontraron {len(resultados)} empleos.")
    
    if resultados:
        exportar_csv(resultados)
        print("Exportado a empleos.csv")
    else:
        print("No se encontraron resultados.")

if __name__ == "__main__":
    main()
