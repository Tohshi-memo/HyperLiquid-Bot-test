# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T15:07:29.918955+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4310`

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

- `market_context_high->unknown_1h` score `368.0169` n `50` status `ready` deltaP `11.3234` edge `30.5975` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `296.3904` n `50` status `ready` deltaP `12.1951` edge `24.6179` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `14.3055` n `50` status `ready` deltaP `29.9792` edge `1.1626` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.8087` n `50` status `ready` deltaP `37.6326` edge `0.8748` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `11.0669` n `62` status `ready` deltaP `38.7097` edge `0.6845` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.6179` n `62` status `ready` deltaP `29.6109` edge `0.7359` maxDD `-2.8784`
- `news_risk_high->crypto_alt_4h` score `7.7117` n `62` status `ready` deltaP `27.203` edge `0.5957` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.4083` n `50` status `ready` deltaP `18.0` edge `0.5677` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.3795` n `50` status `ready` deltaP `18.1707` edge `0.5394` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.6342` n `62` status `ready` deltaP `33.9828` edge `0.1755` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `4.0654` n `62` status `ready` deltaP `27.5325` edge `0.2165` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3345` n `50` status `ready` deltaP `14.9521` edge `0.2445` maxDD `-3.6376`
- `news_risk_high->index_4h` score `3.1739` n `62` status `ready` deltaP `34.289` edge `0.0621` maxDD `-0.4296`
- `market_context_high->fx_4h` score `3.0614` n `50` status `ready` deltaP `34.3659` edge `0.0395` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `3.0326` n `68` status `ready` deltaP `13.9574` edge `0.1952` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.9677` n `50` status `ready` deltaP `13.2515` edge `0.204` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3915` n `62` status `ready` deltaP `19.3302` edge `0.112` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.0713` n `68` status `ready` deltaP `25.546` edge `0.0173` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.6792` n `68` status `ready` deltaP `6.305` edge `0.1498` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.6064` n `50` status `ready` deltaP `22.2874` edge `0.0117` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
