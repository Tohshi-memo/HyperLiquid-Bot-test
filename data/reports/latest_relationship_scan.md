# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T13:22:27.677108+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `news_risk_high->crypto_major_24h` score `21.7997` n `98` status `ready` deltaP `7.0614` edge `2.4554` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `19.9369` n `98` status `ready` deltaP `14.7463` edge `2.0512` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `16.6369` n `61` status `ready` deltaP `1.4844` edge `1.3915` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.9487` n `101` status `ready` deltaP `23.0349` edge `0.4631` maxDD `-7.675`
- `market_context_high->commodity_24h` score `5.3118` n `50` status `ready` deltaP `29.3056` edge `0.2998` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `4.4465` n `101` status `ready` deltaP `21.6629` edge `0.3519` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.2453` n `61` status `ready` deltaP `37.3051` edge `0.1184` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.0977` n `101` status `ready` deltaP `16.8302` edge `0.1925` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2463` n `101` status `ready` deltaP `18.4769` edge `0.1163` maxDD `-2.8494`
- `market_context_high->fx_4h` score `1.6461` n `61` status `ready` deltaP `22.4385` edge `0.0091` maxDD `-0.0543`
- `market_context_high->fx_24h` score `1.6183` n `50` status `ready` deltaP `18.8333` edge `0.0135` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.2463` n `61` status `ready` deltaP `14.6682` edge `0.0343` maxDD `-0.2583`
- `news_risk_high->commodity_24h` score `1.0386` n `98` status `ready` deltaP `22.775` edge `0.1119` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.7884` n `61` status `ready` deltaP `12.273` edge `0.0055` maxDD `-0.063`
- `news_risk_high->equity_24h` score `0.7049` n `98` status `ready` deltaP `16.571` edge `0.0892` maxDD `-4.941`
- `news_risk_high->metal_4h` score `0.6506` n `101` status `ready` deltaP `17.4037` edge `0.0436` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6413` n `101` status `ready` deltaP `14.7477` edge `0.0153` maxDD `-0.8144`
- `market_context_high->metal_1h` score `0.3115` n `61` status `ready` deltaP `8.4176` edge `0.0062` maxDD `-0.4568`
- `news_risk_high->metal_24h` score `0.285` n `98` status `ready` deltaP `15.5046` edge `0.0176` maxDD `-2.4203`
- `news_risk_high->equity_1h` score `0.2161` n `101` status `ready` deltaP `5.2143` edge `0.0238` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
