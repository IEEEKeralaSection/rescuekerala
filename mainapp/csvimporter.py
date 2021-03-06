import codecs
import csv
import datetime


def parsedate(str):
    try:
        if len(str) > 1:
            splitted = str.split("/")
            if len(splitted) == 3:
                if len(splitted[-1]) == 2:
                    return datetime.datetime.strptime(str, "%d/%m/%y")
                else:
                    return datetime.datetime.strptime(str, "%d/%m/%Y")
        return None
    except IndexError:
        return None


def import_inmate_file(csvid, is_recovery=False):

    import django

    django.setup()

    from mainapp.models import Person, CsvBulkUpload

    upload = CsvBulkUpload.objects.get(id=csvid)

    try:
        upload.csv_file.open(mode="rb")
        new_data = csv.DictReader(codecs.iterdecode(upload.csv_file.file, "utf-8"))

        for datum in new_data:
            """
            try:
                identifier_str = (datum.get("phone", "") + datum.get("name","") + datum.get("age",0)).encode('utf-8')
                identifier = md5(identifier_str).hexdigest()
                #this will fail. we should deal with the removed unique_identifier
                p = Person.objects.get(unique_identifier=identifier)
            except ValueError as e:
                print("Invalid camp ID. row = "+ str(datum))
            except RescueCamp.DoesNotExist as e:
                print("Camp does not exist. row = "+ str(datum))

            except Person.DoesNotExist:
            """
            empty = 0
            header = [
                "name",
                "phone",
                "address",
                "notes",
                "district",
                "checkin_date",
                "checkout_date",
                "gender",
                "age",
            ]
            for i in header:
                if not datum.get(i, ""):
                    empty += 1
                    continue
                if datum.get(i, "").strip() == "":
                    empty += 1
            if empty == len(header):
                continue

            gender = 2
            if len(datum.get("gender", "")) > 0:
                if datum.get("gender", "")[0] == "m" or datum.get("gender", "")[0] == "M":
                    gender = 0
                elif datum.get("gender", "")[0] == "f" or datum.get("gender", "")[0] == "F":
                    gender = 1
            age = "-1"
            if datum.get("age", ""):
                if datum.get("age", "").strip() != "":
                    age = datum.get("age", "").strip()
            district = ""
            if datum.get("district", ""):
                district = district.lower()

            Person(
                name=datum.get("name", "")[:50],
                phone=datum.get("phone", ""),
                age=int(float(age)),
                gender=gender,
                address=datum.get("address", ""),
                notes=datum.get("notes", ""),
                camped_at=upload.camp,
                district=datum.get("district", "").lower(),
                status="new",
                checkin_date=parsedate(datum.get("checkin_date", None)),
                checkout_date=parsedate(datum.get("checkout_date", None)),
            ).save()

        if is_recovery:
            csv_name = CsvBulkUpload.objects.get(id=csvid).name
            CsvBulkUpload.objects.filter(id=csvid).update(
                is_completed=True, failure_reason="", name="rec-" + csv_name[:15]
            )
        else:
            CsvBulkUpload.objects.filter(id=csvid).update(is_completed=True, failure_reason="")
    except Exception as e:
        CsvBulkUpload.objects.filter(id=csvid).update(failure_reason=(getattr(e, "message", repr(e))))


# For Shell Testing
# exec(open('mainapp/csvimporter.py').read())
