# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T15:07:39.086022+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `23.3552` n `134` status `ready` deltaP `-20.1027` edge `2.3257` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `2.9756` n `32` status `ready` deltaP `19.7409` edge `0.1346` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9756` n `32` status `ready` deltaP `19.7409` edge `0.1346` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.3547` n `32` status `ready` deltaP `13.6602` edge `0.0451` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3547` n `32` status `ready` deltaP `13.6602` edge `0.0451` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `1.085` n `32` status `ready` deltaP `12.4238` edge `0.0217` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.085` n `32` status `ready` deltaP `12.4238` edge `0.0217` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.9821` n `182` status `ready` deltaP `12.495` edge `0.07` maxDD `-2.7169`
- `market_context_high->commodity_24h` score `0.8722` n `134` status `ready` deltaP `10.1659` edge `0.0936` maxDD `-3.0953`
- `market_context_high->commodity_1h` score `0.8399` n `182` status `ready` deltaP `10.8443` edge `0.0314` maxDD `-0.6965`
- `market_context_high->fx_24h` score `0.2904` n `134` status `ready` deltaP `13.6643` edge `0.0269` maxDD `-1.4613`
- `risk_on_high->fx_1h` score `0.2532` n `32` status `ready` deltaP `6.1003` edge `0.0032` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2532` n `32` status `ready` deltaP `6.1003` edge `0.0032` maxDD `-0.1547`
- `risk_on_high->index_1h` score `0.2026` n `32` status `ready` deltaP `8.4581` edge `0.0071` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2026` n `32` status `ready` deltaP `8.4581` edge `0.0071` maxDD `-0.3343`
- `market_context_high->fx_1h` score `-0.043` n `182` status `ready` deltaP `5.3448` edge `0.0012` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.0708` n `182` status `ready` deltaP `6.6889` edge `0.0068` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.5219` n `32` status `ready` deltaP `-1.753` edge `0.003` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.5219` n `32` status `ready` deltaP `-1.753` edge `0.003` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.8284` n `32` status `ready` deltaP `-4.9588` edge `-0.0188` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
