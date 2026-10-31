# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T08:51:17.290654+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7653`

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

- `market_context_high->unknown_24h` score `1793.1464` n `127` status `ready` deltaP `-5.5733` edge `149.509` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `97.5643` n `98` status `ready` deltaP `-6.0919` edge `8.1996` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `25.8859` n `127` status `ready` deltaP `1.9577` edge `2.1574` maxDD `-0.3966`
- `market_context_high->equity_24h` score `9.0542` n `127` status `ready` deltaP `22.2796` edge `0.8817` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.1865` n `98` status `ready` deltaP `18.638` edge `0.4466` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.3307` n `127` status `ready` deltaP `40.7248` edge `0.1077` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.9321` n `127` status `ready` deltaP `13.6628` edge `0.0156` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.908` n `98` status `ready` deltaP `8.096` edge `0.1046` maxDD `-3.9659`
- `market_context_high->equity_1h` score `0.4596` n `127` status `ready` deltaP `6.3546` edge `0.0835` maxDD `-2.3383`
- `market_context_high->metal_4h` score `0.4591` n `127` status `ready` deltaP `17.0575` edge `0.0327` maxDD `-1.671`
- `market_context_high->crypto_major_1h` score `0.4434` n `127` status `ready` deltaP `9.8425` edge `0.0741` maxDD `-5.2213`
- `market_context_high->commodity_4h` score `0.2609` n `127` status `ready` deltaP `13.3234` edge `0.0548` maxDD `-1.0837`
- `market_context_high->equity_4h` score `-0.0019` n `127` status `ready` deltaP `2.3238` edge `0.1427` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0403` n `127` status `ready` deltaP `4.7468` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2447` n `127` status `ready` deltaP `2.3009` edge `0.0157` maxDD `-0.4475`
- `market_context_high->metal_24h` score `-0.3443` n `127` status `ready` deltaP `6.3525` edge `0.1782` maxDD `-10.5088`
- `market_context_high->fx_4h` score `-0.4989` n `127` status `ready` deltaP `-0.2161` edge `-0.0028` maxDD `-0.4442`
- `market_context_high->index_1h` score `-0.5538` n `127` status `ready` deltaP `1.2589` edge `0.0013` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.7262` n `127` status `ready` deltaP `4.1751` edge `0.0566` maxDD `-7.536`
- `news_risk_high->index_1h` score `-0.8814` n `98` status `ready` deltaP `1.5642` edge `-0.0039` maxDD `-1.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
