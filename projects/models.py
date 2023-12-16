from django.db import models
from django.utils.translation import ugettext as _
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


lessMuch = (
('1', 'Definitely Low'), ('2', 'Very Low'), ('3', 'Low'), ('4', 'Medium'), ('5', 'High'), ('6', 'Very High'),
('7', 'Definitely High'),)

EmergyTime = (
('1', 'Day'), ('2', 'Evening'), ('3', 'Night'),)

YesNo = (
('1', 'Yes'), ('2', 'No'),)



location = (
('1', 'Marmara Bölgesi'), ('2', 'Ege Bölgesi'), ('3', 'Karadeniz Bölgesi'), ('4', 'Akdeniz Bölgesi'), ('5', 'İç Anadolu Bölgesi'),
('6', 'Doğu Anadolu Bölgesi'),('7', 'Güneydoğu Anadolu Bölgesi'),)



class ResponsePlan(models.Model):
    reaction = models.TextField(verbose_name='Reaction')
    time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Time')
    date = models.DateField(verbose_name='Date')
    effect = models.FloatField(verbose_name='Effectiveness of Reaction')
    responsible = models.CharField(max_length=120, verbose_name='Responsible')

class ResponseCat(models.Model):
    catId = models.IntegerField(unique=True, primary_key=True, verbose_name='Catalogue  Id')
    response = models.ManyToManyField(ResponsePlan)




class Deprem(models.Model):

    user = models.ForeignKey('auth.User', verbose_name='creator', related_name='deprems', on_delete=models.SET_NULL, null=True)

    # info
    projectName = models.CharField(max_length=120, verbose_name='Disaster Name')
    summary = models.TextField(verbose_name='Summary')
    crtDate = models.DateTimeField('Creating Date', auto_now_add=True)
    #depremPrjId = models.IntegerField(unique=True, primary_key=True, verbose_name='Project  Id')

    # Factors
    MagnitudeEarthquake = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(9.9)],verbose_name='Magnitude of The Earthquake')
    EmergencyTime = models.CharField(max_length=20, choices=EmergyTime, verbose_name='Emergency Time', default=None)
    FocalDepth = models.FloatField(verbose_name='Focal Depth (km)')
    EmergencyLocation = models.CharField(max_length=20, choices=location, verbose_name='Emergency Location')
    BuildingCollapseRate = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(100.0)],verbose_name='Building Collapse Rate (%)')
    PotentialSecondaryDisasters = models.CharField(max_length=20, choices=YesNo, verbose_name='Potential of Secondary Disasters', default=None)
    PopulationDensity = models.FloatField(verbose_name='Population Density (n/km2)')

    WeatherCondition = models.CharField(max_length=20, choices=lessMuch, verbose_name='Weather Condition', default=None)
    BuildingDensityAccessibilityDisasterArea = models.CharField(max_length=20, choices=lessMuch, verbose_name='Building Density and Accessibility of the Disaster Area', default=None)
    PotentialHazardousMaterial = models.CharField(max_length=20, choices=lessMuch, verbose_name='Potential of Hazardous Material Arising from Debris', default=None)
    EmergencyResourceCompleteness = models.CharField(max_length=20, choices=lessMuch, verbose_name='Emergency Resource Completeness and Readiness Level', default=None)
    EmergencyResourceDuration = models.CharField(max_length=20, choices=lessMuch, verbose_name='Emergency Resource Arrival Duration', default=None)
    InitialResponseLevel = models.CharField(max_length=20, choices=lessMuch, verbose_name='Initial Response Level of Local Units', default=None)
    ConditionRoadTransportation = models.CharField(max_length=20, choices=lessMuch, verbose_name='Condition of Road Transportation Lines', default=None)
    ConditionAirTransportation = models.CharField(max_length=20, choices=lessMuch, verbose_name='Condition of Air Transportation Lines', default=None)
    ConditionRailwayTransportation = models.CharField(max_length=20, choices=lessMuch, verbose_name='Condition of Railway Transportation Lines', default=None)
    ConditionMaritimeTransportation = models.CharField(max_length=20, choices=lessMuch, verbose_name='Condition of Maritime Transportation Lines', default=None)
    ConditionHealthInfrastructure = models.CharField(max_length=20, choices=lessMuch, verbose_name='Condition of Health Infrastructure ', default=None)
    ConditionWaterSupplySewage = models.CharField(max_length=20, choices=lessMuch, verbose_name='Condition of Water Supply and Sewage Systems', default=None)
    ConditionCommunicationInfrastructure = models.CharField(max_length=20, choices=lessMuch, verbose_name='Condition of Communication Infrastructure', default=None)
    ConditionNaturalgas = models.CharField(max_length=20, choices=lessMuch, verbose_name='Condition of the Natural Gas', default=None)
    ConditionPowergrid = models.CharField(max_length=20, choices=lessMuch, verbose_name='Condition of the Power Grid', default=None)
    SufficiencyTemporaryResidential = models.CharField(max_length=20, choices=lessMuch, verbose_name='Sufficiency of Temporary Residential Area', default=None)
    CapacityWasteLandfills = models.CharField(max_length=20, choices=lessMuch, verbose_name='Capacity and Distance of Waste Landfills', default=None)

    responses = models.ForeignKey(ResponseCat,on_delete=models.CASCADE)
    terminate = models.BooleanField(verbose_name='terminate', default=False)

    def __str__(self):
        return self.projectName

    def get_absolute_urlDpr(self):
        return reverse('projects:depremView', kwargs={'id': self.id})

    def get_create_url(self):
        return reverse('projects:depremCreate')

    def get_update_url(self):
        return reverse('projects:depremUpdate', kwargs={'id': self.id})

    def get_update_urlTr(self):
        return reverse('projects:depremUpdateTr', kwargs={'id': self.id})

    def get_Infupdate_url(self):
        return reverse('projects:depremInfUpdate', kwargs={'id': self.id})

    def get_Infupdate_urlTr(self):
        return reverse('projects:depremInfUpdateTr', kwargs={'id': self.id})

    def get_Featureupdate_url(self):
        return reverse('projects:depremFeatureUpdate', kwargs={'id': self.id})

    def get_Featureupdate_urlTr(self):
        return reverse('projects:depremFeatureUpdateTr', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('projects:depremDelete', kwargs={'id': self.id})

    def get_updateRisks_url(self):
        return reverse('projects:depremTerminate', kwargs={'id': self.id})

    def getEmrLocTr(self):
        location = ['Marmara Bölgesi', 'Ege Bölgesi', 'Karadeniz Bölgesi','Akdeniz Bölgesi', 'İç Anadolu Bölgesi', 'Doğu Anadolu Bölgesi','Güneydoğu Anadolu Bölgesi']
        return location[int(self.EmergencyLocation) - 1]


    def getEmrTime(self):
        time = ['Day', 'Evening', 'Night']
        return time[int(self.EmergencyTime) - 1]

    def getPotSecDis(self):
        secDis = ['Yes', 'No']
        return secDis[int(self.PotentialSecondaryDisasters) - 1]

    def getPotSecDisTr(self):
        secDis = ['Evet', 'Hayır']
        return secDis[int(self.PotentialSecondaryDisasters) - 1]

    def getEmrTimeTr(self):
        time = ['Gündüz saat:[06.00-19.00]', 'Akşam saat:[19.00-01.00]', 'Gece saat:[01.00-06.00]']
        return time[int(self.EmergencyTime) - 1]




    def getWeatherCond(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.WeatherCondition) - 1]

    def getBuildDensity(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.BuildingDensityAccessibilityDisasterArea) - 1]

    def getPotHazard(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.PotentialHazardousMaterial) - 1]

    def getEmrResComp(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.EmergencyResourceCompleteness) - 1]

    def getEmrResDur(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.EmergencyResourceDuration) - 1]

    def getInitResponce(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.InitialResponseLevel) - 1]

    def getCondRoad(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.ConditionRoadTransportation) - 1]

    def getCondAir(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.ConditionAirTransportation) - 1]

    def getCondRailway(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.ConditionRailwayTransportation) - 1]

    def getCondMari(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.ConditionMaritimeTransportation) - 1]

    def getCondHealth(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.ConditionHealthInfrastructure) - 1]

    def getCondWaterSupp(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.ConditionWaterSupplySewage) - 1]

    def getCondComm(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.ConditionCommunicationInfrastructure) - 1]

    def getCondNatGas(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.ConditionNaturalgas) - 1]

    def getCondPowerGrid(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.ConditionPowergrid) - 1]

    def getSufficiency(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.SufficiencyTemporaryResidential) - 1]

    def getCapacityWasteLand(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.CapacityWasteLandfills) - 1]


    def getWeatherCondTr(self):
        wdgt = ['Kesinlikle Kötü', 'Çok Kötü', 'Kötü', 'Orta', 'İyi', 'Çok İyi', 'Kesinlikle İyi']
        return wdgt[int(self.WeatherCondition) - 1]

    def getBuildDensityTr(self):
        wdgt = ['Kesinlikle Kötü', 'Çok Kötü', 'Kötü', 'Orta', 'İyi', 'Çok İyi', 'Kesinlikle İyi']
        return wdgt[int(self.BuildingDensityAccessibilityDisasterArea) - 1]

    def getPotHazardTr(self):
        wdgt = ['Kesinlikle Düşük', 'Çok Düşük', 'Düşük', 'Orta', 'Yüksek', 'Çok Yüksek', 'Kesinlikle Yüksek']
        return wdgt[int(self.PotentialHazardousMaterial) - 1]

    def getEmrResCompTr(self):
        wdgt = ['Kesinlikle Düşük', 'Çok Düşük', 'Düşük', 'Orta', 'Yüksek', 'Çok Yüksek', 'Kesinlikle Yüksek']
        return wdgt[int(self.EmergencyResourceCompleteness) - 1]

    def getEmrResDurTr(self):
        wdgt = ['Kesinlikle Uzun', 'Çok Uzun', 'Uzun', 'Orta', 'Kısa', 'Çok Kısa', 'Kesinlikle Kısa']
        return wdgt[int(self.EmergencyResourceDuration) - 1]

    def getInitResponceTr(self):
        wdgt = ['Kesinlikle Düşük', 'Çok Düşük', 'Düşük', 'Orta', 'Yüksek', 'Çok Yüksek', 'Kesinlikle Yüksek']
        return wdgt[int(self.InitialResponseLevel) - 1]

    def getCondRoadTr(self):
        wdgt = ['Kesinlikle Kötü', 'Çok Kötü', 'Kötü', 'Orta', 'İyi', 'Çok İyi', 'Kesinlikle İyi']
        return wdgt[int(self.ConditionRoadTransportation) - 1]

    def getCondAirTr(self):
        wdgt = ['Kesinlikle Kötü', 'Çok Kötü', 'Kötü', 'Orta', 'İyi', 'Çok İyi', 'Kesinlikle İyi']
        return wdgt[int(self.ConditionAirTransportation) - 1]

    def getCondRailwayTr(self):
        wdgt = ['Kesinlikle Kötü', 'Çok Kötü', 'Kötü', 'Orta', 'İyi', 'Çok İyi', 'Kesinlikle İyi']
        return wdgt[int(self.ConditionRailwayTransportation) - 1]

    def getCondMariTr(self):
        wdgt = ['Kesinlikle Kötü', 'Çok Kötü', 'Kötü', 'Orta', 'İyi', 'Çok İyi', 'Kesinlikle İyi']
        return wdgt[int(self.ConditionMaritimeTransportation) - 1]

    def getCondHealthTr(self):
        wdgt = ['Kesinlikle Kötü', 'Çok Kötü', 'Kötü', 'Orta', 'İyi', 'Çok İyi', 'Kesinlikle İyi']
        return wdgt[int(self.ConditionHealthInfrastructure) - 1]

    def getCondWaterSuppTr(self):
        wdgt = ['Kesinlikle Kötü', 'Çok Kötü', 'Kötü', 'Orta', 'İyi', 'Çok İyi', 'Kesinlikle İyi']
        return wdgt[int(self.ConditionWaterSupplySewage) - 1]

    def getCondCommTr(self):
        wdgt = ['Kesinlikle Kötü', 'Çok Kötü', 'Kötü', 'Orta', 'İyi', 'Çok İyi', 'Kesinlikle İyi']
        return wdgt[int(self.ConditionCommunicationInfrastructure) - 1]

    def getCondNatGasTr(self):
        wdgt = ['Kesinlikle Kötü', 'Çok Kötü', 'Kötü', 'Orta', 'İyi', 'Çok İyi', 'Kesinlikle İyi']
        return wdgt[int(self.ConditionNaturalgas) - 1]

    def getCondPowerGridTr(self):
        wdgt = ['Kesinlikle Kötü', 'Çok Kötü', 'Kötü', 'Orta', 'İyi', 'Çok İyi', 'Kesinlikle İyi']
        return wdgt[int(self.ConditionPowergrid) - 1]

    def getSufficiencyTr(self):
        wdgt = ['Kesinlikle Düşük', 'Çok Düşük', 'Düşük', 'Orta', 'Yüksek', 'Çok Yüksek', 'Kesinlikle Yüksek']
        return wdgt[int(self.SufficiencyTemporaryResidential) - 1]

    def getCapacityWasteLandTr(self):
        wdgt = ['Kesinlikle Kötü', 'Çok Kötü', 'Kötü', 'Orta', 'İyi', 'Çok İyi', 'Kesinlikle İyi']
        return wdgt[int(self.CapacityWasteLandfills) - 1]


class Sel(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='creator', related_name='sels', on_delete=models.SET_NULL, null=True)

    # info
    projectName = models.CharField(max_length=120, verbose_name='Disaster Name')
    summary = models.TextField(verbose_name='Summary')
    crtDate = models.DateTimeField('Creating Date', auto_now_add=True)
    #selPrjId = models.IntegerField(unique=True, primary_key=True, verbose_name='Project Id')

    # Factors
    MaximumPrecipitationIntensity = models.FloatField(verbose_name='Maximum Precipitation Intensity (mm/hour)')
    SinglePrecipitationPeriod = models.FloatField(verbose_name='Single Precipitation Period (hour)')
    AveragePrecipitation = models.FloatField(verbose_name='Average Precipitation (mm)')
    MaximumWaterDepth = models.FloatField(verbose_name='Maximum Water Depth (cm)')
    DamageArea = models.FloatField(verbose_name='Damage Area (km2)')
    RescueWorker = models.FloatField(verbose_name='Rescue Worker (person)')
    EmergencyResourceDuration = models.FloatField(verbose_name='Emergency Resource Arrival Duration (min)')
    AltitudeRegion = models.FloatField(verbose_name='Altitude of the Region (m)')
    SlopeRegion = models.FloatField(verbose_name='Slope of the Region (1/m)')

    ConditionRoadTransportation = models.CharField(max_length=20, choices=lessMuch, verbose_name='Condition of Road Transportation Lines',default=None)
    EmergencyResourceCompletenessReadiness = models.CharField(max_length=20, choices=lessMuch, verbose_name='Emergency Resource Completeness and Readiness Level' ,default=None)
    BuildingDensityAccessibility = models.CharField(max_length=20, choices=lessMuch, verbose_name='Building Density and Accessibility of the Disaster Area' ,default=None)

    responses = models.ForeignKey(ResponseCat, on_delete=models.CASCADE)
    terminate = models.BooleanField(verbose_name='terminate', default=False)

    def get_absolute_urlSel(self):
        return reverse('projects:selView', kwargs={'id': self.id})

    def get_create_url(self):
        return reverse('projects:selCreate')

    def get_update_url(self):
        return reverse('projects:selUpdate', kwargs={'id': self.id})

    def get_update_urlTr(self):
        return reverse('projects:selUpdateTr', kwargs={'id': self.id})

    def get_Infupdate_url(self):
        return reverse('projects:selInfUpdate', kwargs={'id': self.id})

    def get_Infupdate_urlTr(self):
        return reverse('projects:selInfUpdateTr', kwargs={'id': self.id})

    def get_Featureupdate_url(self):
        return reverse('projects:selFeatureUpdate', kwargs={'id': self.id})

    def get_Featureupdate_urlTr(self):
        return reverse('projects:selFeatureUpdateTr', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('projects:selDelete', kwargs={'id': self.id})

    def get_updateRisks_url(self):
        return reverse('projects:selTerminate', kwargs={'id': self.id})

    def getCondRoadTransp(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.ConditionRoadTransportation) - 1]

    def getEmrgResComRead(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.EmergencyResourceCompletenessReadiness) - 1]

    def getBuildDensity(self):
        wdgt = ['Definitely Low', 'Very Low', 'Low', 'Medium', 'High', 'Very High', 'Definitely High']
        return wdgt[int(self.BuildingDensityAccessibility) - 1]

    def getCondRoadTranspTr(self):
        wdgt = ['Kesinlikle Düşük', 'Çok Düşük', 'Düşük', 'Orta', 'Yüksek', 'Çok Yüksek', 'Kesinlikle Yüksek']
        return wdgt[int(self.ConditionRoadTransportation) - 1]

    def getEmrgResComReadTr(self):
        wdgt = ['Kesinlikle Düşük', 'Çok Düşük', 'Düşük', 'Orta', 'Yüksek', 'Çok Yüksek', 'Kesinlikle Yüksek']
        return wdgt[int(self.EmergencyResourceCompletenessReadiness) - 1]

    def getBuildDensityTr(self):
        wdgt = ['Kesinlikle Düşük', 'Çok Düşük', 'Düşük', 'Orta', 'Yüksek', 'Çok Yüksek', 'Kesinlikle Yüksek']
        return wdgt[int(self.BuildingDensityAccessibility) - 1]



