# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T07:37:29.389502+00:00`
- Price records: `672`
- Market context records: `5123`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5560`

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

- `market_context_high->unknown_24h` score `26.2192` n `67` status `ready` deltaP `28.8583` edge `2.0268` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.4367` n `126` status `ready` deltaP `7.9817` edge `0.714` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.0972` n `117` status `ready` deltaP `20.3031` edge `0.5583` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.359` n `117` status `ready` deltaP `15.1645` edge `0.5054` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.751` n `117` status `ready` deltaP `12.9052` edge `0.4558` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `0.9152` n `126` status `ready` deltaP `6.5583` edge `0.1287` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.7319` n `126` status `ready` deltaP `8.0411` edge `0.0667` maxDD `-2.745`
- `market_context_high->crypto_major_1h` score `0.6979` n `126` status `ready` deltaP `7.6205` edge `0.1319` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.4724` n `117` status `ready` deltaP `7.3849` edge `0.154` maxDD `-7.4425`
- `market_context_high->commodity_24h` score `0.4115` n `67` status `ready` deltaP `16.5423` edge `0.1048` maxDD `-8.319`
- `market_context_high->metal_1h` score `0.2265` n `126` status `ready` deltaP `8.0102` edge `0.0271` maxDD `-1.4501`
- `market_context_high->index_1h` score `0.0212` n `126` status `ready` deltaP `5.5556` edge `0.0151` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.4086` n `117` status `ready` deltaP `4.3581` edge `0.0303` maxDD `-2.9391`
- `market_context_high->metal_4h` score `-0.5849` n `117` status `ready` deltaP `1.8214` edge `0.0539` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.6565` n `126` status `ready` deltaP `-2.7707` edge `-0.0016` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.9341` n `126` status `ready` deltaP `0.2091` edge `-0.0023` maxDD `-2.155`
- `market_context_high->fx_4h` score `-1.0013` n `117` status `ready` deltaP `-3.2964` edge `0.0009` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.5526` n `67` status `ready` deltaP `-3.3841` edge `-0.0099` maxDD `-1.4206`
- `market_context_high->metal_24h` score `-1.8709` n `67` status `ready` deltaP `-1.3319` edge `0.1073` maxDD `-20.3954`
- `market_context_high->commodity_4h` score `-2.5918` n `117` status `ready` deltaP `-1.5375` edge `-0.031` maxDD `-7.6453`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
