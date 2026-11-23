# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T00:07:31.456701+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5306`

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

- `market_context_high->unknown_1h` score `13463.8601` n `97` status `ready` deltaP `0.7515` edge `1121.9995` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `8929.7513` n `94` status `ready` deltaP `-0.8886` edge `744.1824` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1369.0438` n `31` status `ready` deltaP `3.5783` edge `114.0807` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1201.635` n `31` status `ready` deltaP `4.3962` edge `100.1126` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.0974` n `31` status `ready` deltaP `39.8161` edge `0.7909` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0467` n `31` status `ready` deltaP `25.6933` edge `0.8363` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.7292` n `31` status `ready` deltaP `14.7964` edge `0.9058` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0793` n `31` status `ready` deltaP `20.1371` edge `0.2244` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.641` n `31` status `ready` deltaP `37.8344` edge `0.0772` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7693` n `31` status `ready` deltaP `32.2919` edge `0.024` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5094` n `31` status `ready` deltaP `10.0106` edge `0.3011` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.122` n `31` status `ready` deltaP `8.813` edge `0.249` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.6624` n `31` status `ready` deltaP `22.4183` edge `0.1194` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.582` n `31` status `ready` deltaP `29.7324` edge `0.0325` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7606` n `31` status `ready` deltaP `17.6682` edge `0.0195` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0609` n `31` status `ready` deltaP `1.3811` edge `0.0119` maxDD `-0.0947`
- `market_context_high->index_1h` score `-0.4714` n `97` status `ready` deltaP `-0.9306` edge `-0.0054` maxDD `-1.2394`
- `market_context_high->fx_4h` score `-0.885` n `94` status `ready` deltaP `3.3699` edge `0.0072` maxDD `-1.117`
- `market_context_high->metal_1h` score `-0.8935` n `97` status `ready` deltaP `-0.1312` edge `-0.0071` maxDD `-2.6517`
- `market_context_high->fx_1h` score `-1.3024` n `97` status `ready` deltaP `-9.7599` edge `-0.0013` maxDD `-0.3731`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
