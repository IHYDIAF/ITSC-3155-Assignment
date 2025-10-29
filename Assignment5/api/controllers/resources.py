from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, resources):
    # Create a new instance of the Resources model with the provided data
    db_resources = models.Resources(
        item = resources.item,
        amount = resources.amount
    )
    # Add the newly created Resources object to the database session
    db.add(db_resources)
    # Commit the changes to the database
    db.commit()
    # Refresh the Resources object to ensure it reflects the current state in the database
    db.refresh(db_resources)
    # Return the newly created Resources object
    return db_resources


def read_all(db: Session):
    return db.query(models.Resources).all()


def read_one(db: Session, resources_id):
    return db.query(models.Resources).filter(models.Resources.id == resources_id).first()


def update(db: Session, resources_id, resources):
    # Query the database for the specific resources to update
    db_resources = db.query(models.Resources).filter(models.Resources.id == resources_id)
    # Extract the update data from the provided 'resources' object
    update_data = resources.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_resources.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated resources record
    return db_resources.first()


def delete(db: Session, resources_id):
    # Query the database for the specific resources to delete
    db_resources = db.query(models.Resources).filter(models.Resources.id == resources_id)
    # Delete the database record without synchronizing the session
    db_resources.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
