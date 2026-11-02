# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T02:22:28.746283+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7535`

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

- `market_context_high->unknown_24h` score `7554.3271` n `51` status `ready` deltaP `1.3889` edge `629.518` maxDD `0.0`
- `market_context_high->unknown_4h` score `374.01` n `51` status `ready` deltaP `7.338` edge `31.1229` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `34.9604` n `54` status `ready` deltaP `4.3081` edge `2.8957` maxDD `-0.2178`
- `market_context_high->equity_24h` score `20.7406` n `51` status `ready` deltaP `42.6573` edge `1.4676` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.6402` n `94` status `ready` deltaP `33.0452` edge `1.052` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `6.3217` n `51` status `ready` deltaP `43.7398` edge `0.2663` maxDD `-0.8203`
- `market_context_high->index_24h` score `6.2226` n `51` status `ready` deltaP `49.1319` edge `0.191` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.1939` n `51` status `ready` deltaP `25.798` edge `0.3736` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.4449` n `51` status `ready` deltaP `30.6552` edge `0.283` maxDD `-1.6901`
- `market_context_high->commodity_4h` score `3.7076` n `51` status `ready` deltaP `35.055` edge `0.092` maxDD `-0.3387`
- `market_context_high->equity_4h` score `3.0193` n `51` status `ready` deltaP `3.6615` edge `0.2974` maxDD `-2.283`
- `market_context_high->equity_1h` score `2.3692` n `54` status `ready` deltaP `8.8102` edge `0.1912` maxDD `-1.5336`
- `news_risk_high->crypto_alt_4h` score `2.2906` n `126` status `ready` deltaP `9.3181` edge `0.2674` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.0445` n `51` status `ready` deltaP `8.0065` edge `0.2764` maxDD `-3.0799`
- `market_context_high->crypto_major_1h` score `1.8065` n `54` status `ready` deltaP `8.6605` edge `0.1437` maxDD `-1.4048`
- `market_context_high->crypto_alt_24h` score `1.7478` n `51` status `ready` deltaP `-6.0662` edge `0.4163` maxDD `-8.8096`
- `market_context_high->crypto_alt_1h` score `1.5607` n `54` status `ready` deltaP `4.0031` edge `0.1646` maxDD `-2.2314`
- `market_context_high->metal_4h` score `1.4692` n `51` status `ready` deltaP `17.928` edge `0.0454` maxDD `-0.7323`
- `market_context_high->fx_1h` score `1.4271` n `54` status `ready` deltaP `19.4722` edge `0.0067` maxDD `-0.0736`
- `market_context_high->metal_1h` score `0.8963` n `54` status `ready` deltaP `11.1499` edge `0.0252` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
