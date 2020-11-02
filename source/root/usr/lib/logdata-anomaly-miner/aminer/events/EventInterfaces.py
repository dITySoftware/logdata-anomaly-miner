"""
This file contains interface definition useful implemented by classes in this directory and for use from code outside this directory.
All classes are defined in separate files, only the namespace references are added here to simplify the code.
"""

import abc


class EventHandlerInterface(metaclass=abc.ABCMeta):
    """
    This is the common interface of all components that can be notified on significant log data mining events.
    To avoid interference with the analysis process, the listener may only perform fast actions within the call. Longer running tasks have
    to be performed asynchronously.
    """

    @abc.abstractmethod
    def receive_event(self, event_type, event_message, sorted_log_lines, event_data, log_atom, event_source):
        """
        Receive information about a detected event.
        @param event_type is a string with the event type class this event belongs to. This information can be used to interpret
        type-specific eventData objects. Together with the eventMessage and sortedLogLines, this can be used to create generic log messages.
        @param event_message the first output line of the event.
        @param sorted_log_lines sorted list of log lines that were considered when generating the event, as far as available to the time
        of the event. The list has to contain at least one line.
        @param event_data type-specific event data object, should not be used unless listener really knows about the eventType.
        @param log_atom the log_atom which produced the event.
        @param event_source reference to detector generating the event
        """


class EventSourceInterface(metaclass=abc.ABCMeta):
    """
    This is the common interface of all event sources.
    Component not implementing this interface may still emit events without support for callbacks.
    """

    @abc.abstractmethod
    def allowlist_event(self, event_type, sorted_log_lines, event_data, allowlisting_data):
        """
        Allowlist an event generated by this source using the information emitted when generating the event.
        @return a message with information about allowlisting
        @throws NotImplementedError if this source does not support allowlisting per se
        @throws Exception when allowlisting of this special event using given allowlisting_data was not possible.
        """
