from django import forms
from projects.models import *
from django.forms.models import modelformset_factory


class depremForm(forms.ModelForm):

    class Meta:
        model = Deprem
        fields = ['projectName', 'summary','MagnitudeEarthquake','EmergencyTime', 'FocalDepth', 'EmergencyLocation', 'WeatherCondition',
                  'BuildingCollapseRate','PotentialSecondaryDisasters','PopulationDensity','BuildingDensityAccessibilityDisasterArea','PotentialHazardousMaterial',
                  'EmergencyResourceCompleteness','EmergencyResourceDuration','InitialResponseLevel','ConditionRoadTransportation','ConditionAirTransportation',
                  'ConditionRailwayTransportation','ConditionMaritimeTransportation','ConditionHealthInfrastructure','ConditionWaterSupplySewage',
                  'ConditionCommunicationInfrastructure','ConditionNaturalgas','ConditionPowergrid','SufficiencyTemporaryResidential','CapacityWasteLandfills',]


class depremInfForm(forms.ModelForm):

    class Meta:
        model = Deprem
        fields = ['projectName','summary',]

        
class depremFeatureForm(forms.ModelForm):

    class Meta:
        model = Deprem
        fields = ['MagnitudeEarthquake', 'EmergencyTime', 'FocalDepth', 'EmergencyLocation',
                  'WeatherCondition',
                  'BuildingCollapseRate', 'PotentialSecondaryDisasters', 'PopulationDensity',
                  'BuildingDensityAccessibilityDisasterArea', 'PotentialHazardousMaterial',
                  'EmergencyResourceCompleteness', 'EmergencyResourceDuration', 'InitialResponseLevel',
                  'ConditionRoadTransportation', 'ConditionAirTransportation',
                  'ConditionRailwayTransportation', 'ConditionMaritimeTransportation', 'ConditionHealthInfrastructure',
                  'ConditionWaterSupplySewage',
                  'ConditionCommunicationInfrastructure', 'ConditionNaturalgas', 'ConditionPowergrid',
                  'SufficiencyTemporaryResidential', 'CapacityWasteLandfills', ]
        


class selForm(forms.ModelForm):

    class Meta:
        model = Sel
        fields = ['projectName', 'summary','MaximumPrecipitationIntensity','SinglePrecipitationPeriod', 'AveragePrecipitation', 'MaximumWaterDepth',
                  'ConditionRoadTransportation','DamageArea','RescueWorker','EmergencyResourceDuration','EmergencyResourceCompletenessReadiness','AltitudeRegion',
                  'SlopeRegion','BuildingDensityAccessibility',]

class selInfForm(forms.ModelForm):

    class Meta:
        model = Sel
        fields = ['projectName','summary',]
        


class selFeatureForm(forms.ModelForm):

    class Meta:
        model = Sel
        fields = ['MaximumPrecipitationIntensity', 'SinglePrecipitationPeriod',
                  'AveragePrecipitation', 'MaximumWaterDepth',
                  'ConditionRoadTransportation', 'DamageArea', 'RescueWorker', 'EmergencyResourceDuration',
                  'EmergencyResourceCompletenessReadiness', 'AltitudeRegion',
                  'SlopeRegion', 'BuildingDensityAccessibility', ]


class responseForm(forms.ModelForm):

    class Meta:
        model = ResponsePlan
        fields = ['reaction','date','time','effect','responsible',]





#########
##########
###########
##### Turkish ######


class depremFormTr(forms.ModelForm):


    class Meta:
        model = Deprem
        fields = ['projectName', 'summary', 'MagnitudeEarthquake', 'EmergencyTime', 'FocalDepth', 'EmergencyLocation',
                  'WeatherCondition',
                  'BuildingCollapseRate', 'PotentialSecondaryDisasters', 'PopulationDensity',
                  'BuildingDensityAccessibilityDisasterArea', 'PotentialHazardousMaterial',
                  'EmergencyResourceCompleteness', 'EmergencyResourceDuration', 'InitialResponseLevel',
                  'ConditionRoadTransportation', 'ConditionAirTransportation',
                  'ConditionRailwayTransportation', 'ConditionMaritimeTransportation', 'ConditionHealthInfrastructure',
                  'ConditionWaterSupplySewage',
                  'ConditionCommunicationInfrastructure', 'ConditionNaturalgas', 'ConditionPowergrid',
                  'SufficiencyTemporaryResidential', 'CapacityWasteLandfills', ]




    def __init__(self, *args, **kwargs):
        super(depremFormTr, self).__init__(*args, **kwargs)
        self.fields['projectName'].label = "Afet Adı"
        self.fields['summary'].label = "Afet Özet Bilgi"
        self.fields['MagnitudeEarthquake'].label = "Depremin Büyüklüğü"
        self.fields['EmergencyTime'].label = "Depremin Zamanı"
        self.fields['FocalDepth'].label = "Odak Derinliği (km)"
        self.fields['EmergencyLocation'].label = "Afet Bölgesinin Konumu"
        self.fields['BuildingCollapseRate'].label = "Yıkılan Bina Oranı (%)"
        self.fields['PotentialSecondaryDisasters'].label = "İkincil Afetlerin Oluşma Olasılığı"
        self.fields['PopulationDensity'].label = "Nüfus Yoğunluğu (kişi/km2)"

        self.fields['WeatherCondition'].label = "Afet Anı İklim Koşulları"
        self.fields['BuildingDensityAccessibilityDisasterArea'].label = "Afet Bölgesinin Erişilebilirliği"
        self.fields['PotentialHazardousMaterial'].label = "Tehlikeli Madde Açığa Çıkma Potensiyeli"
        self.fields['EmergencyResourceCompleteness'].label = "Acil Durum Kaynak Yeterliliği ve Hazırlık Seviyesi"
        self.fields['EmergencyResourceDuration'].label = "Kaynakların Tahmini Varış Süresi"
        self.fields['InitialResponseLevel'].label = "Yerel Birimlerin İlk Müdahale Seviyesi"
        self.fields['ConditionRoadTransportation'].label = "Kara Yolu Ulaşım Hatlarının Durumu"
        self.fields['ConditionAirTransportation'].label = "Hava Yolu Ulaşım Hatlarının Durumu"
        self.fields['ConditionRailwayTransportation'].label = "Demir Yolu Ulaşım Hatlarının Durumu"
        self.fields['ConditionMaritimeTransportation'].label = "Deniz Yolu Ulaşım Hatlarının Durumu"
        self.fields['ConditionHealthInfrastructure'].label = "Sağlık Altyapısının Durumu"
        self.fields['ConditionWaterSupplySewage'].label = "Su ve Kanalizasyon Altyapısının Durumu"
        self.fields['ConditionCommunicationInfrastructure'].label = "İletişim Altyapısının Durumu"
        self.fields['ConditionNaturalgas'].label = "Doğalgaz Altyapısının Durumu"
        self.fields['ConditionPowergrid'].label = "Enerji Altyapısının Durumu"
        self.fields['SufficiencyTemporaryResidential'].label = "Geçici Konut Alanlarının Yeterliliği"
        self.fields['CapacityWasteLandfills'].label = "Atık Depolama Alanlarının Yeterliliği ve Mesafesi"

        self.fields['MagnitudeEarthquake'].help_text = 'Bu kriter, deprem sırasında açığa çıkan enerjiyi ifade etmektedir. Lütfen 0.0 ile 9.9 arasında bir değer giriniz.'
        self.fields['EmergencyTime'].help_text = 'Bu kriter, depremin meydana geldiği zaman aralığını ifade etmektedir'
        self.fields['FocalDepth'].help_text = 'Bu kriter, depremde enerjinin açığa çıktığı noktanın yeryüzünden en kısa uzaklığı ifade etmektedir'
        self.fields['EmergencyLocation'].help_text = 'Bu kriter, depremden etkilenen coğrafi bölgeyi ifade etmektedir.'
        self.fields['BuildingCollapseRate'].help_text = 'Bu kriter, deprem nedeniyle yıkılan bina oranını ifade etmektedir. Lütfen 1-100 arası bir değer giriniz.'
        self.fields['PotentialSecondaryDisasters'].help_text = 'Bu kriter, depremden sonra ikincil afetlerin oluşma olasılığını ifade etmektedir.'
        self.fields['PopulationDensity'].help_text = 'Bu kriter, depremden etkilenen bölgedeki nüfus yoğunluğunu ifade etmektedir. '
        self.fields['WeatherCondition'].help_text = 'Bu kriter, depremin oluştuğu andaki iklim koşullarını ifade etmektedir.'
        self.fields['BuildingDensityAccessibilityDisasterArea'].help_text = 'Bu kriter, afet bölgesinin arama-kurtarma ve lojistik açıdan erişilebilirliğini ifade etmektedir.'
        self.fields['PotentialHazardousMaterial'].help_text = 'Bu kriter, depremden sonra tehlikeli madde açığı çıkma olasılığını ifade etmektedir.'
        self.fields['EmergencyResourceCompleteness'].help_text = 'Bu kriter, deprem sonrası yönetim için kullanılacak olan kaynakların yeterliliğini ve hazırlık seviyesini ifade etmektedir. '
        self.fields['EmergencyResourceDuration'].help_text = 'Bu kriter, deprem sonrası yönetim için kullanılacak olan kaynakların deprem bölgesine varış süresini ifade etmektedir.'
        self.fields['InitialResponseLevel'].help_text = 'Bu kriter, deprem sonrası yerel birimlerin ilk müdahale seviyesini ifade etmektedir.'
        self.fields['ConditionRoadTransportation'].help_text = 'Bu kriter, deprem sonrasında kara yolu altyapısının lojistik operasyonlar için kullanılabilirliğini ifade etmektedir.'
        self.fields['ConditionAirTransportation'].help_text = 'Bu kriter, deprem sonrasında hava yolu altyapısının lojistik operasyonlar için kullanılabilirliğini ifade etmektedir.'
        self.fields['ConditionRailwayTransportation'].help_text = 'Bu kriter, deprem sonrasında demir yolu altyapısının lojistik operasyonlar için kullanılabilirliğini ifade etmektedir.'
        self.fields['ConditionMaritimeTransportation'].help_text = 'Bu kriter, deprem sonrasında deniz yolu altyapısının lojistik operasyonlar için kullanılabilirliğini ifade etmektedir.'
        self.fields['ConditionHealthInfrastructure'].help_text = 'Bu kriter, deprem sonrasında sağlık altyapısının yaralıların tedavisi için kullanılabilirliğini ifade etmektedir.'
        self.fields['ConditionWaterSupplySewage'].help_text = 'Bu kriter, deprem sonrasında su ve kanalizasyon altyapısının hizmet durumunu ifade etmektedir.'
        self.fields['ConditionCommunicationInfrastructure'].help_text = 'Bu kriter, deprem sonrasında iletişim altyapısının hizmet durumunu ifade etmektedir.'
        self.fields['ConditionNaturalgas'].help_text = 'Bu kriter, deprem sonrasında doğalgaz altyapısının hizmet durumunu ifade etmektedir.'
        self.fields['ConditionPowergrid'].help_text = 'Bu kriter, deprem sonrasında enerji altyapısının hizmet durumunu ifade etmektedir.'
        self.fields['SufficiencyTemporaryResidential'].help_text = 'Bu kriter, deprem sonrasında geçici konutlar için elverişli alanların yeterliliğini ifade etmektedir.'
        self.fields['CapacityWasteLandfills'].help_text = 'Bu kriter, deprem sonrasında açığa çıkan atıkların depolanması için kullanılacak alanların yeterliliğini ve deprem bölgesine mesafesini ifade etmektedir.'



        newYesNo = (('1', 'Evet'), ('2', 'Hayır'),)
        self.fields['PotentialSecondaryDisasters'].choices = newYesNo

        newEmrgTime = (('1', 'Gündüz   saat:[06.00-19.00]'), ('2', 'Akşam   saat:[19.00-01.00]'), ('3', 'Gece   saat:[01.00-06.00]'),)
        self.fields['EmergencyTime'].choices = newEmrgTime

        newLesMuch = (('1', 'Kesinlikle Düşük'), ('2', 'Çok Düşük'), ('3', 'Düşük'), ('4', 'Orta'), ('5', 'Yüksek'), ('6', 'Çok Yüksek'),('7', 'Kesinlikle Yüksek'),)

        newGoodBad = (('1', 'Kesinlikle Kötü'), ('2', 'Çok Kötü'), ('3', 'Kötü'), ('4', 'Orta'), ('5', 'İyi'), ('6', 'Çok İyi'),('7', 'Kesinlikle İyi'),)

        newShortLong = (('1', 'Kesinlikle Uzun'), ('2', 'Çok Uzun'), ('3', 'Uzun'), ('4', 'Orta'), ('5', 'Kısa'), ('6', 'Çok Kısa'),('7', 'Kesinlikle Kısa'),)

        self.fields['WeatherCondition'].choices = newGoodBad
        self.fields['BuildingDensityAccessibilityDisasterArea'].choices = newGoodBad
        self.fields['PotentialHazardousMaterial'].choices = newLesMuch
        self.fields['EmergencyResourceCompleteness'].choices = newLesMuch
        self.fields['EmergencyResourceDuration'].choices = newShortLong
        self.fields['InitialResponseLevel'].choices = newLesMuch
        self.fields['ConditionRoadTransportation'].choices = newGoodBad
        self.fields['ConditionAirTransportation'].choices = newGoodBad
        self.fields['ConditionRailwayTransportation'].choices = newGoodBad
        self.fields['ConditionMaritimeTransportation'].choices = newGoodBad
        self.fields['ConditionHealthInfrastructure'].choices = newGoodBad
        self.fields['ConditionWaterSupplySewage'].choices = newGoodBad
        self.fields['ConditionCommunicationInfrastructure'].choices = newGoodBad
        self.fields['ConditionNaturalgas'].choices = newGoodBad
        self.fields['ConditionPowergrid'].choices = newGoodBad
        self.fields['SufficiencyTemporaryResidential'].choices = newLesMuch
        self.fields['CapacityWasteLandfills'].choices = newGoodBad

        self.fields['MagnitudeEarthquake'].widget.attrs['placeholder'] = "Lütfen 0.0 ile 9.9 arasında bir değer giriniz."
        self.fields['BuildingCollapseRate'].widget.attrs['placeholder'] = "Lütfen 1-100 arası bir değer giriniz."






class depremInfFormTr(forms.ModelForm):
    class Meta:
        model = Deprem
        fields = ['projectName', 'summary', ]

    def __init__(self, *args, **kwargs):
        super(depremInfFormTr, self).__init__(*args, **kwargs)
        self.fields['projectName'].label = "Afet Adı"
        self.fields['summary'].label = "Afet Özet Bilgi"


class depremFeatureFormTr(forms.ModelForm):
    class Meta:
        model = Deprem
        fields = ['MagnitudeEarthquake', 'EmergencyTime', 'FocalDepth', 'EmergencyLocation',
                  'WeatherCondition',
                  'BuildingCollapseRate', 'PotentialSecondaryDisasters', 'PopulationDensity',
                  'BuildingDensityAccessibilityDisasterArea', 'PotentialHazardousMaterial',
                  'EmergencyResourceCompleteness', 'EmergencyResourceDuration', 'InitialResponseLevel',
                  'ConditionRoadTransportation', 'ConditionAirTransportation',
                  'ConditionRailwayTransportation', 'ConditionMaritimeTransportation', 'ConditionHealthInfrastructure',
                  'ConditionWaterSupplySewage',
                  'ConditionCommunicationInfrastructure', 'ConditionNaturalgas', 'ConditionPowergrid',
                  'SufficiencyTemporaryResidential', 'CapacityWasteLandfills', ]


    def __init__(self, *args, **kwargs):
        super(depremFeatureFormTr, self).__init__(*args, **kwargs)
        self.fields['MagnitudeEarthquake'].label = "Depremin Büyüklüğü"
        self.fields['EmergencyTime'].label = "Depremin Zamanı"
        self.fields['FocalDepth'].label = "Odak Derinliği (km)"
        self.fields['EmergencyLocation'].label = "Afet Bölgesinin Konumu"
        self.fields['WeatherCondition'].label = "Afet Anı İklim Koşulları"
        self.fields['BuildingCollapseRate'].label = "Yıkılan Bina Oranı (%)"
        self.fields['PotentialSecondaryDisasters'].label = "İkincil Afetlerin Oluşma Olasılığı"
        self.fields['PopulationDensity'].label = "Nüfus Yoğunluğu (kişi/km2)"
        self.fields['BuildingDensityAccessibilityDisasterArea'].label = "Afet Bölgesinin Erişilebilirliği"
        self.fields['PotentialHazardousMaterial'].label = "Tehlikeli Madde Açığa Çıkma Potensiyeli"
        self.fields['EmergencyResourceCompleteness'].label = "Acil Durum Kaynak Yeterliliği ve Hazırlık Seviyesi"
        self.fields['EmergencyResourceDuration'].label = "Kaynakların Tahmini Varış Süresi"
        self.fields['InitialResponseLevel'].label = "Yerel Birimlerin İlk Müdahale Seviyesi"
        self.fields['ConditionRoadTransportation'].label = "Kara Yolu Ulaşım Hatlarının Durumu"
        self.fields['ConditionAirTransportation'].label = "Hava Yolu Ulaşım Hatlarının Durumu"
        self.fields['ConditionRailwayTransportation'].label = "Demir Yolu Ulaşım Hatlarının Durumu"
        self.fields['ConditionMaritimeTransportation'].label = "Deniz Yolu Ulaşım Hatlarının Durumu"
        self.fields['ConditionHealthInfrastructure'].label = "Sağlık Altyapısının Durumu"
        self.fields['ConditionWaterSupplySewage'].label = "Su ve Kanalizasyon Altyapısının Durumu"
        self.fields['ConditionCommunicationInfrastructure'].label = "İletişim Altyapısının Durumu"
        self.fields['ConditionNaturalgas'].label = "Doğalgaz Altyapısının Durumu"
        self.fields['ConditionPowergrid'].label = "Enerji Altyapısının Durumu"
        self.fields['SufficiencyTemporaryResidential'].label = "Geçici Konut Alanlarının Yeterliliği"
        self.fields['CapacityWasteLandfills'].label = "Atık Depolama Alanlarının Yeterliliği ve Mesafesi"

        self.fields[
            'MagnitudeEarthquake'].help_text = 'Bu kriter, deprem sırasında açığa çıkan enerjiyi ifade etmektedir. Lütfen 0.0 ile 9.9 arasında bir değer giriniz.'
        self.fields['EmergencyTime'].help_text = 'Bu kriter, depremin meydana geldiği zaman aralığını ifade etmektedir'
        self.fields[
            'FocalDepth'].help_text = 'Bu kriter, depremde enerjinin açığa çıktığı noktanın yeryüzünden en kısa uzaklığı ifade etmektedir'
        self.fields['EmergencyLocation'].help_text = 'Bu kriter, depremden etkilenen coğrafi bölgeyi ifade etmektedir.'
        self.fields[
            'BuildingCollapseRate'].help_text = 'Bu kriter, deprem nedeniyle yıkılan bina oranını ifade etmektedir. Lütfen 1-100 arası bir değer giriniz.'
        self.fields[
            'PotentialSecondaryDisasters'].help_text = 'Bu kriter, depremden sonra ikincil afetlerin oluşma olasılığını ifade etmektedir.'
        self.fields[
            'PopulationDensity'].help_text = 'Bu kriter, depremden etkilenen bölgedeki nüfus yoğunluğunu ifade etmektedir. '
        self.fields[
            'WeatherCondition'].help_text = 'Bu kriter, depremin oluştuğu andaki iklim koşullarını ifade etmektedir.'
        self.fields[
            'BuildingDensityAccessibilityDisasterArea'].help_text = 'Bu kriter, afet bölgesinin arama-kurtarma ve lojistik açıdan erişilebilirliğini ifade etmektedir.'
        self.fields[
            'PotentialHazardousMaterial'].help_text = 'Bu kriter, depremden sonra tehlikeli madde açığı çıkma olasılığını ifade etmektedir.'
        self.fields[
            'EmergencyResourceCompleteness'].help_text = 'Bu kriter, deprem sonrası yönetim için kullanılacak olan kaynakların yeterliliğini ve hazırlık seviyesini ifade etmektedir. '
        self.fields[
            'EmergencyResourceDuration'].help_text = 'Bu kriter, deprem sonrası yönetim için kullanılacak olan kaynakların deprem bölgesine varış süresini ifade etmektedir.'
        self.fields[
            'InitialResponseLevel'].help_text = 'Bu kriter, deprem sonrası yerel birimlerin ilk müdahale seviyesini ifade etmektedir.'
        self.fields[
            'ConditionRoadTransportation'].help_text = 'Bu kriter, deprem sonrasında kara yolu altyapısının lojistik operasyonlar için kullanılabilirliğini ifade etmektedir.'
        self.fields[
            'ConditionAirTransportation'].help_text = 'Bu kriter, deprem sonrasında hava yolu altyapısının lojistik operasyonlar için kullanılabilirliğini ifade etmektedir.'
        self.fields[
            'ConditionRailwayTransportation'].help_text = 'Bu kriter, deprem sonrasında demir yolu altyapısının lojistik operasyonlar için kullanılabilirliğini ifade etmektedir.'
        self.fields[
            'ConditionMaritimeTransportation'].help_text = 'Bu kriter, deprem sonrasında deniz yolu altyapısının lojistik operasyonlar için kullanılabilirliğini ifade etmektedir.'
        self.fields[
            'ConditionHealthInfrastructure'].help_text = 'Bu kriter, deprem sonrasında sağlık altyapısının yaralıların tedavisi için kullanılabilirliğini ifade etmektedir.'
        self.fields[
            'ConditionWaterSupplySewage'].help_text = 'Bu kriter, deprem sonrasında su ve kanalizasyon altyapısının hizmet durumunu ifade etmektedir.'
        self.fields[
            'ConditionCommunicationInfrastructure'].help_text = 'Bu kriter, deprem sonrasında iletişim altyapısının hizmet durumunu ifade etmektedir.'
        self.fields[
            'ConditionNaturalgas'].help_text = 'Bu kriter, deprem sonrasında doğalgaz altyapısının hizmet durumunu ifade etmektedir.'
        self.fields[
            'ConditionPowergrid'].help_text = 'Bu kriter, deprem sonrasında enerji altyapısının hizmet durumunu ifade etmektedir.'
        self.fields[
            'SufficiencyTemporaryResidential'].help_text = 'Bu kriter, deprem sonrasında geçici konutlar için elverişli alanların yeterliliğini ifade etmektedir.'
        self.fields[
            'CapacityWasteLandfills'].help_text = 'Bu kriter, deprem sonrasında açığa çıkan atıkların depolanması için kullanılacak alanların yeterliliğini ve deprem bölgesine mesafesini ifade etmektedir.'

        newYesNo = (('1', 'Evet'), ('2', 'Hayır'),)
        self.fields['PotentialSecondaryDisasters'].choices = newYesNo

        newEmrgTime = (
        ('1', 'Gündüz   saat:[06.00-19.00]'), ('2', 'Akşam   saat:[19.00-01.00]'), ('3', 'Gece   saat:[01.00-06.00]'),)
        self.fields['EmergencyTime'].choices = newEmrgTime

        newLesMuch = (('1', 'Kesinlikle Düşük'), ('2', 'Çok Düşük'), ('3', 'Düşük'), ('4', 'Orta'), ('5', 'Yüksek'),
                      ('6', 'Çok Yüksek'), ('7', 'Kesinlikle Yüksek'),)

        newGoodBad = (
        ('1', 'Kesinlikle Kötü'), ('2', 'Çok Kötü'), ('3', 'Kötü'), ('4', 'Orta'), ('5', 'İyi'), ('6', 'Çok İyi'),
        ('7', 'Kesinlikle İyi'),)

        newShortLong = (
        ('1', 'Kesinlikle Uzun'), ('2', 'Çok Uzun'), ('3', 'Uzun'), ('4', 'Orta'), ('5', 'Kısa'), ('6', 'Çok Kısa'),
        ('7', 'Kesinlikle Kısa'),)

        self.fields['WeatherCondition'].choices = newGoodBad
        self.fields['BuildingDensityAccessibilityDisasterArea'].choices = newGoodBad
        self.fields['PotentialHazardousMaterial'].choices = newLesMuch
        self.fields['EmergencyResourceCompleteness'].choices = newLesMuch
        self.fields['EmergencyResourceDuration'].choices = newShortLong
        self.fields['InitialResponseLevel'].choices = newLesMuch
        self.fields['ConditionRoadTransportation'].choices = newGoodBad
        self.fields['ConditionAirTransportation'].choices = newGoodBad
        self.fields['ConditionRailwayTransportation'].choices = newGoodBad
        self.fields['ConditionMaritimeTransportation'].choices = newGoodBad
        self.fields['ConditionHealthInfrastructure'].choices = newGoodBad
        self.fields['ConditionWaterSupplySewage'].choices = newGoodBad
        self.fields['ConditionCommunicationInfrastructure'].choices = newGoodBad
        self.fields['ConditionNaturalgas'].choices = newGoodBad
        self.fields['ConditionPowergrid'].choices = newGoodBad
        self.fields['SufficiencyTemporaryResidential'].choices = newLesMuch
        self.fields['CapacityWasteLandfills'].choices = newGoodBad

        self.fields['MagnitudeEarthquake'].widget.attrs[
            'placeholder'] = "Lütfen 0.0 ile 9.9 arasında bir değer giriniz."
        self.fields['BuildingCollapseRate'].widget.attrs['placeholder'] = "Lütfen 1-100 arası bir değer giriniz."




class selFormTr(forms.ModelForm):
    class Meta:
        model = Sel
        fields = ['projectName', 'summary', 'MaximumPrecipitationIntensity', 'SinglePrecipitationPeriod',
                  'AveragePrecipitation', 'MaximumWaterDepth',
                  'ConditionRoadTransportation', 'DamageArea', 'RescueWorker', 'EmergencyResourceDuration',
                  'EmergencyResourceCompletenessReadiness', 'AltitudeRegion',
                  'SlopeRegion', 'BuildingDensityAccessibility', ]

    def __init__(self, *args, **kwargs):
        super(selFormTr, self).__init__(*args, **kwargs)
        self.fields['projectName'].label = "Afet Adı"
        self.fields['summary'].label = "Afet Özet Bilgi"
        self.fields['MaximumPrecipitationIntensity'].label = "En Yüksek Yağış Yoğunluğu (mm/saat)"
        self.fields['SinglePrecipitationPeriod'].label = "Tek Yağış Periyodu (saat)"
        self.fields['AveragePrecipitation'].label = "Ortalama Yağış (mm)"
        self.fields['MaximumWaterDepth'].label = "En Yüksek Su Derinliği (cm)"
        self.fields['ConditionRoadTransportation'].label = "Kara Yolu Ulaşım Hatlarının Durumu"
        self.fields['DamageArea'].label = "Hasar Bölgesin Alanı (km2)"
        self.fields['RescueWorker'].label = "Kurtama Personeli Sayısı (kişi)"
        self.fields['EmergencyResourceDuration'].label = "Kaynakların Tahmini Varış Süresi (dakika)"
        self.fields['EmergencyResourceCompletenessReadiness'].label = "Acil Durum Kaynak Yeterliliği ve Hazırlık Seviyesi"
        self.fields['AltitudeRegion'].label = "Bölgenin Rakımı (m)"
        self.fields['SlopeRegion'].label = "Bölgenin Eğimi (1/m)"
        self.fields['BuildingDensityAccessibility'].label = "Afet Bölgesinin Bina Yoğunluğu ve Alanın Erişebilirliği"

        newLesMuch = (('1', 'Kesinlikle Düşük'), ('2', 'Çok Düşük'), ('3', 'Düşük'), ('4', 'Orta'), ('5', 'Yüksek'),
                      ('6', 'Çok Yüksek'), ('7', 'Kesinlikle Yüksek'),)
        self.fields['ConditionRoadTransportation'].choices = newLesMuch
        self.fields['EmergencyResourceCompletenessReadiness'].choices = newLesMuch
        self.fields['BuildingDensityAccessibility'].choices = newLesMuch



class selInfFormTr(forms.ModelForm):
    class Meta:
        model = Sel
        fields = ['projectName', 'summary', ]

    def __init__(self, *args, **kwargs):
        super(selInfFormTr, self).__init__(*args, **kwargs)
        self.fields['projectName'].label = "Afet Adı"
        self.fields['summary'].label = "Afet Özet Bilgi"


class selFeatureFormTr(forms.ModelForm):
    class Meta:
        model = Sel
        fields = ['MaximumPrecipitationIntensity', 'SinglePrecipitationPeriod',
                  'AveragePrecipitation', 'MaximumWaterDepth',
                  'ConditionRoadTransportation', 'DamageArea', 'RescueWorker', 'EmergencyResourceDuration',
                  'EmergencyResourceCompletenessReadiness', 'AltitudeRegion',
                  'SlopeRegion', 'BuildingDensityAccessibility', ]

    def __init__(self, *args, **kwargs):
        super(selFeatureFormTr, self).__init__(*args, **kwargs)
        self.fields['MaximumPrecipitationIntensity'].label = "En Yüksek Yağış Yoğunluğu (mm/saat)"
        self.fields['SinglePrecipitationPeriod'].label = "Tek Yağış Periyodu (saat)"
        self.fields['AveragePrecipitation'].label = "Ortalama Yağış (mm)"
        self.fields['MaximumWaterDepth'].label = "En Yüksek Su Derinliği (cm)"
        self.fields['ConditionRoadTransportation'].label = "Kara Yolu Ulaşım Hatlarının Durumu"
        self.fields['DamageArea'].label = "Hasar Bölgesin Alanı (km2)"
        self.fields['RescueWorker'].label = "Kurtarma Personeli Sayısı (kişi)"
        self.fields['EmergencyResourceDuration'].label = "Kaynakların Tahmini Varış Süresi (dakika)"
        self.fields['EmergencyResourceCompletenessReadiness'].label = "Acil Durum Kaynak Yeterliliği ve Hazırlık Seviyesi"
        self.fields['AltitudeRegion'].label = "Bölgenin Rakımı (m)"
        self.fields['SlopeRegion'].label = "Bölgenin Eğimi (1/m)"
        self.fields['BuildingDensityAccessibility'].label = "Afet Bölgesinin Bina Yoğunluğu ve Alanın Erişebilirliği"

        newLesMuch = (('1', 'Kesinlikle Düşük'), ('2', 'Çok Düşük'), ('3', 'Düşük'), ('4', 'Orta'), ('5', 'Yüksek'),
                      ('6', 'Çok Yüksek'), ('7', 'Kesinlikle Yüksek'),)
        self.fields['ConditionRoadTransportation'].choices = newLesMuch
        self.fields['EmergencyResourceCompletenessReadiness'].choices = newLesMuch
        self.fields['BuildingDensityAccessibility'].choices = newLesMuch



class responseFormTr(forms.ModelForm):
    class Meta:
        model = ResponsePlan
        fields = ['reaction', 'date', 'time', 'effect', 'responsible', ]


    def __init__(self, *args, **kwargs):
        super(responseFormTr, self).__init__(*args, **kwargs)
        self.fields['reaction'].label = "Reaksiyon"
        self.fields['date'].label = "Tarih"
        self.fields['time'].label = "Saat"
        self.fields['effect'].label = "Reaksiyonun Etkinliği"
        self.fields['responsible'].label = "Sorumlu Kurum"