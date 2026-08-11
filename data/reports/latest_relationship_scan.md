# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T11:07:47.403920+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_24h` score `47.0734` n `127` status `ready` deltaP `-18.7803` edge `4.2934` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `2.888` n `32` status `ready` deltaP `18.8262` edge `0.1334` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.888` n `32` status `ready` deltaP `18.8262` edge `0.1334` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `1.6474` n `127` status `ready` deltaP `11.9516` edge `0.1463` maxDD `-3.0953`
- `risk_on_high->commodity_1h` score `1.3235` n `32` status `ready` deltaP `13.5105` edge `0.0435` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3235` n `32` status `ready` deltaP `13.5105` edge `0.0435` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9743` n `32` status `ready` deltaP `11.2043` edge `0.0206` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9743` n `32` status `ready` deltaP `11.2043` edge `0.0206` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.9534` n `181` status `ready` deltaP `11.9719` edge `0.0711` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8642` n `181` status `ready` deltaP `11.0588` edge `0.032` maxDD `-0.6965`
- `market_context_high->fx_24h` score `0.4602` n `127` status `ready` deltaP `16.1942` edge `0.0318` maxDD `-1.4613`
- `risk_on_high->index_1h` score `0.2104` n `32` status `ready` deltaP `8.6078` edge `0.0071` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2104` n `32` status `ready` deltaP `8.6078` edge `0.0071` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.1873` n `32` status `ready` deltaP `5.3518` edge `0.0027` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.1873` n `32` status `ready` deltaP `5.3518` edge `0.0027` maxDD `-0.1547`
- `market_context_high->fx_1h` score `-0.0683` n `181` status `ready` deltaP `4.9029` edge `0.0009` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.124` n `181` status `ready` deltaP `5.8003` edge `0.0059` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.5029` n `32` status `ready` deltaP `-1.4482` edge `0.0034` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.5029` n `32` status `ready` deltaP `-1.4482` edge `0.0034` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.8198` n `32` status `ready` deltaP `-4.9588` edge `-0.0177` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
