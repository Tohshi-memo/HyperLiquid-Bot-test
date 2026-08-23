# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T12:22:26.298829+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_4h` score `14.5094` n `51` status `ready` deltaP `26.088` edge `1.0398` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `4.9119` n `33` status `ready` deltaP `-8.7779` edge `0.7331` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `4.9119` n `33` status `ready` deltaP `-8.7779` edge `0.7331` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.5944` n `51` status `ready` deltaP `19.0295` edge `0.2031` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `2.867` n `51` status `ready` deltaP `33.967` edge `0.0259` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.7343` n `51` status `ready` deltaP `23.2694` edge `0.15` maxDD `-2.1818`
- `risk_on_high->metal_4h` score `2.318` n `33` status `ready` deltaP `30.7142` edge `-0.0028` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.318` n `33` status `ready` deltaP `30.7142` edge `-0.0028` maxDD `-0.0367`
- `risk_on_high->equity_4h` score `1.6145` n `33` status `ready` deltaP `-1.686` edge `0.2613` maxDD `-0.7794`
- `risk_on_and_context->equity_4h` score `1.6145` n `33` status `ready` deltaP `-1.686` edge `0.2613` maxDD `-0.7794`
- `market_context_high->crypto_alt_4h` score `1.5737` n `128` status `ready` deltaP `9.4131` edge `0.2152` maxDD `-7.0785`
- `market_context_high->unknown_1h` score `1.3254` n `128` status `ready` deltaP `6.9891` edge `0.1087` maxDD `-1.5876`
- `news_risk_high->fx_1h` score `1.1871` n `51` status `ready` deltaP `16.3966` edge `0.0066` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `1.0651` n `128` status `ready` deltaP `21.7988` edge `-0.0394` maxDD `-0.3736`
- `market_context_high->commodity_24h` score `0.7808` n `109` status `ready` deltaP `0.3775` edge `0.1099` maxDD `-0.7877`
- `news_risk_high->equity_1h` score `0.7278` n `51` status `ready` deltaP `16.3966` edge `0.0205` maxDD `-0.9204`
- `risk_on_high->fx_4h` score `0.6501` n `33` status `ready` deltaP `15.4287` edge `0.0037` maxDD `-0.1905`
- `risk_on_and_context->fx_4h` score `0.6501` n `33` status `ready` deltaP `15.4287` edge `0.0037` maxDD `-0.1905`
- `news_risk_high->index_4h` score `0.6008` n `51` status `ready` deltaP `10.5003` edge `0.0198` maxDD `-0.1788`
- `risk_on_high->index_4h` score `0.4415` n `33` status `ready` deltaP `9.2526` edge `0.0429` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
