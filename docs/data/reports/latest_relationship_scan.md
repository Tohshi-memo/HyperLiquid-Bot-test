# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T23:07:17.721660+00:00`
- Price records: `672`
- Market context records: `2085`
- Flow alert records: `7896`
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

- `market_context_high->crypto_major_4h` score `10.2767` n `195` status `ready` deltaP `36.2234` edge `0.6679` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `10.0765` n `195` status `ready` deltaP `30.4158` edge `0.7514` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `7.3996` n `195` status `ready` deltaP `24.9969` edge `0.5249` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `4.9508` n `194` status `ready` deltaP `21.5567` edge `0.8009` maxDD `-35.8966`
- `market_context_high->equity_4h` score `4.009` n `195` status `ready` deltaP `21.755` edge `0.2985` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.3407` n `195` status `ready` deltaP `17.403` edge `0.1474` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.2071` n `195` status `ready` deltaP `16.0264` edge `0.1757` maxDD `-3.2225`
- `market_context_high->index_24h` score `1.8651` n `194` status `ready` deltaP `10.6892` edge `0.207` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `1.8224` n `195` status `ready` deltaP `12.3062` edge `0.1812` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.8152` n `194` status `ready` deltaP `21.7512` edge `0.4961` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.635` n `195` status `ready` deltaP `9.6085` edge `0.0677` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.5471` n `195` status `ready` deltaP `5.4675` edge `0.0811` maxDD `-3.0902`
- `market_context_high->crypto_major_24h` score `0.2568` n `194` status `ready` deltaP `21.1625` edge `0.7389` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.0105` n `195` status `ready` deltaP `4.8242` edge `0.026` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.1378` n `194` status `ready` deltaP `14.7326` edge `0.0296` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.1918` n `195` status `ready` deltaP `12.9933` edge `0.1519` maxDD `-11.3602`
- `market_context_high->metal_1h` score `-0.4575` n `195` status `ready` deltaP `4.9578` edge `0.0309` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8396` n `195` status `ready` deltaP `-1.3043` edge `0.0015` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.3153` n `195` status `ready` deltaP `-3.4295` edge `0.0014` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.4397` n `194` status `ready` deltaP `11.0013` edge `0.1968` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
