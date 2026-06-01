# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T15:37:25.190290+00:00`
- Price records: `672`
- Market context records: `2574`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `market_context_high->crypto_alt_4h` score `6.1357` n `146` status `ready` deltaP `26.4158` edge `0.6031` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `4.8356` n `117` status `ready` deltaP `19.3643` edge `0.3067` maxDD `-1.626`
- `market_context_high->crypto_major_24h` score `4.4672` n `117` status `ready` deltaP `12.7137` edge `0.6013` maxDD `-18.4369`
- `market_context_high->crypto_major_4h` score `4.2682` n `146` status `ready` deltaP `18.1173` edge `0.4159` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.5499` n `146` status `ready` deltaP `12.0294` edge `0.1677` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.4395` n `117` status `ready` deltaP `20.4461` edge `0.0502` maxDD `-2.324`
- `market_context_high->unknown_4h` score `1.3116` n `146` status `ready` deltaP `9.9712` edge `0.1478` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `1.0122` n `146` status `ready` deltaP `10.3601` edge `0.1347` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.6419` n `117` status `ready` deltaP `6.25` edge `0.1099` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.3971` n `117` status `ready` deltaP `0.3205` edge `0.6866` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.2634` n `146` status `ready` deltaP `8.6703` edge `0.0483` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1275` n `146` status `ready` deltaP `3.9414` edge `0.0125` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4068` n `146` status `ready` deltaP `1.6508` edge `0.0214` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4159` n `146` status `ready` deltaP `5.502` edge `0.0165` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.585` n `146` status `ready` deltaP `0.0636` edge `0.0043` maxDD `-0.278`
- `market_context_high->fx_24h` score `-0.623` n `117` status `ready` deltaP `1.1485` edge `0.0035` maxDD `-1.6157`
- `market_context_high->metal_4h` score `-0.6596` n `146` status `ready` deltaP `4.1973` edge `0.0558` maxDD `-4.7664`
- `market_context_high->metal_1h` score `-0.668` n `146` status `ready` deltaP `0.8121` edge `0.0137` maxDD `-2.9823`
- `market_context_high->equity_1h` score `-0.8168` n `146` status `ready` deltaP `-0.527` edge `0.0193` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8244` n `146` status `ready` deltaP `0.5367` edge `0.0135` maxDD `-0.8621`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
