# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T01:07:26.463409+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6537`

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

- `market_context_high->equity_24h` score `8.4999` n `34` status `ready` deltaP `15.7782` edge `0.9172` maxDD `-22.7914`
- `market_context_high->index_24h` score `1.2437` n `34` status `ready` deltaP `15.4003` edge `0.1149` maxDD `-2.6491`
- `market_context_high->commodity_24h` score `1.2184` n `34` status `ready` deltaP `6.5768` edge `0.1799` maxDD `-2.4036`
- `market_context_high->fx_24h` score `0.6609` n `34` status `ready` deltaP `10.141` edge `-0.0037` maxDD `-0.0397`
- `market_context_high->commodity_4h` score `0.6428` n `50` status `ready` deltaP `5.2561` edge `0.0574` maxDD `-1.1102`
- `market_context_high->metal_1h` score `0.5685` n `62` status `ready` deltaP `8.2142` edge `0.0254` maxDD `-0.6226`
- `market_context_high->equity_1h` score `-0.1067` n `62` status `ready` deltaP `0.3332` edge `0.1038` maxDD `-5.5762`
- `market_context_high->fx_4h` score `-0.2236` n `50` status `ready` deltaP `5.6159` edge `0.0092` maxDD `-0.6916`
- `market_context_high->metal_4h` score `-0.3208` n `50` status `ready` deltaP `2.8963` edge `-0.0079` maxDD `-1.2025`
- `market_context_high->commodity_1h` score `-0.3255` n `62` status `ready` deltaP `3.6073` edge `0.0076` maxDD `-1.7019`
- `market_context_high->index_4h` score `-0.4751` n `50` status `ready` deltaP `5.3902` edge `-0.004` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.5793` n `62` status `ready` deltaP `-4.5055` edge `0.0141` maxDD `-0.6664`
- `market_context_high->fx_1h` score `-0.7811` n `62` status `ready` deltaP `-9.18` edge `-0.001` maxDD `-0.3682`
- `market_context_high->unknown_4h` score `-0.8564` n `50` status `ready` deltaP `-0.4512` edge `-0.0236` maxDD `-0.9139`
- `market_context_high->crypto_alt_1h` score `-0.9711` n `62` status `ready` deltaP `7.0021` edge `0.0181` maxDD `-10.1421`
- `market_context_high->metal_24h` score `-1.9239` n `34` status `ready` deltaP `4.1667` edge `-0.1328` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-2.0302` n `62` status `ready` deltaP `1.6805` edge `-0.0616` maxDD `-11.7911`
- `market_context_high->crypto_major_24h` score `-6.3225` n `34` status `ready` deltaP `-6.6993` edge `-0.0708` maxDD `-26.9129`
- `market_context_high->equity_4h` score `-6.3471` n `50` status `ready` deltaP `3.0488` edge `-0.1796` maxDD `-24.9053`
- `market_context_high->crypto_alt_4h` score `-10.1187` n `50` status `ready` deltaP `-0.5671` edge `-0.3944` maxDD `-29.6033`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
