from alarm import *

if __name__ == '__main__':
    # - the probability of Mary Calling given that John called
    P_mary_given_john = alarm_infer.query(variables=["MaryCalls"], evidence={"JohnCalls": "yes"})
    print("# - the probability of Mary Calling given that John called")
    print(P_mary_given_john)


    #- The probability of both John and Mary calling given Alarm
    print("#- The probability of both John and Mary calling given Alarm")
    P_john_and_mary_given_alarm = alarm_infer.query(
        variables=["JohnCalls", "MaryCalls"], evidence={"Alarm": "yes"}
    )
    print(P_john_and_mary_given_alarm)

    # - the probability of Alarm, given that Mary called.
    print("# - the probability of Alarm, given that Mary called")
    P_alarm_given_mary = alarm_infer.query(variables=["Alarm"], evidence={"MaryCalls": "yes"})
    print(P_alarm_given_mary)