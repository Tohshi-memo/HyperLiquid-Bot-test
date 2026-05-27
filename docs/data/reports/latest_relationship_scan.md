# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T23:37:15.541701+00:00`
- Price records: `672`
- Market context records: `2087`
- Flow alert records: `7902`
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

- `market_context_high->crypto_major_4h` score `10.3441` n `193` status `ready` deltaP `36.4061` edge `0.6723` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `10.2219` n `193` status `ready` deltaP `30.5241` edge `0.7628` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `7.2561` n `193` status `ready` deltaP `24.7631` edge `0.5145` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `4.6337` n `192` status `ready` deltaP `21.747` edge `0.7732` maxDD `-35.8966`
- `market_context_high->equity_4h` score `4.0416` n `193` status `ready` deltaP `21.7427` edge `0.3013` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.4423` n `193` status `ready` deltaP `18.2374` edge `0.1503` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.2286` n `193` status `ready` deltaP `15.9644` edge `0.1779` maxDD `-3.2225`
- `market_context_high->index_24h` score `1.9268` n `192` status `ready` deltaP `10.8311` edge `0.2112` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `1.8394` n `193` status `ready` deltaP `12.2336` edge `0.1831` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.7834` n `192` status `ready` deltaP `21.9092` edge `0.4924` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.6262` n `193` status `ready` deltaP `9.5731` edge `0.0672` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.5757` n `193` status `ready` deltaP `5.5552` edge `0.0829` maxDD `-3.0902`
- `market_context_high->crypto_major_24h` score `0.1994` n `192` status `ready` deltaP `21.165` edge `0.7341` maxDD `-62.3533`
- `market_context_high->index_1h` score `0.0186` n `193` status `ready` deltaP `5.0829` edge `0.0267` maxDD `-1.3898`
- `market_context_high->metal_4h` score `-0.1101` n `193` status `ready` deltaP `13.6097` edge `0.1546` maxDD `-11.3602`
- `market_context_high->fx_24h` score `-0.1306` n `192` status `ready` deltaP `14.7779` edge `0.0299` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.3992` n `193` status `ready` deltaP `5.5211` edge `0.032` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8266` n `193` status `ready` deltaP `-1.1573` edge `0.0016` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.3312` n `193` status `ready` deltaP `-3.6135` edge `0.0013` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.3899` n `192` status `ready` deltaP `10.9339` edge `0.2014` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
