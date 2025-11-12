import asyncio

async def handle_client(reader, writer):
    while data := await reader.read(1024):
        writer.write(data)
        await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 9092)
    print("Asyncio server running on port 9092")
    async with server:
        await server.serve_forever()

asyncio.run(main())

