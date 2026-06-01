# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T19:22:26.140817+00:00`
- Price records: `672`
- Market context records: `2590`
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

- `market_context_high->unknown_24h` score `7.8453` n `132` status `ready` deltaP `18.1345` edge `0.5657` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.8415` n `146` status `ready` deltaP `26.2634` edge `0.5796` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.0844` n `146` status `ready` deltaP `17.0502` edge `0.4077` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `1.9763` n `132` status `ready` deltaP `3.709` edge `0.7778` maxDD `-39.0265`
- `market_context_high->crypto_alt_1h` score `1.4719` n `146` status `ready` deltaP `12.0294` edge `0.1612` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.0313` n `146` status `ready` deltaP `8.4468` edge `0.1346` maxDD `-3.7312`
- `market_context_high->index_24h` score `0.9111` n `132` status `ready` deltaP `8.7752` edge `0.1155` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.8623` n `146` status `ready` deltaP `9.6116` edge `0.1272` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.2776` n `146` status `ready` deltaP `9.4325` edge `0.0444` maxDD `-2.3986`
- `market_context_high->equity_24h` score `0.2595` n `132` status `ready` deltaP `17.0612` edge `-0.0251` maxDD `-2.3615`
- `market_context_high->index_1h` score `-0.1719` n `146` status `ready` deltaP `3.7917` edge `0.0098` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.3948` n `146` status `ready` deltaP `1.9502` edge `0.0204` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.471` n `146` status `ready` deltaP `5.0529` edge `0.0149` maxDD `-4.3601`
- `market_context_high->metal_4h` score `-0.5988` n `146` status `ready` deltaP `4.807` edge `0.0568` maxDD `-4.7664`
- `market_context_high->crypto_major_24h` score `-0.6177` n `132` status `ready` deltaP `5.6029` edge `0.4335` maxDD `-30.1198`
- `market_context_high->metal_1h` score `-0.632` n `146` status `ready` deltaP `1.1115` edge `0.0147` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.7012` n `146` status `ready` deltaP `-1.2837` edge `0.0036` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.8708` n `146` status `ready` deltaP `-0.6767` edge `0.0158` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.9144` n `146` status `ready` deltaP `-0.378` edge `0.0121` maxDD `-0.8621`
- `market_context_high->fx_24h` score `-0.9264` n `132` status `ready` deltaP `3.2039` edge `0.0008` maxDD `-1.6157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
