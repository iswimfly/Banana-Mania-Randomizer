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
		contentPane.add(panel, BorderLayout.CENTER);
		
		JPanel panel_1 = new JPanel();
		panel.add(panel_1);
		panel_1.setLayout(new BoxLayout(panel_1, BoxLayout.Y_AXIS));
		
		JLabel lblNewLabel = new JLabel("Level Selection");
		lblNewLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
		lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel.setAlignmentY(Component.BOTTOM_ALIGNMENT);
		panel_1.add(lblNewLabel);
		
		JPanel panel_2 = new JPanel();
		panel_1.add(panel_2);
		
		JCheckBox SMB1CasualBool = new JCheckBox("SMB1 Casual");
		SMB1CasualBool.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB1NormalBool = new JCheckBox("New check box");
		SMB1NormalBool.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB1ExpertBool = new JCheckBox("New check box");
		SMB1ExpertBool.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB1MasterBool = new JCheckBox("New check box");
		SMB1MasterBool.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox StoryModeBool = new JCheckBox("New check box");
		StoryModeBool.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB2CasualBool = new JCheckBox("New check box");
		SMB2CasualBool.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB2NormalBool = new JCheckBox("New check box");
		SMB2NormalBool.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB2ExpertBool = new JCheckBox("New check box");
		SMB2ExpertBool.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB2MasterBool = new JCheckBox("New check box");
		SMB2MasterBool.setAlignmentX(Component.CENTER_ALIGNMENT);
		SMB1CasualBool.setHorizontalAlignment(SwingConstants.CENTER);
		SMB1NormalBool.setHorizontalAlignment(SwingConstants.CENTER);
		SMB1ExpertBool.setHorizontalAlignment(SwingConstants.CENTER);
		SMB1MasterBool.setHorizontalAlignment(SwingConstants.CENTER);
		StoryModeBool.setHorizontalAlignment(SwingConstants.CENTER);
		SMB2CasualBool.setHorizontalAlignment(SwingConstants.CENTER);
		SMB2NormalBool.setHorizontalAlignment(SwingConstants.CENTER);
		SMB2ExpertBool.setHorizontalAlignment(SwingConstants.CENTER);
		SMB2MasterBool.setHorizontalAlignment(SwingConstants.CENTER);
		panel_2.setLayout(new BoxLayout(panel_2, BoxLayout.Y_AXIS));
		panel_2.add(SMB1CasualBool);
		panel_2.add(SMB1NormalBool);
		panel_2.add(SMB1ExpertBool);
		panel_2.add(SMB1MasterBool);
		panel_2.add(StoryModeBool);
		panel_2.add(SMB2CasualBool);
		panel_2.add(SMB2NormalBool);
		panel_2.add(SMB2ExpertBool);
		panel_2.add(SMB2MasterBool);
		
		
	}
}
