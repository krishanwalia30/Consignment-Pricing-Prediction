import os
from ConsignmentPricingPrediction.entity import DataValidationConfig
from ConsignmentPricingPrediction.logging import Logger
class DataValidation:

    def __init__(self, config: DataValidationConfig):
        self.config = config

    def initiate_data_validation(self)-> bool:
        try:    
            validation_status = None

            all_files_at_data_path = os.listdir(self.config.data_path)

            for file in self.config.required_files:
                if file in all_files_at_data_path:
                    validation_status = True
                else:
                    validation_status = False
                    break
            
            with open(self.config.status_file, 'w') as file_obj:
                file_obj.write(f"Validation Status: {validation_status}")
                
            # The code below is problematic, see last kernel for explanation
            # for file in all_files_at_data_path:
            #     if file not in self.config.required_files:
            #         validation_status = False
            #         with open(self.config.status_file, 'w') as file_obj:
            #             file_obj.write(f"Validation Status: {validation_status}")

            #     else:
            #         validation_status = True
            #         with open(self.config.status_file, 'w') as file_obj:
            #             file_obj.write(f"Validation Status: {validation_status}")

            Logger.info(f"Data Validation Status: {validation_status}")
            return validation_status
        except Exception as e:
            raise e