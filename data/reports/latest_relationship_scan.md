# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T21:22:31.216409+00:00`
- Price records: `672`
- Market context records: `3007`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `20.1731` n `98` status `ready` deltaP `7.7204` edge `2.0213` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.6292` n `98` status `ready` deltaP `42.6411` edge `0.7792` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `12.2662` n `98` status `ready` deltaP `19.9582` edge `0.9356` maxDD `-1.7175`
- `market_context_high->equity_24h` score `10.2426` n `98` status `ready` deltaP `18.6934` edge `0.9293` maxDD `-12.6963`
- `market_context_high->index_24h` score `6.3558` n `98` status `ready` deltaP `18.3036` edge `0.5057` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.4027` n `105` status `ready` deltaP `17.9603` edge `0.1452` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.5698` n `105` status `ready` deltaP `12.8557` edge `0.1678` maxDD `-12.1029`
- `market_context_high->index_4h` score `0.2753` n `105` status `ready` deltaP `17.6582` edge `0.0956` maxDD `-9.9084`
- `market_context_high->commodity_1h` score `-0.0472` n `111` status `ready` deltaP `1.0547` edge `0.022` maxDD `-0.9706`
- `market_context_high->equity_1h` score `-0.2997` n `111` status `ready` deltaP `4.514` edge `0.0393` maxDD `-5.6254`
- `market_context_high->crypto_alt_4h` score `-0.3077` n `105` status `ready` deltaP `22.1182` edge `0.3679` maxDD `-38.7172`
- `market_context_high->fx_1h` score `-0.4384` n `111` status `ready` deltaP `-3.0008` edge `0.0004` maxDD `-0.2615`
- `market_context_high->index_1h` score `-0.4485` n `111` status `ready` deltaP `4.0514` edge `0.0169` maxDD `-4.1126`
- `market_context_high->crypto_alt_1h` score `-0.7837` n `111` status `ready` deltaP `7.508` edge `0.0976` maxDD `-14.7034`
- `market_context_high->crypto_major_1h` score `-1.0102` n `111` status `ready` deltaP `5.0966` edge `0.0628` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.1934` n `105` status `ready` deltaP `-10.9524` edge `-0.001` maxDD `-0.6521`
- `market_context_high->unknown_1h` score `-1.2099` n `111` status `ready` deltaP `2.7095` edge `-0.0458` maxDD `-3.1801`
- `market_context_high->unknown_4h` score `-1.5719` n `105` status `ready` deltaP `-2.153` edge `-0.0113` maxDD `-3.7602`
- `market_context_high->fx_24h` score `-1.8628` n `98` status `ready` deltaP `-6.3066` edge `-0.026` maxDD `-0.6418`
- `market_context_high->metal_1h` score `-1.9321` n `111` status `ready` deltaP `-3.164` edge `-0.0081` maxDD `-6.8783`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
