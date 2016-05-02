package tr.org.liderahenk.sudoers.commands;

import tr.org.liderahenk.lider.core.api.plugin.ICommand;
import tr.org.liderahenk.sudoers.plugininfo.PluginInfoImpl;

public abstract class BaseCommand implements ICommand {

	PluginInfoImpl info = new PluginInfoImpl();

	@Override
	public String getPluginName() {
		return info.getPluginName();
	}

	@Override
	public String getPluginVersion() {
		return info.getPluginVersion();
	}

}
