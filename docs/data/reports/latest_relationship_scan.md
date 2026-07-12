# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T22:52:26.345806+00:00`
- Price records: `672`
- Market context records: `6548`
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

- `market_context_high->unknown_24h` score `6.4147` n `144` status `ready` deltaP `11.8934` edge `0.7853` maxDD `-15.0689`
- `news_risk_high->fx_4h` score `3.7518` n `34` status `ready` deltaP `39.6073` edge `0.0532` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2829` n `34` status `ready` deltaP `28.1701` edge `0.0205` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.9973` n `201` status `ready` deltaP `-5.2283` edge `0.2914` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3177` n `144` status `ready` deltaP `12.784` edge `0.2114` maxDD `-5.2791`
- `news_risk_high->crypto_major_1h` score `0.5049` n `34` status `ready` deltaP `4.5351` edge `0.0882` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.442` n `193` status `ready` deltaP `11.8089` edge `0.0261` maxDD `-0.4392`
- `market_context_high->crypto_alt_4h` score `0.1314` n `193` status `ready` deltaP `8.8841` edge `0.1071` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `-0.2344` n `34` status `ready` deltaP `-2.6418` edge `0.0385` maxDD `-2.0756`
- `market_context_high->equity_4h` score `-0.3094` n `193` status `ready` deltaP `10.6526` edge `0.0592` maxDD `-8.2573`
- `market_context_high->crypto_major_4h` score `-0.5067` n `193` status `ready` deltaP `11.3531` edge `0.0884` maxDD `-12.6576`
- `market_context_high->index_1h` score `-0.5502` n `201` status `ready` deltaP `-0.2972` edge `0.0034` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.5508` n `201` status `ready` deltaP `0.2398` edge `-0.0039` maxDD `-2.1314`
- `market_context_high->crypto_major_1h` score `-0.6637` n `201` status `ready` deltaP `5.3691` edge `0.0057` maxDD `-6.7936`
- `market_context_high->fx_1h` score `-0.7168` n `201` status `ready` deltaP `-1.0807` edge `-0.0018` maxDD `-0.7249`
- `market_context_high->equity_1h` score `-0.7311` n `201` status `ready` deltaP `2.5337` edge `0.0004` maxDD `-4.2147`
- `news_risk_high->metal_1h` score `-0.9037` n `34` status `ready` deltaP `-4.7816` edge `-0.0216` maxDD `-1.6568`
- `market_context_high->crypto_alt_1h` score `-1.0173` n `201` status `ready` deltaP `5.5233` edge `0.0097` maxDD `-5.8368`
- `market_context_high->unknown_4h` score `-1.0691` n `193` status `ready` deltaP `-18.423` edge `0.2743` maxDD `-10.5788`
- `market_context_high->metal_4h` score `-1.1048` n `193` status `ready` deltaP `0.7187` edge `0.0369` maxDD `-2.6662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
