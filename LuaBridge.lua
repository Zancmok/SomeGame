function get_json(path)

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
    events = {}

    for i, v in pairs(...) do
        if i == 0 or i == -1 then
            goto continue
        end

        --print(v)

        ::continue::
    end
end

main(arg)
