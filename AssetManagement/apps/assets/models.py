from django.db import models

from apps.departments.models import BaseModel


class Asset(BaseModel):
    asset_number = models.CharField(verbose_name="资产编号", max_length=254)  #
    location = models.CharField(verbose_name="原始存放地点", max_length=254, null=True, blank=True)
    asset_name = models.CharField(verbose_name="资产名称", max_length=254, null=True, blank=True)
    classification = models.CharField(verbose_name="分类号", max_length=254, null=True, blank=True)
    category = models.CharField(verbose_name="分类名称", max_length=254, null=True, blank=True)
    assets_class = models.CharField(verbose_name="国资分类号", max_length=254, null=True, blank=True)
    model = models.CharField(verbose_name="型号", max_length=254, null=True, blank=True)
    specifications = models.CharField(verbose_name="规格", max_length=254, null=True, blank=True)
    purchase_date = models.CharField(verbose_name="购置日期", max_length=254, null=True, blank=True)
    price = models.CharField(verbose_name="单价", max_length=254, null=True, blank=True)
    number = models.CharField(verbose_name="数量", max_length=254, null=True, blank=True)
    total_annex = models.CharField(verbose_name="附件总额", max_length=254, null=True, blank=True)
    total_annex_quantity = models.CharField(verbose_name="附件总数量", max_length=254, null=True, blank=True)
    total_amount = models.CharField(verbose_name="总金额", max_length=254, null=True, blank=True)
    exit_Number = models.CharField(verbose_name="出厂编号", max_length=254, null=True, blank=True)
    date_of_production = models.CharField(verbose_name="出厂日期", max_length=254, null=True, blank=True)
    manufacturer = models.CharField(verbose_name="生产厂家", max_length=254, null=True, blank=True)
    employee = models.CharField(verbose_name="领用人", max_length=254, null=True, blank=True)
    acquisition_date = models.CharField(verbose_name="领用日期", max_length=254, null=True, blank=True)
    present_situation = models.CharField(verbose_name="现状", max_length=254, null=True, blank=True)
    direction_of_use = models.CharField(verbose_name="使用方向", max_length=254, null=True, blank=True)
    user_department = models.CharField(verbose_name="使用单位", max_length=254, null=True, blank=True)
    department = models.CharField(verbose_name="科室", max_length=254, null=True, blank=True)
    bar_code = models.CharField(verbose_name="条码", max_length=254, null=True, blank=True)
    original_value = models.CharField(verbose_name="原值", max_length=254, null=True, blank=True)
    original_quantity = models.CharField(verbose_name="原数量", max_length=254, null=True, blank=True)
    total_original_amount = models.CharField(verbose_name="原总金额", max_length=254, null=True, blank=True)
    original_total_amount_annex = models.CharField(verbose_name="附件原总额", max_length=254, null=True, blank=True)
    original_total_number_annexes = models.CharField(verbose_name="附件原总数量", max_length=254, null=True, blank=True)
    entry_time = models.CharField(verbose_name="录入时间", max_length=254, null=True, blank=True)
    administrator = models.CharField(verbose_name="管理人", max_length=254, null=True, blank=True)
    service_life = models.CharField(verbose_name="使用年限", max_length=254, null=True, blank=True)
    number_of_financial_assets = models.CharField(verbose_name="财政资产编号", max_length=254, null=True, blank=True)
    bill_entry_number = models.CharField(verbose_name="入账单编号", max_length=254, null=True, blank=True)
    state_category = models.CharField(verbose_name="国资大类", max_length=254, null=True, blank=True)
    call_out_number = models.CharField(verbose_name="调出编号", max_length=254, null=True, blank=True)
    # asset_status = models.CharField(verbose_name="资产状态", max_length=254, null=True, blank=True)
    original_asset_number = models.CharField(verbose_name="原资产编号", max_length=254, null=True, blank=True)
    provincial_asset_number = models.CharField(verbose_name="省资产编号", max_length=254, null=True, blank=True)
    financial_certificate_number = models.CharField(verbose_name="财务凭证号", max_length=254, null=True, blank=True)
    agent = models.CharField(verbose_name="经办人", max_length=254, null=True, blank=True)
    acceptor = models.CharField(verbose_name="验收人", max_length=254, null=True, blank=True)
    bookkeeper = models.CharField(verbose_name="记账人", max_length=254, null=True, blank=True)
    invoice_number = models.CharField(verbose_name="发票号码", max_length=254, null=True, blank=True)
    financial_classification = models.CharField(verbose_name="财务分类", max_length=254, null=True, blank=True)
    filing_and_registration = models.CharField(verbose_name="备案登记", max_length=254, null=True, blank=True)
    date_of_filing = models.CharField(verbose_name="备案日期", max_length=254, null=True, blank=True)
    account_reconciliation = models.CharField(verbose_name="科目对账", max_length=254, null=True, blank=True)
    accounting_date = models.CharField(verbose_name="记账日期", max_length=254, null=True, blank=True)
    detailed_outlay = models.CharField(verbose_name="经费详目", max_length=254, null=True, blank=True)
    unit_of_measurement = models.CharField(verbose_name="计量单位", max_length=254, null=True, blank=True)

    contact_number = models.CharField(verbose_name="合同编号", max_length=254, null=True, blank=True)  #

    class Meta:
        verbose_name = "资产固定信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.asset_number
