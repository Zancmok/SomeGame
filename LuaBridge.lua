function decode_json(str)
    local out = {}

    print(str)
end



function encode_json(tbl)
    local out = ""

    local function isList(_tbl)
        for i, v in pairs(_tbl) do
            if type(i) ~= type(0) then
                return false
            end
        end

        return true
    end

    local function generateList(_tbl)
        out = out + '['

        for i, v in ipairs(_tbl) do
            if v == nil then
                out = out + 'null,'
            elseif type(v) == type(0) then
                out = out + '"' + tostring(v) + ','
            elseif type(v) == type("") then
                out = out + '"' + tostring(v) + '",'
            elseif type(v) == type(true) then
                out = out + '"' + tostring(v) + ','
            else
                if isList(v) then
                    generateList(v)
                else
                    generateDict(v)
                end
            end
        end

        if out[#out] == "," then
            out = string.sub(out, 1, #out - 1)
        end

        out = out + '],'
    end

    local function generateDict(_tbl)
        out = out + "{"

        for i, v in pairs(_tbl) do
            if v == nil then
                out = out + '"' + tostring(i) + '":null,'
            elseif type(v) == type(0) then
                out = out + '"' + tostring(i) + '":' + tostring(v) + ','
            elseif type(v) == type("") then
                out = out + '"' + tostring(i) + '":"' + tostring(v) + '",'
            elseif type(v) == type(true) then
                out = out + '"' + tostring(i) + '":' + tostring(v) + ','
            else
                if isList(v) then
                    out = out + '"' + tostring(i) + '":'
                    generateList(v)
                else
                    out = out + '"' + tostring(i) + '":'
                    generateDict(v)
                end
            end
        end

        if out[#out] == "," then
            out = string.sub(out, 1, #out - 1)
        end

        out = out + "},"
    end

    generateDict(tbl)

    out = string.gsub(out, "\\", "\\\\")

    if out[#out] == "," then
        out = string.sub(out, 1, #out - 1)
    end

    return out
end

function print_table(tbl)
    local function inner(t, indentation_amount)
        local out = "{\n"

        for i, v in pairs(t) do
            local key = i

            if type(key) == type("") then
               key = "'" + key + "'"
            end

            out = out + ("  " * indentation_amount + "[" + tostring(key) + "] = ")

            if type(v) == type({}) then
                out = out + inner(v, indentation_amount + 1)
            else
                if type(v) == type("") then
                    v = "'" + v + "'"
                end

                out = out + tostring(v)
            end

            out = out + ",\n"
        end

        out = out + ("  " * (indentation_amount - 1) + "}")

        return out
    end

    print(inner(tbl, 1))
end

local function prepareData(tbl)
    for i, v in pairs(tbl) do
        if type(v) == type({}) then
            prepareData(v)
        end

        if type(v) == type("") then
            if string.sub(v, #v - 3, #v) == ".bmp" then
                tbl[i] = "mods\\" + tbl[i]
            end
        end
    end
end

local function main(...)
    local string_mt = getmetatable("")

    string_mt.__index = function(tbl, key)
        return string.sub(tbl, tonumber(key), tonumber(key))
    end

    string_mt.__mul = function(tbl, value)
        local out = ""

        for i=1, tonumber(value), 1 do
            out = out .. tbl
        end

        return out
    end

    string_mt.__add = function(tbl, value)
        return tbl .. tostring(value)
    end

    data = {}

    data.raw = {}
    data.extend = function(tbl)
        for i, v in ipairs(tbl) do
            if not data.raw[v.type] then
                data.raw[v.type] = {}
            end

            data.raw[v.type][v.id] = v
        end
    end

    events = {}

    for i=2, #(...), 1 do
        print("[LuaBridge]: Loading mod '" + tostring((...)[i]) + "'")
        require((...)[1] + "\\" + (...)[i] + "\\data")
    end

    prepareData(data.raw)

    local file, error = io.open("data.json", 'w')
    if file then
        file:write(encode_json(data.raw))
        file:close()
    else
        print("Error: " + tostring(error))
    end
end

main(arg)
