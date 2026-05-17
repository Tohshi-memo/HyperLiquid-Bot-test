# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T13:22:13.370039+00:00`
- Price records: `672`
- Market context records: `1015`
- Flow alert records: `4832`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8634`

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

- `market_context_high->crypto_major_24h` score `13.4472` n `197` status `ready` deltaP `32.3484` edge `0.9638` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.2947` n `197` status `ready` deltaP `11.0844` edge `0.4074` maxDD `-9.5387`
- `market_context_high->equity_24h` score `0.3405` n `197` status `ready` deltaP `6.763` edge `0.1892` maxDD `-8.8066`
- `market_context_high->index_24h` score `0.2926` n `197` status `ready` deltaP `6.1008` edge `0.1605` maxDD `-4.8097`
- `market_context_high->fx_1h` score `-0.2108` n `197` status `ready` deltaP `2.7524` edge `0.0002` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.4456` n `197` status `ready` deltaP `2.8572` edge `0.0246` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.7815` n `197` status `ready` deltaP `-0.744` edge `0.0167` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.7857` n `197` status `ready` deltaP `2.1262` edge `0.0057` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-0.9173` n `197` status `ready` deltaP `3.0449` edge `0.0029` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.2697` n `197` status `ready` deltaP `4.3079` edge `-0.0192` maxDD `-11.4508`
- `market_context_high->equity_4h` score `-1.3637` n `197` status `ready` deltaP `2.2595` edge `0.0865` maxDD `-10.5498`
- `market_context_high->crypto_alt_1h` score `-1.3693` n `197` status `ready` deltaP `-1.4066` edge `-0.0222` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.5506` n `197` status `ready` deltaP `-0.8365` edge `0.024` maxDD `-6.1444`
- `market_context_high->metal_1h` score `-1.8341` n `197` status `ready` deltaP `0.149` edge `-0.0402` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-2.8844` n `197` status `ready` deltaP `6.9503` edge `0.0839` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-2.9448` n `197` status `ready` deltaP `-0.5239` edge `0.0359` maxDD `-15.2248`
- `market_context_high->commodity_4h` score `-3.1812` n `197` status `ready` deltaP `-2.0753` edge `0.0655` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.3208` n `197` status `ready` deltaP `0.3734` edge `-0.0206` maxDD `-19.2774`
- `market_context_high->metal_4h` score `-4.4444` n `197` status `ready` deltaP `-3.0542` edge `-0.1652` maxDD `-24.0716`
- `market_context_high->metal_24h` score `-7.5166` n `197` status `ready` deltaP `-9.3912` edge `0.2079` maxDD `-50.4006`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
