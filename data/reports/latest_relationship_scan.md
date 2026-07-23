# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T19:37:29.839162+00:00`
- Price records: `672`
- Market context records: `7700`
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

- `market_context_high->equity_24h` score `3.6303` n `132` status `ready` deltaP `19.396` edge `0.3074` maxDD `-6.0681`
- `market_context_high->crypto_major_4h` score `1.3392` n `133` status `ready` deltaP `15.8708` edge `0.1776` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.1281` n `133` status `ready` deltaP `13.4573` edge `0.0484` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.8545` n `133` status `ready` deltaP `8.8093` edge `0.1242` maxDD `-3.9374`
- `market_context_high->equity_4h` score `0.8536` n `133` status `ready` deltaP `3.4984` edge `0.2774` maxDD `-6.9701`
- `market_context_high->equity_1h` score `0.6915` n `133` status `ready` deltaP `8.7968` edge `0.0849` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.3914` n `133` status `ready` deltaP `8.9447` edge `0.016` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1641` n `133` status `ready` deltaP `3.6795` edge `0.0324` maxDD `-1.4603`
- `market_context_high->fx_24h` score `-0.0919` n `132` status `ready` deltaP `11.2475` edge `0.022` maxDD `-3.0343`
- `market_context_high->index_4h` score `-0.0955` n `133` status `ready` deltaP `12.8521` edge `0.0479` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `-0.2325` n `133` status `ready` deltaP `3.0945` edge `0.0059` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.3553` n `133` status `ready` deltaP `2.6465` edge `0.0121` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.4939` n `133` status `ready` deltaP `-0.2269` edge `-0.0009` maxDD `-0.4331`
- `market_context_high->metal_24h` score `-0.6545` n `133` status `ready` deltaP `2.8548` edge `0.1355` maxDD `-2.3927`
- `market_context_high->metal_1h` score `-0.8123` n `133` status `ready` deltaP `1.8662` edge `0.0202` maxDD `-0.6936`
- `market_context_high->unknown_1h` score `-1.2398` n `133` status `ready` deltaP `-0.0765` edge `-0.0438` maxDD `-1.054`
- `market_context_high->metal_4h` score `-1.4223` n `133` status `ready` deltaP `1.5954` edge `0.0763` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5449` n `133` status `ready` deltaP `-4.7734` edge `-0.0034` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7201` n `132` status `ready` deltaP `5.6858` edge `-0.0229` maxDD `-7.0012`
- `market_context_high->unknown_4h` score `-2.2507` n `133` status `ready` deltaP `15.3023` edge `-0.1639` maxDD `-1.7206`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
