# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T00:37:28.898998+00:00`
- Price records: `672`
- Market context records: `6556`
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

- `market_context_high->unknown_24h` score `6.3931` n `144` status `ready` deltaP `11.8934` edge `0.7835` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.8262` n `208` status `ready` deltaP `-4.8624` edge `0.2747` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3641` n `144` status `ready` deltaP `13.304` edge `0.2118` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.4028` n `196` status `ready` deltaP `11.8529` edge `0.026` maxDD `-0.7164`
- `market_context_high->crypto_alt_4h` score `-0.1026` n `196` status `ready` deltaP `8.8788` edge `0.1035` maxDD `-8.0324`
- `market_context_high->fx_1h` score `-0.3684` n `208` status `ready` deltaP `0.6448` edge `-0.0008` maxDD `-0.7249`
- `market_context_high->equity_4h` score `-0.3793` n `196` status `ready` deltaP `9.893` edge `0.0553` maxDD `-8.2573`
- `market_context_high->crypto_major_1h` score `-0.4881` n `208` status `ready` deltaP `6.6761` edge `0.0195` maxDD `-6.7936`
- `market_context_high->crypto_major_4h` score `-0.4973` n `196` status `ready` deltaP `11.3241` edge `0.0898` maxDD `-12.6576`
- `market_context_high->crypto_alt_1h` score `-0.5213` n `208` status `ready` deltaP `6.3997` edge `0.0218` maxDD `-5.8368`
- `market_context_high->index_1h` score `-0.5855` n `208` status `ready` deltaP `-0.9615` edge `0.0033` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.8813` n `208` status `ready` deltaP `-0.1094` edge `-0.0044` maxDD `-2.1314`
- `market_context_high->unknown_4h` score `-0.9281` n `196` status `ready` deltaP `-16.8554` edge `0.2756` maxDD `-10.5788`
- `market_context_high->equity_1h` score `-1.1685` n `208` status `ready` deltaP `1.9864` edge `0.0004` maxDD `-4.2147`
- `market_context_high->metal_4h` score `-1.2002` n `196` status `ready` deltaP `0.983` edge `0.0354` maxDD `-2.6662`
- `market_context_high->metal_1h` score `-1.2354` n `208` status `ready` deltaP `-3.1696` edge `-0.0011` maxDD `-2.1239`
- `market_context_high->metal_24h` score `-1.9781` n `144` status `ready` deltaP `5.966` edge `0.0884` maxDD `-5.7746`
- `market_context_high->commodity_4h` score `-2.0371` n `196` status `ready` deltaP `-1.3471` edge `-0.0113` maxDD `-5.6246`
- `market_context_high->fx_4h` score `-3.0238` n `196` status `ready` deltaP `-3.3256` edge `-0.0086` maxDD `-3.3635`
- `market_context_high->fx_24h` score `-3.8561` n `144` status `ready` deltaP `-4.961` edge `-0.0078` maxDD `-9.2795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
