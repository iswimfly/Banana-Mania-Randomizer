import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JCheckBox;
import javax.swing.SwingConstants;
import javax.swing.JSplitPane;
import javax.swing.border.BevelBorder;
import java.awt.FlowLayout;
import javax.swing.BoxLayout;
import java.awt.GridLayout;
import java.awt.CardLayout;
import java.awt.GridBagLayout;
import java.awt.GridBagConstraints;
import javax.swing.GroupLayout;
import javax.swing.GroupLayout.Alignment;
import javax.swing.LayoutStyle.ComponentPlacement;
import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.JTextField;
import java.awt.Font;
import java.awt.Panel;
import java.awt.Component;
import javax.swing.Box;
import java.awt.Color;
import com.jgoodies.forms.layout.FormLayout;
import com.jgoodies.forms.layout.ColumnSpec;
import com.jgoodies.forms.layout.RowSpec;
import javax.swing.SpringLayout;
import java.awt.Insets;

public class LabelDemo extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					LabelDemo frame = new LabelDemo();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public LabelDemo() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 686, 379);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		contentPane.setLayout(new BorderLayout(0, 0));
		setContentPane(contentPane);
		
		JPanel panel = new JPanel();
		contentPane.add(panel, BorderLayout.NORTH);
		panel.setLayout(new BoxLayout(panel, BoxLayout.X_AXIS));
		
		JPanel WorldSelectionPanel = new JPanel();
		panel.add(WorldSelectionPanel);
		WorldSelectionPanel.setAlignmentX(Component.LEFT_ALIGNMENT);
		WorldSelectionPanel.setLayout(new BoxLayout(WorldSelectionPanel, BoxLayout.Y_AXIS));
		
		JPanel panel_1 = new JPanel();
		panel_1.setBorder(new BevelBorder(BevelBorder.LOWERED, null, null, null, null));
		WorldSelectionPanel.add(panel_1);
		panel_1.setLayout(new BoxLayout(panel_1, BoxLayout.Y_AXIS));
		
		JLabel lblNewLabel_1 = new JLabel("World Selection");
		lblNewLabel_1.setAlignmentX(Component.CENTER_ALIGNMENT);
		panel_1.add(lblNewLabel_1);
		
		JPanel panel_3 = new JPanel();
		panel_1.add(panel_3);
		panel_3.setLayout(new BoxLayout(panel_3, BoxLayout.Y_AXIS));
		
		JCheckBox World1Bool = new JCheckBox("World 1");
		JCheckBox World2Bool = new JCheckBox("World 2");
		JCheckBox World3Bool = new JCheckBox("World 3");
		JCheckBox World4Bool = new JCheckBox("World 4");
		JCheckBox World5Bool = new JCheckBox("World 5");
		JCheckBox World6Bool = new JCheckBox("World 6");
		JCheckBox World7Bool = new JCheckBox("World 7");
		JCheckBox World8Bool = new JCheckBox("World 8");
		JCheckBox World9Bool = new JCheckBox("World 9");
		JCheckBox World10Bool = new JCheckBox("World 10");
		
		panel_3.add(World1Bool);
		panel_3.add(World2Bool);
		panel_3.add(World3Bool);
		panel_3.add(World4Bool);
		panel_3.add(World5Bool);
		panel_3.add(World6Bool);
		panel_3.add(World7Bool);
		panel_3.add(World8Bool);
		panel_3.add(World9Bool);
		panel_3.add(World10Bool);
		
		World1Bool.setAlignmentX(Component.CENTER_ALIGNMENT);
		World2Bool.setAlignmentX(Component.CENTER_ALIGNMENT);
		World3Bool.setAlignmentX(Component.CENTER_ALIGNMENT);
		World4Bool.setAlignmentX(Component.CENTER_ALIGNMENT);
		World5Bool.setAlignmentX(Component.CENTER_ALIGNMENT);
		World6Bool.setAlignmentX(Component.CENTER_ALIGNMENT);
		World7Bool.setAlignmentX(Component.CENTER_ALIGNMENT);
		World8Bool.setAlignmentX(Component.CENTER_ALIGNMENT);
		World9Bool.setAlignmentX(Component.CENTER_ALIGNMENT);
		World10Bool.setAlignmentX(Component.CENTER_ALIGNMENT);
		
		JPanel LevelSelectionPanel = new JPanel();
		LevelSelectionPanel.setAlignmentX(Component.RIGHT_ALIGNMENT);
		LevelSelectionPanel.setAlignmentY(0.55f);
		LevelSelectionPanel.setBorder(new BevelBorder(BevelBorder.LOWERED, null, null, null, null));
		panel.add(LevelSelectionPanel);
		LevelSelectionPanel.setLayout(new BoxLayout(LevelSelectionPanel, BoxLayout.Y_AXIS));
		
		JLabel lblNewLabel = new JLabel("Level Selection");
		lblNewLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
		lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel.setAlignmentY(Component.BOTTOM_ALIGNMENT);
		LevelSelectionPanel.add(lblNewLabel);
		
		JPanel panel_2 = new JPanel();
		LevelSelectionPanel.add(panel_2);
		
		JCheckBox SMB1CasualBool = new JCheckBox("SMB1 Casual");
		SMB1CasualBool.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB1NormalBool = new JCheckBox("SMB1 Normal");
		SMB1NormalBool.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB1ExpertBool = new JCheckBox("SMB1 Expert");
		SMB1ExpertBool.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB1MasterBool = new JCheckBox("SMB1 Master");
		SMB1MasterBool.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB2CasualBool = new JCheckBox("SMB2 Casual");
		SMB2CasualBool.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB2NormalBool = new JCheckBox("SMB2 Normal");
		SMB2NormalBool.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB2ExpertBool = new JCheckBox("SMB2 Expert");
		SMB2ExpertBool.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB2MasterBool = new JCheckBox("SMB2 Master");
		SMB2MasterBool.setAlignmentX(Component.CENTER_ALIGNMENT);
		SMB1CasualBool.setHorizontalAlignment(SwingConstants.CENTER);
		SMB1NormalBool.setHorizontalAlignment(SwingConstants.CENTER);
		SMB1ExpertBool.setHorizontalAlignment(SwingConstants.CENTER);
		SMB1MasterBool.setHorizontalAlignment(SwingConstants.CENTER);
		SMB2CasualBool.setHorizontalAlignment(SwingConstants.CENTER);
		SMB2NormalBool.setHorizontalAlignment(SwingConstants.CENTER);
		SMB2ExpertBool.setHorizontalAlignment(SwingConstants.CENTER);
		SMB2MasterBool.setHorizontalAlignment(SwingConstants.CENTER);
		panel_2.setLayout(new BoxLayout(panel_2, BoxLayout.Y_AXIS));
		panel_2.add(SMB1CasualBool);
		panel_2.add(SMB1NormalBool);
		panel_2.add(SMB1ExpertBool);
		panel_2.add(SMB1MasterBool);
		panel_2.add(SMB2CasualBool);
		panel_2.add(SMB2NormalBool);
		panel_2.add(SMB2ExpertBool);
		panel_2.add(SMB2MasterBool);
		
		JCheckBox DeluxeModeBool = new JCheckBox("DX Mode");
		DeluxeModeBool.setHorizontalAlignment(SwingConstants.CENTER);
		DeluxeModeBool.setAlignmentX(0.5f);
		panel_2.add(DeluxeModeBool);
		
		
	}
}
