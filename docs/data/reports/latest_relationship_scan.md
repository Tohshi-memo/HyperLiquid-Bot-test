# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T22:42:19.386447+00:00`
- Price records: `672`
- Market context records: `7715`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `3.5955` n `132` status `ready` deltaP `19.396` edge `0.3045` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `1.1161` n `133` status `ready` deltaP `13.4573` edge `0.0474` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `1.116` n `133` status `ready` deltaP `14.9562` edge `0.1651` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.7127` n `133` status `ready` deltaP `8.6569` edge `0.1134` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.6939` n `133` status `ready` deltaP `9.0971` edge `0.0831` maxDD `-4.2072`
- `market_context_high->equity_4h` score `0.6739` n `133` status `ready` deltaP `2.4281` edge `0.2615` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.4371` n `133` status `ready` deltaP `9.5453` edge `0.0158` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1893` n `133` status `ready` deltaP `3.9789` edge `0.0325` maxDD `-1.4603`
- `market_context_high->fx_24h` score `0.041` n `132` status `ready` deltaP `13.3381` edge `0.0251` maxDD `-3.0343`
- `market_context_high->commodity_4h` score `-0.1653` n `133` status `ready` deltaP `4.4814` edge `0.0157` maxDD `-1.0817`
- `market_context_high->commodity_1h` score `-0.1772` n `133` status `ready` deltaP `3.6951` edge `0.0065` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1968` n `133` status `ready` deltaP `11.323` edge `0.0451` maxDD `-1.3325`
- `market_context_high->metal_24h` score `-0.4467` n `133` status `ready` deltaP `3.202` edge `0.1505` maxDD `-2.3927`
- `market_context_high->fx_1h` score `-0.5432` n `133` status `ready` deltaP `-0.8275` edge `-0.001` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8531` n `133` status `ready` deltaP `1.4171` edge `0.0198` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4393` n `133` status `ready` deltaP `1.443` edge `0.0759` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5703` n `133` status `ready` deltaP `-5.2321` edge `-0.0036` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7525` n `132` status `ready` deltaP `5.6858` edge `-0.0256` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.1349` n `133` status `ready` deltaP `-0.825` edge `-0.1134` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.5918` n `132` status `ready` deltaP `-18.4537` edge `0.001` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
