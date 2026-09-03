# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T17:52:36.018312+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `risk_on_high->unknown_4h` score `30.699` n `133` status `ready` deltaP `12.657` edge `2.5357` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `30.699` n `133` status `ready` deltaP `12.657` edge `2.5357` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `23.934` n `167` status `ready` deltaP `14.2553` edge `1.969` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `16.4237` n `133` status `ready` deltaP `1.0422` edge `1.4194` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `16.4237` n `133` status `ready` deltaP `1.0422` edge `1.4194` maxDD `-1.95`
- `market_context_high->unknown_1h` score `11.9439` n `167` status `ready` deltaP `1.497` edge `1.0484` maxDD `-2.0446`
- `market_context_high->equity_24h` score `2.3694` n `127` status `ready` deltaP `19.428` edge `0.5025` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `2.1141` n `67` status `ready` deltaP `19.0039` edge `0.4378` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `1.8865` n `107` status `ready` deltaP `14.6742` edge `0.4739` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `1.8865` n `107` status `ready` deltaP `14.6742` edge `0.4739` maxDD `-19.828`
- `news_risk_high->crypto_major_24h` score `1.5297` n `67` status `ready` deltaP `15.5007` edge `0.5311` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.0249` n `67` status `ready` deltaP `7.0999` edge `0.3308` maxDD `-15.4056`
- `news_risk_high->commodity_4h` score `0.4199` n `67` status `ready` deltaP `7.7767` edge `0.0379` maxDD `-0.8733`
- `news_risk_high->fx_4h` score `0.0897` n `67` status `ready` deltaP `10.2612` edge `0.0047` maxDD `-1.2507`
- `risk_on_high->metal_1h` score `0.0423` n `133` status `ready` deltaP `11.3649` edge `0.0009` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0423` n `133` status `ready` deltaP `11.3649` edge `0.0009` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0757` n `67` status `ready` deltaP `4.3257` edge `-0.0032` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.1139` n `133` status `ready` deltaP `4.7409` edge `-0.0017` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1139` n `133` status `ready` deltaP `4.7409` edge `-0.0017` maxDD `-0.5605`
- `news_risk_high->commodity_1h` score `-0.131` n `67` status `ready` deltaP `4.9066` edge `0.001` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
