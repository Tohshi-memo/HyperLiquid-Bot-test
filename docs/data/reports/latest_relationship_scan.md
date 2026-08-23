# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T10:45:27.859371+00:00`
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

- `news_risk_high->unknown_4h` score `14.6212` n `51` status `ready` deltaP `26.2404` edge `1.0481` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `4.9766` n `33` status `ready` deltaP `-8.3288` edge `0.7384` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `4.9766` n `33` status `ready` deltaP `-8.3288` edge `0.7384` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.694` n `51` status `ready` deltaP `19.4786` edge `0.2084` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `2.8354` n `51` status `ready` deltaP `33.6621` edge `0.0253` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.7899` n `51` status `ready` deltaP `23.5743` edge `0.1526` maxDD `-2.1818`
- `risk_on_high->metal_4h` score `2.3936` n `33` status `ready` deltaP `31.6288` edge `-0.0026` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.3936` n `33` status `ready` deltaP `31.6288` edge `-0.0026` maxDD `-0.0367`
- `risk_on_high->equity_4h` score `1.6506` n `33` status `ready` deltaP `-1.3811` edge `0.2639` maxDD `-0.7794`
- `risk_on_and_context->equity_4h` score `1.6506` n `33` status `ready` deltaP `-1.3811` edge `0.2639` maxDD `-0.7794`
- `market_context_high->crypto_alt_4h` score `1.4307` n `126` status `ready` deltaP `8.9915` edge `0.2061` maxDD `-7.0785`
- `market_context_high->unknown_1h` score `1.4249` n `128` status `ready` deltaP `7.4382` edge `0.114` maxDD `-1.5876`
- `news_risk_high->fx_1h` score `1.1871` n `51` status `ready` deltaP `16.3966` edge `0.0066` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `1.1221` n `126` status `ready` deltaP `21.852` edge `-0.035` maxDD `-0.3736`
- `market_context_high->commodity_24h` score `0.9308` n `108` status `ready` deltaP `1.6204` edge `0.1141` maxDD `-0.7869`
- `news_risk_high->equity_1h` score `0.7761` n `51` status `ready` deltaP `17.1451` edge `0.0217` maxDD `-0.9204`
- `news_risk_high->index_4h` score `0.6788` n `51` status `ready` deltaP `11.415` edge `0.0202` maxDD `-0.1788`
- `risk_on_high->fx_4h` score `0.6295` n `33` status `ready` deltaP `15.1238` edge `0.0031` maxDD `-0.1905`
- `risk_on_and_context->fx_4h` score `0.6295` n `33` status `ready` deltaP `15.1238` edge `0.0031` maxDD `-0.1905`
- `risk_on_high->index_4h` score `0.4922` n `33` status `ready` deltaP `10.1673` edge `0.0433` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
