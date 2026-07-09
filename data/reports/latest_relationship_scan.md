# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T17:52:30.107345+00:00`
- Price records: `672`
- Market context records: `6203`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `12.8378` n `32` status `ready` deltaP `42.2194` edge `0.8031` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.7179` n `32` status `ready` deltaP `58.5034` edge `0.1698` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0466` n `32` status `ready` deltaP `42.3018` edge `0.0598` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2853` n `32` status `ready` deltaP `27.5449` edge `0.0207` maxDD `-0.1113`
- `news_risk_high->crypto_major_24h` score `2.2324` n `32` status `ready` deltaP `15.625` edge `0.26` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `1.8908` n `192` status `ready` deltaP `1.6623` edge `0.2473` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.393` n `32` status `ready` deltaP `14.2777` edge `0.1301` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7312` n `32` status `ready` deltaP `9.5247` edge `0.0764` maxDD `-1.6923`
- `news_risk_high->commodity_24h` score `0.6198` n `32` status `ready` deltaP `18.3886` edge `-0.0504` maxDD `-0.3101`
- `market_context_high->unknown_4h` score `0.2025` n `192` status `ready` deltaP `-2.9091` edge `0.2895` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.0322` n `192` status `ready` deltaP `19.8023` edge `0.1207` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2612` n `32` status `ready` deltaP `8.801` edge `-0.005` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3315` n `192` status `ready` deltaP `0.4616` edge `-0.001` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.647` n `192` status `ready` deltaP `-1.497` edge `0.0007` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.7662` n `192` status `ready` deltaP `2.1469` edge `0.0062` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.8065` n `32` status `ready` deltaP `-3.7425` edge `-0.0287` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.9` n `192` status `ready` deltaP `1.4658` edge `-0.0049` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.9067` n `192` status `ready` deltaP `4.3819` edge `0.0313` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9325` n `192` status `ready` deltaP `3.7955` edge `0.0304` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-1.0845` n `192` status `ready` deltaP `-2.863` edge `-0.0084` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
