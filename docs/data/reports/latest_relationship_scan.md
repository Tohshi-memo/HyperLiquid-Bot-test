# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T13:52:29.345341+00:00`
- Price records: `672`
- Market context records: `7780`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `7.0206` n `132` status `ready` deltaP `27.41` edge `0.5365` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.4083` n `133` status `ready` deltaP `13.4451` edge `0.2368` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.9434` n `133` status `ready` deltaP `12.7088` edge `0.038` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.7148` n `132` status `ready` deltaP `23.7911` edge `0.0418` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `0.6299` n `133` status `ready` deltaP `12.9745` edge `0.1378` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.552` n `133` status `ready` deltaP `2.2752` edge `0.2469` maxDD `-6.9701`
- `market_context_high->crypto_alt_4h` score `0.4388` n `133` status `ready` deltaP `7.4374` edge `0.0987` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.4202` n `133` status `ready` deltaP `7.4454` edge `0.0713` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.2858` n `133` status `ready` deltaP `7.8937` edge `0.0142` maxDD `-0.7743`
- `market_context_high->commodity_4h` score `0.2111` n `133` status `ready` deltaP `6.622` edge `0.0328` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.1148` n `133` status `ready` deltaP `4.1286` edge `0.0253` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.0475` n `133` status `ready` deltaP `4.7461` edge `0.0103` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2578` n `133` status `ready` deltaP `10.4056` edge `0.0434` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.363` n `133` status `ready` deltaP `1.2746` edge `0.0` maxDD `-0.4331`
- `market_context_high->commodity_24h` score `-0.7532` n `132` status `ready` deltaP `9.867` edge `0.0298` maxDD `-7.0012`
- `market_context_high->metal_1h` score `-0.9465` n `133` status `ready` deltaP `0.5189` edge `0.018` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3738` n `133` status `ready` deltaP `-2.174` edge `0.0012` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.631` n `133` status `ready` deltaP `-0.2339` edge `0.0711` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.8254` n `132` status `ready` deltaP `-11.4851` edge `0.0528` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.1518` n `133` status `ready` deltaP `-0.3759` edge `-0.1178` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
