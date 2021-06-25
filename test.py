members = ["mName", "mZone", "mAc", "mWt", "mStr", "mSta", "mAgi", "mDex", "mInt", "mWis", "mHp", "mMana", "mMr", "mFr", "mCr", "mPr", "mDr", "mClass", "mRace", "mMagic", "mHref", "mNoDrop", "mSlot", "mRaid"]

def main():
    for i in range(len(members)):
        print("def get" + members[i][1:] + "(self):")
        print("   return self."+members[i])
        print("def set" + members[i][1:] + "(self, "+members[i][1:].lower()+"):")
        print("   self."+members[i]+ " = "+ members[i][1:].lower())
        print()


main()