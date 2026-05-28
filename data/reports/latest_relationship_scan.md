# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T02:22:16.791540+00:00`
- Price records: `672`
- Market context records: `2099`
- Flow alert records: `7936`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_alt_4h` score `10.6354` n `182` status `ready` deltaP `31.0423` edge `0.7938` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.4663` n `182` status `ready` deltaP `37.3626` edge `0.6761` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.8888` n `182` status `ready` deltaP `23.8425` edge `0.4067` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.1245` n `182` status `ready` deltaP `22.4487` edge `0.3035` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.8225` n `181` status `ready` deltaP `22.7322` edge `0.6157` maxDD `-35.8966`
- `market_context_high->index_4h` score `2.5306` n `182` status `ready` deltaP `18.7869` edge `0.154` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.2824` n `182` status `ready` deltaP `16.0821` edge `0.1816` maxDD `-3.2225`
- `market_context_high->index_24h` score `2.2373` n `181` status `ready` deltaP `11.5315` edge `0.2324` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `2.0878` n `182` status `ready` deltaP `13.0881` edge `0.1981` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.6478` n `181` status `ready` deltaP `22.7045` edge `0.4758` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.8749` n `182` status `ready` deltaP `11.0466` edge `0.0781` maxDD `-2.6402`
- `market_context_high->metal_4h` score `0.3545` n `182` status `ready` deltaP `14.3108` edge `0.1643` maxDD `-10.7466`
- `market_context_high->unknown_1h` score `0.3479` n `182` status `ready` deltaP `5.6475` edge `0.0633` maxDD `-3.0902`
- `market_context_high->index_1h` score `0.2019` n `182` status `ready` deltaP `6.549` edge `0.0322` maxDD `-1.3898`
- `market_context_high->crypto_major_24h` score `0.0612` n `181` status `ready` deltaP `21.0423` edge `0.7234` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.1178` n `181` status `ready` deltaP `14.9086` edge `0.0301` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.1647` n `182` status `ready` deltaP `7.1922` edge `0.0404` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8546` n `182` status `ready` deltaP `-1.4477` edge `0.0012` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.006` n `182` status `ready` deltaP `-5.8849` edge `-0.0016` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.1194` n `181` status `ready` deltaP `10.3998` edge `0.2275` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
