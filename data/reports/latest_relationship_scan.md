# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T09:37:26.435279+00:00`
- Price records: `672`
- Market context records: `2957`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `17.3002` n `125` status `ready` deltaP `13.1792` edge `1.7455` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `8.5889` n `125` status `ready` deltaP `17.4764` edge `0.6457` maxDD `-1.7175`
- `market_context_high->equity_24h` score `8.053` n `125` status `ready` deltaP `18.1875` edge `0.7502` maxDD `-12.6963`
- `market_context_high->commodity_24h` score `6.1309` n `125` status `ready` deltaP `24.8597` edge `0.4867` maxDD `-4.6554`
- `market_context_high->index_24h` score `3.1991` n `125` status `ready` deltaP `13.8403` edge `0.2724` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.004` n `126` status `ready` deltaP `15.7302` edge `0.1978` maxDD `-1.8533`
- `market_context_high->crypto_alt_4h` score `2.2309` n `126` status `ready` deltaP `21.8762` edge `0.4962` maxDD `-30.8239`
- `market_context_high->unknown_4h` score `0.9672` n `126` status `ready` deltaP `7.2058` edge `0.1379` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.6913` n `126` status `ready` deltaP `13.797` edge `0.0808` maxDD `-2.3986`
- `market_context_high->equity_1h` score `0.1113` n `126` status `ready` deltaP `2.5022` edge `0.0525` maxDD `-1.7925`
- `market_context_high->index_1h` score `0.1055` n `126` status `ready` deltaP `6.1401` edge `0.022` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.2703` n `126` status `ready` deltaP `0.6297` edge `0.004` maxDD `-0.1244`
- `market_context_high->crypto_alt_1h` score `-0.3741` n `126` status `ready` deltaP `5.5556` edge `0.091` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.5057` n `126` status `ready` deltaP `-0.4633` edge `0.0008` maxDD `-3.3365`
- `market_context_high->crypto_major_1h` score `-0.6081` n `126` status `ready` deltaP `4.5813` edge `0.0701` maxDD `-9.622`
- `market_context_high->unknown_1h` score `-0.6264` n `126` status `ready` deltaP `2.0222` edge `0.0074` maxDD `-3.1801`
- `market_context_high->crypto_major_4h` score `-0.6989` n `126` status `ready` deltaP `11.4958` edge `0.3463` maxDD `-33.6701`
- `market_context_high->commodity_4h` score `-0.7268` n `126` status `ready` deltaP `6.3275` edge `0.0436` maxDD `-8.9839`
- `market_context_high->metal_1h` score `-0.7374` n `126` status `ready` deltaP `-0.8246` edge `-0.0003` maxDD `-3.4325`
- `market_context_high->fx_4h` score `-0.7873` n `126` status `ready` deltaP `0.3993` edge `0.0096` maxDD `-0.5631`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
