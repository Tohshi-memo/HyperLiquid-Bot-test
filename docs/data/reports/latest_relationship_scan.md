# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T00:22:17.056058+00:00`
- Price records: `672`
- Market context records: `2091`
- Flow alert records: `7912`
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

- `market_context_high->crypto_alt_4h` score `10.3999` n `190` status `ready` deltaP `30.6787` edge `0.7766` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.3933` n `190` status `ready` deltaP `36.6752` edge `0.6746` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `7.0629` n `190` status `ready` deltaP `24.4031` edge `0.5008` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `4.1544` n `189` status `ready` deltaP `22.0263` edge `0.7314` maxDD `-35.8966`
- `market_context_high->equity_4h` score `4.1119` n `190` status `ready` deltaP `21.9464` edge `0.3058` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.4925` n `190` status `ready` deltaP `18.4002` edge `0.1534` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.3115` n `190` status `ready` deltaP `16.4608` edge `0.1815` maxDD `-3.2225`
- `market_context_high->index_24h` score `2.0272` n `189` status `ready` deltaP `11.0361` edge `0.2182` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `1.9824` n `190` status `ready` deltaP `13.0901` edge `0.1893` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.7874` n `189` status `ready` deltaP `22.1389` edge `0.4912` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.7857` n `190` status `ready` deltaP `10.6367` edge `0.0734` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.6052` n `190` status `ready` deltaP `5.8037` edge `0.0837` maxDD `-3.0902`
- `market_context_high->crypto_major_24h` score `0.1542` n `189` status `ready` deltaP `21.1549` edge `0.7304` maxDD `-62.3533`
- `market_context_high->index_1h` score `0.0962` n `190` status `ready` deltaP `5.6634` edge `0.0293` maxDD `-1.3898`
- `market_context_high->metal_4h` score `-0.1143` n `190` status `ready` deltaP `13.4371` edge `0.1554` maxDD `-11.3602`
- `market_context_high->fx_24h` score `-0.1237` n `189` status `ready` deltaP `14.8341` edge `0.0301` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.3178` n `190` status `ready` deltaP `6.2386` edge `0.034` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.7889` n `190` status `ready` deltaP `-0.6713` edge `0.0015` maxDD `-0.3548`
- `market_context_high->metal_24h` score `-1.3069` n `189` status `ready` deltaP `10.8164` edge `0.2091` maxDD `-23.2095`
- `market_context_high->fx_4h` score `-1.3864` n `190` status `ready` deltaP `-4.2138` edge `0.0007` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
