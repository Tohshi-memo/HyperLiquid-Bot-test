# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T04:22:29.944775+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11840`

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

- `news_risk_high->equity_4h` score `6.9094` n `36` status `ready` deltaP `37.3476` edge `0.3268` maxDD `0.0`
- `risk_on_high->commodity_24h` score `2.5125` n `32` status `ready` deltaP `20.4861` edge `0.0728` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.5125` n `32` status `ready` deltaP `20.4861` edge `0.0728` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.3217` n `32` status `ready` deltaP `16.0823` edge `0.1045` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.3217` n `32` status `ready` deltaP `16.0823` edge `0.1045` maxDD `-0.1258`
- `news_risk_high->index_4h` score `1.9796` n `36` status `ready` deltaP `22.3577` edge `0.0291` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `1.9374` n `32` status `ready` deltaP `15.9722` edge `0.2575` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.9374` n `32` status `ready` deltaP `15.9722` edge `0.2575` maxDD `-6.2481`
- `risk_on_high->fx_24h` score `1.9155` n `32` status `ready` deltaP `21.3542` edge `0.0357` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.9155` n `32` status `ready` deltaP `21.3542` edge `0.0357` maxDD `-0.1418`
- `news_risk_high->equity_1h` score `1.5919` n `36` status `ready` deltaP `7.9841` edge `0.1113` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.1401` n `161` status `ready` deltaP `13.7337` edge `0.0673` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.1317` n `32` status `ready` deltaP `12.4626` edge `0.0345` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1317` n `32` status `ready` deltaP `12.4626` edge `0.0345` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `1.051` n `32` status `ready` deltaP `12.1189` edge `0.0209` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.051` n `32` status `ready` deltaP `12.1189` edge `0.0209` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.8577` n `161` status `ready` deltaP `10.7933` edge `0.0292` maxDD `-0.3742`
- `market_context_high->commodity_24h` score `0.5435` n `161` status `ready` deltaP `10.5482` edge `0.0553` maxDD `-2.4263`
- `risk_on_high->index_1h` score `0.2275` n `32` status `ready` deltaP `8.7575` edge `0.0083` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2275` n `32` status `ready` deltaP `8.7575` edge `0.0083` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
