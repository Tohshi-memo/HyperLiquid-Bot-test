# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T05:22:25.231540+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8790`

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

- `market_context_high->equity_24h` score `10.1439` n `32` status `ready` deltaP `16.6667` edge `0.9715` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.5939` n `32` status `ready` deltaP `8.1597` edge `0.2205` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.4127` n `32` status `ready` deltaP `16.8403` edge `0.1151` maxDD `-2.3671`
- `market_context_high->metal_4h` score `0.9596` n `65` status `ready` deltaP `13.6726` edge `0.0844` maxDD `-1.2025`
- `market_context_high->metal_1h` score `0.9273` n `77` status `ready` deltaP `11.7389` edge `0.0318` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `0.8592` n `65` status `ready` deltaP `5.7317` edge `0.0806` maxDD `-1.1102`
- `market_context_high->fx_24h` score `0.6856` n `32` status `ready` deltaP `10.7639` edge `-0.0058` maxDD `-0.0397`
- `market_context_high->index_4h` score `0.3386` n `65` status `ready` deltaP `14.9343` edge `0.0367` maxDD `-2.4279`
- `market_context_high->equity_1h` score `0.194` n `77` status `ready` deltaP `0.4471` edge `0.1416` maxDD `-5.5762`
- `market_context_high->commodity_1h` score `0.1397` n `77` status `ready` deltaP `7.5473` edge `0.0201` maxDD `-1.7019`
- `market_context_high->index_1h` score `-0.4314` n `77` status `ready` deltaP `0.4471` edge `0.0194` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-0.7527` n `77` status `ready` deltaP `8.7857` edge `0.0342` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-1.0208` n `77` status `ready` deltaP `-13.0337` edge `-0.0041` maxDD `-0.5237`
- `market_context_high->equity_4h` score `-1.2956` n `65` status `ready` deltaP `11.053` edge `0.1382` maxDD `-24.9053`
- `market_context_high->metal_24h` score `-1.6072` n `32` status `ready` deltaP `0.1736` edge `-0.1519` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-1.7916` n `65` status `ready` deltaP `-9.6389` edge `-0.0078` maxDD `-1.6109`
- `market_context_high->crypto_major_1h` score `-1.9003` n `77` status `ready` deltaP `1.7944` edge `-0.0457` maxDD `-11.7911`
- `market_context_high->crypto_major_24h` score `-4.6822` n `32` status `ready` deltaP `-4.8611` edge `0.0065` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-6.4066` n `65` status `ready` deltaP `7.7533` edge `-0.1187` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-9.1282` n `32` status `ready` deltaP `-18.75` edge `-0.1778` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
