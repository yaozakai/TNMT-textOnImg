import io

from PIL import Image, ImageDraw, ImageFont


def insertNamesToImage(image_data, bracket_data, font_data, champion_font_data):
    offset = 20
    # Open the image using PIL
    imageLocal = Image.open(io.BytesIO(image_data))
    I1 = ImageDraw.Draw(imageLocal)
    # Custom font style and font size
    myFont = ImageFont.truetype(io.BytesIO(font_data), 16)
    myFontLrg = ImageFont.truetype(io.BytesIO(font_data), 22)
    myFontXLrg = ImageFont.truetype(io.BytesIO(font_data), 26)
    championFont = ImageFont.truetype(io.BytesIO(champion_font_data), 32)
    pickedData = bracket_data['pickData']
    for region in pickedData:
        skipProcess = False

        if region == 'South':
            y_coord = 16
            x_coord = 20
        elif region == 'East':
            y_coord = 545
            x_coord = 20
        elif region == 'MidWest':
            y_coord = 16
            x_coord = 1727
        elif region == 'West':
            y_coord = 550
            x_coord = 1750
        elif region == 'championshipLoser':
            skipProcess = True
            # y_coord = 545
            # x_coord = 1780
            # I1.text((x_coord, y_coord), pickedData[region], font=myFontLrg, fill=(0, 0, 0))
            # (left, top, right, bottom) = myFont.getbbox(pickedData[region])
        elif region == 'championshipWinner':
            skipProcess = True
            y_coord = 335
            x_coord = 960
            length = championFont.getlength(pickedData[region])
            I1.text((x_coord - length/2, y_coord), pickedData[region], font=championFont,
                    fill=(0, 0, 0))
            # (left, top, right, bottom) = myFont.getbbox(pickedData[region])
        elif region == 'championshipScore':
            skipProcess = True
            y_coord = 630
            x_coord = 820
            length = championFont.getlength(pickedData[region]['teamAScore'])
            I1.text((x_coord - length/2, y_coord), pickedData[region]['teamAScore'], font=championFont,
                    fill=(0, 0, 0))
            y_coord += 60
            length = championFont.getlength(pickedData[region]['teamBScore'])
            I1.text((x_coord - length/2, y_coord), pickedData[region]['teamBScore'], font=championFont,
                    fill=(0, 0, 0))
        elif region == 'finalFour':
            skipProcess = True
            y_coord = 490
            x_coord = 633
            first = True
            for match_up in pickedData[region][0]['games']:
                if first:
                    I1.text((x_coord, y_coord), match_up['teamA'], font=myFontLrg, fill=(0, 0, 0))
                    # (left, top, right, bottom) = myFont.getbbox(match_up['teamA'])
                    y_coord += 60
                    I1.text((x_coord, y_coord), match_up['teamB'], font=myFontLrg, fill=(0, 0, 0))
                    # (left, top, right, bottom) = myFont.getbbox(match_up['teamB'])
                    y_coord = 635
                    x_coord = 880
                    # length = myFontXLrg.getlength(match_up['winner'])
                    I1.text((x_coord, y_coord), match_up['winner'], font=myFontXLrg,
                            fill=(0, 0, 0))
                    first = False
                else:
                    lengthB = myFontLrg.getlength(match_up['teamB'])
                    max_length = myFontLrg.getlength(match_up['teamA'])
                    if lengthB > max_length:
                        max_length = lengthB
                    y_coord = 490
                    x_coord = 1175
                    length = myFontLrg.getlength(match_up['teamA'])
                    I1.text((x_coord + max_length - length, y_coord), match_up['teamA'], font=myFontLrg,
                            fill=(0, 0, 0))
                    # (left, top, right, bottom) = myFontLrg.getbbox(match_up['teamA'])
                    y_coord += 60
                    length = myFontLrg.getlength(match_up['teamB'])
                    I1.text((x_coord + max_length - length, y_coord), match_up['teamB'], font=myFontLrg,
                            fill=(0, 0, 0))
                    y_coord = 695
                    x_coord = 880
                    # length = myFontXLrg.getlength(match_up['winner'])
                    I1.text((x_coord, y_coord), match_up['winner'], font=myFontXLrg,
                            fill=(0, 0, 0))
                    y_coord = 500

        if not skipProcess:
            for game_round in pickedData[region]:
                first = True
                max_length = 0
                # if west or midwest we must right align
                if region == 'West' or 'MidWest':
                    for match_up in game_round['games']:
                        if myFont.getlength(match_up['teamB']) > myFont.getlength(match_up['teamA']):
                            length = myFont.getlength(match_up['teamB'])
                        else:
                            length = myFont.getlength(match_up['teamA'])
                        if length > max_length:
                            max_length = length
                if game_round['round'] == 1:
                    max_length_seed = 0
                    for match_up in game_round['games']:
                        if myFont.getlength(match_up['teamBSeedNum']) > myFont.getlength(match_up['teamASeedNum']):
                            seed_length = myFont.getlength(match_up['teamBSeedNum'])
                        else:
                            seed_length = myFont.getlength(match_up['teamASeedNum'])
                        if seed_length > max_length_seed:
                            max_length_seed = seed_length

                for match_up in game_round['games']:
                    # round 1 handler
                    if game_round['round'] == 1:
                        if region == 'South' or region == 'East':
                            I1.text((x_coord, y_coord), match_up['teamASeedNum'], font=myFont, fill=(0, 0, 0))
                            I1.text((x_coord + offset, y_coord), match_up['teamA'], font=myFont, fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamA'])
                            y_coord += 28 + top
                            I1.text((x_coord, y_coord), match_up['teamBSeedNum'], font=myFont, fill=(0, 0, 0))
                            I1.text((x_coord + offset, y_coord), match_up['teamB'], font=myFont, fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamB'])
                            y_coord += 28 + top
                        else:
                            length = myFont.getlength(match_up['teamASeedNum'])
                            I1.text((x_coord + max_length - length + 10, y_coord), match_up['teamASeedNum'], font=myFont,
                                    fill=(0, 0, 0))
                            length = myFont.getlength(match_up['teamA'])
                            I1.text((x_coord + max_length - length - offset/2, y_coord), match_up['teamA'], font=myFont,
                                    fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamA'])
                            y_coord += 28 + top
                            length = myFont.getlength(match_up['teamBSeedNum'])
                            I1.text((x_coord + max_length - length + 10, y_coord), match_up['teamBSeedNum'], font=myFont,
                                    fill=(0, 0, 0))
                            length = myFont.getlength(match_up['teamB'])
                            I1.text((x_coord + max_length - length - offset/2, y_coord), match_up['teamB'], font=myFont,
                                    fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamB'])
                            y_coord += 28 + top
                    elif game_round['round'] == 2:
                        if first:
                            if region == 'East' or region == 'West':
                                y_coord = 577
                            else:
                                y_coord = 49
                            first = False
                        if region == 'South' or region == 'East':
                            x_coord = 235
                            I1.text((x_coord, y_coord), match_up['teamA'], font=myFont, fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamA'])
                            y_coord += 28 + top
                            I1.text((x_coord, y_coord), match_up['teamB'], font=myFont, fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamB'])
                            y_coord += 28 + top + 66
                        else:
                            if region == 'West':
                                x_coord = 1570
                            else:
                                x_coord = 1605
                            length = myFont.getlength(match_up['teamA'])
                            I1.text((x_coord + max_length - length, y_coord), match_up['teamA'], font=myFont,
                                    fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamA'])
                            y_coord += 28 + top
                            length = myFont.getlength(match_up['teamB'])
                            I1.text((x_coord + max_length - length, y_coord), match_up['teamB'], font=myFont,
                                    fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamB'])
                            y_coord += 28 + top + 66
                    elif game_round['round'] == 3:
                        if first:
                            if region == 'East':
                                y_coord = 650
                            elif region == 'West':
                                y_coord = 649
                            elif region == 'MidWest':
                                y_coord = 118
                            else:
                                y_coord = 120
                            first = False
                        if region == 'South' or region == 'East':
                            x_coord = 444
                            I1.text((x_coord, y_coord), match_up['teamA'], font=myFont, fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamA'])
                            y_coord += 28 + top
                            I1.text((x_coord, y_coord), match_up['teamB'], font=myFont, fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamB'])
                            y_coord += 230
                        else:
                            if region == 'MidWest':
                                x_coord = 1410
                            else:
                                x_coord = 1360

                            length = myFont.getlength(match_up['teamA'])
                            I1.text((x_coord + max_length - length, y_coord), match_up['teamA'], font=myFont,
                                    fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamA'])
                            y_coord += 28 + top
                            length = myFont.getlength(match_up['teamB'])
                            I1.text((x_coord + max_length - length, y_coord), match_up['teamB'], font=myFont,
                                    fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamB'])
                            y_coord += 232
                    elif game_round['round'] == 4:
                        if first:
                            if region == 'East' or region == 'West':
                                y_coord = 777
                            else:
                                y_coord = 247
                            first = False
                        if region == 'South' or region == 'East':
                            x_coord = 633

                            I1.text((x_coord, y_coord), match_up['teamA'], font=myFont, fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamA'])
                            y_coord += 28 + top
                            I1.text((x_coord, y_coord), match_up['teamB'], font=myFont, fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamB'])
                            y_coord += 230
                        else:
                            if region == 'MidWest':
                                x_coord = 1230
                            else:
                                x_coord = 1210
                            length = myFont.getlength(match_up['teamA'])
                            I1.text((x_coord + max_length - length, y_coord), match_up['teamA'], font=myFont,
                                    fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamA'])
                            y_coord += 28 + top
                            length = myFont.getlength(match_up['teamB'])
                            I1.text((x_coord + max_length - length, y_coord), match_up['teamB'], font=myFont,
                                    fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamB'])
                            y_coord += 230
                    elif game_round['round'] == 5:
                        x_coord = 633
                        if first:
                            y_coord = 247
                            first = False
                        if region == 'South' or region == 'East':
                            I1.text((x_coord, y_coord), match_up['teamA'], font=myFont, fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamA'])
                            y_coord += 28 + top
                            I1.text((x_coord, y_coord), match_up['teamB'], font=myFont, fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamB'])
                            y_coord += 230
                        else:
                            length = myFont.getlength(match_up['teamA'])
                            I1.text((x_coord + max_length - length, y_coord), match_up['teamA'], font=myFont,
                                    fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamA'])
                            y_coord += 28 + top
                            length = myFont.getlength(match_up['teamB'])
                            I1.text((x_coord + max_length - length, y_coord), match_up['teamB'], font=myFont,
                                    fill=(0, 0, 0))
                            (left, top, right, bottom) = myFont.getbbox(match_up['teamB'])
                            y_coord += 230
    return imageLocal.getdata()
