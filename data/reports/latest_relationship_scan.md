# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T08:22:28.892363+00:00`
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

- `news_risk_high->unknown_4h` score `384.6374` n `83` status `ready` deltaP `-21.6629` edge `32.287` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `14.3611` n `83` status `ready` deltaP `34.7055` edge `1.1033` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `13.3426` n `83` status `ready` deltaP `26.7717` edge `1.1329` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `9.7562` n `83` status `ready` deltaP `36.0045` edge `0.7504` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `8.6424` n `52` status `ready` deltaP `46.875` edge `0.4077` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.6424` n `52` status `ready` deltaP `46.875` edge `0.4077` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.3433` n `149` status `ready` deltaP `40.1636` edge `0.3967` maxDD `-0.8682`
- `news_risk_high->index_24h` score `6.0339` n `83` status `ready` deltaP `41.4345` edge `0.2442` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.2016` n `83` status `ready` deltaP `31.6432` edge `0.1846` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.6181` n `52` status `ready` deltaP `33.8408` edge `-0.0032` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.6181` n `52` status `ready` deltaP `33.8408` edge `-0.0032` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4832` n `149` status `ready` deltaP `31.0659` edge `0.0214` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.358` n `52` status `ready` deltaP `29.1862` edge `0.0369` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.358` n `52` status `ready` deltaP `29.1862` edge `0.0369` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.2577` n `149` status `ready` deltaP `25.6885` edge `0.0587` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9515` n `149` status `ready` deltaP `14.7139` edge `0.0189` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.343` n `83` status `ready` deltaP `11.4311` edge `0.0306` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3283` n `52` status `ready` deltaP `7.796` edge `0.0106` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3283` n `52` status `ready` deltaP `7.796` edge `0.0106` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.0742` n `52` status `ready` deltaP `5.2165` edge `0.0053` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
