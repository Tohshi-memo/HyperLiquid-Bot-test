# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T14:52:29.501445+00:00`
- Price records: `672`
- Market context records: `7784`
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

- `market_context_high->equity_24h` score `7.4795` n `132` status `ready` deltaP `28.1068` edge `0.5701` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.5035` n `133` status `ready` deltaP `14.1395` edge `0.2401` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `1.0585` n `133` status `ready` deltaP `13.1579` edge `0.0446` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `0.8863` n `133` status `ready` deltaP `13.5842` edge `0.1551` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.8498` n `133` status `ready` deltaP `2.8868` edge `0.281` maxDD `-6.9701`
- `market_context_high->fx_24h` score `0.7604` n `132` status `ready` deltaP `24.4879` edge `0.043` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7046` n `133` status `ready` deltaP `8.046` edge `0.091` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.6916` n `133` status `ready` deltaP `8.0471` edge `0.1157` maxDD `-3.9374`
- `market_context_high->index_1h` score `0.3602` n `133` status `ready` deltaP `8.4943` edge `0.0164` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2288` n `133` status `ready` deltaP `4.5777` edge `0.0318` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `0.2183` n `133` status `ready` deltaP `6.622` edge `0.0334` maxDD `-1.0817`
- `market_context_high->commodity_1h` score `-0.0319` n `133` status `ready` deltaP `4.8963` edge `0.0106` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.194` n `133` status `ready` deltaP `11.0172` edge `0.0475` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3618` n `133` status `ready` deltaP `1.2746` edge `0.0001` maxDD `-0.4331`
- `market_context_high->commodity_24h` score `-0.6363` n `132` status `ready` deltaP `10.5638` edge `0.0349` maxDD `-7.0012`
- `market_context_high->metal_1h` score `-0.9345` n `133` status `ready` deltaP `0.5189` edge `0.019` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3373` n `133` status `ready` deltaP `-1.5624` edge `0.0018` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5462` n `133` status `ready` deltaP `0.3759` edge `0.0741` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.751` n `132` status `ready` deltaP `-10.7882` edge `0.0577` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.333` n `133` status `ready` deltaP `0.0732` edge `-0.1359` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
