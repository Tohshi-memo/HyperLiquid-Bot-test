# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T08:37:26.080521+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10695`

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

- `risk_on_high->crypto_major_24h` score `2.1647` n `97` status `ready` deltaP `14.2541` edge `0.9151` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `2.1647` n `97` status `ready` deltaP `14.2541` edge `0.9151` maxDD `-47.9416`
- `market_context_high->equity_24h` score `1.0024` n `183` status `ready` deltaP `12.6708` edge `0.3529` maxDD `-16.9737`
- `risk_on_high->index_1h` score `-0.1006` n `145` status `ready` deltaP `5.2364` edge `-0.0031` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1006` n `145` status `ready` deltaP `5.2364` edge `-0.0031` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.1122` n `145` status `ready` deltaP `8.4978` edge `0.0002` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.1122` n `145` status `ready` deltaP `8.4978` edge `0.0002` maxDD `-1.699`
- `risk_on_high->equity_1h` score `-0.4221` n `145` status `ready` deltaP `6.8026` edge `-0.012` maxDD `-2.6638`
- `risk_on_and_context->equity_1h` score `-0.4221` n `145` status `ready` deltaP `6.8026` edge `-0.012` maxDD `-2.6638`
- `risk_on_high->crypto_alt_1h` score `-0.4264` n `145` status `ready` deltaP `1.7933` edge `0.0542` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.4264` n `145` status `ready` deltaP `1.7933` edge `0.0542` maxDD `-5.4685`
- `risk_on_high->commodity_1h` score `-0.5267` n `145` status `ready` deltaP `0.954` edge `0.0001` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.5267` n `145` status `ready` deltaP `0.954` edge `0.0001` maxDD `-1.0281`
- `market_context_high->commodity_1h` score `-0.6915` n `250` status `ready` deltaP `1.3126` edge `-0.0014` maxDD `-1.5315`
- `risk_on_high->crypto_major_1h` score `-0.7718` n `145` status `ready` deltaP `1.2802` edge `0.0226` maxDD `-7.4065`
- `risk_on_and_context->crypto_major_1h` score `-0.7718` n `145` status `ready` deltaP `1.2802` edge `0.0226` maxDD `-7.4065`
- `market_context_high->metal_1h` score `-0.9103` n `250` status `ready` deltaP `3.9461` edge `-0.0064` maxDD `-2.9947`
- `market_context_high->index_1h` score `-1.05` n `250` status `ready` deltaP `3.3054` edge `0.0009` maxDD `-3.1683`
- `market_context_high->index_4h` score `-1.2026` n `245` status `ready` deltaP `5.8008` edge `0.0008` maxDD `-5.825`
- `market_context_high->equity_1h` score `-1.2937` n `250` status `ready` deltaP `4.6647` edge `-0.0224` maxDD `-7.2983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
