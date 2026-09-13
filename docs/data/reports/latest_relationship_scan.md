# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T23:22:26.958159+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12657`

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

- `market_context_high->unknown_24h` score `2445.7428` n `56` status `ready` deltaP `10.2093` edge `203.764` maxDD `-0.613`
- `news_risk_high->unknown_1h` score `435.8932` n `82` status `ready` deltaP `-5.4002` edge `36.4026` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.9546` n `82` status `ready` deltaP `36.8923` edge `1.3824` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3352` n `82` status `ready` deltaP `38.0236` edge `1.4215` maxDD `-9.098`
- `news_risk_high->equity_24h` score `10.2616` n `82` status `ready` deltaP `30.5467` edge `0.8295` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.5223` n `82` status `ready` deltaP `54.3187` edge `0.2824` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `5.2946` n `56` status `ready` deltaP `39.8276` edge `0.1757` maxDD `0.0`
- `news_risk_high->metal_24h` score `4.9847` n `82` status `ready` deltaP `28.7259` edge `0.2693` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.9694` n `30` status `ready` deltaP `39.8276` edge `0.1486` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.9694` n `30` status `ready` deltaP `39.8276` edge `0.1486` maxDD `0.0`
- `risk_on_high->fx_24h` score `3.4084` n `30` status `ready` deltaP `60.0574` edge `0.0471` maxDD `-0.1745`
- `risk_on_and_context->fx_24h` score `3.4084` n `30` status `ready` deltaP `60.0574` edge `0.0471` maxDD `-0.1745`
- `risk_on_high->crypto_alt_24h` score `1.9985` n `30` status `ready` deltaP `0.6322` edge `0.3821` maxDD `-6.7415`
- `risk_on_and_context->crypto_alt_24h` score `1.9985` n `30` status `ready` deltaP `0.6322` edge `0.3821` maxDD `-6.7415`
- `risk_on_high->commodity_4h` score `1.7978` n `52` status `ready` deltaP `24.8241` edge `0.0193` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.7978` n `52` status `ready` deltaP `24.8241` edge `0.0193` maxDD `-0.1313`
- `market_context_high->fx_24h` score `1.7961` n `56` status `ready` deltaP `41.7241` edge `0.0268` maxDD `-1.6423`
- `market_context_high->commodity_4h` score `1.4908` n `128` status `ready` deltaP `20.6174` edge `0.0286` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.4655` n `82` status `ready` deltaP `13.2622` edge `0.0341` maxDD `-0.6935`
- `market_context_high->crypto_alt_24h` score `0.3483` n `56` status `ready` deltaP `-1.3916` edge `0.2812` maxDD `-15.7649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
