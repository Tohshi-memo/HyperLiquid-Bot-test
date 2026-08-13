# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T05:37:31.063272+00:00`
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

- `news_risk_high->equity_4h` score `6.8004` n `36` status `ready` deltaP `36.5854` edge `0.3228` maxDD `0.0`
- `risk_on_high->commodity_24h` score `2.6599` n `32` status `ready` deltaP `21.3542` edge `0.0793` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.6599` n `32` status `ready` deltaP `21.3542` edge `0.0793` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.3205` n `32` status `ready` deltaP `16.0823` edge `0.1044` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.3205` n `32` status `ready` deltaP `16.0823` edge `0.1044` maxDD `-0.1258`
- `risk_on_high->fx_24h` score `1.9921` n `32` status `ready` deltaP `22.2222` edge `0.0363` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.9921` n `32` status `ready` deltaP `22.2222` edge `0.0363` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.9007` n `36` status `ready` deltaP `21.5955` edge `0.0276` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `1.8209` n `32` status `ready` deltaP `15.2778` edge `0.2472` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.8209` n `32` status `ready` deltaP `15.2778` edge `0.2472` maxDD `-6.2481`
- `news_risk_high->equity_1h` score `1.5368` n `36` status `ready` deltaP `7.535` edge `0.1097` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.1389` n `161` status `ready` deltaP `13.7337` edge `0.0672` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.0646` n `32` status `ready` deltaP `11.7141` edge `0.0339` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0646` n `32` status `ready` deltaP `11.7141` edge `0.0339` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9841` n `32` status `ready` deltaP `11.3567` edge `0.0204` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9841` n `32` status `ready` deltaP `11.3567` edge `0.0204` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.7907` n `161` status `ready` deltaP `10.0448` edge `0.0286` maxDD `-0.3742`
- `market_context_high->commodity_24h` score `0.691` n `161` status `ready` deltaP `11.4163` edge `0.0618` maxDD `-2.4263`
- `risk_on_high->index_1h` score `0.2174` n `32` status `ready` deltaP `8.6078` edge `0.008` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2174` n `32` status `ready` deltaP `8.6078` edge `0.008` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
