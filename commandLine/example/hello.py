import sys

if __name__ == '__main__':

    try:
        for arg in sys.argv:
            print("------> ", arg)

        input("Press enter to exit ")

    except Exception:

        import sys
        import traceback

        print(sys.exc_info()[0])
        print(traceback.format_exc())
        print("Press Enter to continue ...")
        input("Press enter to exit ;)")
