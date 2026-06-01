# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T15:07:56.452711+00:00`
- Price records: `672`
- Market context records: `2572`
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

- `market_context_high->crypto_alt_4h` score `6.0417` n `146` status `ready` deltaP `26.1109` edge `0.5973` maxDD `-15.4319`
- `market_context_high->crypto_major_24h` score `5.0089` n `116` status `ready` deltaP `13.2663` edge `0.6174` maxDD `-16.7415`
- `market_context_high->unknown_24h` score `4.705` n `116` status `ready` deltaP `19.4863` edge `0.295` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.1826` n `146` status `ready` deltaP `17.8124` edge `0.4108` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.5379` n `146` status `ready` deltaP `11.8797` edge `0.1677` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.5291` n `116` status `ready` deltaP `20.546` edge `0.057` maxDD `-2.324`
- `market_context_high->unknown_4h` score `1.3344` n `146` status `ready` deltaP `9.9712` edge `0.1497` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.999` n `146` status `ready` deltaP `10.2104` edge `0.1346` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.6434` n `116` status `ready` deltaP `6.0584` edge `0.1113` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.4067` n `116` status `ready` deltaP `0.3711` edge `0.6875` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.2294` n `146` status `ready` deltaP `8.3654` edge `0.0475` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1251` n `146` status `ready` deltaP `3.9414` edge `0.0127` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.426` n `146` status `ready` deltaP `1.6508` edge `0.0198` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4386` n `146` status `ready` deltaP `5.3523` edge `0.0156` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.5599` n `146` status `ready` deltaP `0.363` edge `0.0044` maxDD `-0.278`
- `market_context_high->fx_24h` score `-0.5941` n `116` status `ready` deltaP `1.5685` edge `0.0044` maxDD `-1.6157`
- `market_context_high->metal_1h` score `-0.6392` n `146` status `ready` deltaP `0.9618` edge `0.0151` maxDD `-2.9823`
- `market_context_high->metal_4h` score `-0.7236` n `146` status `ready` deltaP `3.8924` edge `0.0525` maxDD `-4.7664`
- `market_context_high->equity_1h` score `-0.7749` n `146` status `ready` deltaP `-0.3773` edge `0.0218` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8244` n `146` status `ready` deltaP `0.5367` edge `0.0135` maxDD `-0.8621`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
