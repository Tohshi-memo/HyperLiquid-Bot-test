# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T15:07:26.207850+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14776`

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

- `news_risk_high->unknown_4h` score `13.8961` n `51` status `ready` deltaP `25.0209` edge `0.9958` maxDD `-0.0348`
- `risk_on_high->unknown_1h` score `4.7814` n `33` status `ready` deltaP `-9.6761` edge `0.7224` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `4.7814` n `33` status `ready` deltaP `-9.6761` edge `0.7224` maxDD `-1.5916`
- `news_risk_high->unknown_1h` score `3.3783` n `51` status `ready` deltaP `18.1313` edge `0.1911` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `2.9803` n `51` status `ready` deltaP `35.339` edge `0.0262` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.6974` n `51` status `ready` deltaP `23.2694` edge `0.1467` maxDD `-2.164`
- `risk_on_high->metal_4h` score `2.2876` n `33` status `ready` deltaP `30.4093` edge `-0.0033` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.2876` n `33` status `ready` deltaP `30.4093` edge `-0.0033` maxDD `-0.0367`
- `risk_on_high->equity_4h` score `1.5816` n `33` status `ready` deltaP `-1.686` edge `0.257` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `1.5816` n `33` status `ready` deltaP `-1.686` edge `0.257` maxDD `-0.773`
- `news_risk_high->fx_1h` score `1.1763` n `51` status `ready` deltaP `16.2469` edge `0.0067` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.1297` n `129` status `ready` deltaP `6.321` edge `0.0969` maxDD `-1.5916`
- `market_context_high->crypto_alt_4h` score `1.0421` n `128` status `ready` deltaP `8.6509` edge `0.1756` maxDD `-7.0478`
- `news_risk_high->equity_1h` score `0.727` n `51` status `ready` deltaP `16.3966` edge `0.0203` maxDD `-0.9128`
- `risk_on_high->fx_4h` score `0.7238` n `33` status `ready` deltaP `16.8007` edge `0.004` maxDD `-0.1905`
- `risk_on_and_context->fx_4h` score `0.7238` n `33` status `ready` deltaP `16.8007` edge `0.004` maxDD `-0.1905`
- `market_context_high->commodity_24h` score `0.514` n `112` status `ready` deltaP `-1.5129` edge `0.1004` maxDD `-0.7984`
- `news_risk_high->index_4h` score `0.4972` n `51` status `ready` deltaP `9.2808` edge `0.0193` maxDD `-0.1788`
- `market_context_high->unknown_4h` score `0.418` n `128` status `ready` deltaP `20.7317` edge `-0.0862` maxDD `-0.3741`
- `risk_on_high->index_4h` score `0.3742` n `33` status `ready` deltaP `8.0331` edge `0.0424` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
