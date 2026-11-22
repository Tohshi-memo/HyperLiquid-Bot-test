# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T13:07:28.053486+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4008`

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

- `market_context_high->unknown_1h` score `12041.8856` n `106` status `ready` deltaP `-0.3927` edge `1003.5129` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7515.0973` n `106` status `ready` deltaP `-2.5742` edge `626.3058` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1421.5233` n `31` status `ready` deltaP `4.4765` edge `118.448` maxDD `-0.7389`
- `news_risk_high->equity_1h` score `4.0002` n `31` status `ready` deltaP `19.8377` edge `0.2198` maxDD `-0.163`
- `news_risk_high->index_1h` score `2.7094` n `31` status `ready` deltaP `31.6931` edge `0.023` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5203` n `31` status `ready` deltaP `9.7112` edge `0.3045` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1243` n `31` status `ready` deltaP `8.6633` edge `0.2503` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5228` n `31` status `ready` deltaP `28.6845` edge `0.0319` maxDD `-0.2315`
- `news_risk_high->commodity_1h` score `-0.1292` n `31` status `ready` deltaP `0.6326` edge `0.0112` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3207` n `106` status `ready` deltaP `2.6042` edge `0.008` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4071` n `106` status `ready` deltaP `1.9913` edge `0.0015` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.1867` n `106` status `ready` deltaP `-8.1771` edge `-0.0014` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.5187` n `106` status `ready` deltaP `-0.164` edge `0.0036` maxDD `-1.444`
- `market_context_high->crypto_major_1h` score `-1.8028` n `106` status `ready` deltaP `3.5335` edge `-0.0437` maxDD `-13.8788`
- `news_risk_high->fx_1h` score `-1.9787` n `31` status `ready` deltaP `-17.824` edge `-0.0023` maxDD `-0.1678`
- `market_context_high->equity_1h` score `-2.0322` n `106` status `ready` deltaP `5.8694` edge `-0.0109` maxDD `-13.1399`
- `market_context_high->metal_4h` score `-2.216` n `106` status `ready` deltaP `0.3221` edge `-0.0062` maxDD `-10.1161`
- `market_context_high->commodity_1h` score `-2.4937` n `106` status `ready` deltaP `-10.962` edge `-0.0272` maxDD `-4.2689`
- `market_context_high->index_4h` score `-3.5371` n `106` status `ready` deltaP `-14.6945` edge `-0.0335` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.72` n `106` status `ready` deltaP `-5.0616` edge `-0.0652` maxDD `-13.8848`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
