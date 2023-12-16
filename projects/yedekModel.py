from django.db import models
from django.utils.translation import ugettext as _
from django.urls import reverse
from django import forms

# Create your models here.

types = (('1', 'Dam'), ('2', 'Bridge'), ('3', 'Airport'), ('4', 'Subway'), ('5', 'Highway'), ('6', 'Residential'),
         ('7', 'Buildings'), ('8', 'Hotel'), ('9', 'Sport Complex'), ('10', 'Railway'),
         ('11', 'Refineries'), ('12', 'Chemical plant'), ('13', 'Power Generation'), ('14', 'Manifacturing Plants'),
         ('15', 'Hospital'),
         ('16', 'Water or Waste Water Distribution'), ('17', 'Harbour'), ('18', 'Power Transfer'),
         ('19', 'High-Rise Buildings'), ('20', 'Pipeline Transport'),
         )
countries = (
('AD', _('Andorra')), ('AE', _('United Arab Emirates')), ('AF', _('Afghanistan')), ('AG', _('Antigua & Barbuda')),
('AI', _('Anguilla')), ('AL', _('Albania')), ('AM', _('Armenia')), ('AN', _('Netherlands Antilles')),
('AO', _('Angola')), ('AQ', _('Antarctica')),
('AR', _('Argentina')), ('AS', _('American Samoa')), ('AT', _('Austria')), ('AU', _('Australia')), ('AW', _('Aruba')),
('AZ', _('Azerbaijan')), ('BA', _('Bosnia and Herzegovina')),
('BB', _('Barbados')), ('BD', _('Bangladesh')), ('BE', _('Belgium')), ('BF', _('Burkina Faso')), ('BG', _('Bulgaria')),
('BH', _('Bahrain')), ('BI', _('Burundi')), ('BJ', _('Benin')),
('BM', _('Bermuda')), ('BN', _('Brunei Darussalam')), ('BO', _('Bolivia')), ('BR', _('Brazil')), ('BS', _('Bahama')),
('BT', _('Bhutan')), ('BV', _('Bouvet Island')),
('BW', _('Botswana')), ('BY', _('Belarus')), ('BZ', _('Belize')), ('CA', _('Canada')),
('CC', _('Cocos (Keeling) Islands')), ('CF', _('Central African Republic')), ('CG', _('Congo')),
('CH', _('Switzerland')), ('CI', _('Ivory Coast')), ('CK', _('Cook Iislands')), ('CL', _('Chile')),
('CM', _('Cameroon')), ('CN', _('China')), ('CO', _('Colombia')),
('CR', _('Costa Rica')), ('CU', _('Cuba')), ('CV', _('Cape Verde')), ('CX', _('Christmas Island')), ('CY', _('Cyprus')),
('CZ', _('Czech Republic')), ('DE', _('Germany')),
('DJ', _('Djibouti')), ('DK', _('Denmark')), ('DM', _('Dominica')), ('DO', _('Dominican Republic')),
('DZ', _('Algeria')), ('EC', _('Ecuador')), ('EE', _('Estonia')),
('EG', _('Egypt')), ('EH', _('Western Sahara')), ('ER', _('Eritrea')), ('ES', _('Spain')), ('ET', _('Ethiopia')),
('FI', _('Finland')), ('FJ', _('Fiji')),
('FK', _('Falkland Islands (Malvinas)')), ('FM', _('Micronesia')), ('FO', _('Faroe Islands')), ('FR', _('France')),
('FX', _('France, Metropolitan')), ('GA', _('Gabon')),
('GB', _('United Kingdom (Great Britain)')), ('GD', _('Grenada')), ('GE', _('Georgia')), ('GF', _('French Guiana')),
('GH', _('Ghana')), ('GI', _('Gibraltar')),
('GL', _('Greenland')), ('GM', _('Gambia')), ('GN', _('Guinea')), ('GP', _('Guadeloupe')),
('GQ', _('Equatorial Guinea')), ('GR', _('Greece')), ('GS', _('South Georgia and the South Sandwich Islands')),
('GT', _('Guatemala')), ('GU', _('Guam')), ('GW', _('Guinea-Bissau')), ('GY', _('Guyana')), ('HK', _('Hong Kong')),
('HM', _('Heard & McDonald Islands')), ('HN', _('Honduras')),
('HR', _('Croatia')), ('HT', _('Haiti')), ('HU', _('Hungary')), ('ID', _('Indonesia')), ('IE', _('Ireland')),
('IL', _('Israel')), ('IN', _('India')),
('IO', _('British Indian Ocean Territory')),
('IQ', _('Iraq')), ('IR', _('Islamic Republic of Iran')), ('IS', _('Iceland')), ('IT', _('Italy')),
('JM', _('Jamaica')), ('JO', _('Jordan')), ('JP', _('Japan')),
('KE', _('Kenya')), ('KG', _('Kyrgyzstan')), ('KH', _('Cambodia')), ('KI', _('Kiribati')), ('KM', _('Comoros')),
('KN', _('St. Kitts and Nevis')), ('KP', _('Korea, Democratic People\'s Republic of')),
('KR', _('Korea, Republic of')), ('KW', _('Kuwait')), ('KY', _('Cayman Islands')), ('KZ', _('Kazakhstan')),
('LA', _('Lao People\'s Democratic Republic')), ('LB', _('Lebanon')),
('LC', _('Saint Lucia')), ('LI', _('Liechtenstein')), ('LK', _('Sri Lanka')), ('LR', _('Liberia')),
('LS', _('Lesotho')), ('LT', _('Lithuania')), ('LU', _('Luxembourg')),
('LV', _('Latvia')), ('LY', _('Libyan Arab Jamahiriya')), ('MA', _('Morocco')), ('MC', _('Monaco')),
('MD', _('Moldova, Republic of')), ('MG', _('Madagascar')), ('MH', _('Marshall Islands')),
('ML', _('Mali')), ('MN', _('Mongolia')), ('MM', _('Myanmar')), ('MO', _('Macau')),
('MP', _('Northern Mariana Islands')), ('MQ', _('Martinique')), ('MR', _('Mauritania')),
('MS', _('Monserrat')), ('MT', _('Malta')), ('MU', _('Mauritius')), ('MV', _('Maldives')), ('MW', _('Malawi')),
('MX', _('Mexico')), ('MY', _('Malaysia')), ('MZ', _('Mozambique')),
('NA', _('Namibia')), ('NC', _('New Caledonia')), ('NE', _('Niger')), ('NF', _('Norfolk Island')), ('NG', _('Nigeria')),
('NI', _('Nicaragua')), ('NL', _('Netherlands')), ('NO', _('Norway')),
('NP', _('Nepal')), ('NR', _('Nauru')), ('NU', _('Niue')), ('NZ', _('New Zealand')), ('OM', _('Oman')),
('PA', _('Panama')), ('PE', _('Peru')), ('PF', _('French Polynesia')),
('PG', _('Papua New Guinea')), ('PH', _('Philippines')), ('PK', _('Pakistan')), ('PL', _('Poland')),
('PM', _('St. Pierre & Miquelon')), ('PN', _('Pitcairn')), ('PR', _('Puerto Rico')),
('PT', _('Portugal')), ('PW', _('Palau')), ('PY', _('Paraguay')), ('QA', _('Qatar')), ('RE', _('Reunion')),
('RO', _('Romania')), ('RU', _('Russian Federation')), ('RW', _('Rwanda')),
('SA', _('Saudi Arabia')), ('SB', _('Solomon Islands')), ('SC', _('Seychelles')), ('SD', _('Sudan')),
('SE', _('Sweden')), ('SG', _('Singapore')), ('SH', _('St. Helena')),
('SI', _('Slovenia')), ('SJ', _('Svalbard & Jan Mayen Islands')), ('SK', _('Slovakia')), ('SL', _('Sierra Leone')),
('SM', _('San Marino')), ('SN', _('Senegal')), ('SO', _('Somalia')), ('SR', _('Suriname')),
('ST', _('Sao Tome & Principe')), ('SV', _('El Salvador')), ('SY', _('Syrian Arab Republic')), ('SZ', _('Swaziland')),
('TC', _('Turks & Caicos Islands')), ('TD', _('Chad')),
('TF', _('French Southern Territories')), ('TG', _('Togo')), ('TH', _('Thailand')), ('TJ', _('Tajikistan')),
('TK', _('Tokelau')), ('TM', _('Turkmenistan')), ('TN', _('Tunisia')),
('TO', _('Tonga')), ('TP', _('East Timor')), ('TR', _('Turkey')), ('TT', _('Trinidad & Tobago')), ('TV', _('Tuvalu')),
('TW', _('Taiwan, Province of China')), ('TZ', _('Tanzania, United Republic of')),
('UA', _('Ukraine')), ('UG', _('Uganda')), ('UM', _('United States Minor Outlying Islands')),
('US', _('United States of America')), ('UY', _('Uruguay')), ('UZ', _('Uzbekistan')),
('VA', _('Vatican City State (Holy See)')), ('VC', _('St. Vincent & the Grenadines')), ('VE', _('Venezuela')),
('VG', _('British Virgin Islands')), ('VI', _('United States Virgin Islands')),
('VN', _('Viet Nam')), ('VU', _('Vanuatu')), ('WF', _('Wallis & Futuna Islands')), ('WS', _('Samoa')),
('YE', _('Yemen')), ('YT', _('Mayotte')), ('YU', _('Yugoslavia')), ('ZA', _('South Africa')),
('ZM', _('Zambia')), ('ZR', _('Zaire')), ('ZW', _('Zimbabwe')), ('ZZ', _('Unknown or unspecified country')),
)

deliverySys = (('1', 'Design Bid Build'), ('2', 'Design Build'), ('3', 'Construction Management'),
               ('4', 'Public Private Partnership'),)
payType = (('1', 'Unit Price'), ('2', 'Lump Sum- Fixed Fee'), ('3', 'Turn-Key'), ('4', 'Cost Plus'),)
lessMuch = (
('1', 'Definitely Low'), ('2', 'Very Low'), ('3', 'Low'), ('4', 'Medium'), ('5', 'High'), ('6', 'Very High'),
('7', 'Definitely High'),)


class fieldSet(models.Model):
    riskEvent = models.CharField(max_length=100, verbose_name='Risk Event')
    impact = models.IntegerField(editable=True, verbose_name='Impact')
    probability = models.IntegerField(editable=True, verbose_name='Probability')
    effect = models.IntegerField(editable=True, verbose_name='Risk Effect')
    strategy = models.CharField(max_length=100, editable=True, choices=payType, verbose_name='Strategy')
    description = models.CharField(max_length=200, editable=True, verbose_name='Description')
    responcive = models.CharField(max_length=100, choices=payType, verbose_name='Responcible')


class War(models.Model):
    war = models.OneToOneField(fieldSet, verbose_name='War', on_delete=models.CASCADE, primary_key=111)


class Revolution(models.Model):
    Revolution = models.OneToOneField(fieldSet, verbose_name='Revolution', on_delete=models.CASCADE, primary_key=112)


class CivilDisorders(models.Model):
    CivilDisorders = models.OneToOneField(fieldSet, verbose_name='CivilDisorders', on_delete=models.CASCADE,
                                          primary_key=113)


class InconsistencyOfGovernmentalPolicies(models.Model):
    InconsistencyOfGovernmentalPolicies = models.OneToOneField(fieldSet,
                                                               verbose_name='InconsistencyOfGovernmentalPolicies',
                                                               on_delete=models.CASCADE, primary_key=114)


class GNPDecreases(models.Model):
    GNPDecreases = models.OneToOneField(fieldSet, verbose_name='GNPDecreases', on_delete=models.CASCADE,
                                        primary_key=121)


class IncompatibleGNPPerCapita(models.Model):
    IncompatibleGNPPerCapita = models.OneToOneField(fieldSet, verbose_name='IncompatibleGNPPerCapita',
                                                    on_delete=models.CASCADE, primary_key=122)


class InterestRateFluctuation(models.Model):
    InterestRateFluctuation = models.OneToOneField(fieldSet, verbose_name='InterestRateFluctuation',
                                                   on_delete=models.CASCADE, primary_key=123)


class InflationRateIncreasing(models.Model):
    InflationRateIncreasing = models.OneToOneField(fieldSet, verbose_name='InflationRateIncreasing',
                                                   on_delete=models.CASCADE, primary_key=124)


class CurrencyExchangeRateFluctuation(models.Model):
    CurrencyExchangeRateFluctuation = models.OneToOneField(fieldSet, verbose_name='CurrencyExchangeRateFluctuation',
                                                           on_delete=models.CASCADE, primary_key=125)


class TaxRateIncreasing(models.Model):
    TaxRateIncreasing = models.OneToOneField(fieldSet, verbose_name='TaxRateIncreasing', on_delete=models.CASCADE,
                                             primary_key=126)


class LanguageBarrier(models.Model):
    LanguageBarrier = models.OneToOneField(fieldSet, verbose_name='LanguageBarrier', on_delete=models.CASCADE,
                                           primary_key=131)


class ReligiousInconsistency(models.Model):
    ReligiousInconsistency = models.OneToOneField(fieldSet, verbose_name='ReligiousInconsistency',
                                                  on_delete=models.CASCADE, primary_key=132)


class CultureTraditionDifferences(models.Model):
    CultureTraditionDifferences = models.OneToOneField(fieldSet, verbose_name='CultureTraditionDifferences',
                                                       on_delete=models.CASCADE, primary_key=133)


class InsecurityAndCrime(models.Model):
    InsecurityAndCrime = models.OneToOneField(fieldSet, verbose_name='InsecurityAndCrime', on_delete=models.CASCADE,
                                              primary_key=134)


class Pestilence(models.Model):
    Pestilence = models.OneToOneField(fieldSet, verbose_name='Pestilence', on_delete=models.CASCADE, primary_key=135)


class BribeAndCorruption(models.Model):
    BribeAndCorruption = models.OneToOneField(fieldSet, verbose_name='BribeAndCorruption', on_delete=models.CASCADE,
                                              primary_key=136)


class PopularInInformalRelationships(models.Model):
    PopularInInformalRelationships = models.OneToOneField(fieldSet, verbose_name='PopularInInformalRelationships',
                                                          on_delete=models.CASCADE, primary_key=137)


class LackOfPublicSupport(models.Model):
    LackOfPublicSupport = models.OneToOneField(fieldSet, verbose_name='LackOfPublicSupport', on_delete=models.CASCADE,
                                               primary_key=138)


class Brotherhood(models.Model):
    Brotherhood = models.OneToOneField(fieldSet, verbose_name='Brotherhood', on_delete=models.CASCADE, primary_key=139)


class DemandingDecreasing(models.Model):
    DemandingDecreasing = models.OneToOneField(fieldSet, verbose_name='DemandingDecreasing', on_delete=models.CASCADE,
                                               primary_key=211)


class StructureChanges(models.Model):
    StructureChanges = models.OneToOneField(fieldSet, verbose_name='StructureChanges', on_delete=models.CASCADE,
                                            primary_key=212)


class IncompatibleArbitrationSystem(models.Model):
    IncompatibleArbitrationSystem = models.OneToOneField(fieldSet, verbose_name='IncompatibleArbitrationSystem',
                                                         on_delete=models.CASCADE, primary_key=221)


class ComplexPlanningApprovalAndPermitProcedures(models.Model):
    ComplexPlanningApprovalAndPermitProcedures = models.OneToOneField(fieldSet,
                                                                      verbose_name='ComplexPlanningApprovalAndPermitProcedures',
                                                                      on_delete=models.CASCADE, primary_key=222)


class ImportExportRestrictions(models.Model):
    ImportExportRestrictions = models.OneToOneField(fieldSet, verbose_name='ImportExportRestrictions',
                                                    on_delete=models.CASCADE, primary_key=223)


class ConstraintsOnEmploymentAvailabilities(models.Model):
    ConstraintsOnEmploymentAvailabilities = models.OneToOneField(fieldSet,
                                                                 verbose_name='ConstraintsOnEmploymentAvailabilities',
                                                                 on_delete=models.CASCADE, primary_key=224)


class ConstraintsOnMaterialsAvailabilities(models.Model):
    ConstraintsOnMaterialsAvailabilities = models.OneToOneField(fieldSet,
                                                                verbose_name='ConstraintsOnMaterialsAvailabilities',
                                                                on_delete=models.CASCADE, primary_key=225)


class MonetaryRestrictions(models.Model):
    MonetaryRestrictions = models.OneToOneField(fieldSet, verbose_name='MonetaryRestrictions', on_delete=models.CASCADE,
                                                primary_key=226)


class InconsistenciesInDesignAndConstruction(models.Model):
    InconsistenciesInDesignAndConstruction = models.OneToOneField(fieldSet,
                                                                  verbose_name='InconsistenciesInDesignAndConstruction',
                                                                  on_delete=models.CASCADE, primary_key=231)


class DifferencesInSafetyAndHealthCare(models.Model):
    DifferencesInSafetyAndHealthCare = models.OneToOneField(fieldSet, verbose_name='DifferencesInSafetyAndHealthCare',
                                                            on_delete=models.CASCADE, primary_key=232)


class PollutionsAndNuisances(models.Model):
    PollutionsAndNuisances = models.OneToOneField(fieldSet, verbose_name='PollutionsAndNuisances',
                                                  on_delete=models.CASCADE, primary_key=233)


class NonstandardContractForm(models.Model):
    NonstandardContractForm = models.OneToOneField(fieldSet, verbose_name='NonstandardContractForm',
                                                   on_delete=models.CASCADE, primary_key=241)


class DifferencesInLegalRelationshipsBetweenPartners(models.Model):
    DifferencesInLegalRelationshipsBetweenPartners = models.OneToOneField(fieldSet,
                                                                          verbose_name='DifferencesInLegalRelationshipsBetweenPartners',
                                                                          on_delete=models.CASCADE, primary_key=242)


class UnfamiliarWithContractConditionsForClaimsAndLitigations(models.Model):
    UnfamiliarWithContractConditionsForClaimsAndLitigations = models.OneToOneField(fieldSet,
                                                                                   verbose_name='UnfamiliarWithContractConditionsForClaimsAndLitigations',
                                                                                   on_delete=models.CASCADE,
                                                                                   primary_key=243)


class DifferencesInDefectiveLiabilities(models.Model):
    DifferencesInDefectiveLiabilities = models.OneToOneField(fieldSet, verbose_name='DifferencesInDefectiveLiabilities',
                                                             on_delete=models.CASCADE, primary_key=244)


class SpecialLocalRequirements(models.Model):
    SpecialLocalRequirements = models.OneToOneField(fieldSet, verbose_name='SpecialLocalRequirements',
                                                    on_delete=models.CASCADE, primary_key=245)


class UnclearRequirements(models.Model):
    UnclearRequirements = models.OneToOneField(fieldSet, verbose_name='UnclearRequirements', on_delete=models.CASCADE,
                                               primary_key=311)


class FundingShortage(models.Model):
    FundingShortage = models.OneToOneField(fieldSet, verbose_name='FundingShortage', on_delete=models.CASCADE,
                                           primary_key=312)


class DisadvantagedContracts(models.Model):
    DisadvantagedContracts = models.OneToOneField(fieldSet, verbose_name='DisadvantagedContracts',
                                                  on_delete=models.CASCADE, primary_key=313)


class UnclearDetailDesignOrSpecifications(models.Model):
    UnclearDetailDesignOrSpecifications = models.OneToOneField(fieldSet,
                                                               verbose_name='UnclearDetailDesignOrSpecifications',
                                                               on_delete=models.CASCADE, primary_key=321)


class UnfamiliarWithLocalStandardsAndCodes(models.Model):
    UnfamiliarWithLocalStandardsAndCodes = models.OneToOneField(fieldSet,
                                                                verbose_name='UnfamiliarWithLocalStandardsAndCodes',
                                                                on_delete=models.CASCADE, primary_key=322)


class LackOfInteractionWithConstructionMethod(models.Model):
    LackOfInteractionWithConstructionMethod = models.OneToOneField(fieldSet,
                                                                   verbose_name='LackOfInteractionWithConstructionMethod',
                                                                   on_delete=models.CASCADE, primary_key=323)


class DirectLabourDisturbance(models.Model):
    DirectLabourDisturbance = models.OneToOneField(fieldSet, verbose_name='DirectLabourDisturbance',
                                                   on_delete=models.CASCADE, primary_key=331)


class UnfavourableSubContractors(models.Model):
    UnfavourableSubContractors = models.OneToOneField(fieldSet, verbose_name='UnfavourableSubContractors',
                                                      on_delete=models.CASCADE, primary_key=332)


class HealthAndSafetyIssues(models.Model):
    HealthAndSafetyIssues = models.OneToOneField(fieldSet, verbose_name='HealthAndSafetyIssues',
                                                 on_delete=models.CASCADE, primary_key=333)


class HighTurnoverRate(models.Model):
    HighTurnoverRate = models.OneToOneField(fieldSet, verbose_name='HighTurnoverRate', on_delete=models.CASCADE,
                                            primary_key=334)


class UnfavourableSubSuppliers(models.Model):
    UnfavourableSubSuppliers = models.OneToOneField(fieldSet, verbose_name='UnfavourableSubSuppliers',
                                                    on_delete=models.CASCADE, primary_key=341)


class DefaultSupplyOfMaterials(models.Model):
    DefaultSupplyOfMaterials = models.OneToOneField(fieldSet, verbose_name='DefaultSupplyOfMaterials',
                                                    on_delete=models.CASCADE, primary_key=342)


class DefaultSupplyOfEquipment(models.Model):
    DefaultSupplyOfEquipment = models.OneToOneField(fieldSet, verbose_name='DefaultSupplyOfEquipment',
                                                    on_delete=models.CASCADE, primary_key=343)


class DefaultSupplyOfPlants(models.Model):
    DefaultSupplyOfPlants = models.OneToOneField(fieldSet, verbose_name='DefaultSupplyOfPlants',
                                                 on_delete=models.CASCADE, primary_key=344)


class NaturalForce(models.Model):
    NaturalForce = models.OneToOneField(fieldSet, verbose_name='NaturalForce', on_delete=models.CASCADE,
                                        primary_key=411)


class PoorDesign(models.Model):
    PoorDesign = models.OneToOneField(fieldSet, verbose_name='PoorDesign', on_delete=models.CASCADE, primary_key=412)


class LackOfProperConstructionTechniques(models.Model):
    LackOfProperConstructionTechniques = models.OneToOneField(fieldSet,
                                                              verbose_name='LackOfProperConstructionTechniques',
                                                              on_delete=models.CASCADE, primary_key=413)


class DamagesByHumanErrors(models.Model):
    DamagesByHumanErrors = models.OneToOneField(fieldSet, verbose_name='DamagesByHumanErrors', on_delete=models.CASCADE,
                                                primary_key=414)


class DefectiveMaterials(models.Model):
    DefectiveMaterials = models.OneToOneField(fieldSet, verbose_name='DefectiveMaterials', on_delete=models.CASCADE,
                                              primary_key=415)


class DifficultyInQualityControl(models.Model):
    DifficultyInQualityControl = models.OneToOneField(fieldSet, verbose_name='DifficultyInQualityControl',
                                                      on_delete=models.CASCADE, primary_key=416)


class IncompleteDesign(models.Model):
    IncompleteDesign = models.OneToOneField(fieldSet, verbose_name='IncompleteDesign', on_delete=models.CASCADE,
                                            primary_key=421)


class LateConstructionPossession(models.Model):
    LateConstructionPossession = models.OneToOneField(fieldSet, verbose_name='LateConstructionPossession',
                                                      on_delete=models.CASCADE, primary_key=422)


class BadWeather(models.Model):
    BadWeather = models.OneToOneField(fieldSet, verbose_name='BadWeather', on_delete=models.CASCADE, primary_key=423)


class UnforeseenGroundConditions(models.Model):
    UnforeseenGroundConditions = models.OneToOneField(fieldSet, verbose_name='UnforeseenGroundConditions',
                                                      on_delete=models.CASCADE, primary_key=424)


class DisturbancesInLabour(models.Model):
    DisturbancesInLabour = models.OneToOneField(fieldSet, verbose_name='DisturbancesInLabour', on_delete=models.CASCADE,
                                                primary_key=425)


class DisturbancesInMaterialSupplying(models.Model):
    DisturbancesInMaterialSupplying = models.OneToOneField(fieldSet, verbose_name='DisturbancesInMaterialSupplying',
                                                           on_delete=models.CASCADE, primary_key=426)


class InefficientCommunicationsCordinations(models.Model):
    InefficientCommunicationsCordinations = models.OneToOneField(fieldSet,
                                                                 verbose_name='InefficientCommunicationsCordinations',
                                                                 on_delete=models.CASCADE, primary_key=427)


class UnclearBoundariesOfWorks(models.Model):
    UnclearBoundariesOfWorks = models.OneToOneField(fieldSet, verbose_name='UnclearBoundariesOfWorks',
                                                    on_delete=models.CASCADE, primary_key=431)


class InaccurateEstimation(models.Model):
    InaccurateEstimation = models.OneToOneField(fieldSet, verbose_name='InaccurateEstimation', on_delete=models.CASCADE,
                                                primary_key=432)


class InadequateInsurance(models.Model):
    InadequateInsurance = models.OneToOneField(fieldSet, verbose_name='InadequateInsurance', on_delete=models.CASCADE,
                                               primary_key=433)


class LabourMaterialsPriceFluctuations(models.Model):
    LabourMaterialsPriceFluctuations = models.OneToOneField(fieldSet, verbose_name='LabourMaterialsPriceFluctuations',
                                                            on_delete=models.CASCADE, primary_key=434)


class riskCatalogue(models.Model):
    # risk catalogue and risks' id
    War = models.FloatField(editable=True, verbose_name='War')
    Revolution = models.FloatField(editable=True, verbose_name='Revolution')
    CivilDisorders = models.FloatField(editable=True, verbose_name='Civil Disorders')
    InconsistencyOfGovernmentalPolicies = models.FloatField(editable=True,
                                                            verbose_name='Inconsistency Of Governmental Policies')

    PoliticalSituation = [War, Revolution, CivilDisorders, InconsistencyOfGovernmentalPolicies]

    GNPDecreases = models.FloatField(editable=True, verbose_name='GNP Decreases')
    IncompatibleGNPPerCapita = models.FloatField(editable=True, verbose_name='Incompatible GNP Per Capita')
    InterestRateFluctuation = models.FloatField(editable=True, verbose_name='Interest Rate Fluctuation')
    InflationRateIncreasing = models.FloatField(editable=True, verbose_name='Inflation Rate Increasing')
    CurrencyExchangeRateFluctuation = models.FloatField(editable=True,
                                                        verbose_name='Currency Exchange Rate Fluctuation')
    TaxRateIncreasing = models.FloatField(editable=True, verbose_name='Tax Rate Increasing')

    EconomicalAndFinancialSituation = [GNPDecreases, IncompatibleGNPPerCapita, InterestRateFluctuation,
                                       InflationRateIncreasing, CurrencyExchangeRateFluctuation, TaxRateIncreasing]

    LanguageBarrier = models.FloatField(editable=True, verbose_name='Language Barrier')
    ReligiousInconsistency = models.FloatField(editable=True, verbose_name='Religious Inconsistency')
    CultureTraditionDifferences = models.FloatField(editable=True, verbose_name='Culture Tradition Differences')
    InsecurityAndCrime = models.FloatField(editable=True, verbose_name='Insecurity And Crime')
    Pestilence = models.FloatField(editable=True, verbose_name='Pestilence')
    BribeAndCorruption = models.FloatField(editable=True, verbose_name='Bribe And Corruption')
    PopularInInformalRelationships = models.FloatField(editable=True, verbose_name='Popular In Informal Relationships')
    LackOfPublicSupport = models.FloatField(editable=True, verbose_name='Lack Of Public Support')
    Brotherhood = models.FloatField(editable=True, verbose_name='Brotherhood')

    SocialEnvironment = [LanguageBarrier, ReligiousInconsistency, CultureTraditionDifferences, InsecurityAndCrime,
                         Pestilence, BribeAndCorruption, PopularInInformalRelationships,
                         LackOfPublicSupport, Brotherhood]

    Country = [PoliticalSituation, EconomicalAndFinancialSituation, SocialEnvironment]

    DemandingDecreasing = models.FloatField(editable=True, verbose_name='Demanding Decreasing')
    StructureChanges = models.FloatField(editable=True, verbose_name='Structure Changes')

    IncompatibleArbitrationSystem = models.FloatField(editable=True, verbose_name='Incompatible Arbitration System')
    ComplexPlanningApprovalAndPermitProcedures = models.FloatField(editable=True,
                                                                   verbose_name='Complex Planning Approval And Permit Procedures')
    ImportExportRestrictions = models.FloatField(editable=True, verbose_name='Import Export Restrictions')
    ConstraintsOnEmploymentAvailabilities = models.FloatField(editable=True,
                                                              verbose_name='Constraints On Employment Availabilities')
    ConstraintsOnMaterialsAvailabilities = models.FloatField(editable=True,
                                                             verbose_name='Constraints On Materials Availabilities')
    MonetaryRestrictions = models.FloatField(editable=True, verbose_name='Monetary Restrictions')

    InconsistenciesInDesignAndConstruction = models.FloatField(editable=True,
                                                               verbose_name='Inconsistencies In Design And Construction')
    DifferencesInSafetyAndHealthCare = models.FloatField(editable=True,
                                                         verbose_name='Differences In Safety And Health Care')
    PollutionsAndNuisances = models.FloatField(editable=True, verbose_name='Pollutions And Nuisances')

    NonstandardContractForm = models.FloatField(editable=True, verbose_name='Nonstandard ContractForm')
    DifferencesInLegalRelationshipsBetweenPartners = models.FloatField(editable=True,
                                                                       verbose_name='Differences In Legal Relationships Between Partners')
    UnfamiliarWithContractConditionsForClaimsAndLitigations = models.FloatField(editable=True,
                                                                                verbose_name='Unfamiliar With Contract Conditions For Claims And Litigations')
    DifferencesInDefectiveLiabilities = models.FloatField(editable=True,
                                                          verbose_name='Differences In Defective Liabilities')
    SpecialLocalRequirements = models.FloatField(editable=True, verbose_name='Special Local Requirements')

    UnclearRequirements = models.FloatField(editable=True, verbose_name='Unclear Requirements')
    FundingShortage = models.FloatField(editable=True, verbose_name='Funding Shortage')
    DisadvantagedContracts = models.FloatField(editable=True, verbose_name='Disadvantaged Contracts')

    UnclearDetailDesignOrSpecifications = models.FloatField(editable=True,
                                                            verbose_name='Unclear Detail Design Or Specifications')
    UnfamiliarWithLocalStandardsAndCodes = models.FloatField(editable=True,
                                                             verbose_name='Unfamiliar With Local Standards And Codes')
    LackOfInteractionWithConstructionMethod = models.FloatField(editable=True,
                                                                verbose_name='Lack Of Interaction With Construction Method')

    DirectLabourDisturbance = models.FloatField(editable=True, verbose_name='Direct Labour Disturbance')
    UnfavourableSubContractors = models.FloatField(editable=True, verbose_name='Unfavourable Sub Contractors')
    HealthAndSafetyIssues = models.FloatField(editable=True, verbose_name='Health And Safety Issues')
    HighTurnoverRate = models.FloatField(editable=True, verbose_name='High Turnover Rate')

    UnfavourableSubSuppliers = models.FloatField(editable=True, verbose_name='Unfavourable Sub Suppliers')
    DefaultSupplyOfMaterials = models.FloatField(editable=True, verbose_name='Default Supply Of Materials')
    DefaultSupplyOfEquipment = models.FloatField(editable=True, verbose_name='Default Supply Of Equipment')
    DefaultSupplyOfPlants = models.FloatField(editable=True, verbose_name='Default Supply Of Plants')

    NaturalForce = models.FloatField(editable=True, verbose_name='Natural Force')
    PoorDesign = models.FloatField(editable=True, verbose_name='Poor Design')
    LackOfProperConstructionTechniques = models.FloatField(editable=True,
                                                           verbose_name='Lack Of Proper Construction Techniques')
    DamagesByHumanErrors = models.FloatField(editable=True, verbose_name='Damages By Human Errors')
    DefectiveMaterials = models.FloatField(editable=True, verbose_name='Defective Materials')
    DifficultyInQualityControl = models.FloatField(editable=True, verbose_name='Difficulty In Quality Control')

    IncompleteDesign = models.FloatField(editable=True, verbose_name='Incomplete Design')
    LateConstructionPossession = models.FloatField(editable=True, verbose_name='Late Construction Possession')
    BadWeather = models.FloatField(editable=True, verbose_name='Bad Weather')
    UnforeseenGroundConditions = models.FloatField(editable=True, verbose_name='Unforeseen Ground Conditions')
    DisturbancesInLabour = models.FloatField(editable=True, verbose_name='Disturbances In Labour')
    DisturbancesInMaterialSupplying = models.FloatField(editable=True,
                                                        verbose_name='Disturbances In Material Supplying')
    InefficientCommunicationsCordinations = models.FloatField(editable=True,
                                                              verbose_name='Inefficient Communications Cordinations')

    UnclearBoundariesOfWorks = models.FloatField(editable=True, verbose_name='Unclear Boundaries Of Works')
    InaccurateEstimation = models.FloatField(editable=True, verbose_name='Inaccurate Estimation')
    InadequateInsurance = models.FloatField(editable=True, verbose_name='Inadequate Insurance')
    LabourMaterialsPriceFluctuations = models.FloatField(editable=True,
                                                         verbose_name='Labour Materials Price Fluctuations')


class Project(models.Model):
    # project info
    projectName = models.CharField(max_length=120, verbose_name='Project Name')
    summary = models.TextField(verbose_name='Summary')
    crtDate = models.DateTimeField('Creating Date', auto_now_add=True)

    # project features
    prjType = models.CharField(max_length=50, choices=types, verbose_name='Project Type')
    prjCountry = models.CharField(max_length=100, choices=countries, verbose_name='Country')
    dlvSystem = models.CharField(max_length=100, choices=deliverySys, verbose_name='Delivery System')
    cost = models.IntegerField(verbose_name='Project Value($)')
    duration = models.IntegerField(verbose_name='Duration(month)')
    area = models.IntegerField(verbose_name='Total Construction Area')
    payment = models.CharField(max_length=50, choices=payType, verbose_name='Payment Type')

    complexity = models.CharField(max_length=20, choices=lessMuch, verbose_name='Complexity of Design', default=None)
    compLevel = models.CharField(max_length=20, choices=lessMuch, verbose_name='Completion Level of Design',
                                 default=None)
    consLevel = models.CharField(max_length=20, choices=lessMuch, verbose_name='Constructability Level', default=None)
    qltyDsgn = models.CharField(max_length=20, choices=lessMuch, verbose_name='Quality of Design', default=None)
    complCons = models.CharField(max_length=20, choices=lessMuch, verbose_name='Complexity of Construction Method',
                                 default=None)
    AccesSite = models.CharField(max_length=20, choices=lessMuch, verbose_name='Accessibility of Site', default=None)
    geotech = models.CharField(max_length=20, choices=lessMuch,
                               verbose_name='Comprehensiveness of Geotechnical Investigation', default=None)
    climate = models.CharField(max_length=20, choices=lessMuch, verbose_name='Climate Conditions', default=None)
    strQuality = models.CharField(max_length=20, choices=lessMuch,
                                  verbose_name='Strict Quality Management Requirements', default=None)
    strEnv = models.CharField(max_length=20, choices=lessMuch,
                              verbose_name='Strict Environmental Management Requirements', default=None)
    strSafe = models.CharField(max_length=20, choices=lessMuch, verbose_name='Strict Safety Requirements', default=None)
    strPrjct = models.CharField(max_length=20, choices=lessMuch, verbose_name='Strict Project Management Requirements',
                                default=None)
    vaguenes = models.CharField(max_length=20, choices=lessMuch, verbose_name='Vagueness in Contract Clause',
                                default=None)
    avConsErr = models.CharField(max_length=20, choices=lessMuch, verbose_name='Clarity of Contract Errors',
                                 default=None)

    prjRisks = models.OneToOneField(riskCatalogue, on_delete=models.CASCADE)

    def __str__(self):
        return self.projectName

    def get_absolute_url(self):
        return reverse('projects:view', kwargs={'id': self.id})









    War = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='War',primary_key=111)
    Revolution = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Revolution',primary_key=112)
    CivilDisorders = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Civil Disorders',primary_key=113)
    InconsistencyOfGovernmentalPolicies = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Inconsistency Of Governmental Policies',primary_key=114)

    PoliticalSituation = [War, Revolution, CivilDisorders, InconsistencyOfGovernmentalPolicies]

    GNPDecreases = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='GNP Decreases',primary_key=121)
    IncompatibleGNPPerCapita = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Incompatible GNP Per Capita',primary_key=122)
    InterestRateFluctuation = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Interest Rate Fluctuation',primary_key=123)
    InflationRateIncreasing = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Inflation Rate Increasing',primary_key=124)
    CurrencyExchangeRateFluctuation = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,
                                                        verbose_name='Currency Exchange Rate Fluctuation',primary_key=125)
    TaxRateIncreasing = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Tax Rate Increasing',primary_key=126)

    EconomicalAndFinancialSituation = [GNPDecreases, IncompatibleGNPPerCapita, InterestRateFluctuation,
                                       InflationRateIncreasing, CurrencyExchangeRateFluctuation, TaxRateIncreasing]

    LanguageBarrier = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Language Barrier',primary_key=131)
    ReligiousInconsistency = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Religious Inconsistency',primary_key=132)
    CultureTraditionDifferences = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Culture Tradition Differences',primary_key=133)
    InsecurityAndCrime = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Insecurity And Crime',primary_key=134)
    Pestilence = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Pestilence',primary_key=135)
    BribeAndCorruption = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Bribe And Corruption',primary_key=136)
    PopularInInformalRelationships = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Popular In Informal Relationships',primary_key=137)
    LackOfPublicSupport = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Lack Of Public Support',primary_key=138)
    Brotherhood = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Brotherhood',primary_key=139)

    SocialEnvironment = [LanguageBarrier, ReligiousInconsistency, CultureTraditionDifferences, InsecurityAndCrime,
                         Pestilence, BribeAndCorruption, PopularInInformalRelationships,
                         LackOfPublicSupport, Brotherhood]

    Country = [PoliticalSituation, EconomicalAndFinancialSituation, SocialEnvironment]

    DemandingDecreasing = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Demanding Decreasing',primary_key=211)
    StructureChanges = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Structure Changes',primary_key=212)

    IncompatibleArbitrationSystem = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Incompatible Arbitration System',primary_key=221)
    ComplexPlanningApprovalAndPermitProcedures = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Complex Planning Approval And Permit Procedures',primary_key=222)
    ImportExportRestrictions = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Import Export Restrictions',primary_key=223)
    ConstraintsOnEmploymentAvailabilities = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Constraints On Employment Availabilities',primary_key=224)
    ConstraintsOnMaterialsAvailabilities = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Constraints On Materials Availabilities',primary_key=225)
    MonetaryRestrictions = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Monetary Restrictions',primary_key=226)

    InconsistenciesInDesignAndConstruction = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Inconsistencies In Design And Construction',primary_key=231)
    DifferencesInSafetyAndHealthCare = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Differences In Safety And Health Care',primary_key=232)
    PollutionsAndNuisances = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Pollutions And Nuisances',primary_key=233)

    NonstandardContractForm = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Nonstandard ContractForm',primary_key=241)
    DifferencesInLegalRelationshipsBetweenPartners = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Differences In Legal Relationships Between Partners',primary_key=242)
    UnfamiliarWithContractConditionsForClaimsAndLitigations = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Unfamiliar With Contract Conditions For Claims And Litigations',primary_key=243)
    DifferencesInDefectiveLiabilities = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Differences In Defective Liabilities',primary_key=244)
    SpecialLocalRequirements = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Special Local Requirements',primary_key=245)



    UnclearRequirements = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Unclear Requirements',primary_key=311)
    FundingShortage = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Funding Shortage',primary_key=312)
    DisadvantagedContracts = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE, verbose_name='Disadvantaged Contracts',primary_key=313)

    UnclearDetailDesignOrSpecifications = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Unclear Detail Design Or Specifications',primary_key=321)
    UnfamiliarWithLocalStandardsAndCodes = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Unfamiliar With Local Standards And Codes',primary_key=322)
    LackOfInteractionWithConstructionMethod = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Lack Of Interaction With Construction Method',primary_key=323)

    DirectLabourDisturbance = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Direct Labour Disturbance',primary_key=331)
    UnfavourableSubContractors = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Unfavourable Sub Contractors',primary_key=332)
    HealthAndSafetyIssues = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Health And Safety Issues',primary_key=333)
    HighTurnoverRate = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='High Turnover Rate',primary_key=334)

    UnfavourableSubSuppliers = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Unfavourable Sub Suppliers',primary_key=341)
    DefaultSupplyOfMaterials = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Default Supply Of Materials',primary_key=342)
    DefaultSupplyOfEquipment = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Default Supply Of Equipment',primary_key=343)
    DefaultSupplyOfPlants = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Default Supply Of Plants',primary_key=344)



    NaturalForce = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Natural Force',primary_key=411)
    PoorDesign = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Poor Design',primary_key=412)
    LackOfProperConstructionTechniques = models.OneToOneField(fieldSet,on_delete=models.CASCADE,editable=True,verbose_name='Lack Of Proper Construction Techniques',primary_key=413)
    DamagesByHumanErrors = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Damages By Human Errors',primary_key=414)
    DefectiveMaterials = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Defective Materials',primary_key=415)
    DifficultyInQualityControl = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Difficulty In Quality Control',primary_key=416)

    IncompleteDesign = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Incomplete Design',primary_key=421)
    LateConstructionPossession = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Late Construction Possession',primary_key=422)
    BadWeather = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Bad Weather',primary_key=423)
    UnforeseenGroundConditions = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Unforeseen Ground Conditions',primary_key=424)
    DisturbancesInLabour = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Disturbances In Labour',primary_key=425)
    DisturbancesInMaterialSupplying = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Disturbances In Material Supplying',primary_key=426)
    InefficientCommunicationsCordinations = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Inefficient Communications Cordinations',primary_key=427)

    UnclearBoundariesOfWorks = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Unclear Boundaries Of Works',primary_key=431)
    InaccurateEstimation = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Inaccurate Estimation',primary_key=432)
    InadequateInsurance = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Inadequate Insurance',primary_key=433)
    LabourMaterialsPriceFluctuations = models.OneToOneField(fieldSet,editable=True,on_delete=models.CASCADE,verbose_name='Labour Materials Price Fluctuations',primary_key=434)

class riskForm(forms.ModelForm):
    class Meta:
        model = riskCatalogue
        fields = ['War','Revolution','CivilDisorders','InconsistencyOfGovernmentalPolicies','GNPDecreases','IncompatibleGNPPerCapita','InterestRateFluctuation',
                  'InflationRateIncreasing','CurrencyExchangeRateFluctuation','TaxRateIncreasing','LanguageBarrier','ReligiousInconsistency','CultureTraditionDifferences',
                  'InsecurityAndCrime','Pestilence','BribeAndCorruption','PopularInInformalRelationships','LackOfPublicSupport','Brotherhood',
                  'DemandingDecreasing','StructureChanges','IncompatibleArbitrationSystem','ComplexPlanningApprovalAndPermitProcedures','ImportExportRestrictions',
                  'ConstraintsOnEmploymentAvailabilities','ConstraintsOnMaterialsAvailabilities','MonetaryRestrictions','InconsistenciesInDesignAndConstruction',
                  'DifferencesInSafetyAndHealthCare','PollutionsAndNuisances','NonstandardContractForm','DifferencesInLegalRelationshipsBetweenPartners',
                  'UnfamiliarWithContractConditionsForClaimsAndLitigations','DifferencesInDefectiveLiabilities','SpecialLocalRequirements',
                  'UnclearRequirements','FundingShortage','DisadvantagedContracts','UnclearDetailDesignOrSpecifications','UnfamiliarWithLocalStandardsAndCodes',
                  'LackOfInteractionWithConstructionMethod','DirectLabourDisturbance','UnfavourableSubContractors','HealthAndSafetyIssues','HighTurnoverRate',
                  'UnfavourableSubSuppliers','DefaultSupplyOfMaterials','DefaultSupplyOfEquipment','DefaultSupplyOfPlants','NaturalForce','PoorDesign',
                  'LackOfProperConstructionTechniques','DamagesByHumanErrors','DefectiveMaterials','DifficultyInQualityControl','IncompleteDesign',
                  'LateConstructionPossession','BadWeather','UnforeseenGroundConditions','DisturbancesInLabour','DisturbancesInMaterialSupplying',
                  'InefficientCommunicationsCordinations','UnclearBoundariesOfWorks','InaccurateEstimation','InadequateInsurance','LabourMaterialsPriceFluctuations',
                  ]


def projectCreate(request):
    form = Form(request.POST or None)
    if form.is_valid():
        project = form.save()
        return HttpResponseRedirect(project.get_absolute_url())

    context = {
       'form':form,
    }
    return render(request, 'projects/create.html',context)


def calculateRisks(request,id):
    obj = get_object_or_404(Project, id=id)
    maxTable = similarityAlgorithm(request, obj.id)

    dummyProject = Project.objects.order_by('id')[maxTable[0]]
    dummyPrjRisks = dummyProject.prjRisks.risk.all()
    for obj in dummyPrjRisks:
        obj.probability = 1
    i = 1
    while i < 5:
        tmpProject = Project.objects.order_by('id')[maxTable[i]]
        tmpPrjRisks = tmpProject.prjRisks.risk.all()
        for obj in tmpPrjRisks:
            for obj2 in dummyPrjRisks:
                if obj.riskId != obj2.riskId:
                    dummyPrjRisks.create(name = obj.name,riskId=obj.riskId,probability=1)
                else:
                    obj2.probability = obj2.probability + 1
        i = i+1

    context = {
        'tmpRisks': dummyPrjRisks
    }
    return render(request, 'projects/riskCreate.html', context)


for obj2 in dummyPrjRisks:
    if obj.riskId != obj2.riskId:
        obj.probability = 1
        prj.prjRisks.risk.add(obj)
        # dummyPrjRisks.create(name = obj.name,riskId=obj.riskId,probability=1)
    else:
        obj2.probability = obj2.probability + 1


        class profileForm(forms.ModelForm):
            pos = (
            ('1', 'Planning Engineer'), ('2', 'Manager'), ('3', 'General Manager'), ('4', 'Tendering Specialist'),
            ('5', 'Project Coordinator'), ('6', 'General Coordinator'),
            ('7', 'Busines Development Specialist'), ('8', 'Bidding Engineer'), ('7', 'Academics'),)

            username = forms.CharField(max_length=100, label='User Name')
            name = forms.CharField(max_length=100, label='First Name')
            surname = forms.CharField(max_length=100, label='Last Name')
            eMail = forms.EmailField(max_length=100, label='E-mail')
            company = forms.CharField(max_length=100, label='Company')
            # position = forms.Select(choices = pos)
            password1 = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)
            password2 = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)

            class Meta:
                model = User
                fields = [
                    'username',
                    'password1',
                    'password2',
                    'name',
                    'surname',
                    'email',
                    'company',
                ]

            def clean_password2(self):
                password1 = self.cleaned_data.get("password1")
                password2 = self.cleaned_data.get("password2")
                if password1 and password2 and password1 != password2:
                    raise forms.ValidationError("The passwords don't match!")
                return password2

            newRisk = riskInf()
            newRisk.name = obj.inf.name
            newRisk.riskId = obj.inf.riskId
            rsks.inf = newRisk
            rsks.probability = rsks.probability + 1

            rsk = risks()
            rsks = rsk

            count = 0
            i = 0
            while i < 5:
                tmpProject = Project.prjRisks.objects.order_by('id')[maxTable[i]]
                tmpRisks = tmpProject.objects.all()
                for obj in tmpRisks:
                    k = 1
                    search = 0
                    while k <= count and search != 0:
                        rid = rsks.objects.order_by('risk__inf__riskId')[k]
                        if obj.inf.riskId == rid.riskId:
                            search == 1
                        k = k + 1
                    if k > count:
                        newRisk = riskInf()
                        newRisk.name = obj.inf.name
                        newRisk.riskId = obj.inf.riskId
                        rsk.inf = newRisk
                        rsk.probabilty = rsk.probabilty + 1
                    else:
                        rid = rsks.objects.order_by('risk__inf__riskId')[k]
                        rid.probability = rid.probability + 1


