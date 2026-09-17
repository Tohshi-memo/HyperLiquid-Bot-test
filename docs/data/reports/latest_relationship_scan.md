# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T07:07:28.804779+00:00`
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

- `news_risk_high->unknown_4h` score `384.6748` n `83` status `ready` deltaP `-21.5105` edge `32.2891` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `14.9238` n `83` status `ready` deltaP `35.5735` edge `1.1444` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `13.7624` n `83` status `ready` deltaP `27.6397` edge `1.1621` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `10.1065` n `83` status `ready` deltaP `36.8725` edge `0.7738` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `8.4338` n `52` status `ready` deltaP `46.0069` edge `0.3961` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.4338` n `52` status `ready` deltaP `46.0069` edge `0.3961` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.1346` n `149` status `ready` deltaP `39.2955` edge `0.3851` maxDD `-0.8682`
- `news_risk_high->index_24h` score `6.1394` n `83` status `ready` deltaP `42.3026` edge `0.2472` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.3302` n `83` status `ready` deltaP `31.9905` edge `0.193` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.6205` n `52` status `ready` deltaP `33.8408` edge `-0.003` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.6205` n `52` status `ready` deltaP `33.8408` edge `-0.003` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4856` n `149` status `ready` deltaP `31.0659` edge `0.0216` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.2634` n `52` status `ready` deltaP `28.424` edge `0.0341` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2634` n `52` status `ready` deltaP `28.424` edge `0.0341` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.1632` n `149` status `ready` deltaP `24.9263` edge `0.0559` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9372` n `149` status `ready` deltaP `14.5642` edge `0.0187` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3825` n `83` status `ready` deltaP `12.0408` edge `0.0316` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3139` n `52` status `ready` deltaP `7.6463` edge `0.0104` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3139` n `52` status `ready` deltaP `7.6463` edge `0.0104` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1163` n `52` status `ready` deltaP `5.8153` edge `0.0067` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
