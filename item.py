


class Item:
   def __init__(self, name, zone, ac, wt, Istr, sta, agi, dex, Iint, wis, hp, mana, mr, fr, cr, pr, dr, Iclass, race, lore, magic, href, nodrop, slot, raid):
      self.mName = name
      self.mZone = zone
      self.mAc = ac
      self.mWt = wt
      self.mStr = Istr
      self.mSta = sta
      self.mAgi = agi
      self.mDex = dex
      self.mInt = Iint
      self.mWis = wis
      self.mHp = hp
      self.mMana = mana
      self.mMr = mr
      self.mFr = fr
      self.mCr = cr
      self.mPr = pr
      self.mDr = dr
      self.mClass = Iclass
      self.mRace = race
      self.mLore = lore
      self.mMagic = magic
      self.mHref = href
      self.mNoDrop = nodrop
      self.mSlot = slot
      self.mRaid = raid

   def getName(self):
      return self.mName
   def setName(self, name):
      self.mName = name

   def getZone(self):
      return self.mZone
   def setZone(self, zone):
      self.mZone = zone

   def getAc(self):
      return self.mAc
   def setAc(self, ac):
      self.mAc = ac

   def getWt(self):
      return self.mWt
   def setWt(self, wt):
      self.mWt = wt

   def getStr(self):
      return self.mStr
   def setStr(self, Istr):
      self.mStr = Istr

   def getSta(self):
      return self.mSta
   def setSta(self, sta):
      self.mSta = sta

   def getAgi(self):
      return self.mAgi
   def setAgi(self, agi):
      self.mAgi = agi

   def getDex(self):
      return self.mDex
   def setDex(self, dex):
      self.mDex = dex

   def getInt(self):
      return self.mInt
   def setInt(self, Iint):
      self.mInt = Iint

   def getWis(self):
      return self.mWis
   def setWis(self, wis):
      self.mWis = wis

   def getHp(self):
      return self.mHp
   def setHp(self, hp):
      self.mHp = hp

   def getMana(self):
      return self.mMana
   def setMana(self, mana):
      self.mMana = mana

   def getMr(self):
      return self.mMr
   def setMr(self, mr):
      self.mMr = mr

   def getFr(self):
      return self.mFr
   def setFr(self, fr):
      self.mFr = fr

   def getCr(self):
      return self.mCr
   def setCr(self, cr):
      self.mCr = cr

   def getPr(self):
      return self.mPr
   def setPr(self, pr):
      self.mPr = pr

   def getDr(self):
      return self.mDr
   def setDr(self, dr):
      self.mDr = dr

   def getClass(self):
      return self.mClass
   def setClass(self, Iclass):
      self.mClass = Iclass

   def getRace(self):
      return self.mRace
   def setRace(self, race):
      self.mRace = race

   def getMagic(self):
      return self.mMagic
   def setMagic(self, magic):
      self.mMagic = magic

   def getHref(self):
      return self.mHref
   def setHref(self, href):
      self.mHref = href

   def getNoDrop(self):
      return self.mNoDrop
   def setNoDrop(self, nodrop):
      self.mNoDrop = nodrop

   def getSlot(self):
      return self.mSlot
   def setSlot(self, slot):
      self.mSlot = slot

   def getRaid(self):
      return self.mRaid
   def setRaid(self, raid):
      self.mRaid = raid