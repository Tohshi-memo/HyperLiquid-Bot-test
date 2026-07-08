# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T19:52:30.492702+00:00`
- Price records: `672`
- Market context records: `6118`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `9.5416` n `30` status `ready` deltaP `37.2569` edge `0.5615` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.9278` n `30` status `ready` deltaP `70.3125` edge `0.1919` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2397` n `32` status `ready` deltaP `44.1311` edge `0.0637` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3787` n `32` status `ready` deltaP `28.5928` edge `0.0215` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.2324` n `32` status `ready` deltaP `13.5292` edge `0.1145` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.7693` n `195` status `ready` deltaP `5.8841` edge `0.1166` maxDD `-2.671`
- `news_risk_high->crypto_alt_1h` score `0.6135` n `32` status `ready` deltaP `8.4768` edge `0.0683` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.0386` n `30` status `ready` deltaP `8.7152` edge `0.0241` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.284` n `195` status `ready` deltaP `1.2851` edge `-0.0004` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.4843` n `30` status `ready` deltaP `14.0973` edge `-0.1138` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.713` n `195` status `ready` deltaP `2.7799` edge `0.0088` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7248` n `195` status `ready` deltaP `-1.8394` edge `-0.0035` maxDD `-0.5708`
- `market_context_high->equity_1h` score `-0.7736` n `195` status `ready` deltaP `-0.2595` edge `0.0141` maxDD `-4.2573`
- `news_risk_high->metal_1h` score `-0.8096` n `32` status `ready` deltaP `-3.4431` edge `-0.0311` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8799` n `195` status `ready` deltaP `1.9415` edge `-0.0064` maxDD `-2.0564`
- `market_context_high->index_4h` score `-0.9594` n `195` status `ready` deltaP `0.7841` edge `0.0182` maxDD `-1.381`
- `market_context_high->crypto_alt_1h` score `-0.9624` n `195` status `ready` deltaP `3.4608` edge `0.0288` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9656` n `195` status `ready` deltaP `4.3145` edge `0.0242` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.1716` n `32` status `ready` deltaP `-10.872` edge `-0.0214` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.3293` n `195` status `ready` deltaP `-3.8047` edge `0.0015` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
