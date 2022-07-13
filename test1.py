import unittest

class Test_test1(unittest.TestCase):
    def test_A(self):
        arr = [
'n = {id} ,Mod = "Mod/Npc/Human/Npc1/lxy.FBX", CHName = "[color=#7FFFD4]李逍遥[/color]",Role = "Spr/Npc/lxy.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc1/hy.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc1/x.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc1/jl.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc1/ws.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc1/zle.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc1/XM.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc1/anu.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc1/lyr.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc1/llb.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc1/lly.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc1/wyy.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc1/mcl.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc1/yj.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc2/bbl.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc2/ganyu.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc2/hutao.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc2/keli.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc2/y.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc2/YX.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc2/cp.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc2/JG.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc2/SL.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc3/Aqua.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc3/Megumin.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc3/Darkness.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc4/zx.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc4/lk.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc4/xj.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
'n = {id} ,Mod = "Mod/Npc/Human/Npc4/hlk/lk.FBX", CHName = "[color=#7FFFD4]{id}[/color]",Role = "Spr/H/{id}.png"',
            ]
        menu_data = '<li><Display>{id}</Display><OKResult>me:AddModifier("Female_Model_Change_{id}", false);</OKResult></li>'
        xml_data = '<Modifier Name="Female_Model_Change_{id}" Type="Normal"><ModScale>0.3</ModScale><MaxStack>0</MaxStack><Duration>1</Duration><Display>0</Display><Desc>{id}</Desc><LuaClassName>Female_Model_Change_Lua_2112</LuaClassName></Modifier>'
        for i in range(1, len(arr)+1):
            print(arr[i-1].format(id=i))
        for i in range(1, len(arr)+1):
            print(menu_data.format(id=i))
        for i in range(1, len(arr)+1):
            print(xml_data.format(id=i))
        
        self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
