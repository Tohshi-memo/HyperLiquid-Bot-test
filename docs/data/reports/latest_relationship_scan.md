# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T01:07:22.806340+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8640`

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

- `market_context_high->unknown_24h` score `1104.2241` n `38` status `ready` deltaP `3.9861` edge `91.9921` maxDD `0.0`
- `news_risk_high->equity_24h` score `47.1741` n `50` status `ready` deltaP `50.565` edge `3.6647` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `44.2303` n `64` status `ready` deltaP `8.9939` edge `3.6259` maxDD `0.0`
- `market_context_high->equity_24h` score `33.7955` n `38` status `ready` deltaP `36.2492` edge `2.7288` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `30.3414` n `38` status `ready` deltaP `55.5505` edge `2.2658` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `21.681` n `50` status `ready` deltaP `43.2686` edge `2.6055` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.7368` n `50` status `ready` deltaP `36.628` edge `0.8469` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `11.5547` n `38` status `ready` deltaP `11.5844` edge `1.3212` maxDD `-30.1765`
- `news_risk_high->crypto_alt_24h` score `9.133` n `50` status `ready` deltaP `20.6031` edge `1.4841` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.0027` n `38` status `ready` deltaP `46.3514` edge `0.2832` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.8015` n `50` status `ready` deltaP `42.2461` edge `0.3155` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.2608` n `50` status `ready` deltaP `41.0745` edge `0.2479` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.9226` n `50` status `ready` deltaP `43.9268` edge `0.155` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.507` n `38` status `ready` deltaP `54.4468` edge `0.304` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.3408` n `50` status `ready` deltaP `20.5366` edge `0.3624` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.1286` n `50` status `ready` deltaP `25.622` edge `0.3168` maxDD `-9.4848`
- `news_risk_high->commodity_4h` score `3.7372` n `50` status `ready` deltaP `34.2866` edge `0.1082` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.7118` n `50` status `ready` deltaP `19.7006` edge `0.241` maxDD `-3.7082`
- `news_risk_high->index_4h` score `2.409` n `50` status `ready` deltaP `23.122` edge `0.0816` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1574` n `50` status `ready` deltaP `24.6946` edge `0.0406` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
