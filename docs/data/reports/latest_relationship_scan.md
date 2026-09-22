# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T01:22:32.175759+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9964`

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

- `market_context_high->unknown_4h` score `42.805` n `50` status `ready` deltaP `7.3171` edge `3.5183` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `26.0299` n `50` status `ready` deltaP `17.1667` edge `2.2962` maxDD `-17.3189`
- `market_context_high->equity_24h` score `12.9478` n `50` status `ready` deltaP `10.3958` edge `1.1144` maxDD `-6.378`
- `market_context_high->crypto_alt_24h` score `10.8303` n `50` status `ready` deltaP `15.6111` edge `1.0317` maxDD `-17.3265`
- `news_risk_high->crypto_major_24h` score `10.3523` n `101` status `ready` deltaP `-0.5363` edge `1.5521` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `5.8727` n `101` status `ready` deltaP `-0.1513` edge `0.9785` maxDD `-32.7147`
- `market_context_high->index_24h` score `4.4357` n `50` status `ready` deltaP `14.3889` edge `0.3071` maxDD `-0.671`
- `news_risk_high->crypto_alt_4h` score `2.9666` n `101` status `ready` deltaP `14.4983` edge `0.2715` maxDD `-7.675`
- `news_risk_high->commodity_24h` score `2.5793` n `101` status `ready` deltaP `31.7038` edge `0.2499` maxDD `-3.4467`
- `news_risk_high->crypto_alt_1h` score `2.3325` n `101` status `ready` deltaP `14.2853` edge `0.1457` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1248` n `101` status `ready` deltaP `16.3276` edge `0.194` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.6659` n `101` status `ready` deltaP `16.0817` edge `0.0839` maxDD `-2.8494`
- `market_context_high->equity_1h` score `0.7671` n `50` status `ready` deltaP `6.1198` edge `0.0479` maxDD `-0.3155`
- `market_context_high->index_4h` score `0.7047` n `50` status `ready` deltaP `16.9268` edge `0.0126` maxDD `-0.4751`
- `market_context_high->index_1h` score `0.6443` n `50` status `ready` deltaP `10.2156` edge `0.0109` maxDD `-0.0249`
- `news_risk_high->fx_4h` score `0.5762` n `101` status `ready` deltaP `12.4517` edge `0.0286` maxDD `-0.421`
- `news_risk_high->metal_1h` score `0.4831` n `101` status `ready` deltaP `13.2507` edge `0.0121` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.1845` n `101` status `ready` deltaP `13.2878` edge `0.0322` maxDD `-2.0994`
- `market_context_high->fx_1h` score `0.0571` n `50` status `ready` deltaP `5.4012` edge `0.0044` maxDD `-0.1854`
- `news_risk_high->fx_1h` score `0.0319` n `101` status `ready` deltaP `5.8368` edge `0.0081` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
