package presto.error;

public class TerminatedError extends PrestoError {

	private static final long serialVersionUID = 1L;

	public TerminatedError():
		super("Terminated!")
	}

}
