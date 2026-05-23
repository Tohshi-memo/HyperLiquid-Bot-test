# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T08:37:19.669681+00:00`
- Price records: `672`
- Market context records: `1613`
- Flow alert records: `6553`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `12.2598` n `187` status `ready` deltaP `28.0062` edge `0.9881` maxDD `-7.919`
- `market_context_high->crypto_alt_24h` score `4.7912` n `187` status `ready` deltaP `24.2981` edge `0.8961` maxDD `-49.372`
- `market_context_high->crypto_major_24h` score `4.5214` n `187` status `ready` deltaP `24.1728` edge `0.6971` maxDD `-34.5176`
- `market_context_high->index_24h` score `3.7681` n `187` status `ready` deltaP `20.1519` edge `0.2883` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.0636` n `187` status `ready` deltaP `18.7073` edge `0.4476` maxDD `-21.0276`
- `market_context_high->equity_4h` score `1.3244` n `194` status `ready` deltaP `11.073` edge `0.146` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.3165` n `194` status `ready` deltaP `13.2497` edge `0.2842` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.1736` n `194` status `ready` deltaP `9.3365` edge `0.2309` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.2351` n `187` status `ready` deltaP `7.6519` edge `0.0343` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.2714` n `194` status `ready` deltaP `0.7146` edge `0.0628` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.4864` n `194` status `ready` deltaP `1.2779` edge `0.0318` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6703` n `194` status `ready` deltaP `0.5124` edge `0.0039` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.8542` n `194` status `ready` deltaP `-0.6991` edge `-0.0033` maxDD `-0.3914`
- `market_context_high->crypto_major_1h` score `-0.8659` n `194` status `ready` deltaP `-0.9646` edge `0.0311` maxDD `-6.1883`
- `market_context_high->index_4h` score `-0.886` n `194` status `ready` deltaP `0.1901` edge `0.0338` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-1.0991` n `194` status `ready` deltaP `-0.0833` edge `0.0011` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.1472` n `194` status `ready` deltaP `4.8877` edge `0.0054` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.3971` n `194` status `ready` deltaP `9.0096` edge `0.0927` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.4092` n `194` status `ready` deltaP `-11.0055` edge `-0.0144` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.1797` n `194` status `ready` deltaP `-13.8091` edge `-0.1093` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
