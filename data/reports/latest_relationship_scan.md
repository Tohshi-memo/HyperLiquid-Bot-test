# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T20:37:28.825139+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4252`

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

- `market_context_high->unknown_1h` score `380.7296` n `50` status `ready` deltaP `11.9222` edge `31.6529` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `321.5418` n `50` status `ready` deltaP `12.6524` edge `26.7108` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.7652` n `50` status `ready` deltaP `29.286` edge `1.1222` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.5955` n `50` status `ready` deltaP `37.1127` edge `0.8605` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.708` n `62` status `ready` deltaP `29.9575` edge `0.7411` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.3589` n `68` status `ready` deltaP `37.4193` edge `0.6341` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.3258` n `68` status `ready` deltaP `26.3092` edge `0.5695` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.959` n `50` status `ready` deltaP `15.7134` edge `0.5455` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.6092` n `50` status `ready` deltaP `15.4268` edge `0.4935` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.5806` n `62` status `ready` deltaP `33.4629` edge `0.1745` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8267` n `68` status `ready` deltaP `26.9637` edge `0.2004` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.098` n `50` status `ready` deltaP `34.8232` edge `0.0395` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `3.0025` n `50` status `ready` deltaP `12.8563` edge `0.2308` maxDD `-3.6376`
- `news_risk_high->index_4h` score `2.9595` n `68` status `ready` deltaP `32.3888` edge `0.0569` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.836` n `68` status `ready` deltaP `12.6101` edge `0.1878` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.7712` n `50` status `ready` deltaP `11.9042` edge `0.1966` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.4368` n `68` status `ready` deltaP `20.9021` edge `0.1053` maxDD `-0.993`
- `news_risk_high->index_1h` score `1.936` n `68` status `ready` deltaP `23.8993` edge `0.017` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.5945` n `50` status `ready` deltaP `22.1377` edge `0.0117` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.5324` n `50` status `ready` deltaP `9.2478` edge `0.321` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
