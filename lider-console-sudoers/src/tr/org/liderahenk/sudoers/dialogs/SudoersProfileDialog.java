package tr.org.liderahenk.sudoers.dialogs;

import java.util.HashMap;
import java.util.Map;

import org.eclipse.swt.SWT;
import org.eclipse.swt.layout.GridLayout;
import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.widgets.Composite;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import tr.org.liderahenk.liderconsole.core.dialogs.IProfileDialog;
import tr.org.liderahenk.liderconsole.core.model.Profile;
import tr.org.liderahenk.sudoers.constants.SudoersConstants;
import tr.org.liderahenk.sudoers.i18n.Messages;

public class SudoersProfileDialog implements IProfileDialog {
	
	private static final Logger logger = LoggerFactory.getLogger(SudoersProfileDialog.class);
	
	// Widgets
	private Button[] btnPrivilege = new Button[2];
	
	@Override
	public void init() {
	}
	
	@Override
	public void createDialogArea(Composite parent, Profile profile) {
		logger.debug("Profile recieved: {}", profile != null ? profile.toString() : null);
		createSudoersInputs(parent, profile);
	}
	
	private void createSudoersInputs(Composite parent, Profile profile){
		
		Composite composite = new Composite(parent, SWT.NONE);
		composite.setLayout(new GridLayout(1, false));
		
		btnPrivilege[0] = new Button(composite, SWT.RADIO);
		btnPrivilege[0].setText(Messages.getString("GRANT_PRIVILEGE"));
		
		btnPrivilege[1] = new Button(composite, SWT.RADIO);
		btnPrivilege[1].setText(Messages.getString("NOT_GRANT_PRIVILEGE"));
		btnPrivilege[1].setSelection(true);
	}
	
	@Override
	public Map<String, Object> getProfileData() throws Exception {
		Map<String, Object> profileData = new HashMap<String, Object>();
		if(btnPrivilege[0].getSelection()) {
			profileData.put(SudoersConstants.PARAMETERS.PRIVILEGE, true);
		}
		else {
			profileData.put(SudoersConstants.PARAMETERS.PRIVILEGE, false);
		}
		return profileData;
	}
	
}
