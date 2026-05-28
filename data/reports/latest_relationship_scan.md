# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T00:07:18.749720+00:00`
- Price records: `672`
- Market context records: `2090`
- Flow alert records: `7908`
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

- `market_context_high->crypto_major_4h` score `10.3813` n `191` status `ready` deltaP `36.5861` edge `0.6742` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `10.3491` n `191` status `ready` deltaP `30.6283` edge `0.7727` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `7.1278` n `191` status `ready` deltaP `24.5244` edge `0.5054` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `4.3174` n `190` status `ready` deltaP `21.934` edge `0.7456` maxDD `-35.8966`
- `market_context_high->equity_4h` score `4.0945` n `191` status `ready` deltaP `21.8794` edge `0.3048` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.4762` n `191` status `ready` deltaP `18.3469` edge `0.1524` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.2817` n `191` status `ready` deltaP `16.2688` edge `0.1803` maxDD `-3.2225`
- `market_context_high->index_24h` score `1.9955` n `190` status `ready` deltaP `10.9689` edge `0.216` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `1.9444` n `191` status `ready` deltaP `12.9009` edge `0.1874` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.7873` n `190` status `ready` deltaP `22.0633` edge `0.4917` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.7234` n `191` status `ready` deltaP `10.2784` edge `0.0706` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.5541` n `191` status `ready` deltaP `5.495` edge `0.0815` maxDD `-3.0902`
- `market_context_high->crypto_major_24h` score `0.1714` n `190` status `ready` deltaP `21.1601` edge `0.7318` maxDD `-62.3533`
- `market_context_high->index_1h` score `0.055` n `191` status `ready` deltaP `5.3438` edge `0.028` maxDD `-1.3898`
- `market_context_high->metal_4h` score `-0.0975` n `191` status `ready` deltaP `13.4969` edge `0.1564` maxDD `-11.3602`
- `market_context_high->fx_24h` score `-0.1263` n `190` status `ready` deltaP `14.817` edge `0.03` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.3412` n `191` status `ready` deltaP `6.0962` edge `0.033` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.7969` n `191` status `ready` deltaP `-0.7861` edge `0.0016` maxDD `-0.3548`
- `market_context_high->metal_24h` score `-1.3312` n `190` status `ready` deltaP `10.8578` edge `0.2068` maxDD `-23.2095`
- `market_context_high->fx_4h` score `-1.3637` n `191` status `ready` deltaP `-3.9602` edge `0.0009` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
