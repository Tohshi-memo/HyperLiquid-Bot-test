# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T22:37:16.705811+00:00`
- Price records: `672`
- Market context records: `2082`
- Flow alert records: `7889`
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

- `market_context_high->crypto_major_4h` score `10.1755` n `197` status `ready` deltaP `36.0383` edge `0.6607` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `9.8378` n `197` status `ready` deltaP `29.5932` edge `0.737` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `7.4703` n `197` status `ready` deltaP `24.9211` edge `0.5313` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `5.2474` n `196` status `ready` deltaP `21.3633` edge `0.8269` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.8869` n `197` status `ready` deltaP `21.0536` edge `0.293` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.2577` n `197` status `ready` deltaP `16.8905` edge `0.1439` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.1242` n `197` status `ready` deltaP `15.5149` edge `0.1722` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.8226` n `196` status `ready` deltaP `21.5893` edge `0.4978` maxDD `-33.1875`
- `market_context_high->index_24h` score `1.8006` n `196` status `ready` deltaP `10.543` edge `0.2026` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `1.7966` n `197` status `ready` deltaP `12.163` edge `0.18` maxDD `-4.9097`
- `market_context_high->equity_1h` score `0.6277` n `197` status `ready` deltaP `9.6371` edge `0.0669` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.4874` n `197` status `ready` deltaP `5.2319` edge `0.0777` maxDD `-3.0902`
- `market_context_high->crypto_major_24h` score `0.2981` n `196` status `ready` deltaP `21.1531` edge `0.7424` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.0729` n `197` status `ready` deltaP `4.2099` edge `0.0249` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.148` n `196` status `ready` deltaP `14.6812` edge `0.0291` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.2469` n `197` status `ready` deltaP `12.6942` edge `0.1493` maxDD `-11.3602`
- `market_context_high->metal_1h` score `-0.5553` n `197` status `ready` deltaP `4.5556` edge `0.0296` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8704` n `197` status `ready` deltaP `-1.6596` edge `0.0013` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.3309` n `197` status `ready` deltaP `-3.6105` edge `0.0013` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.4926` n `196` status `ready` deltaP `11.0603` edge `0.192` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
