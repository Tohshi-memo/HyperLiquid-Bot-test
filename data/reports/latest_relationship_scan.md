# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T07:22:25.452971+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4790`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->unknown_4h` score `125.1168` n `37` status `ready` deltaP `-4.7009` edge `10.5025` maxDD `-0.9139`
- `market_context_high->equity_1h` score `3.2928` n `37` status `ready` deltaP `10.8068` edge `0.2483` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.2473` n `37` status `ready` deltaP `35.1434` edge `0.0453` maxDD `-0.0521`
- `market_context_high->index_4h` score `2.0316` n `37` status `ready` deltaP `26.5079` edge `0.0396` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.7815` n `51` status `ready` deltaP `10.2533` edge `0.1022` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.8998` n `51` status `ready` deltaP `7.4935` edge `0.1393` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.8118` n `37` status `ready` deltaP `10.0502` edge `0.0592` maxDD `-3.0172`
- `market_context_high->crypto_alt_1h` score `0.5192` n `37` status `ready` deltaP `11.6969` edge `0.0701` maxDD `-3.1881`
- `market_context_high->fx_1h` score `0.4218` n `37` status `ready` deltaP `7.0724` edge `0.0151` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.3225` n `37` status `ready` deltaP `2.2496` edge `0.0389` maxDD `-0.1621`
- `news_risk_high->index_4h` score `0.3212` n `51` status `ready` deltaP `10.1327` edge `0.0214` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.2155` n `51` status `ready` deltaP `6.0968` edge `0.1538` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.1273` n `37` status `ready` deltaP `9.1682` edge `0.0098` maxDD `-1.7019`
- `news_risk_high->index_1h` score `0.1033` n `54` status `ready` deltaP `8.3056` edge `0.0032` maxDD `-0.2931`
- `news_risk_high->fx_4h` score `0.0927` n `51` status `ready` deltaP `7.2155` edge `0.0074` maxDD `-0.1563`
- `market_context_high->commodity_4h` score `0.0469` n `37` status `ready` deltaP `4.0541` edge `0.0244` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0085` n `37` status `ready` deltaP `2.2496` edge `0.0167` maxDD `-0.6226`
- `news_risk_high->equity_1h` score `-0.0914` n `54` status `ready` deltaP `-0.5046` edge `0.0466` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.152` n `54` status `ready` deltaP `2.3176` edge `0.0036` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.6394` n `37` status `ready` deltaP `22.8618` edge `0.0936` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
