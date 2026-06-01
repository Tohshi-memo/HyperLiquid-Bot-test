# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T20:22:23.663938+00:00`
- Price records: `672`
- Market context records: `2594`
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

- `market_context_high->unknown_24h` score `7.7428` n `133` status `ready` deltaP `18.1743` edge `0.5569` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.5911` n `146` status `ready` deltaP `25.6536` edge `0.5628` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8724` n `146` status `ready` deltaP `16.4405` edge `0.3941` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `1.7248` n `133` status `ready` deltaP `3.3847` edge `0.759` maxDD `-39.0265`
- `market_context_high->crypto_alt_1h` score `1.4132` n `146` status `ready` deltaP `11.5803` edge `0.1593` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.9218` n `133` status `ready` deltaP `8.9233` edge `0.1154` maxDD `-2.5127`
- `market_context_high->unknown_4h` score `0.9153` n `146` status `ready` deltaP `7.837` edge `0.129` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.8144` n `146` status `ready` deltaP `9.3122` edge `0.1252` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.2462` n `146` status `ready` deltaP `9.28` edge `0.0428` maxDD `-2.3986`
- `market_context_high->equity_24h` score `0.0894` n `133` status `ready` deltaP `16.2098` edge `-0.0336` maxDD `-2.3615`
- `market_context_high->index_1h` score `-0.1311` n `146` status `ready` deltaP `4.0911` edge `0.0112` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.3912` n `146` status `ready` deltaP `1.9502` edge `0.0207` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.417` n `146` status `ready` deltaP `5.3523` edge `0.0174` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.6128` n `146` status `ready` deltaP `1.2612` edge `0.0153` maxDD `-2.9823`
- `market_context_high->metal_4h` score `-0.634` n `146` status `ready` deltaP `4.5021` edge `0.0559` maxDD `-4.7664`
- `market_context_high->fx_1h` score `-0.6641` n `146` status `ready` deltaP `-0.8346` edge `0.0037` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.7893` n `146` status `ready` deltaP `-0.0779` edge `0.0186` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.9144` n `146` status `ready` deltaP `-0.378` edge `0.0121` maxDD `-0.8621`
- `market_context_high->crypto_major_24h` score `-0.9214` n `133` status `ready` deltaP `4.8285` edge `0.4179` maxDD `-30.15`
- `market_context_high->fx_24h` score `-0.9633` n `133` status `ready` deltaP `2.8627` edge `0.0` maxDD `-1.6157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
