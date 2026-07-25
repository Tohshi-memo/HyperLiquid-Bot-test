# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T01:07:31.552750+00:00`
- Price records: `672`
- Market context records: `7829`
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

- `market_context_high->equity_24h` score `9.5634` n `132` status `ready` deltaP `28.5507` edge `0.7408` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.3599` n `133` status `ready` deltaP `5.9449` edge `0.326` maxDD `-6.9701`
- `market_context_high->metal_24h` score `1.3295` n `133` status `ready` deltaP `12.3246` edge `0.2377` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `1.2422` n `133` status `ready` deltaP `15.1086` edge `0.1746` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0753` n `133` status `ready` deltaP `13.1579` edge `0.046` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.8823` n `133` status `ready` deltaP `8.9618` edge `0.1255` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.8304` n `132` status `ready` deltaP `25.2187` edge `0.0471` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7454` n `133` status `ready` deltaP `8.046` edge `0.0944` maxDD `-4.2072`
- `market_context_high->commodity_24h` score `0.6406` n `132` status `ready` deltaP `17.6443` edge `0.0941` maxDD `-7.0012`
- `market_context_high->commodity_4h` score `0.4371` n `133` status `ready` deltaP `8.4569` edge `0.0394` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3254` n `133` status `ready` deltaP `8.0438` edge `0.0165` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2755` n `133` status `ready` deltaP `5.1765` edge `0.0317` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0545` n `133` status `ready` deltaP `5.647` edge `0.0128` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.0705` n `133` status `ready` deltaP `12.8521` edge `0.0511` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3738` n `133` status `ready` deltaP `1.1245` edge `0.0001` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8495` n `133` status `ready` deltaP `1.4171` edge `0.0201` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.3315` n `132` status `ready` deltaP `-6.531` edge `0.0831` maxDD `-2.1544`
- `market_context_high->fx_4h` score `-1.3818` n `133` status `ready` deltaP `-2.3269` edge `0.0012` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.4249` n `133` status `ready` deltaP `1.443` edge `0.0771` maxDD `-1.4368`
- `market_context_high->crypto_alt_24h` score `-2.1219` n `133` status `ready` deltaP `14.7431` edge `0.1592` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
