# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T16:22:25.368741+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4210`

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

- `market_context_high->unknown_1h` score `368.2052` n `50` status `ready` deltaP `11.7725` edge `30.6102` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `297.0192` n `50` status `ready` deltaP `12.1951` edge `24.6703` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `14.2839` n `50` status `ready` deltaP `29.9792` edge `1.1608` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.8255` n `50` status `ready` deltaP `37.6326` edge `0.8762` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `10.7536` n `65` status `ready` deltaP `38.4686` edge `0.66` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.6624` n `62` status `ready` deltaP `29.9575` edge `0.7373` maxDD `-2.8784`
- `news_risk_high->crypto_alt_4h` score `7.6106` n `65` status `ready` deltaP `27.4085` edge `0.5859` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.2621` n `50` status `ready` deltaP `17.2378` edge `0.5606` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.1769` n `50` status `ready` deltaP `17.4085` edge `0.5276` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.6179` n `62` status `ready` deltaP `33.8095` edge `0.1753` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.9739` n `65` status `ready` deltaP `27.5891` edge `0.2085` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.325` n `50` status `ready` deltaP `14.8024` edge `0.2447` maxDD `-3.6376`
- `news_risk_high->index_4h` score `3.1258` n `65` status `ready` deltaP `34.0479` edge `0.0597` maxDD `-0.4296`
- `market_context_high->fx_4h` score `3.1114` n `50` status `ready` deltaP `34.9756` edge `0.0396` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `3.0266` n `68` status `ready` deltaP `13.9574` edge `0.1947` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.9617` n `50` status `ready` deltaP `13.2515` edge `0.2035` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3624` n `65` status `ready` deltaP `19.5075` edge `0.1084` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.0593` n `68` status `ready` deltaP `25.3963` edge `0.0173` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.6696` n `68` status `ready` deltaP `6.1553` edge `0.15` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.5945` n `50` status `ready` deltaP `22.1377` edge `0.0117` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
