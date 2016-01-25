import discord
import subprocess
import youtube_dl
####For  getting DJ up and running! WIP###
subprocess.Popen("run.py", shell=True)

#Server details, channels ID's, Bot Login details####
server_id = 134475106515681281
client = discord.Client()
client.login('user', 'pass')

#Channel ID's for use with discord.Channel()###
general_channel = 134475106515681281 ###should be == to server_id if default!
notification_channel = 140236349763485706
gamingpictures_channel =135156847454715904

######Commands and Responses, WIP####
ggl = "https://goo.gl/"
video_command = ["!HotlineBoom","!Benji","!Xyzzy", "!wow" ]
response_video = ["Y7ilii", "https://youtu.be/s3FXqil1vL8?t=1s"]
text_command = ["!SecHelp"]
response_text = ["For a list of video commands type !SecVideo, for images !SecImage "]
image_command = ["!Sean", "!Gio", "!Lou" ]
response_image = ["https://goo.gl/erhVSI", "http://www.diet-blog.com/wp-content/uploads/SubwaySandwichBIG.jpg", "http://www.costumemaze.com/images/images_big/70217-SUPER-JUMBO-AFRO.jpg" ]

######Youtube player variables and definitions##
##voice = yield from client.join_voice_channel(channel)



@client.event
def on_member_join(member):
    server = member.server
    send_message(discord.Object(general_channel), 'Welcome {0} to {1.name}!'.format(member.mention(), server))

@client.event
def on_message(msg):
    if msg.content.startswith("!HotlineBoom"):
        client.send_message(msg.channel, ggl+"Y7ilii")
    if msg.content.startswith("!Benji"):
        client.send_message(msg.channel, "https://youtu.be/s3FXqil1vL8?t=1s")

        #Auto play WIP
    #if msg.content.startswith("!Test"):
        #player = youtube_dl.create_ytdl_player(response_video[1])
        #player.start()

    if msg.content.startswith(text_command[0]):
        client.send_message(msg.author, response_text[0] )
    if msg.content.startswith("!Sean"):
        client.send_message(msg.channel, ggl+"erhVSI")
    if msg.content.startswith("!Gio"):
        client.send_message(msg.channel, "http://www.diet-blog.com/wp-content/uploads/SubwaySandwichBIG.jpg")
    if msg.content.startswith("!Lou"):
        client.send_message(msg.channel, ggl+"YZklt")
    if msg.content.startswith("!Xyzzy"):
        client.send_message(msg.channel, ggl+"NHk10r")
    if msg.content.startswith("!wow"):
        client.send_message(msg.channel, ggl+"TsGqG8")

#Status variables#

offline = discord.Member().self.status('offline')  # status[0]
online = discord.Member().status(online) # status[1]
idle = discord.Member().status(idle) # status [2]
status = [offline,online,idle]

@client.event
def on_member_update(before, after):
    if before == status[2] or before == status[1] and after == status[0] :
        client.send_message(discord.Object(notification_channel),discord.Member(id)+" is now offline!")
    if before == status[0] or before == status[2] and after == status[1]:
        client.send_message(discord.Object(notification_channel),Member+" is now online!")
    if before == status[0] or before == status[1] and after == status[2]:
        client.send_message(discord.Object(notification_channel),Member+" is now idle!")

@client.event
def on_ready():
    #client.send_message(discord.Object(notification_channel), "The secretary is now online, type !SecHelp for the basic chat commands" )
    print('Logged in as')
    print(client.user .name)
    print(client.user .id)
    print('Discord version:'+discord.__version__)
    print('------')

client.run()
