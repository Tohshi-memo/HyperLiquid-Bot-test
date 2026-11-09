# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T02:46:02.745017+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6611`

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

- `market_context_high->equity_24h` score `11.1468` n `32` status `ready` deltaP `18.4028` edge `1.0435` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.9667` n `32` status `ready` deltaP `9.8958` edge `0.24` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.5427` n `32` status `ready` deltaP `18.5764` edge `0.1202` maxDD `-2.3671`
- `market_context_high->metal_1h` score `1.167` n `67` status `ready` deltaP `13.5803` edge `0.0395` maxDD `-0.6226`
- `market_context_high->equity_1h` score `1.0986` n `67` status `ready` deltaP `5.2283` edge `0.1764` maxDD `-5.5762`
- `market_context_high->fx_24h` score `0.6144` n `32` status `ready` deltaP `10.0694` edge `-0.0071` maxDD `-0.0397`
- `market_context_high->metal_4h` score `0.3471` n `55` status `ready` deltaP `6.6796` edge `0.0525` maxDD `-1.2025`
- `market_context_high->commodity_4h` score `0.0388` n `55` status `ready` deltaP `-0.0166` edge `0.0523` maxDD `-1.1102`
- `market_context_high->commodity_1h` score `-0.027` n `67` status `ready` deltaP `6.1087` edge `0.0158` maxDD `-1.7019`
- `market_context_high->index_4h` score `-0.1938` n `55` status `ready` deltaP `9.3902` edge `0.0141` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.2457` n `67` status `ready` deltaP `2.2433` edge `0.0229` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-0.3012` n `67` status `ready` deltaP `13.1491` edge `0.063` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-0.8907` n `67` status `ready` deltaP `-10.6086` edge `-0.0042` maxDD `-0.475`
- `market_context_high->fx_4h` score `-0.9981` n `55` status `ready` deltaP `-2.7716` edge `-0.0002` maxDD `-1.0765`
- `market_context_high->metal_24h` score `-1.4918` n `32` status `ready` deltaP `1.0417` edge `-0.1429` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-1.5507` n `67` status `ready` deltaP `5.3825` edge `-0.0248` maxDD `-11.7911`
- `market_context_high->crypto_major_24h` score `-4.7182` n `32` status `ready` deltaP `-4.8611` edge `0.0035` maxDD `-23.1423`
- `market_context_high->equity_4h` score `-4.8608` n `55` status `ready` deltaP `4.2628` edge `-0.0555` maxDD `-24.9053`
- `market_context_high->crypto_alt_4h` score `-7.8553` n `55` status `ready` deltaP `4.7644` edge `-0.2195` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-8.7862` n `32` status `ready` deltaP `-18.75` edge `-0.1493` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
