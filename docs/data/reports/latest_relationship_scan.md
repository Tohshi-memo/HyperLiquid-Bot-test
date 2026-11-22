# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T23:07:30.301328+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5108`

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

- `market_context_high->unknown_1h` score `12810.6119` n `101` status `ready` deltaP `1.119` edge `1067.5597` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `8610.9522` n `96` status `ready` deltaP `-2.6423` edge `717.6275` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1377.055` n `31` status `ready` deltaP `3.5783` edge `114.7483` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1211.5592` n `31` status `ready` deltaP `4.5486` edge `100.9386` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.1856` n `31` status `ready` deltaP `40.2734` edge `0.7952` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0625` n `31` status `ready` deltaP `25.8457` edge `0.8366` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.7952` n `31` status `ready` deltaP `15.4062` edge `0.9102` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0673` n `31` status `ready` deltaP `20.1371` edge `0.2234` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.647` n `31` status `ready` deltaP `37.8344` edge `0.0777` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7645` n `31` status `ready` deltaP `32.2919` edge `0.0236` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5265` n `31` status `ready` deltaP `10.1603` edge `0.3023` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1266` n `31` status `ready` deltaP `8.813` edge `0.2496` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.7072` n `31` status `ready` deltaP `22.8757` edge `0.1221` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.5844` n `31` status `ready` deltaP `29.7324` edge `0.0328` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7536` n `31` status `ready` deltaP `17.6682` edge `0.0186` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0837` n `31` status `ready` deltaP `1.2314` edge `0.011` maxDD `-0.0947`
- `market_context_high->index_1h` score `-0.4914` n `101` status `ready` deltaP `1.1517` edge `0.0002` maxDD `-1.2394`
- `market_context_high->metal_1h` score `-0.5851` n `101` status `ready` deltaP `2.0736` edge `0.0039` maxDD `-2.6517`
- `market_context_high->fx_4h` score `-1.1644` n `96` status `ready` deltaP `0.9655` edge `0.0052` maxDD `-1.2071`
- `market_context_high->fx_1h` score `-1.318` n `101` status `ready` deltaP `-9.981` edge `-0.0011` maxDD `-0.3752`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
