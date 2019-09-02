## 系说明

- 房间 (room) 和资产 (asset) 是多对多的关系, 所以有 changes 这个中间实体. 一个房间有多个资产, 一个资产在不同时间段内可能在不同的房间
- changes 和 assets 之间不用实际的外键连接, 只有隐性的外键关系. 可以通过提交修改的资产编号查到 asset_id, 然后再加到 changes 表中. 

## 表说明

- assetManager: 哪个负责人负责哪些资产的表
- users: 各级管理员和普通人的表
- 

## 数据字典

### userProfile

| 字段      | 说明                        |
| --------- | --------------------------- |
| is_staff  | 值为1时才能登录后台管理系统 |
| is_active | 如果为0表示用户已经被删除   |
|           |                             |
|           |                             |

### assetManager

| 字段      | 说明                             |
| --------- | -------------------------------- |
| status    | 资产状态(使用, 维修, 损坏, 报废) |
| change_id | xiu'gai                          |
|           |                                  |
|           |                                  |

### changes

| 字段         | 说明                       |
| ------------ | -------------------------- |
| status       | 修改资产状态               |
| asset_number | 隐式外键                   |
| manager_id   | 审核的人                   |
| is_approved  | 是否通过审核               |
| summit_id    | 提交变更申请的人的 user_id |

## 一些查询逻辑

- 查询一个部门的所有资产: 查询部门的所有负责人 -> 所有负责人负责的所有资产
- 查询一个资产的所有历史移动: 在 assets 表中查得资产的最近更新 change_id, 通过 change_id 在 changes 表中不断查到 last_change_id, 直到 last_change_id 为空, 得到所有历史记录. 使用changes 表中的 room_id 在 rooms 表中查询可得到具体的地址