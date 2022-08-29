import discord
from discord.ext import commands


class Logger(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.channel = None

    @commands.Cog.listener("on_ready")
    async def on_ready(self):
        self.channel = self.bot.get_channel(739087150109879552)

    @commands.Cog.listener("on_member_join")
    async def join_logger(self, member: discord.Member):
        """
        Sendet ein Embed mit der Log-Nachricht in den Log-Channel, wenn ein neues Mitglied in dem Server beitritt.
        :param member: Beigetretenes Mitglied
        :return:
        """
        embed = discord.Embed(title="Neues Mitglied",
                              description=f"{member.mention} ist dem Server beigetreten!\n"
                                          f"Erstellt am <t:{member.created_at.timestamp()}:F> (<t:"
                                          f"{member.created_at.timestamp()}:R>.",
                              colour=discord.Colour.green())
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"{member} ({member.id})")
        await self.channel.send(embed=embed)

    @commands.Cog.listener("on_member_remove")
    async def leave_logger(self, member: discord.Member):
        """
        Sendet ein Embed mit der Log-Nachricht in den Log-Channel, wenn ein Mitglied den Server verlässt.
        :param member: Beigetretenes Mitglied
        :return:
        """
        embed = discord.Embed(title="Server verlassen",
                              description=f"{member} hat den Server verlassen!\n"
                                          f"Beigetreten am <t:{member.joined_at.timestamp()}:F> (<t:"
                                          f"{member.joined_at.timestamp()}:R>.",
                              colour=discord.Colour.red())
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"{member} ({member.id})")
        await self.channel.send(embed=embed)

    @commands.Cog.listener("on_invite_create")
    async def invite_logger(self, invite: discord.Invite):
        """
        Sendet ein Embed mit der Log-Nachricht in den Log-Channel, wenn ein neuer Invite Link erstellt wurde.
        :param invite: Erstellter Link
        :return:
        """
        embed = discord.Embed(title="Neuer Invite Link",
                              description=f"{invite.inviter.mention} hat einen neuen Link erstellt.\n"
                                          f"Link: {invite.url}",
                              colour=discord.Colour.blue())
        embed.set_footer(text=f"{invite.inviter} ({invite.inviter.id})")
        await self.channel.send(embed=embed)

    @commands.Cog.listener("on_message_delete")
    async def message_delete_logger(self, message: discord.Message):
        """
        Sendet ein Embed mit der Log-Nachricht in den Log-Channel, wenn eine Nachricht gelöscht wurde.
        :param message: Gelöschte Nachricht
        :return:
        """
        embed = discord.Embed(title="Nachricht gelöscht",
                              description=f"{message.author.mention} hat eine Nachricht gelöscht.\n"
                                          f"Nachricht: {message.content}",
                              colour=discord.Colour.red())
        embed.set_footer(text=f"{message.author} ({message.author.id})")
        await self.channel.send(embed=embed)

    @commands.Cog.listener("on_message_edit")
    async def message_edit_logger(self, before: discord.Message, after: discord.Message):
        """
        Sendet ein Embed mit der Log-Nachricht in den Log-Channel, wenn eine Nachricht bearbeitet wurde.
        :param before: Vorherige Nachricht
        :param after: Neue Nachricht
        :return:
        """
        embed = discord.Embed(title="Nachricht bearbeitet",
                              description=f"{before.author.mention} hat eine Nachricht bearbeitet.\n"
                                          f"**Vorher:**\n{before.content}\n"
                                          f"**Nachher:**\n{after.content}",
                              colour=discord.Colour.blue())
        embed.set_footer(text=f"{before.author} ({before.author.id})")
        await self.channel.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Logger(bot))