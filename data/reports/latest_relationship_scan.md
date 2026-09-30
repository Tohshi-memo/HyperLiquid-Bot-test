# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T05:52:32.386475+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7330`

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

- `news_risk_high->unknown_24h` score `1342.5592` n `135` status `ready` deltaP `1.9097` edge `111.8672` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.8025` n `135` status `ready` deltaP `29.0741` edge `1.394` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `8.578` n `135` status `ready` deltaP `29.0741` edge `0.7559` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `8.0697` n `135` status `ready` deltaP `23.9931` edge `0.8279` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.9708` n `135` status `ready` deltaP `35.2662` edge `0.1436` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.6438` n `135` status `ready` deltaP `27.4421` edge `0.2481` maxDD `-2.192`
- `news_risk_high->equity_4h` score `3.0102` n `135` status `ready` deltaP `30.0858` edge `0.2104` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.9796` n `135` status `ready` deltaP `11.5696` edge `0.3538` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.1377` n `135` status `ready` deltaP `9.5509` edge `0.1222` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.9595` n `135` status `ready` deltaP `9.8503` edge `0.0766` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.546` n `135` status `ready` deltaP `9.4167` edge `0.0115` maxDD `-0.302`
- `news_risk_high->index_4h` score `-0.0591` n `135` status `ready` deltaP `7.7111` edge `0.029` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.485` n `135` status `ready` deltaP `1.1577` edge `0.0148` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.494` n `135` status `ready` deltaP `2.6391` edge `0.0695` maxDD `-7.2607`
- `news_risk_high->metal_4h` score `-1.2735` n `135` status `ready` deltaP `-7.5418` edge `0.0278` maxDD `-2.9297`
- `news_risk_high->fx_4h` score `-1.3673` n `135` status `ready` deltaP `7.8376` edge `-0.0062` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.5806` n `135` status `ready` deltaP `-3.6833` edge `0.0934` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-1.8281` n `135` status `ready` deltaP `-8.6682` edge `-0.0091` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.902` n `135` status `ready` deltaP `-9.9534` edge `-0.0041` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.2192` n `135` status `ready` deltaP `-8.6924` edge `0.0153` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
