# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T03:22:26.349939+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9754`

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

- `market_context_high->unknown_4h` score `46.0448` n `46` status `ready` deltaP `7.1646` edge `3.7893` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.6235` n `46` status `ready` deltaP `13.5341` edge `2.394` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6177` n `46` status `ready` deltaP `12.1453` edge `1.3139` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.8568` n `46` status `ready` deltaP `10.5903` edge `1.0008` maxDD `0.0`
- `market_context_high->index_24h` score `5.6325` n `46` status `ready` deltaP `20.6522` edge `0.3404` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.9299` n `96` status `ready` deltaP `-9.2014` edge `1.158` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.5114` n `96` status `ready` deltaP `34.8958` edge `0.2612` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.843` n `97` status `ready` deltaP `13.9128` edge `0.2019` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.2552` n `97` status `ready` deltaP `9.0348` edge `0.2275` maxDD `-5.9838`
- `market_context_high->index_4h` score `2.0613` n `46` status `ready` deltaP `24.2311` edge `0.0236` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `1.8407` n `102` status `ready` deltaP `10.9545` edge `0.1294` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.4315` n `102` status `ready` deltaP `13.2001` edge `0.0748` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3997` n `97` status `ready` deltaP `20.661` edge `0.0425` maxDD `-0.421`
- `news_risk_high->fx_24h` score `0.8753` n `96` status `ready` deltaP `23.7847` edge `0.1126` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.7981` n `46` status `ready` deltaP `6.7626` edge `0.0457` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6938` n `46` status `ready` deltaP `10.8045` edge `0.0111` maxDD `-0.0249`
- `market_context_high->equity_4h` score `0.5773` n `46` status `ready` deltaP `4.4804` edge `0.0489` maxDD `-0.4529`
- `news_risk_high->metal_1h` score `0.4419` n `102` status `ready` deltaP `13.0445` edge `0.0092` maxDD `-0.7468`
- `market_context_high->metal_24h` score `0.4329` n `46` status `ready` deltaP `17.7537` edge `-0.0589` maxDD `-0.2042`
- `news_risk_high->metal_4h` score `0.4081` n `97` status `ready` deltaP `13.5404` edge `0.0395` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
