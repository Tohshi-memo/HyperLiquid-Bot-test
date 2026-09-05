# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T14:07:27.358924+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10483`

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

- `risk_on_high->unknown_4h` score `22.4085` n `140` status `ready` deltaP `3.1359` edge `1.9083` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `22.4085` n `140` status `ready` deltaP `3.1359` edge `1.9083` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `10.4983` n `228` status `ready` deltaP `4.9529` edge `0.9232` maxDD `-2.8419`
- `news_risk_high->crypto_alt_24h` score `7.4315` n `37` status `ready` deltaP `25.1783` edge `0.4784` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.8553` n `37` status `ready` deltaP `20.4861` edge `0.1847` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.6486` n `37` status `ready` deltaP `17.1803` edge `0.2308` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3259` n `37` status `ready` deltaP `23.5416` edge `0.059` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.902` n `37` status `ready` deltaP `11.4288` edge `0.1024` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6111` n `37` status `ready` deltaP `13.3841` edge `0.0841` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.2334` n `37` status `ready` deltaP `14.7152` edge `0.024` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.205` n `37` status `ready` deltaP `6.4655` edge `0.0756` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1383` n `37` status `ready` deltaP `14.2742` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_major_24h` score `1.0319` n `37` status `ready` deltaP `16.5776` edge `0.2994` maxDD `-18.2098`
- `news_risk_high->crypto_alt_1h` score `0.9861` n `37` status `ready` deltaP `9.326` edge `0.0465` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.6407` n `37` status `ready` deltaP `6.3983` edge `0.0436` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.5001` n `37` status `ready` deltaP `15.0947` edge `0.0426` maxDD `-3.1244`
- `market_context_high->equity_24h` score `0.2713` n `187` status `ready` deltaP `15.1719` edge `0.3682` maxDD `-20.7654`
- `risk_on_high->metal_1h` score `0.0118` n `151` status `ready` deltaP `10.7775` edge `0.0009` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0118` n `151` status `ready` deltaP `10.7775` edge `0.0009` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `-0.0075` n `37` status `ready` deltaP `6.0245` edge `0.0035` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
