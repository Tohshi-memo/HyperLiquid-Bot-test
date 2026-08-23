# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T10:37:25.665841+00:00`
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

- `news_risk_high->unknown_4h` score `14.6454` n `51` status `ready` deltaP `26.3929` edge `1.0491` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `4.9875` n `33` status `ready` deltaP `-8.1791` edge `0.7388` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `4.9875` n `33` status `ready` deltaP `-8.1791` edge `0.7388` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.7108` n `51` status `ready` deltaP `19.6283` edge `0.2088` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `2.8488` n `51` status `ready` deltaP `33.8146` edge `0.0254` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.8081` n `51` status `ready` deltaP `23.7267` edge `0.1531` maxDD `-2.1818`
- `risk_on_high->metal_4h` score `2.3936` n `33` status `ready` deltaP `31.6288` edge `-0.0026` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.3936` n `33` status `ready` deltaP `31.6288` edge `-0.0026` maxDD `-0.0367`
- `risk_on_high->equity_4h` score `1.6624` n `33` status `ready` deltaP `-1.2287` edge `0.2644` maxDD `-0.7794`
- `risk_on_and_context->equity_4h` score `1.6624` n `33` status `ready` deltaP `-1.2287` edge `0.2644` maxDD `-0.7794`
- `market_context_high->unknown_1h` score `1.4417` n `128` status `ready` deltaP `7.5879` edge `0.1144` maxDD `-1.5876`
- `market_context_high->crypto_alt_4h` score `1.2659` n `125` status `ready` deltaP `8.7756` edge `0.1938` maxDD `-7.0785`
- `news_risk_high->fx_1h` score `1.1871` n `51` status `ready` deltaP `16.3966` edge `0.0066` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `1.1219` n `125` status `ready` deltaP `21.9537` edge `-0.0357` maxDD `-0.3736`
- `market_context_high->commodity_24h` score `0.932` n `108` status `ready` deltaP `1.6204` edge `0.1142` maxDD `-0.7869`
- `news_risk_high->equity_1h` score `0.7846` n `51` status `ready` deltaP `17.2948` edge `0.0218` maxDD `-0.9204`
- `news_risk_high->index_4h` score `0.68` n `51` status `ready` deltaP `11.415` edge `0.0203` maxDD `-0.1788`
- `risk_on_high->fx_4h` score `0.6383` n `33` status `ready` deltaP `15.2763` edge `0.0032` maxDD `-0.1905`
- `risk_on_and_context->fx_4h` score `0.6383` n `33` status `ready` deltaP `15.2763` edge `0.0032` maxDD `-0.1905`
- `risk_on_high->index_4h` score `0.493` n `33` status `ready` deltaP `10.1673` edge `0.0434` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
