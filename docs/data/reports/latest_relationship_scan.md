# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T07:37:24.083473+00:00`
- Price records: `672`
- Market context records: `2949`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `17.0208` n `133` status `ready` deltaP `14.7256` edge `1.7119` maxDD `-22.6673`
- `market_context_high->equity_24h` score `8.1144` n `133` status `ready` deltaP `18.4158` edge `0.7538` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `7.629` n `133` status `ready` deltaP `16.8481` edge `0.5699` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `3.705` n `133` status `ready` deltaP `20.0958` edge `0.4121` maxDD `-9.6523`
- `market_context_high->index_24h` score `3.053` n `133` status `ready` deltaP `14.3092` edge `0.2571` maxDD `-2.5127`
- `market_context_high->equity_4h` score `1.9555` n `134` status `ready` deltaP `11.6286` edge `0.1741` maxDD `-4.0934`
- `market_context_high->crypto_alt_4h` score `0.8237` n `134` status `ready` deltaP `18.0856` edge `0.4042` maxDD `-30.8239`
- `market_context_high->index_4h` score `0.7673` n `134` status `ready` deltaP `15.0778` edge `0.082` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.3609` n `134` status `ready` deltaP `4.1568` edge `0.1077` maxDD `-3.7602`
- `market_context_high->index_1h` score `0.1097` n `134` status `ready` deltaP `6.2651` edge `0.0217` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.1308` n `134` status `ready` deltaP `2.0779` edge `0.0517` maxDD `-2.1163`
- `market_context_high->crypto_alt_1h` score `-0.2545` n `134` status `ready` deltaP `6.5667` edge `0.0996` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.3176` n `134` status `ready` deltaP `0.143` edge `0.0033` maxDD `-0.1244`
- `market_context_high->crypto_major_1h` score `-0.5652` n `134` status `ready` deltaP `5.2328` edge `0.0796` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6108` n `134` status `ready` deltaP `0.6055` edge `0.0064` maxDD `-3.4325`
- `market_context_high->fx_4h` score `-0.7535` n `134` status `ready` deltaP `0.8668` edge `0.0093` maxDD `-0.5631`
- `market_context_high->commodity_1h` score `-0.781` n `134` status `ready` deltaP `-1.9483` edge `-0.0118` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.8921` n `134` status `ready` deltaP `0.8915` edge `-0.0072` maxDD `-3.1801`
- `market_context_high->commodity_4h` score `-1.0472` n `134` status `ready` deltaP `3.7245` edge `0.0256` maxDD `-9.4411`
- `market_context_high->crypto_major_4h` score `-1.2927` n `134` status `ready` deltaP `8.416` edge `0.2907` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
