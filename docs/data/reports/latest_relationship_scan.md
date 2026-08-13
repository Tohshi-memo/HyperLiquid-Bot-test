# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T20:37:30.552265+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `85.9321` n `153` status `ready` deltaP `-26.2868` edge `7.6275` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.7225` n `32` status `ready` deltaP `-41.6667` edge `4.6762` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.7225` n `32` status `ready` deltaP `-41.6667` edge `4.6762` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.6442` n `36` status `ready` deltaP `10.0694` edge `0.7745` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.6541` n `36` status `ready` deltaP `35.6707` edge `0.3167` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.5246` n `32` status `ready` deltaP `31.5972` edge `0.1664` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.5246` n `32` status `ready` deltaP `31.5972` edge `0.1664` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.8706` n `32` status `ready` deltaP `20.1982` edge `0.1228` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8706` n `32` status `ready` deltaP `20.1982` edge `0.1228` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `2.5404` n `153` status `ready` deltaP `21.1397` edge `0.1511` maxDD `-2.4263`
- `news_risk_high->index_24h` score `2.451` n `36` status `ready` deltaP `15.2778` edge `0.1024` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.6936` n `32` status `ready` deltaP `19.2708` edge `0.0311` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.6936` n `32` status `ready` deltaP `19.2708` edge `0.0311` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.6275` n `36` status `ready` deltaP `19.1565` edge `0.0211` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.5848` n `153` status `ready` deltaP `17.2366` edge `0.081` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.5488` n `36` status `ready` deltaP `7.3853` edge `0.1117` maxDD `-0.5496`
- `risk_on_high->crypto_major_24h` score `1.344` n `32` status `ready` deltaP `13.0208` edge `0.2011` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.344` n `32` status `ready` deltaP `13.0208` edge `0.2011` maxDD `-6.2481`
- `risk_on_high->commodity_1h` score `1.2862` n `32` status `ready` deltaP `13.8099` edge `0.0384` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2862` n `32` status `ready` deltaP `13.8099` edge `0.0384` maxDD `-0.1957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
