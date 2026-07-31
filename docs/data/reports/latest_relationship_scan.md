# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T19:52:26.467774+00:00`
- Price records: `672`
- Market context records: `8545`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5925`

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

- `news_risk_high->unknown_24h` score `5436.3533` n `58` status `ready` deltaP `42.409` edge `452.7888` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.5649` n `64` status `ready` deltaP `20.0457` edge `0.3898` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.9135` n `64` status `ready` deltaP `15.5869` edge `0.0746` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `1.8477` n `60` status `ready` deltaP `12.5813` edge `0.1658` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.6354` n `64` status `ready` deltaP `15.6531` edge `0.0796` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9801` n `64` status `ready` deltaP `6.2881` edge `0.1613` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.6735` n `64` status `ready` deltaP `13.4146` edge `0.1361` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4882` n `64` status `ready` deltaP `8.561` edge `0.0582` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3703` n `64` status `ready` deltaP `7.064` edge `0.0516` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.069` n `64` status `ready` deltaP `4.9869` edge `0.0037` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0127` n `64` status `ready` deltaP `3.3215` edge `0.0079` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0459` n `64` status `ready` deltaP `1.5625` edge `0.0313` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `-0.0963` n `64` status `ready` deltaP `10.0991` edge `0.0204` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.1886` n `64` status `ready` deltaP `2.6572` edge `0.0069` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2957` n `62` status `ready` deltaP `1.9123` edge `-0.0004` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3013` n `62` status `ready` deltaP `4.0081` edge `-0.0028` maxDD `-2.0038`
- `market_context_high->fx_4h` score `-0.4154` n `60` status `ready` deltaP `5.2033` edge `0.0103` maxDD `-1.3685`
- `market_context_high->crypto_alt_1h` score `-0.4886` n `62` status `ready` deltaP `-2.4773` edge `0.0166` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.8028` n `62` status `ready` deltaP `0.3477` edge `-0.0163` maxDD `-1.5667`
- `market_context_high->metal_4h` score `-0.9257` n `60` status `ready` deltaP `2.0833` edge `-0.0091` maxDD `-3.211`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
