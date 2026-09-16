# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T23:37:27.991283+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10503`

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

- `news_risk_high->unknown_4h` score `372.1308` n `83` status `ready` deltaP `-20.9007` edge `31.2397` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `17.8376` n `83` status `ready` deltaP `40.7819` edge `1.3525` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `16.3043` n `83` status `ready` deltaP `32.848` edge `1.3392` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `12.5355` n `83` status `ready` deltaP `42.0809` edge `0.9415` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `7.0343` n `52` status `ready` deltaP `40.7986` edge `0.3142` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0343` n `52` status `ready` deltaP `40.7986` edge `0.3142` maxDD `0.0`
- `news_risk_high->index_24h` score `6.826` n `83` status `ready` deltaP `47.5109` edge `0.2697` maxDD `-0.075`
- `market_context_high->commodity_24h` score `5.7351` n `149` status `ready` deltaP `34.0872` edge `0.3032` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `5.0782` n `83` status `ready` deltaP `32.6849` edge `0.2507` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.424` n `52` status `ready` deltaP `32.1047` edge `-0.0078` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.424` n `52` status `ready` deltaP `32.1047` edge `-0.0078` maxDD `-0.0054`
- `risk_on_high->commodity_4h` score `2.3704` n `52` status `ready` deltaP `29.4911` edge `0.0359` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.3704` n `52` status `ready` deltaP `29.4911` edge `0.0359` maxDD `-0.1313`
- `market_context_high->fx_24h` score `2.2891` n `149` status `ready` deltaP `29.3298` edge `0.0168` maxDD `-0.0593`
- `market_context_high->commodity_4h` score `2.2701` n `149` status `ready` deltaP `25.9934` edge `0.0577` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9827` n `149` status `ready` deltaP `15.0133` edge `0.0195` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.395` n `83` status `ready` deltaP `12.0408` edge `0.0332` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3594` n `52` status `ready` deltaP `8.0954` edge `0.0112` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3594` n `52` status `ready` deltaP `8.0954` edge `0.0112` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1872` n `52` status `ready` deltaP `6.8632` edge `0.0088` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
