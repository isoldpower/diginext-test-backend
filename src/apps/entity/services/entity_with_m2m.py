from ..models import Label, CoordinateEntity


def create_with_m2m(self, validated_data):
    label = validated_data.pop('labels', [])
    instance = CoordinateEntity.objects.create(**validated_data)
    instance.labels.set(get_or_create_labels(self, label))
    return instance


def update_with_m2m(self, instance, validated_data):
    label = validated_data.pop('labels', [])
    instance.labels.set(create_or_update_labels(self, label))
    fields = ['id', 'name', 'x', 'y']
    for field in fields:
        try:
            setattr(instance, field, validated_data[field])
        except KeyError:
            pass
    instance.save()
    return instance


def get_or_create_labels(self, labels):
    label_ids = []

    for label in labels:
        label_instance, created = Label.objects.get_or_create(pk=label.get('id'), defaults=label)
        label_ids.append(label_instance.pk)
    return label_ids


def create_or_update_labels(self, labels):
    label_ids = []

    for label in labels:
        label_instance, created = Label.objects.update_or_create(pk=label.get('id'), defaults=label)
        label_ids.append(label_instance.pk)
    return label_ids
