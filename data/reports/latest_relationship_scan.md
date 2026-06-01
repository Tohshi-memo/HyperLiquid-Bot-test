# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T18:52:23.769570+00:00`
- Price records: `672`
- Market context records: `2587`
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

- `market_context_high->unknown_24h` score `7.4955` n `130` status `ready` deltaP `18.0529` edge `0.5371` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.9583` n `146` status `ready` deltaP `26.5683` edge `0.5873` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.1772` n `146` status `ready` deltaP `17.3551` edge `0.4134` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `1.7995` n `130` status `ready` deltaP `3.2986` edge `0.7658` maxDD `-39.0265`
- `market_context_high->crypto_alt_1h` score `1.4551` n `146` status `ready` deltaP `11.8797` edge `0.1608` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.0821` n `146` status `ready` deltaP `8.7517` edge `0.1368` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.9007` n `146` status `ready` deltaP `9.911` edge `0.1284` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.8689` n `130` status `ready` deltaP `8.4722` edge `0.114` maxDD `-2.5127`
- `market_context_high->equity_24h` score `0.3939` n `130` status `ready` deltaP `17.2569` edge `-0.0152` maxDD `-2.3615`
- `market_context_high->index_4h` score `0.292` n `146` status `ready` deltaP `9.4325` edge `0.0456` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.2042` n `146` status `ready` deltaP `3.4923` edge `0.0091` maxDD `-1.2855`
- `market_context_high->crypto_major_24h` score `-0.2089` n `130` status `ready` deltaP `6.477` edge `0.4483` maxDD `-29.7109`
- `market_context_high->commodity_1h` score `-0.4398` n `146` status `ready` deltaP `5.2026` edge `0.0165` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4416` n `146` status `ready` deltaP `1.6508` edge `0.0185` maxDD `-2.6375`
- `market_context_high->metal_4h` score `-0.5734` n `146` status `ready` deltaP `4.9594` edge `0.0579` maxDD `-4.7664`
- `market_context_high->metal_1h` score `-0.6488` n `146` status `ready` deltaP `0.9618` edge `0.0143` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.7132` n `146` status `ready` deltaP `-1.4334` edge `0.0036` maxDD `-0.278`
- `market_context_high->fx_4h` score `-0.8986` n `146` status `ready` deltaP `-0.2255` edge `0.0124` maxDD `-0.8621`
- `market_context_high->equity_1h` score `-0.9116` n `146` status `ready` deltaP `-0.9761` edge `0.0144` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.9553` n `130` status `ready` deltaP `2.8285` edge `0.0009` maxDD `-1.6157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
