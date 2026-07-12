# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T23:06:57.126366+00:00`
- Price records: `672`
- Market context records: `6549`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9854`

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

- `market_context_high->unknown_24h` score `6.4123` n `144` status `ready` deltaP `11.8934` edge `0.7851` maxDD `-15.0689`
- `news_risk_high->fx_4h` score `3.7235` n `33` status `ready` deltaP `39.4032` edge `0.0522` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4636` n `33` status `ready` deltaP `30.2486` edge `0.0217` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.9382` n `202` status `ready` deltaP `-5.4574` edge `0.288` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3141` n `144` status `ready` deltaP `12.784` edge `0.2111` maxDD `-5.2791`
- `news_risk_high->crypto_major_1h` score `0.4471` n `33` status `ready` deltaP `3.1982` edge `0.0897` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.4085` n `194` status `ready` deltaP `11.6168` edge `0.0257` maxDD `-0.5286`
- `market_context_high->crypto_alt_4h` score `0.0913` n `194` status `ready` deltaP `8.7267` edge `0.1048` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `-0.1626` n `33` status `ready` deltaP `-1.3655` edge `0.0392` maxDD `-2.0756`
- `market_context_high->equity_4h` score `-0.3268` n `194` status `ready` deltaP `10.4979` edge `0.058` maxDD `-8.2573`
- `market_context_high->crypto_major_4h` score `-0.5317` n `194` status `ready` deltaP `11.1878` edge `0.0863` maxDD `-12.6576`
- `market_context_high->index_1h` score `-0.5636` n `202` status `ready` deltaP `-0.541` edge `0.0033` maxDD `-0.7564`
- `market_context_high->crypto_major_1h` score `-0.651` n `202` status `ready` deltaP `5.5834` edge `0.0059` maxDD `-6.7936`
- `market_context_high->fx_1h` score `-0.7067` n `202` status `ready` deltaP `-0.9545` edge `-0.0018` maxDD `-0.7249`
- `market_context_high->equity_1h` score `-0.7402` n `202` status `ready` deltaP `2.4174` edge `0.0` maxDD `-4.2147`
- `market_context_high->commodity_1h` score `-0.8756` n `202` status `ready` deltaP `-0.0237` edge `-0.0045` maxDD `-2.1314`
- `news_risk_high->unknown_1h` score `-0.9159` n `33` status `ready` deltaP `3.0485` edge `-0.0595` maxDD `-0.9718`
- `news_risk_high->metal_1h` score `-0.9972` n `33` status `ready` deltaP `-6.4145` edge `-0.0227` maxDD `-1.6568`
- `market_context_high->crypto_alt_1h` score `-1.0103` n `202` status `ready` deltaP `5.5952` edge `0.0098` maxDD `-5.8368`
- `market_context_high->unknown_4h` score `-1.0667` n `194` status `ready` deltaP `-18.049` edge `0.272` maxDD `-10.5788`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
