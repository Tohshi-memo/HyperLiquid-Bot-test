# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T12:37:28.969690+00:00`
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

- `news_risk_high->unknown_4h` score `14.471` n `51` status `ready` deltaP `26.088` edge `1.0366` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `4.8917` n `33` status `ready` deltaP `-8.7779` edge `0.7305` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `4.8917` n `33` status `ready` deltaP `-8.7779` edge `0.7305` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.5633` n `51` status `ready` deltaP `19.0295` edge `0.2005` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `2.8792` n `51` status `ready` deltaP `34.1194` edge `0.0259` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.7307` n `51` status `ready` deltaP `23.2694` edge `0.1497` maxDD `-2.1818`
- `risk_on_high->metal_4h` score `2.3046` n `33` status `ready` deltaP `30.5617` edge `-0.0029` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.3046` n `33` status `ready` deltaP `30.5617` edge `-0.0029` maxDD `-0.0367`
- `risk_on_high->equity_4h` score `1.6121` n `33` status `ready` deltaP `-1.686` edge `0.261` maxDD `-0.7794`
- `risk_on_and_context->equity_4h` score `1.6121` n `33` status `ready` deltaP `-1.686` edge `0.261` maxDD `-0.7794`
- `market_context_high->crypto_alt_4h` score `1.5413` n `128` status `ready` deltaP `9.4131` edge `0.2125` maxDD `-7.0785`
- `market_context_high->unknown_1h` score `1.2942` n `128` status `ready` deltaP `6.9891` edge `0.1061` maxDD `-1.5876`
- `news_risk_high->fx_1h` score `1.1751` n `51` status `ready` deltaP `16.2469` edge `0.0066` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `1.0267` n `128` status `ready` deltaP `21.7988` edge `-0.0426` maxDD `-0.3736`
- `news_risk_high->equity_1h` score `0.7184` n `51` status `ready` deltaP `16.2469` edge `0.0203` maxDD `-0.9204`
- `market_context_high->commodity_24h` score `0.6845` n `110` status `ready` deltaP `-0.3315` edge `0.1067` maxDD `-0.7961`
- `risk_on_high->fx_4h` score `0.658` n `33` status `ready` deltaP `15.5811` edge `0.0037` maxDD `-0.1905`
- `risk_on_and_context->fx_4h` score `0.658` n `33` status `ready` deltaP `15.5811` edge `0.0037` maxDD `-0.1905`
- `news_risk_high->index_4h` score `0.5874` n `51` status `ready` deltaP `10.3479` edge `0.0197` maxDD `-0.1788`
- `risk_on_high->index_4h` score `0.4328` n `33` status `ready` deltaP `9.1002` edge `0.0428` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
