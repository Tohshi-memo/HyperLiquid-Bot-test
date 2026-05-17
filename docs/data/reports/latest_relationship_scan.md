# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T12:22:14.478419+00:00`
- Price records: `672`
- Market context records: `1011`
- Flow alert records: `4820`
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

- `market_context_high->crypto_major_24h` score `13.2319` n `201` status `ready` deltaP `32.1916` edge `0.9469` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1939` n `201` status `ready` deltaP `11.0232` edge `0.3994` maxDD `-9.5387`
- `market_context_high->index_24h` score `-0.0878` n `201` status `ready` deltaP `5.2411` edge `0.1468` maxDD `-5.1243`
- `market_context_high->equity_24h` score `-0.4529` n `201` status `ready` deltaP `5.5483` edge `0.1651` maxDD `-10.1867`
- `market_context_high->commodity_1h` score `-0.5613` n `201` status `ready` deltaP `2.4458` edge `0.0177` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.5688` n `201` status `ready` deltaP `1.6311` edge `-0.0002` maxDD `-0.3124`
- `market_context_high->fx_4h` score `-0.659` n `201` status `ready` deltaP `1.9741` edge `0.002` maxDD `-1.6381`
- `market_context_high->equity_1h` score `-0.7209` n `201` status `ready` deltaP `-0.047` edge `0.0171` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.742` n `201` status `ready` deltaP `2.6432` edge `0.0059` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.2706` n `201` status `ready` deltaP `4.3212` edge `-0.0194` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.4013` n `201` status `ready` deltaP `-1.6623` edge `-0.0246` maxDD `-8.1842`
- `market_context_high->equity_4h` score `-1.4597` n `201` status `ready` deltaP `1.689` edge `0.0823` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.72` n `201` status `ready` deltaP `-1.6814` edge `0.0197` maxDD `-6.4794`
- `market_context_high->metal_1h` score `-1.8128` n `201` status `ready` deltaP `0.3322` edge `-0.0387` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-3.0238` n `201` status `ready` deltaP `6.3478` edge `0.0763` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.0868` n `201` status `ready` deltaP `-1.0762` edge `0.0667` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.2375` n `201` status `ready` deltaP `-1.827` edge `0.0202` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.3914` n `201` status `ready` deltaP `-0.376` edge `-0.0215` maxDD `-19.5298`
- `market_context_high->metal_4h` score `-4.561` n `201` status `ready` deltaP `-4.0028` edge `-0.1662` maxDD `-24.6816`
- `market_context_high->commodity_24h` score `-8.4667` n `201` status `ready` deltaP `1.6806` edge `0.3681` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
