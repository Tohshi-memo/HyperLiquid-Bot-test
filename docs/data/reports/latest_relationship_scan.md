# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T15:37:31.959289+00:00`
- Price records: `672`
- Market context records: `5785`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8556`

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

- `market_context_high->equity_24h` score `0.4603` n `242` status `ready` deltaP `15.0755` edge `0.4664` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.0321` n `299` status `ready` deltaP `7.0107` edge `0.1198` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2474` n `305` status `ready` deltaP `2.3736` edge `0.001` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.627` n `305` status `ready` deltaP `3.292` edge `0.0265` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.6575` n `305` status `ready` deltaP `2.0595` edge `-0.001` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.7353` n `305` status `ready` deltaP `-1.3468` edge `-0.0048` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.9618` n `305` status `ready` deltaP `2.8723` edge `0.0328` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.9772` n `305` status `ready` deltaP `0.2705` edge `0.0036` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.9936` n `242` status `ready` deltaP `14.1429` edge `0.04` maxDD `-3.9339`
- `market_context_high->crypto_alt_1h` score `-1.076` n `305` status `ready` deltaP `1.7675` edge `0.032` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2001` n `299` status `ready` deltaP `0.6404` edge `0.0106` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.4095` n `299` status `ready` deltaP `0.8019` edge `0.0039` maxDD `-1.8625`
- `market_context_high->commodity_4h` score `-2.4622` n `299` status `ready` deltaP `-3.3613` edge `-0.0257` maxDD `-14.071`
- `market_context_high->index_24h` score `-2.8575` n `242` status `ready` deltaP `2.7333` edge `0.0299` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.9369` n `299` status `ready` deltaP `7.5751` edge `0.142` maxDD `-25.6458`
- `market_context_high->metal_4h` score `-3.8333` n `299` status `ready` deltaP `-5.3843` edge `-0.0476` maxDD `-11.5426`
- `market_context_high->crypto_alt_4h` score `-4.5256` n `299` status `ready` deltaP `5.3272` edge `0.0882` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-7.0917` n `242` status `ready` deltaP `-7.8986` edge `-0.2496` maxDD `-27.5543`
- `market_context_high->crypto_major_24h` score `-7.2408` n `242` status `ready` deltaP `1.7691` edge `-0.107` maxDD `-29.6555`
- `market_context_high->commodity_24h` score `-10.9859` n `242` status `ready` deltaP `-14.3064` edge `-0.0825` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
