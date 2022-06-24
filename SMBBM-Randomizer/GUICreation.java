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

public class GUICreation extends JFrame {

	private JPanel contentPane;
	private JTextField GreenGoalMin;
	private JTextField GreenGoalMax;
	private JTextField RedGoalMin;
	private JTextField RedGoalMax;
	private JTextField Seed;
	private JTextField LevelCount;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					GUICreation frame = new GUICreation();
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
	public GUICreation() {
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
		WorldSelectionPanel.setAlignmentY(0.6f);
		panel.add(WorldSelectionPanel);
		WorldSelectionPanel.setAlignmentX(Component.LEFT_ALIGNMENT);
		WorldSelectionPanel.setLayout(new BoxLayout(WorldSelectionPanel, BoxLayout.Y_AXIS));
		
		JPanel panel_1 = new JPanel();
		panel_1.setBorder(new BevelBorder(BevelBorder.LOWERED, null, null, null, null));
		WorldSelectionPanel.add(panel_1);
		panel_1.setLayout(new BoxLayout(panel_1, BoxLayout.Y_AXIS));
		
		JLabel lblNewLabel_1 = new JLabel("World Selection");
		lblNewLabel_1.setVerticalAlignment(SwingConstants.TOP);
		lblNewLabel_1.setAlignmentY(Component.TOP_ALIGNMENT);
		lblNewLabel_1.setAlignmentX(Component.CENTER_ALIGNMENT);
		panel_1.add(lblNewLabel_1);
		
		JPanel panel_3 = new JPanel();
		panel_1.add(panel_3);
		panel_3.setLayout(new BoxLayout(panel_3, BoxLayout.Y_AXIS));
		
		JCheckBox World1Box = new JCheckBox("World 1");
		JCheckBox World2Box = new JCheckBox("World 2");
		JCheckBox World3Box = new JCheckBox("World 3");
		JCheckBox World4Box = new JCheckBox("World 4");
		JCheckBox World5Box = new JCheckBox("World 5");
		JCheckBox World6Box = new JCheckBox("World 6");
		JCheckBox World7Box = new JCheckBox("World 7");
		JCheckBox World8Box = new JCheckBox("World 8");
		JCheckBox World9Box = new JCheckBox("World 9");
		JCheckBox World10Box = new JCheckBox("World 10");
		
		panel_3.add(World1Box);
		panel_3.add(World2Box);
		panel_3.add(World3Box);
		panel_3.add(World4Box);
		panel_3.add(World5Box);
		panel_3.add(World6Box);
		panel_3.add(World7Box);
		panel_3.add(World8Box);
		panel_3.add(World9Box);
		panel_3.add(World10Box);
		
		World1Box.setAlignmentX(Component.CENTER_ALIGNMENT);
		World2Box.setAlignmentX(Component.CENTER_ALIGNMENT);
		World3Box.setAlignmentX(Component.CENTER_ALIGNMENT);
		World4Box.setAlignmentX(Component.CENTER_ALIGNMENT);
		World5Box.setAlignmentX(Component.CENTER_ALIGNMENT);
		World6Box.setAlignmentX(Component.CENTER_ALIGNMENT);
		World7Box.setAlignmentX(Component.CENTER_ALIGNMENT);
		World8Box.setAlignmentX(Component.CENTER_ALIGNMENT);
		World9Box.setAlignmentX(Component.CENTER_ALIGNMENT);
		World10Box.setAlignmentX(Component.CENTER_ALIGNMENT);
		
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
		
		JCheckBox SMB1CasualBox = new JCheckBox("SMB1 Casual");
		SMB1CasualBox.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB1NormalBox = new JCheckBox("SMB1 Normal");
		SMB1NormalBox.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB1ExpertBox = new JCheckBox("SMB1 Expert");
		SMB1ExpertBox.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB1MasterBox = new JCheckBox("SMB1 Master");
		SMB1MasterBox.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB2CasualBox = new JCheckBox("SMB2 Casual");
		SMB2CasualBox.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB2NormalBox = new JCheckBox("SMB2 Normal");
		SMB2NormalBox.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB2ExpertBox = new JCheckBox("SMB2 Expert");
		SMB2ExpertBox.setAlignmentX(Component.CENTER_ALIGNMENT);
		JCheckBox SMB2MasterBox = new JCheckBox("SMB2 Master");
		SMB2MasterBox.setAlignmentX(Component.CENTER_ALIGNMENT);
		SMB1CasualBox.setHorizontalAlignment(SwingConstants.CENTER);
		SMB1NormalBox.setHorizontalAlignment(SwingConstants.CENTER);
		SMB1ExpertBox.setHorizontalAlignment(SwingConstants.CENTER);
		SMB1MasterBox.setHorizontalAlignment(SwingConstants.CENTER);
		SMB2CasualBox.setHorizontalAlignment(SwingConstants.CENTER);
		SMB2NormalBox.setHorizontalAlignment(SwingConstants.CENTER);
		SMB2ExpertBox.setHorizontalAlignment(SwingConstants.CENTER);
		SMB2MasterBox.setHorizontalAlignment(SwingConstants.CENTER);
		panel_2.setLayout(new BoxLayout(panel_2, BoxLayout.Y_AXIS));
		panel_2.add(SMB1CasualBox);
		panel_2.add(SMB1NormalBox);
		panel_2.add(SMB1ExpertBox);
		panel_2.add(SMB1MasterBox);
		panel_2.add(SMB2CasualBox);
		panel_2.add(SMB2NormalBox);
		panel_2.add(SMB2ExpertBox);
		panel_2.add(SMB2MasterBox);
		
		JCheckBox DeluxeModeBox = new JCheckBox("DX Mode");
		DeluxeModeBox.setHorizontalAlignment(SwingConstants.CENTER);
		DeluxeModeBox.setAlignmentX(0.5f);
		panel_2.add(DeluxeModeBox);
		
		JCheckBox ReverseModeBox = new JCheckBox("Reverse Mode");
		ReverseModeBox.setAlignmentX(Component.CENTER_ALIGNMENT);
		ReverseModeBox.setHorizontalAlignment(SwingConstants.CENTER);
		panel_2.add(ReverseModeBox);
		
		JCheckBox OriginalStageBox = new JCheckBox("OG Stage Mode");
		OriginalStageBox.setAlignmentX(Component.CENTER_ALIGNMENT);
		panel_2.add(OriginalStageBox);
		
		JPanel GoalPanel = new JPanel();
		panel.add(GoalPanel);
		GoalPanel.setLayout(new BoxLayout(GoalPanel, BoxLayout.Y_AXIS));
		
		JLabel GoalLabel = new JLabel("Goal Randomization");
		GoalLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
		GoalPanel.add(GoalLabel);
		
		JPanel GreenGoal = new JPanel();
		GoalPanel.add(GreenGoal);
		
		GreenGoalMin = new JTextField();
		GreenGoalMin.setText("-1");
		GreenGoalMin.setColumns(2);
		
		GreenGoalMax = new JTextField();
		GreenGoalMax.setText("3");
		GreenGoalMax.setColumns(2);
		
		JLabel GreenMinLabel = new JLabel("Min:");
		GreenGoal.setLayout(new FlowLayout(FlowLayout.CENTER, 5, 5));
		
		JCheckBox GreenGoalRandomizedBox = new JCheckBox("Randomize Green Goals?");
		GreenGoalRandomizedBox.setAlignmentX(Component.CENTER_ALIGNMENT);
		GreenGoal.add(GreenGoalRandomizedBox);
		GreenGoal.add(GreenMinLabel);
		GreenGoal.add(GreenGoalMin);
		
		JLabel GreenMaxLabel = new JLabel("Max:");
		GreenGoal.add(GreenMaxLabel);
		GreenGoal.add(GreenGoalMax);
		
		JPanel RedGoal = new JPanel();
		GoalPanel.add(RedGoal);
		
		JCheckBox RedGoalRandomizedBox = new JCheckBox("Randomize Red Goals?");
		RedGoalRandomizedBox.setAlignmentX(0.5f);
		RedGoal.add(RedGoalRandomizedBox);
		
		JLabel RedGoalMinLabel = new JLabel("Min:");
		RedGoal.add(RedGoalMinLabel);
		
		RedGoalMin = new JTextField();
		RedGoalMin.setText("-2");
		RedGoalMin.setColumns(2);
		RedGoal.add(RedGoalMin);
		
		JLabel RedGoalMaxLabel = new JLabel("Max:");
		RedGoal.add(RedGoalMaxLabel);
		
		RedGoalMax = new JTextField();
		RedGoalMax.setText("7");
		RedGoalMax.setColumns(2);
		RedGoal.add(RedGoalMax);
		
		Component verticalStrut = Box.createVerticalStrut(150);
		GoalPanel.add(verticalStrut);
		
		JPanel LevelCountPanel = new JPanel();
		GoalPanel.add(LevelCountPanel);
		
		JCheckBox CustomLevelCountBox = new JCheckBox("Custom Level Count:");
		LevelCountPanel.add(CustomLevelCountBox);
		
		LevelCount = new JTextField();
		LevelCount.setColumns(10);
		LevelCount.setToolTipText("Use this to set a custom level count. Otherwise, the level count will be the total of all difficulties/worlds selected.");
		LevelCountPanel.add(LevelCount);
		
		JPanel SeedPanel = new JPanel();
		GoalPanel.add(SeedPanel);
		
		JLabel SeedLabel = new JLabel("Seed:");
		SeedPanel.add(SeedLabel);
		
		Seed = new JTextField();
		Seed.setColumns(10);
		Seed.setToolTipText("Use this to seed your randomization!");
		SeedPanel.add(Seed);
		
		JPanel RandomizeButton = new JPanel();
		contentPane.add(RandomizeButton, BorderLayout.SOUTH);
		
		JButton StartRandomization = new JButton("Randomize!");
		RandomizeButton.add(StartRandomization);
		
		
	}
}
