package tr.org.liderahenk.sudoers.plugininfo;

import tr.org.liderahenk.lider.core.api.plugin.IPluginInfo;

public class PluginInfoImpl implements IPluginInfo {
	
	@Override
	public String getPluginName() {
		return "sudoers";
	}

	@Override
	public String getPluginVersion() {
		return "1.0.0";
	}

	@Override
	public String getDescription() {
		return null;
	}

	@Override
	public boolean isMachineOriented() {
		return false;
	}

	@Override
	public boolean isUserOriented() {
		return true;
	}

	@Override
	public boolean isPolicyPlugin() {
		return true;
	}
	
	@Override
	public boolean isxBased() {
		return false;
	}
	
}