# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T00:07:23.513893+00:00`
- Price records: `672`
- Market context records: `2611`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `8.103` n `146` status `ready` deltaP `18.2958` edge `0.5861` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.2411` n `146` status `ready` deltaP `25.0439` edge `0.5377` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.4803` n `146` status `ready` deltaP `14.7636` edge `0.3726` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.3568` n `146` status `ready` deltaP `11.4306` edge `0.1556` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `0.9943` n `146` status `ready` deltaP `7.6846` edge `0.1366` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.7317` n `146` status `ready` deltaP `8.8631` edge `0.1213` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.6544` n `146` status `ready` deltaP `8.281` edge `0.0974` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.6328` n `146` status `ready` deltaP `2.0643` edge `0.6768` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.2012` n `146` status `ready` deltaP `8.8227` edge `0.0421` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.094` n `146` status `ready` deltaP `4.3905` edge `0.0123` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.417` n `146` status `ready` deltaP `5.3523` edge `0.0174` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4632` n `146` status `ready` deltaP `1.8005` edge `0.0157` maxDD `-2.6375`
- `market_context_high->metal_1h` score `-0.5889` n `146` status `ready` deltaP `1.5606` edge `0.0153` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.6377` n `146` status `ready` deltaP `-0.5352` edge `0.0039` maxDD `-0.278`
- `market_context_high->metal_4h` score `-0.694` n `146` status `ready` deltaP `4.5021` edge `0.0509` maxDD `-4.7664`
- `market_context_high->equity_1h` score `-0.7761` n `146` status `ready` deltaP `-0.0779` edge `0.0197` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.854` n `146` status `ready` deltaP `4.4092` edge `-0.0012` maxDD `-1.6157`
- `market_context_high->fx_4h` score `-0.8936` n `146` status `ready` deltaP `-0.0731` edge `0.0118` maxDD `-0.8621`
- `market_context_high->commodity_4h` score `-1.0772` n `146` status `ready` deltaP `3.339` edge `0.0339` maxDD `-10.2078`
- `market_context_high->equity_4h` score `-1.3674` n `146` status `ready` deltaP `1.6497` edge `0.0155` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
