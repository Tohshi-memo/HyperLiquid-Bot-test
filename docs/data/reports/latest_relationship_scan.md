# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T08:07:38.634768+00:00`
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

- `news_risk_high->equity_4h` score `6.9732` n `36` status `ready` deltaP `37.5` edge `0.3311` maxDD `0.0`
- `risk_on_high->commodity_24h` score `2.9373` n `32` status `ready` deltaP `22.9167` edge `0.092` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.9373` n `32` status `ready` deltaP `22.9167` edge `0.092` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.2563` n `32` status `ready` deltaP `15.625` edge `0.1021` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.2563` n `32` status `ready` deltaP `15.625` edge `0.1021` maxDD `-0.1258`
- `risk_on_high->fx_24h` score `2.085` n `32` status `ready` deltaP `23.2639` edge `0.0371` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `2.085` n `32` status `ready` deltaP `23.2639` edge `0.0371` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.9372` n `36` status `ready` deltaP `22.0528` edge `0.0276` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6051` n `36` status `ready` deltaP `7.9841` edge `0.1124` maxDD `-0.5496`
- `risk_on_high->crypto_major_24h` score `1.5317` n `32` status `ready` deltaP `13.5417` edge `0.2217` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.5317` n `32` status `ready` deltaP `13.5417` edge `0.2217` maxDD `-6.2481`
- `risk_on_high->commodity_1h` score `1.1065` n `32` status `ready` deltaP `12.0135` edge `0.0354` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1065` n `32` status `ready` deltaP `12.0135` edge `0.0354` maxDD `-0.1957`
- `market_context_high->commodity_4h` score `1.0748` n `161` status `ready` deltaP `13.2764` edge `0.0649` maxDD `-2.1077`
- `market_context_high->commodity_24h` score `0.9684` n `161` status `ready` deltaP `12.9788` edge `0.0745` maxDD `-2.4263`
- `risk_on_high->fx_4h` score `0.8989` n `32` status `ready` deltaP `10.4421` edge `0.0194` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8989` n `32` status `ready` deltaP `10.4421` edge `0.0194` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.8326` n `161` status `ready` deltaP `10.3442` edge `0.0301` maxDD `-0.3742`
- `risk_on_high->index_1h` score `0.2376` n `32` status `ready` deltaP `9.0569` edge `0.0076` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2376` n `32` status `ready` deltaP `9.0569` edge `0.0076` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
