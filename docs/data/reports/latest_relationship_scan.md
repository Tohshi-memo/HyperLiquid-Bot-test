# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T09:07:27.172183+00:00`
- Price records: `672`
- Market context records: `2648`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9223`

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

- `market_context_high->unknown_24h` score `7.696` n `129` status `ready` deltaP `17.6639` edge `0.5564` maxDD `-1.626`
- `market_context_high->crypto_alt_24h` score `5.7761` n `129` status `ready` deltaP `8.6603` edge `0.8171` maxDD `-23.4795`
- `market_context_high->crypto_alt_4h` score `5.6972` n `129` status `ready` deltaP `26.3353` edge `0.5671` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.3029` n `129` status `ready` deltaP `17.111` edge `0.4255` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.3033` n `129` status `ready` deltaP `7.5427` edge `0.1633` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1718` n `133` status `ready` deltaP `10.3035` edge `0.1477` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.9818` n `129` status `ready` deltaP `11.0384` edge `0.1063` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.5284` n `133` status `ready` deltaP `6.8468` edge `0.1178` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.3444` n `129` status `ready` deltaP `9.9074` edge `0.0468` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0552` n `133` status `ready` deltaP `4.455` edge `0.0151` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.1433` n `133` status `ready` deltaP `1.7401` edge `0.0306` maxDD `-1.665`
- `market_context_high->metal_4h` score `-0.1466` n `129` status `ready` deltaP `5.762` edge `0.031` maxDD `-2.5301`
- `market_context_high->commodity_1h` score `-0.3508` n `133` status `ready` deltaP `4.7341` edge `0.0113` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4579` n `133` status `ready` deltaP `0.3861` edge `0.0039` maxDD `-0.2373`
- `market_context_high->fx_24h` score `-0.5395` n `129` status `ready` deltaP `6.4357` edge `0.0` maxDD `-0.6957`
- `market_context_high->metal_1h` score `-0.6851` n `133` status `ready` deltaP `-0.6787` edge `0.0051` maxDD `-1.6135`
- `market_context_high->equity_1h` score `-0.8647` n `133` status `ready` deltaP `-1.3799` edge `0.021` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-1.023` n `129` status `ready` deltaP `-1.899` edge `0.0105` maxDD `-0.6474`
- `market_context_high->commodity_4h` score `-1.2688` n `129` status `ready` deltaP `3.0441` edge `0.0113` maxDD `-10.2078`
- `market_context_high->equity_24h` score `-1.2802` n `129` status `ready` deltaP `8.4101` edge `-0.065` maxDD `-3.1535`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
