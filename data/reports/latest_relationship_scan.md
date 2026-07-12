# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T23:37:26.163372+00:00`
- Price records: `672`
- Market context records: `6551`
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

- `market_context_high->unknown_24h` score `6.4111` n `144` status `ready` deltaP `11.8934` edge `0.785` maxDD `-15.0689`
- `news_risk_high->fx_4h` score `3.6085` n `31` status `ready` deltaP `38.9261` edge `0.0458` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3397` n `31` status `ready` deltaP `28.6845` edge `0.0218` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.8229` n `204` status `ready` deltaP `-5.9088` edge `0.2814` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3129` n `144` status `ready` deltaP `12.784` edge `0.211` maxDD `-5.2791`
- `news_risk_high->crypto_major_1h` score `0.453` n `31` status `ready` deltaP `3.3417` edge `0.0895` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.3444` n `196` status `ready` deltaP `11.2431` edge `0.0252` maxDD `-0.7164`
- `news_risk_high->crypto_alt_1h` score `-0.1529` n `31` status `ready` deltaP `-1.4632` edge `0.0411` maxDD `-2.0756`
- `market_context_high->crypto_alt_4h` score `-0.2003` n `196` status `ready` deltaP `8.4215` edge `0.0984` maxDD `-8.0324`
- `news_risk_high->unknown_1h` score `-0.35` n `31` status `ready` deltaP `6.5675` edge `-0.0358` maxDD `-0.9718`
- `market_context_high->equity_4h` score `-0.3856` n `196` status `ready` deltaP `9.893` edge `0.0545` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.4295` n `204` status `ready` deltaP `-0.411` edge `-0.0016` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.5709` n `204` status `ready` deltaP `-0.681` edge `0.0033` maxDD `-0.7564`
- `market_context_high->crypto_major_4h` score `-0.5843` n `196` status `ready` deltaP `10.8667` edge `0.0817` maxDD `-12.6576`
- `market_context_high->crypto_major_1h` score `-0.6306` n `204` status `ready` deltaP `5.8559` edge `0.0067` maxDD `-6.7936`
- `news_risk_high->commodity_4h` score `-0.7575` n `31` status `ready` deltaP `-5.8566` edge `-0.0064` maxDD `-1.4672`
- `market_context_high->commodity_1h` score `-0.9088` n `204` status `ready` deltaP `-0.3933` edge `-0.0048` maxDD `-2.1314`
- `news_risk_high->index_1h` score `-1.0069` n `31` status `ready` deltaP `-7.7651` edge `-0.021` maxDD `-1.1725`
- `market_context_high->crypto_alt_1h` score `-1.0134` n `204` status `ready` deltaP `5.5419` edge `0.0099` maxDD `-5.8368`
- `news_risk_high->metal_1h` score `-1.0398` n `31` status `ready` deltaP `-6.949` edge `-0.0246` maxDD `-1.6568`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
