# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T21:37:20.764889+00:00`
- Price records: `672`
- Market context records: `2701`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->crypto_alt_24h` score `10.3255` n `111` status `ready` deltaP `16.3523` edge `1.1008` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6556` n `111` status `ready` deltaP `17.4784` edge `0.6376` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.837` n `143` status `ready` deltaP `5.9441` edge `0.1351` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.2602` n `143` status `ready` deltaP `12.0758` edge `0.037` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1518` n `143` status `ready` deltaP `3.2003` edge `0.0086` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2363` n `143` status `ready` deltaP `2.5994` edge `0.0358` maxDD `-3.1587`
- `market_context_high->crypto_major_24h` score `-0.2615` n `111` status `ready` deltaP `6.5175` edge `0.6793` maxDD `-44.169`
- `market_context_high->fx_1h` score `-0.4536` n `143` status `ready` deltaP `0.401` edge `0.0039` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.4572` n `143` status `ready` deltaP `1.9985` edge `0.0034` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.5861` n `143` status `ready` deltaP `5.9954` edge `0.0609` maxDD `-10.747`
- `market_context_high->crypto_alt_4h` score `-0.599` n `143` status `ready` deltaP `16.0584` edge `0.2771` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-0.6042` n `111` status `ready` deltaP `6.3063` edge `-0.0052` maxDD `-0.6418`
- `market_context_high->metal_1h` score `-0.7543` n `143` status `ready` deltaP `-1.3997` edge `-0.0028` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-0.8814` n `143` status `ready` deltaP `-0.8966` edge `0.0104` maxDD `-0.5631`
- `market_context_high->commodity_24h` score `-0.9673` n `111` status `ready` deltaP `6.4002` edge `0.1427` maxDD `-12.4171`
- `market_context_high->crypto_major_1h` score `-1.0297` n `143` status `ready` deltaP `3.0485` edge `0.0346` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.0336` n `143` status `ready` deltaP `4.4101` edge `0.0301` maxDD `-10.0279`
- `market_context_high->index_24h` score `-1.1383` n `111` status `ready` deltaP `2.6277` edge `-0.0143` maxDD `-2.5127`
- `market_context_high->equity_1h` score `-1.2487` n `143` status `ready` deltaP `-4.4857` edge `0.0097` maxDD `-2.7085`
- `market_context_high->equity_4h` score `-1.9733` n `143` status `ready` deltaP `-1.034` edge `-0.0171` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
