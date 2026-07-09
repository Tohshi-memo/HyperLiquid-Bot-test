# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T01:37:28.180451+00:00`
- Price records: `672`
- Market context records: `6145`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `11.6087` n `30` status `ready` deltaP `41.0764` edge `0.7083` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.7306` n `30` status `ready` deltaP `68.4028` edge `0.1882` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3323` n `32` status `ready` deltaP `45.1982` edge `0.0643` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.429` n `32` status `ready` deltaP `29.1916` edge `0.0217` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.3999` n `195` status `ready` deltaP `0.3555` edge `0.2151` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.1942` n `32` status `ready` deltaP `12.9304` edge `0.1136` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6245` n `32` status `ready` deltaP `8.3271` edge `0.0707` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.25` n `195` status `ready` deltaP `3.2927` edge `0.0906` maxDD `-2.671`
- `news_risk_high->crypto_major_24h` score `0.151` n `30` status `ready` deltaP `11.5972` edge `0.02` maxDD `-4.2368`
- `news_risk_high->index_24h` score `-0.2149` n `30` status `ready` deltaP `7.5` edge `0.0096` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2513` n `195` status `ready` deltaP `1.8839` edge `-0.0002` maxDD `-0.5659`
- `market_context_high->unknown_4h` score `-0.3665` n `195` status `ready` deltaP `-2.6118` edge `0.2401` maxDD `-11.925`
- `market_context_high->metal_4h` score `-0.599` n `195` status `ready` deltaP `3.847` edge `0.0163` maxDD `-3.4996`
- `news_risk_high->commodity_24h` score `-0.6067` n `30` status `ready` deltaP `14.0973` edge `-0.124` maxDD `-0.3101`
- `market_context_high->metal_24h` score `-0.6091` n `195` status `ready` deltaP `17.078` edge `0.0649` maxDD `-11.8809`
- `market_context_high->commodity_1h` score `-0.7487` n `195` status `ready` deltaP `-1.9891` edge `-0.0045` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7652` n `32` status `ready` deltaP `-2.994` edge `-0.0284` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8116` n `195` status `ready` deltaP `2.3906` edge `-0.0037` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.8554` n `195` status `ready` deltaP `-1.3074` edge `0.0106` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.9514` n `195` status `ready` deltaP `3.3111` edge `0.0312` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
