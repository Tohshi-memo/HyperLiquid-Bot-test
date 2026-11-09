# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T00:37:29.986527+00:00`
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

- `market_context_high->equity_24h` score `5.6929` n `36` status `ready` deltaP `12.6736` edge `0.7823` maxDD `-28.7236`
- `market_context_high->index_24h` score `1.1473` n `36` status `ready` deltaP `14.4097` edge `0.1141` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.8554` n `36` status `ready` deltaP `10.9375` edge `0.0072` maxDD `-0.0397`
- `market_context_high->metal_1h` score `0.3351` n `62` status `ready` deltaP `6.751` edge `0.0157` maxDD `-0.6226`
- `market_context_high->commodity_24h` score `0.2083` n `36` status `ready` deltaP `3.4722` edge `0.1063` maxDD `-5.2193`
- `market_context_high->commodity_4h` score `0.1989` n `50` status `ready` deltaP `3.4085` edge `0.0444` maxDD `-1.3297`
- `market_context_high->fx_4h` score `0.1142` n `50` status `ready` deltaP `9.311` edge `0.0183` maxDD `-0.592`
- `market_context_high->unknown_4h` score `0.0892` n `50` status `ready` deltaP `-0.4512` edge `0.0552` maxDD `-0.9139`
- `market_context_high->commodity_1h` score `-0.1584` n `62` status `ready` deltaP `5.0705` edge `0.0076` maxDD `-1.7019`
- `market_context_high->equity_1h` score `-0.1754` n `62` status `ready` deltaP `0.3332` edge `0.095` maxDD `-5.5762`
- `market_context_high->index_4h` score `-0.2795` n `50` status `ready` deltaP `7.2378` edge `0.0046` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.5738` n `62` status `ready` deltaP `-4.5055` edge `0.0148` maxDD `-0.6664`
- `market_context_high->metal_4h` score `-0.6517` n `50` status `ready` deltaP `-0.7988` edge `-0.0257` maxDD `-1.2025`
- `market_context_high->fx_1h` score `-0.6782` n `62` status `ready` deltaP `-7.7168` edge `0.0021` maxDD `-0.3414`
- `market_context_high->crypto_alt_1h` score `-1.4586` n `62` status `ready` deltaP `4.0757` edge `-0.0249` maxDD `-10.1421`
- `market_context_high->metal_24h` score `-1.6429` n `36` status `ready` deltaP `6.9445` edge `-0.1279` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-2.4094` n `62` status `ready` deltaP `-1.2459` edge `-0.0907` maxDD `-11.7911`
- `market_context_high->equity_4h` score `-5.2999` n `50` status `ready` deltaP `6.7439` edge `-0.1253` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-7.6602` n `36` status `ready` deltaP `-8.3333` edge `-0.1268` maxDD `-30.4794`
- `market_context_high->crypto_alt_4h` score `-9.0935` n `50` status `ready` deltaP `3.128` edge `-0.3604` maxDD `-28.1265`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
