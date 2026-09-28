# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T09:22:29.683753+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7886`

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

- `news_risk_high->unknown_24h` score `855.9468` n `139` status `ready` deltaP `1.2153` edge `71.3208` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `5.1681` n `139` status `ready` deltaP `18.6988` edge `0.7012` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `2.4462` n `139` status `ready` deltaP `14.1299` edge `0.5531` maxDD `-26.1424`
- `news_risk_high->index_24h` score `2.2736` n `139` status `ready` deltaP `23.2339` edge `0.1041` maxDD `-2.2287`
- `news_risk_high->equity_24h` score `2.1241` n `139` status `ready` deltaP `17.6021` edge `0.3153` maxDD `-11.1179`
- `news_risk_high->equity_4h` score `1.4487` n `139` status `ready` deltaP `21.5334` edge `0.1381` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.2714` n `139` status `ready` deltaP `20.3013` edge `0.1561` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.61` n `139` status `ready` deltaP `6.9738` edge `0.2703` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.5991` n `139` status `ready` deltaP `6.8679` edge `0.0952` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.3258` n `139` status `ready` deltaP `6.3564` edge `0.0509` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.2778` n `139` status `ready` deltaP `6.8055` edge `0.0068` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.5436` n `139` status `ready` deltaP `3.3043` edge `0.018` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.546` n `139` status `ready` deltaP `1.1911` edge `0.0095` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.7134` n `139` status `ready` deltaP `-0.7507` edge `0.0418` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1562` n `139` status `ready` deltaP `-8.6687` edge `-0.0024` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2175` n `139` status `ready` deltaP `10.1344` edge `-0.0023` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5361` n `139` status `ready` deltaP `-10.6806` edge `0.0237` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9976` n `139` status `ready` deltaP `-11.2674` edge `-0.0135` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.186` n `139` status `ready` deltaP `-7.225` edge `0.0394` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.8164` n `139` status `ready` deltaP `-11.1697` edge `-0.0017` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
