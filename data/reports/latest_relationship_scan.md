# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T09:37:27.010797+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6505`

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

- `market_context_high->unknown_24h` score `7032.549` n `55` status `ready` deltaP `3.4722` edge `586.0226` maxDD `0.0`
- `market_context_high->unknown_4h` score `374.0523` n `55` status `ready` deltaP `5.3464` edge `31.1397` maxDD `-0.0124`
- `news_risk_high->unknown_1h` score `59.7563` n `118` status `ready` deltaP `-6.4168` edge `5.0511` maxDD `-0.9571`
- `market_context_high->unknown_1h` score `58.8592` n `55` status `ready` deltaP `3.0131` edge `4.8959` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.4611` n `55` status `ready` deltaP `44.8832` edge `1.5128` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `12.8684` n `98` status `ready` deltaP `29.6379` edge `1.0104` maxDD `-6.8493`
- `market_context_high->index_24h` score `7.1286` n `55` status `ready` deltaP `58.5069` edge `0.204` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.6076` n `55` status `ready` deltaP `45.9628` edge `0.2753` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.6891` n `55` status `ready` deltaP `22.6829` edge `0.3523` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.3675` n `55` status `ready` deltaP `29.673` edge `0.2831` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `4.7741` n `108` status `ready` deltaP `17.6829` edge `0.4186` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `3.3695` n `55` status `ready` deltaP `31.5244` edge `0.0957` maxDD `-0.3387`
- `market_context_high->equity_4h` score `3.3066` n `55` status `ready` deltaP `5.4379` edge `0.3095` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.4572` n `55` status `ready` deltaP `10.8586` edge `0.3103` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.789` n `55` status `ready` deltaP `-5.1673` edge `0.4156` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.5534` n `55` status `ready` deltaP `18.3508` edge `0.0496` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.3739` n `55` status `ready` deltaP `1.5297` edge `0.1568` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.3065` n `55` status `ready` deltaP `7.583` edge `0.1193` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.2936` n `55` status `ready` deltaP `3.6255` edge `0.1507` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.86` n `55` status `ready` deltaP `10.7267` edge `0.025` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
