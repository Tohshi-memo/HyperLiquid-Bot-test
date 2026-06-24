# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T23:22:29.196857+00:00`
- Price records: `672`
- Market context records: `4668`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9870`

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

- `market_context_high->unknown_1h` score `71.7732` n `144` status `ready` deltaP `9.9426` edge `5.9596` maxDD `-1.916`
- `market_context_high->unknown_4h` score `4.3924` n `144` status `ready` deltaP `10.332` edge `0.4182` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.4461` n `144` status `ready` deltaP `9.2014` edge `0.1515` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.475` n `144` status `ready` deltaP `2.312` edge `0.0246` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5422` n `144` status `ready` deltaP `-1.5677` edge `-0.0036` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.7218` n `144` status `ready` deltaP `4.1159` edge `-0.0077` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.7565` n `144` status `ready` deltaP `1.5074` edge `0.0012` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.8199` n `144` status `ready` deltaP `-1.7423` edge `0.0052` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-1.2332` n `144` status `ready` deltaP `1.7277` edge `0.0073` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.3122` n `144` status `ready` deltaP `3.9634` edge `0.0161` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.7098` n `144` status `ready` deltaP `-4.3829` edge `-0.0124` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.8694` n `144` status `ready` deltaP `-4.1417` edge `-0.0751` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.7112` n `144` status `ready` deltaP `13.7153` edge `0.0664` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-5.0543` n `144` status `ready` deltaP `-10.4167` edge `-0.0105` maxDD `-5.9661`
- `market_context_high->crypto_alt_1h` score `-5.3465` n `144` status `ready` deltaP `-1.5926` edge `-0.1062` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.5919` n `144` status `ready` deltaP `-5.4059` edge `-0.138` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.5305` n `144` status `ready` deltaP `-7.1181` edge `-0.0426` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.1553` n `144` status `ready` deltaP `-0.6944` edge `-0.1752` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.5855` n `144` status `ready` deltaP `-3.5739` edge `-0.2837` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-11.3164` n `144` status `ready` deltaP `-2.9472` edge `-0.3368` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
