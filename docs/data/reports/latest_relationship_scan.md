# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T08:07:28.431257+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8682`

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

- `news_risk_high->unknown_4h` score `384.6386` n `83` status `ready` deltaP `-21.6629` edge `32.2871` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `14.4722` n `83` status `ready` deltaP `34.8791` edge `1.1114` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `13.4261` n `83` status `ready` deltaP `26.9453` edge `1.1387` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `9.8253` n `83` status `ready` deltaP `36.1781` edge `0.755` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `8.6045` n `52` status `ready` deltaP `46.7014` edge `0.4057` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.6045` n `52` status `ready` deltaP `46.7014` edge `0.4057` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.3054` n `149` status `ready` deltaP `39.99` edge `0.3947` maxDD `-0.8682`
- `news_risk_high->index_24h` score `6.0538` n `83` status `ready` deltaP `41.6081` edge `0.2447` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.2196` n `83` status `ready` deltaP `31.6432` edge `0.1861` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.6193` n `52` status `ready` deltaP `33.8408` edge `-0.0031` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.6193` n `52` status `ready` deltaP `33.8408` edge `-0.0031` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4844` n `149` status `ready` deltaP `31.0659` edge `0.0215` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.341` n `52` status `ready` deltaP `29.0338` edge `0.0365` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.341` n `52` status `ready` deltaP `29.0338` edge `0.0365` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.2407` n `149` status `ready` deltaP `25.5361` edge `0.0583` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9515` n `149` status `ready` deltaP `14.7139` edge `0.0189` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3438` n `83` status `ready` deltaP `11.4311` edge `0.0307` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3283` n `52` status `ready` deltaP `7.796` edge `0.0106` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3283` n `52` status `ready` deltaP `7.796` edge `0.0106` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.0742` n `52` status `ready` deltaP `5.2165` edge `0.0053` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
