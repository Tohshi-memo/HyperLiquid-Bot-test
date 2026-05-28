# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T01:52:19.327916+00:00`
- Price records: `672`
- Market context records: `2097`
- Flow alert records: `7930`
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

- `market_context_high->crypto_alt_4h` score `10.6155` n `184` status `ready` deltaP `30.9584` edge `0.7927` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.4541` n `184` status `ready` deltaP `37.1951` edge `0.6762` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.1638` n `184` status `ready` deltaP `23.8004` edge `0.4299` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.1197` n `184` status `ready` deltaP `22.329` edge `0.3039` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `3.1568` n `183` status `ready` deltaP `22.5613` edge `0.6447` maxDD `-35.8966`
- `market_context_high->index_4h` score `2.527` n `184` status `ready` deltaP `18.697` edge `0.1543` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.3027` n `184` status `ready` deltaP `16.1709` edge `0.1827` maxDD `-3.2225`
- `market_context_high->index_24h` score `2.1919` n `183` status `ready` deltaP `11.4149` edge `0.2294` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `2.1045` n `184` status `ready` deltaP `13.3266` edge `0.1979` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.6863` n `183` status `ready` deltaP `22.5698` edge `0.4799` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.8263` n `184` status `ready` deltaP `10.6939` edge `0.0764` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.5422` n `184` status `ready` deltaP `5.796` edge `0.0785` maxDD `-3.0902`
- `market_context_high->index_1h` score `0.1686` n `184` status `ready` deltaP `6.2679` edge `0.0313` maxDD `-1.3898`
- `market_context_high->crypto_major_24h` score `0.0884` n `183` status `ready` deltaP `21.0827` edge `0.7254` maxDD `-62.3533`
- `market_context_high->metal_4h` score `0.0759` n `184` status `ready` deltaP `13.6598` edge `0.1578` maxDD `-11.0698`
- `market_context_high->fx_24h` score `-0.1184` n `183` status `ready` deltaP `14.9006` edge `0.0301` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.2451` n `184` status `ready` deltaP `6.5771` edge `0.0378` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8203` n `184` status `ready` deltaP `-1.0479` edge `0.0014` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-0.9791` n `184` status `ready` deltaP `-5.4878` edge `-0.0008` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.1735` n `183` status `ready` deltaP `10.5187` edge `0.2222` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
