import discord
import asyncio
import time
import sys
global voice
global player
global link

client = discord.Client()

def is_me(m):
    return m.author == client.user
def nukeable(m):
	return m.content.startswith('!') 
@client.event
async def on_ready():
	print("Whale cum to WhaleBot")
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	await client.change_presence(game=discord.Game(name='Ceasing Resistance'))
	channel = "370019624168849408"
	voice = await client.join_voice_channel(client.get_channel(channel))
	await voice.disconnect()
    
@client.event
async def on_message(message):
	global voice
	global player
	global isPlaying
	global link
	textChannel = message.channel
	voiceChannel = message.author.voice_channel
	author = str(message.author)
	if "supercharger" in message.content.lower():
		await client.delete_message(message)
		#await client.send_message(message.channel, '***CEASE YOUR RESISTANCE***')
		voice = await client.join_voice_channel(voiceChannel)
		player = voice.create_ffmpeg_player('orisa.mp3')
		#player = await voice.create_ytdl_player("https://www.youtube.com/watch?v=J6CYcVch7rs")
		#player = await play_file("orisa.mp3")
		player.volume = 0.10
		player.start()
		time.sleep(3)
		await voice.disconnect()
	if message.content.startswith('!leave'):
		await client.delete_message(message)
		await voice.disconnect()
	if message.content.startswith('!nuke'):
		await client.delete_message(message)
		await client.purge_from(textChannel, limit=1000, check=is_me)
		await client.purge_from(textChannel, limit=1000, check=nukeable)
	if message.content.startswith('!pause'):
		await client.delete_message(message)
		player.pause()
	if message.content.startswith('!play'):
		await client.delete_message(message)
		player.resume()
	if message.content.startswith('!join'):
		await client.delete_message(message)
		voice = await client.join_voice_channel(voiceChannel)

	if message.content.startswith('!again'):
		await client.delete_message(message)
		voice = await client.join_voice_channel(voiceChannel)
		player = await voice.create_ytdl_player(link)
		currentSong = "Now Playing: "+player.title
		await client.send_message(textChannel, currentSong)
		player.volume = 0.5
		player.start()
		time.sleep(player.duration)
		await voice.disconnect()
	if message.content.startswith('!https://www.yo'):
		await client.delete_message(message)
		link = message.content
		link = link.replace("!",'')
		voice = await client.join_voice_channel(voiceChannel)
		player = await voice.create_ytdl_player(link)
		currentSong = "Now Playing: "+player.title+" "+link+" By request of: @"+author
		await client.send_message(textChannel, currentSong)
		player.volume = 0.5
		player.start()
		time.sleep(player.duration)
		await voice.disconnect()
	if message.content.startswith('!quitoverride'):
		await client.delete_message(message)
		sys.exit()

client.run('MzcxNzkzMDc0ODY4OTc3NjY3.DM60hg.7H_5H8yikyOMatgE7RpJ6jGf_JU')
