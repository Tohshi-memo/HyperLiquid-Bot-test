# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T21:07:29.599344+00:00`
- Price records: `672`
- Market context records: `7707`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `3.6159` n `132` status `ready` deltaP `19.396` edge `0.3062` maxDD `-6.0681`
- `market_context_high->crypto_major_4h` score `1.233` n `133` status `ready` deltaP `15.4135` edge `0.1718` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0718` n `133` status `ready` deltaP `13.0082` edge `0.0467` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.7981` n `133` status `ready` deltaP `8.8093` edge `0.1195` maxDD `-3.9374`
- `market_context_high->equity_4h` score `0.7718` n `133` status `ready` deltaP `2.8868` edge `0.271` maxDD `-6.9701`
- `market_context_high->equity_1h` score `0.6206` n `133` status `ready` deltaP `8.4964` edge `0.081` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.3842` n `133` status `ready` deltaP `8.9447` edge `0.0154` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.121` n `133` status `ready` deltaP `3.3801` edge `0.0308` maxDD `-1.4603`
- `market_context_high->fx_24h` score `-0.0243` n `132` status `ready` deltaP `12.2928` edge `0.0237` maxDD `-3.0343`
- `market_context_high->index_4h` score `-0.1335` n `133` status `ready` deltaP `12.2405` edge `0.0471` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `-0.1916` n `133` status `ready` deltaP `3.5449` edge `0.0063` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.2591` n `133` status `ready` deltaP `3.5639` edge `0.014` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.5311` n `133` status `ready` deltaP `-0.6773` edge `-0.001` maxDD `-0.4331`
- `market_context_high->metal_24h` score `-0.5482` n `133` status `ready` deltaP `3.0284` edge `0.1432` maxDD `-2.3927`
- `market_context_high->metal_1h` score `-0.8662` n `133` status `ready` deltaP `1.2674` edge `0.0197` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4113` n `133` status `ready` deltaP `1.7479` edge `0.0762` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5782` n `133` status `ready` deltaP `-5.385` edge `-0.0036` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7453` n `132` status `ready` deltaP `5.6858` edge `-0.025` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.1325` n `133` status `ready` deltaP `-0.825` edge `-0.1132` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.5879` n `132` status `ready` deltaP `-18.4537` edge `0.0015` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
