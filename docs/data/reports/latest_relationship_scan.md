# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T19:37:28.054760+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8284`

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

- `market_context_high->unknown_24h` score `592.8165` n `60` status `ready` deltaP `3.9861` edge `49.3748` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.8433` n `50` status `ready` deltaP `50.565` edge `3.5538` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.9178` n `60` status `ready` deltaP `45.8983` edge `3.258` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `34.1599` n `60` status `ready` deltaP `63.0965` edge `2.5337` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.1157` n `50` status `ready` deltaP `45.8683` edge `2.7721` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.1063` n `50` status `ready` deltaP `38.4573` edge `0.8655` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.503` n `50` status `ready` deltaP `20.4298` edge `1.5327` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.1607` n `60` status `ready` deltaP `49.2461` edge `0.3604` maxDD `-0.0251`
- `market_context_high->crypto_major_24h` score `7.3182` n `60` status `ready` deltaP `14.535` edge `1.3044` maxDD `-58.6492`
- `market_context_high->metal_24h` score `6.6845` n `60` status `ready` deltaP `63.5759` edge `0.5223` maxDD `-3.7989`
- `news_risk_high->index_24h` score `6.6167` n `50` status `ready` deltaP `42.2461` edge `0.3001` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.5314` n `50` status `ready` deltaP `42.8076` edge `0.2589` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.1653` n `50` status `ready` deltaP `22.5183` edge `0.4179` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `4.8858` n `50` status `ready` deltaP `44.2317` edge `0.1499` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.5458` n `50` status `ready` deltaP `27.1463` edge `0.3414` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0103` n `50` status `ready` deltaP `21.497` edge `0.2539` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6856` n `50` status `ready` deltaP `34.2866` edge `0.1039` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5343` n `50` status `ready` deltaP `24.4939` edge `0.0829` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1849` n `50` status `ready` deltaP `24.994` edge `0.0409` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3058` n `50` status `ready` deltaP `17.3473` edge `0.0233` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
