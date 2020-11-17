from app.main import db
from app.main.model.notice import Notice


def save_new_notice(data):
    notice = Notice.query.filter_by(
        user_id=data['user_id'], wine_id=data['wine_id']
    ).first()
    if not notice:
        new_notice = Notice(
            user_id=data['user_id'],
            wine_id=data['wine_id'],
            description=data['description'],
            date=data['date'],
        )
        save_changes(new_notice)
        response_object = {'status': 'success', 'message': 'Successfully registered'}
        return response_object, 201
    else:
        response_object = {'status': 'fail', 'message': 'Notice already exists'}
        return response_object, 409


def get_all_notices(args=None):
    if args.page is None and args.item is None:
        return Notice.query.all()
    else:
        return Notice.query.order_by(Notice.id).paginate(args.page,args.item).items


def get_a_notice(id):
    return Notice.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

def delete(id):
    Notice.query.filter_by(id=id).delete()
    db.session.commit()