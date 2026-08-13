# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T06:22:28.668422+00:00`
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

- `news_risk_high->equity_4h` score `6.7786` n `36` status `ready` deltaP `36.4329` edge `0.322` maxDD `0.0`
- `risk_on_high->commodity_24h` score `2.7496` n `32` status `ready` deltaP `21.875` edge `0.0833` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.7496` n `32` status `ready` deltaP `21.875` edge `0.0833` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.3121` n `32` status `ready` deltaP `16.0823` edge `0.1037` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.3121` n `32` status `ready` deltaP `16.0823` edge `0.1037` maxDD `-0.1258`
- `risk_on_high->fx_24h` score `2.0374` n `32` status `ready` deltaP `22.7431` edge `0.0366` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `2.0374` n `32` status `ready` deltaP `22.7431` edge `0.0366` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.8813` n `36` status `ready` deltaP `21.4431` edge `0.027` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `1.7314` n `32` status `ready` deltaP `14.7569` edge `0.2392` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.7314` n `32` status `ready` deltaP `14.7569` edge `0.2392` maxDD `-6.2481`
- `news_risk_high->equity_1h` score `1.5104` n `36` status `ready` deltaP `7.3853` edge `0.1085` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.1305` n `161` status `ready` deltaP `13.7337` edge `0.0665` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.0526` n `32` status `ready` deltaP `11.5644` edge `0.0339` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0526` n `32` status `ready` deltaP `11.5644` edge `0.0339` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9451` n `32` status `ready` deltaP `10.8994` edge `0.0202` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9451` n `32` status `ready` deltaP `10.8994` edge `0.0202` maxDD `-0.1285`
- `market_context_high->commodity_24h` score `0.7806` n `161` status `ready` deltaP `11.9371` edge `0.0658` maxDD `-2.4263`
- `market_context_high->commodity_1h` score `0.7787` n `161` status `ready` deltaP `9.8951` edge `0.0286` maxDD `-0.3742`
- `risk_on_high->index_1h` score `0.2143` n `32` status `ready` deltaP `8.6078` edge `0.0076` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2143` n `32` status `ready` deltaP `8.6078` edge `0.0076` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
