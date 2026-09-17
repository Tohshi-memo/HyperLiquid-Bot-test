# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T07:52:30.475625+00:00`
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
- `news_risk_high->crypto_alt_24h` score `14.5881` n `83` status `ready` deltaP `35.0527` edge `1.1199` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `13.5143` n `83` status `ready` deltaP `27.1189` edge `1.1449` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `9.898` n `83` status `ready` deltaP `36.3517` edge `0.7599` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `8.5642` n `52` status `ready` deltaP `46.5278` edge `0.4035` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5642` n `52` status `ready` deltaP `46.5278` edge `0.4035` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2651` n `149` status `ready` deltaP `39.8164` edge `0.3925` maxDD `-0.8682`
- `news_risk_high->index_24h` score `6.0749` n `83` status `ready` deltaP `41.7817` edge `0.2453` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.2551` n `83` status `ready` deltaP `31.8169` edge `0.1879` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.6205` n `52` status `ready` deltaP `33.8408` edge `-0.003` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.6205` n `52` status `ready` deltaP `33.8408` edge `-0.003` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4856` n `149` status `ready` deltaP `31.0659` edge `0.0216` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.3228` n `52` status `ready` deltaP `28.8813` edge `0.036` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.3228` n `52` status `ready` deltaP `28.8813` edge `0.036` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.2225` n `149` status `ready` deltaP `25.3836` edge `0.0578` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9527` n `149` status `ready` deltaP `14.7139` edge `0.019` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3532` n `83` status `ready` deltaP `11.5835` edge `0.0309` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3295` n `52` status `ready` deltaP `7.796` edge `0.0107` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3295` n `52` status `ready` deltaP `7.796` edge `0.0107` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.0844` n `52` status `ready` deltaP `5.3662` edge `0.0056` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
