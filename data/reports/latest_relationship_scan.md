# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T18:07:24.557994+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->metal_24h` score `2.9867` n `97` status `ready` deltaP `13.1075` edge `0.2191` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.2707` n `109` status `ready` deltaP `13.3028` edge `0.0845` maxDD `-2.7169`
- `market_context_high->equity_24h` score `1.2275` n `97` status `ready` deltaP `-4.5988` edge `0.4681` maxDD `-21.1456`
- `market_context_high->fx_24h` score `0.9076` n `97` status `ready` deltaP `24.9719` edge `0.0542` maxDD `-3.0128`
- `market_context_high->index_24h` score `0.5167` n `97` status `ready` deltaP `7.1359` edge `0.1468` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `0.3939` n `119` status `ready` deltaP `9.7217` edge `0.0255` maxDD `-1.1847`
- `market_context_high->fx_4h` score `0.1238` n `109` status `ready` deltaP `9.3113` edge `0.0069` maxDD `-1.6928`
- `market_context_high->fx_1h` score `-0.3248` n `119` status `ready` deltaP `4.3803` edge `-0.0055` maxDD `-1.0616`
- `market_context_high->index_4h` score `-0.6212` n `109` status `ready` deltaP `-1.6698` edge `-0.008` maxDD `-1.1743`
- `market_context_high->index_1h` score `-0.6977` n `119` status `ready` deltaP `-1.0089` edge `-0.0097` maxDD `-1.3375`
- `market_context_high->metal_4h` score `-0.9229` n `109` status `ready` deltaP `2.9397` edge `0.0032` maxDD `-2.6429`
- `market_context_high->crypto_alt_1h` score `-0.9351` n `119` status `ready` deltaP `-5.9352` edge `-0.0174` maxDD `-2.3669`
- `market_context_high->metal_1h` score `-1.037` n `119` status `ready` deltaP `-4.3702` edge `-0.0077` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-1.0379` n `119` status `ready` deltaP `4.4583` edge `-0.024` maxDD `-9.1031`
- `market_context_high->crypto_alt_4h` score `-1.4165` n `109` status `ready` deltaP `-0.1427` edge `-0.0375` maxDD `-5.7857`
- `market_context_high->equity_4h` score `-1.6381` n `109` status `ready` deltaP `5.5255` edge `-0.0813` maxDD `-10.244`
- `market_context_high->crypto_major_1h` score `-3.1088` n `119` status `ready` deltaP `-7.5341` edge `-0.0633` maxDD `-8.3095`
- `market_context_high->crypto_major_24h` score `-3.3186` n `97` status `ready` deltaP `0.0999` edge `-0.1767` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.321` n `97` status `ready` deltaP `-14.8766` edge `-0.1166` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-6.6799` n `109` status `ready` deltaP `-7.6485` edge `-0.1888` maxDD `-19.0158`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
