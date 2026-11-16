# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T03:22:25.049028+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8884`

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

- `market_context_high->unknown_24h` score `1280.3025` n `30` status `ready` deltaP `3.9861` edge `106.6653` maxDD `0.0`
- `news_risk_high->equity_24h` score `47.8377` n `50` status `ready` deltaP `50.565` edge `3.72` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `40.4157` n `64` status `ready` deltaP `6.1738` edge `3.3354` maxDD `-0.02`
- `market_context_high->crypto_alt_24h` score `28.9767` n `30` status `ready` deltaP `49.9364` edge `2.1895` maxDD `-6.2814`
- `market_context_high->equity_24h` score `26.9521` n `30` status `ready` deltaP `29.2317` edge `2.2053` maxDD `-9.0005`
- `news_risk_high->crypto_major_24h` score `21.3` n `50` status `ready` deltaP `41.8821` edge `2.5659` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.907` n `50` status `ready` deltaP `37.3902` edge `0.856` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `11.3415` n `30` status `ready` deltaP `17.2154` edge `1.2011` maxDD `-26.3264`
- `news_risk_high->crypto_alt_24h` score `9.0651` n `50` status `ready` deltaP `20.6031` edge `1.4754` maxDD `-29.0448`
- `news_risk_high->index_24h` score `6.8723` n `50` status `ready` deltaP `42.2461` edge `0.3214` maxDD `-0.4279`
- `market_context_high->index_24h` score `6.3015` n `30` status `ready` deltaP `44.2461` edge `0.2388` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `6.2608` n `50` status `ready` deltaP `41.0745` edge `0.2479` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.9904` n `50` status `ready` deltaP `44.3841` edge `0.1576` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.3484` n `50` status `ready` deltaP `20.8415` edge `0.361` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.1396` n `50` status `ready` deltaP `25.7744` edge `0.3167` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9121` n `50` status `ready` deltaP `20.2994` edge `0.2537` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.8983` n `50` status `ready` deltaP `35.5061` edge `0.1135` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.6983` n `30` status `ready` deltaP `47.4293` edge `0.2471` maxDD `-3.7989`
- `news_risk_high->index_4h` score `2.4588` n `50` status `ready` deltaP `23.5793` edge `0.0827` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2569` n `50` status `ready` deltaP `25.4431` edge `0.0439` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
