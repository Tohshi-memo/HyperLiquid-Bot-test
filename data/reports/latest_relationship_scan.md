# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T00:37:22.140654+00:00`
- Price records: `672`
- Market context records: `2092`
- Flow alert records: `7915`
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

- `market_context_high->crypto_alt_4h` score `10.453` n `189` status `ready` deltaP `30.7282` edge `0.7807` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.4111` n `189` status `ready` deltaP `36.7636` edge `0.6755` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.9499` n `189` status `ready` deltaP `24.2806` edge `0.4922` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.1316` n `189` status `ready` deltaP `22.0125` edge `0.307` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `3.9973` n `188` status `ready` deltaP `22.1178` edge `0.7177` maxDD `-35.8966`
- `market_context_high->index_4h` score `2.5063` n `189` status `ready` deltaP `18.4524` edge `0.1542` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.298` n `189` status `ready` deltaP `16.277` edge `0.1816` maxDD `-3.2225`
- `market_context_high->index_24h` score `2.0649` n `188` status `ready` deltaP `11.1021` edge `0.2209` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `2.0182` n `189` status `ready` deltaP `13.283` edge `0.191` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.7885` n `188` status `ready` deltaP `22.2134` edge `0.4908` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.8387` n `189` status `ready` deltaP `10.9987` edge `0.0754` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.6421` n `189` status `ready` deltaP `5.9659` edge `0.0857` maxDD `-3.0902`
- `market_context_high->crypto_major_24h` score `0.1392` n `188` status `ready` deltaP `21.1477` edge `0.7292` maxDD `-62.3533`
- `market_context_high->index_1h` score `0.1353` n `189` status `ready` deltaP `5.9865` edge `0.0304` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.1225` n `188` status `ready` deltaP `14.8495` edge `0.0301` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.1336` n `189` status `ready` deltaP `13.3752` edge `0.1542` maxDD `-11.3602`
- `market_context_high->metal_1h` score `-0.299` n `189` status `ready` deltaP `6.3841` edge `0.0346` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8099` n `189` status `ready` deltaP `-0.933` edge `0.0015` maxDD `-0.3548`
- `market_context_high->metal_24h` score `-1.2816` n `188` status `ready` deltaP `10.7727` edge `0.2115` maxDD `-23.2095`
- `market_context_high->fx_4h` score `-1.4093` n `189` status `ready` deltaP `-4.4699` edge `0.0005` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
