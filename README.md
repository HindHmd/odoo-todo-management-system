# نظام إدارة المهام - Todo Management System



## 🌍 اللغات المدعومة
- يدعم النظام كلاً من اللغتين **العربية** و**الإنجليزية** بشكل كامل
- واجهة المستخدم متعددة اللغات
- التقارير متاحة باللغتين

## ✨ المميزات الرئيسية / Key Features

### 🛠 نظام الصلاحيات المتقدم / Advanced Permission System
| العربية | English |
|---------|---------|
| ![صلاحيات المدير] | ![Admin Permissions] |
| - صلاحيات كاملة للمدراء | - Full access for managers |
| - مستخدمون عاديون: صلاحيات محددة | - Regular users: Restricted access |

### 📝 إدارة المهام / Task Management
| العربية | English |
|---------|---------|
| ![إنشاء مهمة] | ![Create Task] |
| - تعيين المهام بشكل جماعي | - Bulk task assignment |
| - تتبع حالة المهام | - Task status tracking |

### 🔗 واجهة برمجة التطبيقات / API
```python
# مثال API / API Example
@app.route('/api/tasks/ar', methods=['GET'])  # العربية
@app.route('/api/tasks/en', methods=['GET'])  # English
