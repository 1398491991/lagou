/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50713
Source Host           : localhost:3306
Source Database       : lagou

Target Server Type    : MYSQL
Target Server Version : 50713
File Encoding         : 65001

Date: 2016-09-24 14:27:36
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for gongsi
-- ----------------------------
DROP TABLE IF EXISTS `gongsi`;
CREATE TABLE `gongsi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company_id` int(11) NOT NULL COMMENT '来自网站的公司唯一标识符',
  `detail` text NOT NULL COMMENT '通过 http://www.lagou.com/gongsi/0-0-0.json post 获取到的',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
