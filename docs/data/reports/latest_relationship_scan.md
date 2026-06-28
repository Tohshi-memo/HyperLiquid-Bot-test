# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T10:22:27.178749+00:00`
- Price records: `672`
- Market context records: `5030`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10174`

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

- `market_context_high->unknown_1h` score `15.1352` n `93` status `ready` deltaP `3.6685` edge `1.2869` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0505` n `93` status `ready` deltaP `21.7545` edge `0.7114` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.5035` n `93` status `ready` deltaP `16.7946` edge `0.5051` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3192` n `93` status `ready` deltaP `14.4834` edge `0.4861` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.255` n `93` status `ready` deltaP `13.3916` edge `0.1232` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8764` n `93` status `ready` deltaP `8.3365` edge `0.0748` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.7745` n `93` status `ready` deltaP `6.1039` edge `0.1156` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.4239` n `93` status `ready` deltaP `2.9685` edge `0.1727` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3736` n `93` status `ready` deltaP `6.4033` edge `0.0381` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1937` n `93` status `ready` deltaP `5.2604` edge `0.092` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.0435` n `74` status `ready` deltaP `9.558` edge `0.0069` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.1241` n `93` status `ready` deltaP `3.8667` edge `0.04` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.322` n `93` status `ready` deltaP `1.5582` edge `0.0143` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5359` n `93` status `ready` deltaP `2.5111` edge `0.0127` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.8178` n `93` status `ready` deltaP `3.393` edge `-0.0022` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0188` n `93` status `ready` deltaP `-4.3732` edge `-0.0026` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.8216` n `93` status `ready` deltaP `-12.7471` edge `-0.0058` maxDD `-0.5482`
- `market_context_high->unknown_24h` score `-3.3602` n `74` status `ready` deltaP `27.0364` edge `-0.426` maxDD `-1.4072`
- `market_context_high->metal_24h` score `-3.7492` n `74` status `ready` deltaP `5.2083` edge `0.0301` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.5735` n `74` status `ready` deltaP `1.2809` edge `-0.084` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
