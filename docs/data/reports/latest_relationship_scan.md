# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T23:37:26.153736+00:00`
- Price records: `672`
- Market context records: `7719`
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

- `market_context_high->equity_24h` score `3.5667` n `132` status `ready` deltaP `19.396` edge `0.3021` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `1.0381` n `133` status `ready` deltaP `13.1579` edge `0.0429` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `0.9847` n `133` status `ready` deltaP `14.4989` edge `0.1572` maxDD `-6.7444`
- `market_context_high->equity_1h` score `0.6339` n `133` status `ready` deltaP `8.7968` edge `0.0801` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.6166` n `133` status `ready` deltaP `8.5045` edge `0.1064` maxDD `-3.9374`
- `market_context_high->equity_4h` score `0.5477` n `133` status `ready` deltaP `1.8165` edge `0.2494` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3974` n `133` status `ready` deltaP `9.0949` edge `0.0155` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1257` n `133` status `ready` deltaP `3.8292` edge `0.0282` maxDD `-1.4603`
- `market_context_high->fx_24h` score `0.0835` n `132` status `ready` deltaP `14.035` edge `0.0259` maxDD `-3.0343`
- `market_context_high->commodity_4h` score `-0.18` n `133` status `ready` deltaP `4.3285` edge `0.0155` maxDD `-1.0817`
- `market_context_high->commodity_1h` score `-0.1892` n `133` status `ready` deltaP `3.5449` edge `0.0065` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2442` n `133` status `ready` deltaP `10.7114` edge `0.0431` maxDD `-1.3325`
- `market_context_high->metal_24h` score `-0.3638` n `133` status `ready` deltaP `3.5492` edge `0.1551` maxDD `-2.3927`
- `market_context_high->fx_1h` score `-0.5552` n `133` status `ready` deltaP `-0.9776` edge `-0.001` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8423` n `133` status `ready` deltaP `1.5668` edge `0.0197` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4989` n `133` status `ready` deltaP `0.8332` edge `0.075` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5862` n `133` status `ready` deltaP `-5.5379` edge `-0.0036` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7489` n `132` status `ready` deltaP `5.6858` edge `-0.0253` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.1577` n `133` status `ready` deltaP `-0.9747` edge `-0.1143` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.5973` n `132` status `ready` deltaP `-18.4537` edge `0.0003` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
