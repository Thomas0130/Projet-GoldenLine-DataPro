SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema goldenlineDB
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `goldenlineDB` ;

-- -----------------------------------------------------
-- Schema goldenlineDB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `goldenlineDB` DEFAULT CHARACTER SET utf8 ;
USE `goldenlineDB` ;

-- -----------------------------------------------------
-- Table `goldenlineDB`.`COLLECTE`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `goldenlineDB`.`COLLECTE` ;

CREATE TABLE IF NOT EXISTS `goldenlineDB`.`COLLECTE` (
  `idCOLLECTE` INT NOT NULL AUTO_INCREMENT,
  `prixAlimentaire` INT NOT NULL DEFAULT 0,
  `prixMultimedia` INT NOT NULL DEFAULT 0,
  `prixVetements` INT NOT NULL DEFAULT 0,
  `prixJeux` INT NOT NULL DEFAULT 0,
  `prixElectromenager` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`idCOLLECTE`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `goldenlineDB`.`CLIENT`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `goldenlineDB`.`CLIENT` ;

CREATE TABLE IF NOT EXISTS `goldenlineDB`.`CLIENT` (
  `idCLIENT` INT NOT NULL AUTO_INCREMENT,
  `nbEnfants` INT NOT NULL DEFAULT 0,
  `categorieSocioprofessionnelle` VARCHAR(64) NOT NULL,
  `prixPanier` INT NOT NULL DEFAULT 0,
  `idCollecte` INT NOT NULL,
  PRIMARY KEY (`idCLIENT`),
  INDEX `idCollecte_idx` (`idCollecte` ASC) VISIBLE,
  CONSTRAINT `idCollecte`
    FOREIGN KEY (`idCollecte`)
    REFERENCES `goldenlineDB`.`COLLECTE` (`idCOLLECTE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
