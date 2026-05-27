# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T21:52:21.785840+00:00`
- Price records: `672`
- Market context records: `2079`
- Flow alert records: `7880`
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

- `market_context_high->crypto_major_4h` score `10.0545` n `200` status `ready` deltaP `35.7561` edge `0.6525` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `9.5714` n `200` status `ready` deltaP `28.7378` edge `0.7205` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `7.2019` n `200` status `ready` deltaP `23.7561` edge `0.5167` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `5.6437` n `199` status `ready` deltaP `21.0672` edge `0.8619` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.7286` n `200` status `ready` deltaP `20.1098` edge `0.2861` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.1399` n `200` status `ready` deltaP `16.1524` edge `0.139` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.0077` n `200` status `ready` deltaP `14.8982` edge `0.1666` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.8122` n `199` status `ready` deltaP `21.3394` edge `0.4986` maxDD `-33.1875`
- `market_context_high->index_24h` score `1.702` n `199` status `ready` deltaP `10.3163` edge `0.1959` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `1.6387` n `200` status `ready` deltaP `11.5539` edge `0.1709` maxDD `-4.9097`
- `market_context_high->equity_1h` score `0.5405` n `200` status `ready` deltaP `8.9671` edge `0.0641` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.4209` n `200` status `ready` deltaP `4.8054` edge `0.075` maxDD `-3.0902`
- `market_context_high->crypto_major_24h` score `0.3787` n `199` status `ready` deltaP `21.1264` edge `0.7493` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.1311` n `200` status `ready` deltaP `3.6617` edge `0.0237` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.1658` n `199` status `ready` deltaP `14.5929` edge `0.0282` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.3314` n `200` status `ready` deltaP `12.2683` edge `0.1451` maxDD `-11.3602`
- `market_context_high->fx_1h` score `-0.6026` n `200` status `ready` deltaP `-2.2485` edge `0.0005` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.7495` n `200` status `ready` deltaP `4.1976` edge `0.0283` maxDD `-5.166`
- `market_context_high->fx_4h` score `-1.3905` n `200` status `ready` deltaP `-4.25` edge `0.0006` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.5839` n `199` status `ready` deltaP `11.1335` edge `0.1839` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
