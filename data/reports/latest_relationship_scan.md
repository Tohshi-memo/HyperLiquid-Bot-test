# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T17:54:36.112823+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4238`

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

- `market_context_high->unknown_1h` score `368.9972` n `50` status `ready` deltaP `12.0719` edge `30.6742` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `297.998` n `50` status `ready` deltaP `12.8049` edge `24.7478` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `14.1805` n `50` status `ready` deltaP `29.6326` edge `1.1545` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.7647` n `50` status `ready` deltaP `37.1127` edge `0.8746` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.6684` n `62` status `ready` deltaP `29.9575` edge `0.7378` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.4629` n `68` status `ready` deltaP `38.0291` edge `0.6387` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.5432` n `68` status `ready` deltaP `27.3763` edge `0.5805` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.063` n `50` status `ready` deltaP `16.3232` edge `0.5501` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.8265` n `50` status `ready` deltaP `16.4939` edge `0.5045` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.5842` n `62` status `ready` deltaP `33.4629` edge `0.1748` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8753` n `68` status `ready` deltaP `27.4211` edge `0.2014` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.1859` n `50` status `ready` deltaP `13.9042` edge `0.2391` maxDD `-3.6376`
- `market_context_high->fx_4h` score `3.1114` n `50` status `ready` deltaP `34.9756` edge `0.0396` maxDD `-0.0791`
- `news_risk_high->index_4h` score `3.063` n `68` status `ready` deltaP `33.6083` edge `0.0574` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9079` n `68` status `ready` deltaP `13.0592` edge `0.1908` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.8431` n `50` status `ready` deltaP `12.3533` edge `0.1996` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3624` n `68` status `ready` deltaP `19.9875` edge `0.1052` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.009` n `68` status `ready` deltaP `24.7975` edge `0.0171` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.6076` n `50` status `ready` deltaP `22.2874` edge `0.0118` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `1.5306` n `68` status `ready` deltaP `5.2571` edge `0.1444` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
