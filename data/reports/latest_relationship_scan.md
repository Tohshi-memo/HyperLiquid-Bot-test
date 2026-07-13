# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T06:07:25.406034+00:00`
- Price records: `672`
- Market context records: `6576`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `6.2066` n `144` status `ready` deltaP `11.032` edge `0.7737` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.7676` n `210` status `ready` deltaP `-5.2794` edge `0.2726` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.4193` n `144` status `ready` deltaP `13.3492` edge `0.2161` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3456` n `210` status `ready` deltaP `1.008` edge `-0.0003` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.3932` n `210` status `ready` deltaP `7.197` edge `0.0282` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.5025` n `210` status `ready` deltaP `6.1905` edge `0.0256` maxDD `-5.8368`
- `market_context_high->index_1h` score `-0.5724` n `210` status `ready` deltaP `-0.6801` edge `0.0031` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.625` n `210` status `ready` deltaP `-1.008` edge `-0.0051` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.9755` n `210` status `ready` deltaP `8.2371` edge `0.008` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.2316` n `210` status `ready` deltaP `1.6325` edge `-0.0025` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.2883` n `210` status `ready` deltaP `-3.7268` edge `-0.0018` maxDD `-2.1239`
- `market_context_high->commodity_4h` score `-1.3502` n `210` status `ready` deltaP `-1.8642` edge `-0.0112` maxDD `-5.6246`
- `market_context_high->unknown_4h` score `-1.5525` n `210` status `ready` deltaP `-15.8561` edge `0.2169` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.7223` n `210` status `ready` deltaP `7.8825` edge `0.0581` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.772` n `210` status `ready` deltaP `-0.385` edge `-0.0034` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.9216` n `210` status `ready` deltaP `5.2381` edge `0.0589` maxDD `-19.2145`
- `market_context_high->metal_24h` score `-1.9309` n `144` status `ready` deltaP `6.0917` edge `0.0915` maxDD `-5.7746`
- `market_context_high->metal_4h` score `-2.1437` n `210` status `ready` deltaP `-1.3779` edge `0.0204` maxDD `-5.2172`
- `market_context_high->index_24h` score `-3.6957` n `144` status `ready` deltaP `1.4429` edge `0.0045` maxDD `-10.7676`
- `market_context_high->fx_24h` score `-3.8297` n `144` status `ready` deltaP `-4.8143` edge `-0.0054` maxDD `-9.2795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
