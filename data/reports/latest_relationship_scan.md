# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T08:52:30.928766+00:00`
- Price records: `672`
- Market context records: `7759`
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

- `market_context_high->equity_24h` score `5.7206` n `132` status `ready` deltaP `23.9256` edge `0.4514` maxDD `-6.0681`
- `market_context_high->metal_24h` score `0.9205` n `133` status `ready` deltaP `9.9729` edge `0.2193` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.7768` n `133` status `ready` deltaP `11.5112` edge `0.0321` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.4959` n `132` status `ready` deltaP `20.481` edge `0.0358` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `0.4673` n `133` status `ready` deltaP `12.5172` edge `0.1273` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.3981` n `133` status `ready` deltaP `1.9694` edge `0.2292` maxDD `-6.9701`
- `market_context_high->equity_1h` score `0.3734` n `133` status `ready` deltaP `7.5955` edge `0.0664` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.3182` n `133` status `ready` deltaP `8.3441` edge `0.0139` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.21` n `133` status `ready` deltaP `6.8276` edge `0.0837` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `-0.047` n `133` status `ready` deltaP `3.0807` edge `0.0188` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `-0.0981` n `133` status `ready` deltaP `4.4814` edge `0.0213` maxDD `-1.0817`
- `market_context_high->commodity_1h` score `-0.1124` n `133` status `ready` deltaP `4.2957` edge `0.0079` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.26` n `133` status `ready` deltaP `10.5585` edge `0.0421` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.4495` n `133` status `ready` deltaP `0.2236` edge `-0.0002` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8687` n `133` status `ready` deltaP `1.4171` edge `0.0185` maxDD `-0.6936`
- `market_context_high->commodity_24h` score `-1.4268` n `132` status `ready` deltaP `6.3827` edge `-0.0031` maxDD `-7.0012`
- `market_context_high->fx_4h` score `-1.4769` n `133` status `ready` deltaP `-3.8559` edge `-0.0008` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5073` n `133` status `ready` deltaP `0.8332` edge `0.0743` maxDD `-1.4368`
- `market_context_high->index_24h` score `-2.1603` n `132` status `ready` deltaP `-14.9694` edge `0.0331` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.3075` n `133` status `ready` deltaP `-1.8729` edge `-0.1208` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
