# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T01:37:28.779340+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->unknown_4h` score `35.634` n `149` status `ready` deltaP `-0.311` edge `2.9949` maxDD `-0.5326`
- `news_risk_high->unknown_4h` score `24.1014` n `68` status `ready` deltaP `-4.9498` edge `2.0623` maxDD `-0.3345`
- `risk_on_high->unknown_4h` score `9.5127` n `52` status `ready` deltaP `-7.5516` edge `0.8656` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.5127` n `52` status `ready` deltaP `-7.5516` edge `0.8656` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.052` n `52` status `ready` deltaP `50.0` edge `0.421` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.052` n `52` status `ready` deltaP `50.0` edge `0.421` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.2018` n `44` status `ready` deltaP `29.9085` edge `0.622` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.7529` n `149` status `ready` deltaP `43.2886` edge `0.41` maxDD `-0.8682`
- `news_risk_high->index_24h` score `3.7485` n `44` status `ready` deltaP `26.5625` edge `0.1529` maxDD `-0.075`
- `news_risk_high->equity_24h` score `3.4194` n `44` status `ready` deltaP `7.4495` edge `0.4127` maxDD `-6.5262`
- `risk_on_high->commodity_4h` score `3.0281` n `52` status `ready` deltaP `33.3021` edge `0.0653` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0281` n `52` status `ready` deltaP `33.3021` edge `0.0653` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.9278` n `149` status `ready` deltaP `29.8044` edge `0.0871` maxDD `-0.345`
- `risk_on_high->fx_24h` score `1.6419` n `52` status `ready` deltaP `24.6394` edge `-0.0232` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.6419` n `52` status `ready` deltaP `24.6394` edge `-0.0232` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.5071` n `149` status `ready` deltaP `21.8645` edge `0.0014` maxDD `-0.0593`
- `news_risk_high->crypto_major_24h` score `1.2749` n `44` status `ready` deltaP `1.9413` edge `0.35` maxDD `-13.2931`
- `market_context_high->commodity_1h` score `1.232` n `149` status `ready` deltaP `17.1091` edge `0.0263` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.1295` n `44` status `ready` deltaP `8.0019` edge `0.0862` maxDD `-0.6334`
- `news_risk_high->equity_4h` score `0.8743` n `68` status `ready` deltaP `11.0474` edge `0.0829` maxDD `-3.3619`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
