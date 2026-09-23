# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T21:22:35.827984+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9826`

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

- `market_context_high->unknown_1h` score `72.1615` n `47` status `ready` deltaP `9.9663` edge `5.9541` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `33.8623` n `46` status `ready` deltaP `20.305` edge `2.7021` maxDD `-0.5817`
- `market_context_high->equity_24h` score `19.4981` n `46` status `ready` deltaP `17.7008` edge `1.5169` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `17.1006` n `46` status `ready` deltaP `15.2778` edge `1.3232` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `8.2062` n `97` status `ready` deltaP `-3.1823` edge `1.3909` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.5758` n `46` status `ready` deltaP `26.7286` edge `0.3785` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `4.4876` n `103` status `ready` deltaP `17.2804` edge `0.3165` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `4.4864` n `103` status `ready` deltaP `13.1645` edge `0.3859` maxDD `-5.9838`
- `news_risk_high->crypto_alt_24h` score `3.2099` n `97` status `ready` deltaP `-5.3408` edge `0.7912` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.7622` n `97` status `ready` deltaP `26.1258` edge `0.1739` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.4982` n `103` status `ready` deltaP `13.3074` edge `0.1685` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.392` n `47` status `ready` deltaP `28.3861` edge `0.0255` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.0121` n `103` status `ready` deltaP `15.7026` edge `0.1065` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.4552` n `103` status `ready` deltaP `21.6997` edge `0.0402` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.2918` n `46` status `ready` deltaP `20.7051` edge `-0.007` maxDD `-0.2042`
- `market_context_high->equity_4h` score `1.1323` n `47` status `ready` deltaP `9.3701` edge `0.0737` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.1184` n `97` status `ready` deltaP `27.7957` edge `0.1212` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.6971` n `47` status `ready` deltaP `11.7658` edge `0.0075` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.5811` n `103` status `ready` deltaP `14.7535` edge `0.0094` maxDD `-0.7468`
- `news_risk_high->metal_24h` score `0.5016` n `97` status `ready` deltaP `16.783` edge `0.0442` maxDD `-3.0086`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
