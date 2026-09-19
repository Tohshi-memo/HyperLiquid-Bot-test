# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T04:52:26.686592+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8324`

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

- `news_risk_high->crypto_major_24h` score `60.5412` n `56` status `ready` deltaP `35.2182` edge `4.8995` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `54.5502` n `56` status `ready` deltaP `37.5992` edge `4.4331` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.3455` n `149` status `ready` deltaP `-1.3781` edge `3.0613` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `14.3836` n `56` status `ready` deltaP `48.7847` edge `0.8734` maxDD `0.0`
- `risk_on_high->unknown_4h` score `10.2241` n `52` status `ready` deltaP `-8.6187` edge `0.932` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `10.2241` n `52` status `ready` deltaP `-8.6187` edge `0.932` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.9144` n `72` status `ready` deltaP `28.6755` edge `0.6643` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.2712` n `52` status `ready` deltaP `44.9653` edge `0.3895` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2712` n `52` status `ready` deltaP `44.9653` edge `0.3895` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.9721` n `149` status `ready` deltaP `38.2539` edge `0.3785` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.0466` n `72` status `ready` deltaP `24.9492` edge `0.455` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.7039` n `56` status `ready` deltaP `37.9464` edge `0.1548` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.2817` n `81` status `ready` deltaP `17.3006` edge `0.2047` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6293` n `81` status `ready` deltaP `20.0691` edge `0.1376` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.52` n `52` status `ready` deltaP `30.1008` edge `0.0443` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.52` n `52` status `ready` deltaP `30.1008` edge `0.0443` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4197` n `149` status `ready` deltaP `26.6031` edge `0.0661` maxDD `-0.345`
- `news_risk_high->equity_4h` score `1.5523` n `72` status `ready` deltaP `12.3984` edge `0.1367` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.5519` n `72` status `ready` deltaP `16.9207` edge `0.0384` maxDD `-0.084`
- `news_risk_high->fx_24h` score `1.3696` n `56` status `ready` deltaP `7.4157` edge `0.0689` maxDD `-0.0029`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
