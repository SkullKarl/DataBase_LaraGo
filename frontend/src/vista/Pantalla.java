package vista;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.border.EmptyBorder;
import javax.swing.table.DefaultTableModel;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;

import java.awt.CardLayout;
import java.awt.Font;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.Color;

import javax.swing.DefaultListModel;
import javax.swing.ImageIcon;
import javax.swing.JSeparator;
import javax.swing.JTable;
import java.awt.Component;
import javax.swing.SwingConstants;
import javax.swing.JList;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Pantalla extends JFrame {

	private static final long serialVersionUID = 1L;
	private JPanel contentPane;

	//cardlayour
	
	CardLayout layout = new CardLayout(0,0);
	private JTextField textField;
	private JTextField textField_1;
	private JTable catalogo;
	
	//paneles
	
	private JPanel inventario;
	private JTextField textField_2;
	
	//paneles cotizaciones
	
	private JPanel cotizaciones;
	
	public Pantalla() {
		
		//ventana
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 1124, 640);
		
		//content pane (panel padre/raiz) 
		
		contentPane = new JPanel();
		contentPane.setBackground(new Color(255, 236, 0));
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		
		//seteo del cardlayout en el contentPane
		
		contentPane.setLayout(layout);
		
		//adicion de los sub-paneles al contentPane
		
		JPanel inicio_de_sesion = new JPanel();
		inicio_de_sesion.setBackground(new Color(251, 220, 0));
		contentPane.add(inicio_de_sesion, "inicio_de_sesion");
		inicio_de_sesion.setLayout(null);
		
		JPanel panel_5 = new JPanel();
		panel_5.setBackground(new Color(95, 95, 95));
		panel_5.setBounds(0, 0, 1100, 571);
		inicio_de_sesion.add(panel_5);
		panel_5.setLayout(null);
		
		JSeparator separator = new JSeparator();
		separator.setBounds(53, 200, 980, 2);
		panel_5.add(separator);
		separator.setBackground(new Color(128, 128, 128));
		
		JPanel panel = new JPanel();
		panel.setBounds(275, 213, 551, 301);
		panel_5.add(panel);
		panel.setBackground(new Color(255, 255, 255));
		panel.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("Nombre de usuario:");
		lblNewLabel.setFont(new Font("Tahoma", Font.PLAIN, 16));
		lblNewLabel.setBounds(21, 92, 199, 29);
		panel.add(lblNewLabel);
		
		JLabel lblContrasea = new JLabel("Contraseña:");
		lblContrasea.setFont(new Font("Tahoma", Font.PLAIN, 16));
		lblContrasea.setBounds(21, 167, 199, 29);
		panel.add(lblContrasea);
		
		textField = new JTextField();
		textField.setFont(new Font("Tahoma", Font.PLAIN, 16));
		textField.setBounds(218, 92, 291, 29);
		panel.add(textField);
		textField.setColumns(10);
		
		textField_1 = new JTextField();
		textField_1.setFont(new Font("Tahoma", Font.PLAIN, 16));
		textField_1.setColumns(10);
		textField_1.setBounds(218, 167, 291, 29);
		panel.add(textField_1);
		
		JButton btnNewButton = new JButton("Iniciar sesion");
		btnNewButton.setForeground(new Color(0, 0, 0));
		btnNewButton.setBackground(new Color(255, 255, 255));
		btnNewButton.setFont(new Font("Tahoma", Font.PLAIN, 17));
		btnNewButton.setBounds(218, 245, 144, 29);
		panel.add(btnNewButton);
		
		JPanel ventas = new JPanel();
		contentPane.add(ventas, "ventas");
		
		inventario = new JPanel();
		inventario.setBackground(new Color(103, 103, 103));
		contentPane.add(inventario, "Inventario");
		inventario.setLayout(null);
		
		

		
		//clientes
		
		JPanel clientes = new JPanel();
		clientes.setBackground(new Color(100, 100, 100));
		contentPane.add(clientes, "Clientes");
		clientes.setLayout(null);
		

		//se crea el modelo y tabla de clientes
		
		DefaultTableModel modeloTablaClientes = new DefaultTableModel();
		
		var tablaClientes = new JTable(modeloTablaClientes); 
				
		tablaClientes.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);
		
		//se añaden las columnas y filas al modelo de la tabla clientes
		
		modeloTablaClientes.addColumn("Rut");
		modeloTablaClientes.addColumn("Nombre");
		modeloTablaClientes.addColumn("Correo");
		modeloTablaClientes.addColumn("Telefono");
		modeloTablaClientes.addColumn("Direccion");
		
				
		Object fila1[] = {"12.345.678-5","Marcelo garcia","mGar241@gmail.com","+1 555 123-4567","-"};
		Object fila2[] = {"12.345.678-5","Ernan torres","mGar241@gmail.com","+1 555 987-6543","-"};
		Object fila3[] = {"16.234.567-9","Pedro salazar","mGar241@gmail.com","+44 7700 900123","-"};
		
		modeloTablaClientes.addRow(fila1);
		modeloTablaClientes.addRow(fila2);
		modeloTablaClientes.addRow(fila3);
	
		
		
		tablaClientes.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);
		
		
		tablaClientes.getColumnModel().getColumn(1).setPreferredWidth(200);
		tablaClientes.getColumnModel().getColumn(2).setPreferredWidth(100);
		tablaClientes.getColumnModel().getColumn(3).setPreferredWidth(200);
		tablaClientes.getColumnModel().getColumn(4).setPreferredWidth(200);
		
		//se crea el scroll de la tabla clientes  y se le añade la tabla clientes
			
		var scrollTablaClientes = new JScrollPane(tablaClientes);
		
		scrollTablaClientes.setBounds(149, 124, 774, 420); // tamaño visible
				
		//se añade el scroll de la tabla inventario al inventario y se añade la tabla inventario al scroll
				
		clientes.add(scrollTablaClientes);
				
		JPanel panel_2 = new JPanel();
		panel_2.setLayout(null);
		panel_2.setBackground(new Color(48, 47, 74));
		panel_2.setBounds(10, 25, 344, 42);
		clientes.add(panel_2);
		
		JLabel lblNewLabel_2 = new JLabel("Clientes");
		lblNewLabel_2.setBackground(new Color(255, 255, 255));
		lblNewLabel_2.setForeground(new Color(255, 255, 255));
		lblNewLabel_2.setFont(new Font("Tahoma", Font.PLAIN, 19));
		lblNewLabel_2.setBounds(10, 11, 100, 20);
		panel_2.add(lblNewLabel_2);
		
		JButton btnNewButton_2 = new JButton("Añadir");
		btnNewButton_2.setBounds(501, 74, 127, 22);
		clientes.add(btnNewButton_2);
		
		JButton btnNewButton_2_1 = new JButton("Editar");
		btnNewButton_2_1.setBounds(651, 74, 127, 22);
		clientes.add(btnNewButton_2_1);
		
		JButton btnNewButton_2_2 = new JButton("Eliminar");
		btnNewButton_2_2.setBounds(796, 74, 127, 22);
		clientes.add(btnNewButton_2_2);
		
		//paneles orden de compra
		
		JPanel ordenesDeCompra = new JPanel();
		contentPane.add(ordenesDeCompra, "name_617796545983100");
		
		JPanel recepcionDeCompra = new JPanel();
		contentPane.add(recepcionDeCompra, "name_617844210476100");
		
		JPanel crearOrdenDeCompra = new JPanel();
		contentPane.add(crearOrdenDeCompra, "CrearOrdenDeCompra");
		crearOrdenDeCompra.setLayout(null);
		
		JPanel panel_1 = new JPanel();
		panel_1.setLayout(null);
		panel_1.setBackground(new Color(48, 47, 74));
		panel_1.setBounds(10, 29, 344, 42);
		crearOrdenDeCompra.add(panel_1);
		
		JLabel lblNewLabel_1_1 = new JLabel("Crear orden de compra");
		lblNewLabel_1_1.setVerticalAlignment(SwingConstants.BOTTOM);
		lblNewLabel_1_1.setHorizontalAlignment(SwingConstants.RIGHT);
		lblNewLabel_1_1.setForeground(Color.WHITE);
		lblNewLabel_1_1.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblNewLabel_1_1.setBounds(10, 11, 193, 22);
		panel_1.add(lblNewLabel_1_1);
		
		JPanel panel_3 = new JPanel();
		panel_3.setBounds(79, 116, 510, 261);
		crearOrdenDeCompra.add(panel_3);
		
		JPanel crearCotizacion = new JPanel();
		contentPane.add(crearCotizacion, "crearCotizacion");
		
		cotizaciones = new JPanel();
		cotizaciones.setBackground(new Color(100, 100, 100));
		contentPane.add(cotizaciones, "cotizaciones");
		cotizaciones.setLayout(null);
		
		
		//Jmenu y JMenuBar
		
		var barra = new JMenuBar();
		
		this.setJMenuBar(barra);
				
		var menu1 = new JMenu("Opciones de sesion");
		
		var menu2 = new JMenu("Usuarios");
		
		var menu3 = new JMenu("Clientes");
		
		var menu9 = new JMenu("Proveedores");
		
		var menu4 = new JMenu("Materiales");
		
		var menu10 = new JMenu("Productos");
		
		var menu5 = new JMenu("Cotizaciones");
		
		var menu6 = new JMenu("Ventas");
		
		var menu7 = new JMenu("Compras");
		
		var menu8 = new JMenu("Manufacturacion");
		
	
		
		
		
		barra.add(menu1);
		barra.add(menu2);
		barra.add(menu6);
		barra.add(menu9);
		barra.add(menu7);
		barra.add(menu4);
		barra.add(menu3);
		barra.add(menu10);
		barra.add(menu4);
		barra.add(menu5);
		barra.add(menu6);
		barra.add(menu7);
		barra.add(menu8);
		
		//items
		
		//items de inventario
		
		var itemInventario = new JMenuItem("inventario");
		
		//items de compra
		
		var itemCrearOrdenDeCompra= new JMenuItem("Crear orden de compra");
		var itemOrdenesDeCompra= new JMenuItem("Ordenes de compra");
		var itemRecepcionDeCompra= new JMenuItem("Recepcion de compra");
		
		//items de cliente
		
		var itemClientes = new JMenuItem("Clientes");
		
		
		//items de cotizaciones
		
		var itemCrearCotizacion = new JMenuItem("Crear cotizacion");
		
		var itemCotizaciones = new JMenuItem("Cotizaciones");
		
		
		//se añaden los items
		
		menu7.add(itemCrearOrdenDeCompra);
		menu7.add(itemOrdenesDeCompra);
		menu7.add(itemRecepcionDeCompra);
		
		menu4.add(itemInventario);
		
		menu3.add(itemClientes);
		
		menu5.add(itemCrearCotizacion);
		menu5.add(itemCotizaciones);
		
		
		
		
		//action listeners items
		
		itemInventario.addActionListener(e->{
			
			layout.show(contentPane,"Inventario" );
			
		});
		
		//se generan las tablas
		
		generarTablaInventario();
		
		generarTablaCotizaciones();
		
		
	
	
		itemClientes.addActionListener(e->{
		
		layout.show(contentPane,"Clientes" );
		
		});
	
		
		
		itemCotizaciones.addActionListener(e->{
			
		layout.show(contentPane,"cotizaciones");
			
		});
	
	
		
}
	
	
	
	public void generarTablaInventario() {
		
		//tabla inventario******************
		
		DefaultTableModel modeloTablaInventario = new DefaultTableModel();
		
		modeloTablaInventario.addColumn("Reponer");
		modeloTablaInventario.addColumn("Cantidad de existencias");
		modeloTablaInventario.addColumn("N.º de artículo");
		modeloTablaInventario.addColumn("Fecha del último pedido");
		modeloTablaInventario.addColumn("Nombre del artículo");
		modeloTablaInventario.addColumn("Proveedor");
		modeloTablaInventario.addColumn("Ubicación de existencias");
		modeloTablaInventario.addColumn("Descripción");
		modeloTablaInventario.addColumn("Costo por artículo");
		modeloTablaInventario.addColumn("Fecha de última venta");
		modeloTablaInventario.addColumn("Valor total");
		modeloTablaInventario.addColumn("Nivel de reposición");
		modeloTablaInventario.addColumn("Días por pedido");
		modeloTablaInventario.addColumn("Cantidad de reposición del artículo");
		modeloTablaInventario.addColumn("Notas");
		
		Object fila1[] = {"ACEPTAR","100","A123","20-05-2025","A","Cole","Almacen A estante 2"};
		Object fila2[] = {"ACEPTAR","100","B123","20-05-2025","B","Cole","Palé exterior"};
		Object fila3[] = {"REPONER","100","C123","20-05-2025","C","Cole","Sótano,estante 4"};
		Object fila4[] = {"REPONER","100","D123","20-05-2025","D","Cole","Almacen A estante 2"};
		Object fila5[] = {"ACEPTAR","100","E123","20-05-2025","E","Cole","Palé exterior"};
		Object fila6[] = {"ACEPTAR","100","F123","20-05-2025","F","Cole","Sótano,estante 4"};
		Object fila7[] = {"REPONER","100","G123","20-05-2025","G","Cole","Almacen A estante 2"};
		Object fila8[] = {"REPONER","100","H123","20-05-2025","H","Cole","Palé exterior"};
		Object fila9[] = {"ACEPTAR","100","I123","20-05-2025","I","Cole","Sótano,estante 4"};
	
		
		modeloTablaInventario.addRow(fila1);
		modeloTablaInventario.addRow(fila2);
		modeloTablaInventario.addRow(fila3);
		modeloTablaInventario.addRow(fila4);
		modeloTablaInventario.addRow(fila5);
		modeloTablaInventario.addRow(fila6);
		modeloTablaInventario.addRow(fila7);
		modeloTablaInventario.addRow(fila8);
		modeloTablaInventario.addRow(fila9);
		
		//se crea la tabla inventario y se le asigna el modelo de la tabla inventario
		
		var tablaInventario = new JTable(modeloTablaInventario); 
		
		tablaInventario.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);
		
	
		tablaInventario.getColumnModel().getColumn(1).setPreferredWidth(200);
		tablaInventario.getColumnModel().getColumn(2).setPreferredWidth(100);
		tablaInventario.getColumnModel().getColumn(3).setPreferredWidth(200);
		tablaInventario.getColumnModel().getColumn(4).setPreferredWidth(200);
		tablaInventario.getColumnModel().getColumn(5).setPreferredWidth(100);
		tablaInventario.getColumnModel().getColumn(6).setPreferredWidth(200);
		tablaInventario.getColumnModel().getColumn(7).setPreferredWidth(100);
		tablaInventario.getColumnModel().getColumn(8).setPreferredWidth(200);
		tablaInventario.getColumnModel().getColumn(9).setPreferredWidth(200);
		tablaInventario.getColumnModel().getColumn(10).setPreferredWidth(100);
		tablaInventario.getColumnModel().getColumn(11).setPreferredWidth(200);
		tablaInventario.getColumnModel().getColumn(12).setPreferredWidth(100);
		tablaInventario.getColumnModel().getColumn(13).setPreferredWidth(200);
		tablaInventario.getColumnModel().getColumn(14).setPreferredWidth(100);
		
		
		//se crea el scroll de la tabla inventario y se le añade la tabla inventario 
		var scrollTablaInventario = new JScrollPane(tablaInventario);
		scrollTablaInventario.setBounds(10, 120, 1100, 420); // tamaño visible
		
		//se añade el scroll de la tabla inventario al inventario y se añade la tabla inventario al scroll
		
		inventario.add(scrollTablaInventario);
		
		JPanel panel_1 = new JPanel();
		panel_1.setLayout(null);
		panel_1.setBackground(new Color(48, 47, 74));
		panel_1.setBounds(10, 25, 344, 42);
		inventario.add(panel_1);
		
		JLabel lblNewLabel_1 = new JLabel("Valor total del inventario");
		lblNewLabel_1.setVerticalAlignment(SwingConstants.BOTTOM);
		lblNewLabel_1.setHorizontalAlignment(SwingConstants.RIGHT);
		lblNewLabel_1.setForeground(Color.WHITE);
		lblNewLabel_1.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblNewLabel_1.setBounds(10, 11, 193, 22);
		panel_1.add(lblNewLabel_1);
		
		textField_2 = new JTextField();
		textField_2.setColumns(10);
		textField_2.setBounds(10, 66, 344, 30);
		inventario.add(textField_2);
		
		JButton btnNewButton_2_2 = new JButton("Actualizar");
		btnNewButton_2_2.setBounds(866, 70, 127, 22);
		inventario.add(btnNewButton_2_2);
		
		
		
	}
	
	
	public void generarTablaCotizaciones() {
		
		DefaultTableModel modeloTablaCotizaciones= new DefaultTableModel();
		
		modeloTablaCotizaciones.addColumn("ID Cotizacion");
		modeloTablaCotizaciones.addColumn("Estado");
		modeloTablaCotizaciones.addColumn("Fecha");
		modeloTablaCotizaciones.addColumn("Precio");
		modeloTablaCotizaciones.addColumn("ID Usuario");
		modeloTablaCotizaciones.addColumn("RUT Cliente");
		//modeloTablaCotizaciones.addColumn("Descripcion");
		
		
		Object fila1[] = {"143214","Pendiente","20-05-2025 ","-","124122","12.345.678-5"};
		Object fila2[] = {"983217","Aprobada","20-05-2025","-","12.345.678-0"};
		Object fila3[] = {"147519","Rechazada","20-05-2025","-","9.876.543-K"};
		
		modeloTablaCotizaciones.addRow(fila1);
		modeloTablaCotizaciones.addRow(fila2);
		modeloTablaCotizaciones.addRow(fila3);
		
	//se crea la tabla cotizciones y se le asigna el modelo de la tabla cotizaciones
		
		var tablaCotizaciones = new JTable(modeloTablaCotizaciones); 
		
		
	//cambio de tamaño a las columnas
		
		tablaCotizaciones.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);
		
		tablaCotizaciones.getColumnModel().getColumn(0).setPreferredWidth(150);
		tablaCotizaciones.getColumnModel().getColumn(1).setPreferredWidth(150);
		tablaCotizaciones.getColumnModel().getColumn(2).setPreferredWidth(150);
		tablaCotizaciones.getColumnModel().getColumn(3).setPreferredWidth(150);
		tablaCotizaciones.getColumnModel().getColumn(4).setPreferredWidth(100);
		tablaCotizaciones.getColumnModel().getColumn(5).setPreferredWidth(100);
		
		
		
		
		
	//se crea el scroll de la tabla inventario y se le añade la tabla inventario 
		var scrollTablaCotizaciones = new JScrollPane(tablaCotizaciones);
		scrollTablaCotizaciones.setBounds(10, 120, 805, 420); // tamaño visible
				
		//se añade el scroll de la tabla inventario al inventario y se añade la tabla inventario al scroll
				
		cotizaciones.add(scrollTablaCotizaciones);
		
		DefaultListModel<String> modeloListDescripcionCotizacion = new DefaultListModel();
		
		
		
		modeloListDescripcionCotizacion.addElement("Foodtruck 3.5x2");
		modeloListDescripcionCotizacion.addElement("-Aislación térmica del tráiler completo en AISLAPOL ");
		modeloListDescripcionCotizacion.addElement("-Mano de enganche para vehículo");
		modeloListDescripcionCotizacion.addElement("-2 cadenas de se)guridad");
		modeloListDescripcionCotizacion.addElement("-Estabilizador con rueda marca (rueda de maniobra)");
		modeloListDescripcionCotizacion.addElement("-4 llantas americanas, aro 15” pernadura 6x139, con una capacidad de carga de 900 kg c/u ");
		modeloListDescripcionCotizacion.addElement("-4 neumáticos r15 de 8 telas, capacidad de carga de 900 kg c/u");
		
		
		
		JList listDescripcionCotizacion = new JList(modeloListDescripcionCotizacion);
		listDescripcionCotizacion.setBounds(825, 172, 265, 368);
		cotizaciones.add(listDescripcionCotizacion);
		
		JPanel panel = new JPanel();
		panel.setBackground(new Color(0, 0, 64));
		panel.setBounds(825, 122, 265, 49);
		cotizaciones.add(panel);
		panel.setLayout(null);
		
		JLabel lblNewLabel_3 = new JLabel("Descripcion");
		lblNewLabel_3.setBounds(70, 11, 121, 29);
		panel.add(lblNewLabel_3);
		lblNewLabel_3.setForeground(new Color(255, 255, 255));
		lblNewLabel_3.setBackground(new Color(255, 255, 255));
		lblNewLabel_3.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_3.setFont(new Font("Tahoma", Font.PLAIN, 24));
		
		JButton btnNewButton_1 = new JButton("Crear");
		btnNewButton_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btnNewButton_1.setFont(new Font("Tahoma", Font.PLAIN, 14));
		btnNewButton_1.setForeground(new Color(0, 0, 0));
		btnNewButton_1.setBackground(new Color(255, 255, 255));
		btnNewButton_1.setBounds(10, 47, 103, 35);
		cotizaciones.add(btnNewButton_1);
		
		JButton btnNewButton_1_1 = new JButton("Editar");
		btnNewButton_1_1.setForeground(Color.BLACK);
		btnNewButton_1_1.setFont(new Font("Tahoma", Font.PLAIN, 14));
		btnNewButton_1_1.setBackground(Color.WHITE);
		btnNewButton_1_1.setBounds(123, 47, 103, 35);
		cotizaciones.add(btnNewButton_1_1);
		
		JButton btnNewButton_1_2 = new JButton("Aceptar");
		btnNewButton_1_2.setForeground(Color.BLACK);
		btnNewButton_1_2.setFont(new Font("Tahoma", Font.PLAIN, 14));
		btnNewButton_1_2.setBackground(Color.WHITE);
		btnNewButton_1_2.setBounds(712, 47, 103, 35);
		cotizaciones.add(btnNewButton_1_2);
		
	}
}
