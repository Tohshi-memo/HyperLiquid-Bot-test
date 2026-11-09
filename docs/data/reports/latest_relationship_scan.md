# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T05:07:35.361616+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6818`

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

- `market_context_high->equity_24h` score `10.2562` n `32` status `ready` deltaP `16.8403` edge `0.9797` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.6257` n `32` status `ready` deltaP `8.3333` edge `0.222` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.4272` n `32` status `ready` deltaP `17.0139` edge `0.1158` maxDD `-2.3671`
- `market_context_high->metal_1h` score `0.9894` n `76` status `ready` deltaP `12.4094` edge `0.0325` maxDD `-0.6226`
- `market_context_high->metal_4h` score `0.9338` n `64` status `ready` deltaP `13.0716` edge `0.0851` maxDD `-1.2025`
- `market_context_high->commodity_4h` score `0.8046` n `64` status `ready` deltaP `5.2591` edge `0.0792` maxDD `-1.1102`
- `market_context_high->fx_24h` score `0.6844` n `32` status `ready` deltaP `10.7639` edge `-0.0059` maxDD `-0.0397`
- `market_context_high->index_4h` score `0.3128` n `64` status `ready` deltaP `14.5579` edge `0.0359` maxDD `-2.4279`
- `market_context_high->equity_1h` score `0.2519` n `76` status `ready` deltaP `1.0794` edge `0.1448` maxDD `-5.5762`
- `market_context_high->commodity_1h` score `0.2353` n `76` status `ready` deltaP `8.3675` edge `0.0226` maxDD `-1.7019`
- `market_context_high->index_1h` score `-0.3904` n `76` status `ready` deltaP `0.9297` edge `0.0196` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-0.6882` n `76` status `ready` deltaP `9.4863` edge `0.0378` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-0.9913` n `76` status `ready` deltaP `-12.5039` edge `-0.004` maxDD `-0.512`
- `market_context_high->equity_4h` score `-1.4236` n `64` status `ready` deltaP `10.5564` edge `0.1251` maxDD `-24.9053`
- `market_context_high->metal_24h` score `-1.5888` n `32` status `ready` deltaP `0.3472` edge `-0.1507` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-1.7145` n `64` status `ready` deltaP `-9.0701` edge `-0.0068` maxDD `-1.537`
- `market_context_high->crypto_major_1h` score `-1.8393` n `76` status `ready` deltaP `2.4267` edge `-0.0421` maxDD `-11.7911`
- `market_context_high->crypto_major_24h` score `-4.687` n `32` status `ready` deltaP `-4.8611` edge `0.0061` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-6.3542` n `64` status `ready` deltaP `8.4985` edge `-0.1193` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-9.0994` n `32` status `ready` deltaP `-18.75` edge `-0.1754` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
