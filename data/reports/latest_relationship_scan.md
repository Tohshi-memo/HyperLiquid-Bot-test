# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T13:22:26.990517+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4064`

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

- `market_context_high->unknown_24h` score `93.4497` n `30` status `ready` deltaP `3.9861` edge `7.7609` maxDD `0.0`
- `news_risk_high->equity_24h` score `52.1756` n `50` status `ready` deltaP `56.8042` edge `4.0399` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.5701` n `50` status `ready` deltaP `42.5754` edge `2.5959` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.6585` n `30` status `ready` deltaP `15.1357` edge `1.6084` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `13.1498` n `50` status `ready` deltaP `41.1202` edge `0.9347` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.7056` n `30` status `ready` deltaP `44.5754` edge `1.6588` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.3526` n `50` status `ready` deltaP `25.8024` edge `1.6058` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.712` n `50` status `ready` deltaP `47.792` edge `0.3544` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.0544` n `50` status `ready` deltaP `41.0745` edge `0.2307` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `5.1493` n `50` status `ready` deltaP `29.035` edge `0.3791` maxDD `-9.4848`
- `news_risk_high->metal_4h` score `5.0973` n `50` status `ready` deltaP `45.3607` edge `0.16` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.7419` n `50` status `ready` deltaP `22.7306` edge `0.3812` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.0752` n `50` status `ready` deltaP `21.0479` edge `0.2623` maxDD `-3.7082`
- `market_context_high->metal_24h` score `3.8625` n `30` status `ready` deltaP `47.256` edge `0.2693` maxDD `-3.7989`
- `news_risk_high->commodity_4h` score `3.7411` n `50` status `ready` deltaP `34.8158` edge `0.105` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.7464` n `50` status `ready` deltaP `25.9452` edge `0.0909` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1982` n `50` status `ready` deltaP `24.8443` edge `0.043` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3154` n `50` status `ready` deltaP `17.3473` edge `0.0241` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9839` n `50` status `ready` deltaP `18.5893` edge `0.2195` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.9643` n `50` status `ready` deltaP `18.7904` edge `0.0963` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
