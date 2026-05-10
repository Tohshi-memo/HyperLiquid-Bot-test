# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T08:37:13.344863+00:00`
- Price records: `672`
- Market context records: `957`
- Flow alert records: `2682`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `14.853` n `158` status `ready` deltaP `32.9465` edge `1.0515` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `8.7672` n `158` status `ready` deltaP `9.375` edge `0.6681` maxDD `0.0`
- `market_context_high->equity_24h` score `1.1315` n `158` status `ready` deltaP `2.2152` edge `0.34` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.3832` n `158` status `ready` deltaP `0.7867` edge `0.2262` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.3289` n `204` status `ready` deltaP `2.3805` edge `0.0375` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.3926` n `204` status `ready` deltaP `1.0098` edge `0.001` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.6072` n `204` status `ready` deltaP `1.4794` edge `0.0164` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.7267` n `204` status `ready` deltaP `2.8942` edge `0.0055` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-1.0345` n `192` status `ready` deltaP `1.7149` edge `0.002` maxDD `-1.6381`
- `market_context_high->equity_4h` score `-1.2135` n `192` status `ready` deltaP `2.6677` edge `0.0963` maxDD `-10.5498`
- `market_context_high->unknown_1h` score `-1.3938` n `204` status `ready` deltaP `-3.2817` edge `-0.0171` maxDD `-3.5069`
- `market_context_high->index_4h` score `-1.468` n `192` status `ready` deltaP `0.3049` edge `0.0279` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6002` n `204` status `ready` deltaP `6.4283` edge `-0.0039` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.8864` n `204` status `ready` deltaP `1.5704` edge `-0.0237` maxDD `-8.1842`
- `market_context_high->metal_1h` score `-1.8954` n `204` status `ready` deltaP `-2.5155` edge `-0.0303` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-2.3303` n `192` status `ready` deltaP `-0.7749` edge `0.0819` maxDD `-13.0076`
- `market_context_high->crypto_major_4h` score `-2.4401` n `192` status `ready` deltaP `8.9939` edge `0.1073` maxDD `-22.648`
- `market_context_high->unknown_4h` score `-3.3173` n `192` status `ready` deltaP `6.6565` edge `-0.133` maxDD `-8.3588`
- `market_context_high->crypto_alt_4h` score `-3.3192` n `192` status `ready` deltaP `-2.2485` edge `0.0162` maxDD `-15.2248`
- `market_context_high->unknown_24h` score `-4.1903` n `158` status `ready` deltaP `6.639` edge `-0.0309` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
