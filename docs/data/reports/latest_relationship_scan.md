# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T02:07:23.577903+00:00`
- Price records: `672`
- Market context records: `2098`
- Flow alert records: `7933`
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

- `market_context_high->crypto_alt_4h` score `10.6309` n `183` status `ready` deltaP `31.0009` edge `0.7937` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.4668` n `183` status `ready` deltaP `37.2793` edge `0.6767` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.0216` n `183` status `ready` deltaP `23.8222` edge `0.4179` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.1233` n `183` status `ready` deltaP `22.3894` edge `0.3038` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.9885` n `182` status `ready` deltaP `22.6472` edge `0.6301` maxDD `-35.8966`
- `market_context_high->index_4h` score `2.5295` n `183` status `ready` deltaP `18.7425` edge `0.1542` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.2992` n `183` status `ready` deltaP `16.1276` edge `0.1827` maxDD `-3.2225`
- `market_context_high->index_24h` score `2.2134` n `182` status `ready` deltaP `11.4738` edge `0.2308` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `2.113` n `183` status `ready` deltaP `13.2833` edge `0.1989` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.6665` n `182` status `ready` deltaP `22.6377` edge `0.4778` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.8682` n `183` status `ready` deltaP `11.0681` edge `0.0774` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.4475` n `183` status `ready` deltaP `5.723` edge `0.0711` maxDD `-3.0902`
- `market_context_high->metal_4h` score `0.2277` n `183` status `ready` deltaP `13.9835` edge `0.1613` maxDD `-10.8438`
- `market_context_high->index_1h` score `0.2005` n `183` status `ready` deltaP `6.6065` edge `0.0317` maxDD `-1.3898`
- `market_context_high->crypto_major_24h` score `0.0725` n `182` status `ready` deltaP `21.0636` edge `0.7242` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.118` n `182` status `ready` deltaP `14.9055` edge `0.0301` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.2027` n `183` status `ready` deltaP `6.883` edge `0.0393` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8433` n `183` status `ready` deltaP `-1.3211` edge `0.0013` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-0.9964` n `183` status `ready` deltaP `-5.761` edge `-0.0012` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.147` n `182` status `ready` deltaP `10.4605` edge `0.2248` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
