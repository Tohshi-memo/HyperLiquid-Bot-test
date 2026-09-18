# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T01:22:28.003519+00:00`
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

- `market_context_high->unknown_4h` score `35.64` n `149` status `ready` deltaP `-0.311` edge `2.9954` maxDD `-0.5326`
- `news_risk_high->unknown_4h` score `23.9896` n `68` status `ready` deltaP `-4.9498` edge `2.058` maxDD `-0.7362`
- `risk_on_high->unknown_4h` score `9.5187` n `52` status `ready` deltaP `-7.5516` edge `0.8661` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.5187` n `52` status `ready` deltaP `-7.5516` edge `0.8661` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.0604` n `52` status `ready` deltaP `50.0` edge `0.4217` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.0604` n `52` status `ready` deltaP `50.0` edge `0.4217` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.3709` n `45` status `ready` deltaP `30.3125` edge `0.6334` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.7613` n `149` status `ready` deltaP `43.2886` edge `0.4107` maxDD `-0.8682`
- `news_risk_high->index_24h` score `3.8338` n `45` status `ready` deltaP `27.1181` edge `0.1563` maxDD `-0.075`
- `news_risk_high->equity_24h` score `3.6432` n `45` status `ready` deltaP `8.6111` edge `0.4236` maxDD `-6.5262`
- `risk_on_high->commodity_4h` score `3.0293` n `52` status `ready` deltaP `33.3021` edge `0.0654` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0293` n `52` status `ready` deltaP `33.3021` edge `0.0654` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.929` n `149` status `ready` deltaP `29.8044` edge `0.0872` maxDD `-0.345`
- `risk_on_high->fx_24h` score `1.6618` n `52` status `ready` deltaP `24.813` edge `-0.0227` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.6618` n `52` status `ready` deltaP `24.813` edge `-0.0227` maxDD `-0.0054`
- `news_risk_high->crypto_major_24h` score `1.5489` n `45` status `ready` deltaP `2.9514` edge `0.3784` maxDD `-13.2931`
- `market_context_high->fx_24h` score `1.527` n `149` status `ready` deltaP `22.0381` edge `0.0019` maxDD `-0.0593`
- `news_risk_high->metal_24h` score `1.2624` n `45` status `ready` deltaP `9.0625` edge `0.0902` maxDD `-0.6334`
- `market_context_high->commodity_1h` score `1.2463` n `149` status `ready` deltaP `17.2588` edge `0.0265` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.8971` n `68` status `ready` deltaP `11.0474` edge `0.0848` maxDD `-3.3619`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
