# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T09:07:26.561206+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2886`

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

- `news_risk_high->unknown_1h` score `3221.7457` n `31` status `ready` deltaP `1.6322` edge `268.4855` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3180.5806` n `31` status `ready` deltaP `3.7864` edge `265.0288` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `19.9041` n `31` status `ready` deltaP `29.8611` edge `1.4596` maxDD `0.0`
- `news_risk_high->equity_24h` score `17.8236` n `31` status `ready` deltaP `29.3403` edge `1.2897` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.8702` n `31` status `ready` deltaP `28.9931` edge `1.0459` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.7744` n `31` status `ready` deltaP `21.425` edge `0.6754` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.5607` n `31` status `ready` deltaP `30.8222` edge `0.3893` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.5697` n `31` status `ready` deltaP `14.3391` edge `0.7602` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.0988` n `31` status `ready` deltaP `17.2771` edge `0.3372` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.6322` n `31` status `ready` deltaP `38.5865` edge `0.1416` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.2114` n `31` status `ready` deltaP `30.9028` edge `0.0616` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5786` n `31` status `ready` deltaP `30.06` edge `0.0405` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.5597` n `31` status `ready` deltaP `16.0952` edge `0.1247` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3835` n `31` status `ready` deltaP `28.8488` edge `0.0148` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.034` n `31` status `ready` deltaP `6.4178` edge `0.2641` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8434` n `31` status `ready` deltaP `9.5615` edge `0.2083` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1387` n `31` status `ready` deltaP `24.7923` edge `0.0086` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.394` n `31` status `ready` deltaP `12.0525` edge `0.0259` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.0831` n `31` status `ready` deltaP `5.7779` edge `-0.0094` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6983` n `31` status `ready` deltaP `-5.2057` edge `0.0027` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
