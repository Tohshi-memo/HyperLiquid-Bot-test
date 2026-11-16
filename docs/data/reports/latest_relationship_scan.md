# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T12:22:25.305142+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4058`

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

- `market_context_high->unknown_24h` score `100.7997` n `30` status `ready` deltaP `3.9861` edge `8.3734` maxDD `0.0`
- `news_risk_high->equity_24h` score `51.6893` n `50` status `ready` deltaP `56.1109` edge `4.004` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.4734` n `50` status `ready` deltaP `42.5754` edge `2.5835` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.3834` n `30` status `ready` deltaP `14.4425` edge `1.5901` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `12.7483` n `50` status `ready` deltaP `40.5114` edge `0.9053` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.6089` n `30` status `ready` deltaP `44.5754` edge `1.6464` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.1738` n `50` status `ready` deltaP `25.1092` edge `1.5875` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.6133` n `50` status `ready` deltaP `47.0988` edge `0.3508` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.0244` n `50` status `ready` deltaP `41.0745` edge `0.2282` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0913` n `50` status `ready` deltaP `45.3607` edge `0.1595` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.9194` n `50` status `ready` deltaP `28.4262` edge `0.364` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.5674` n `50` status `ready` deltaP `22.274` edge `0.3697` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `3.9769` n `50` status `ready` deltaP `20.4491` edge `0.2581` maxDD `-3.7082`
- `market_context_high->metal_24h` score `3.8957` n `30` status `ready` deltaP `47.7759` edge `0.2701` maxDD `-3.7989`
- `news_risk_high->commodity_4h` score `3.6588` n `50` status `ready` deltaP `34.207` edge `0.1022` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.6605` n `50` status `ready` deltaP `25.3364` edge `0.0878` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1802` n `50` status `ready` deltaP `24.6946` edge `0.0425` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.313` n `50` status `ready` deltaP `17.3473` edge `0.0239` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `1.0172` n `50` status `ready` deltaP `19.1092` edge `0.2203` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8629` n `50` status `ready` deltaP `18.1916` edge `0.0873` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
