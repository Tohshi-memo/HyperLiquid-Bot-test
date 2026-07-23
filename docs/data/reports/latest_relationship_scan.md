# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T16:37:35.839322+00:00`
- Price records: `672`
- Market context records: `7687`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `2.5726` n `136` status `ready` deltaP `16.9451` edge `0.2356` maxDD `-6.0681`
- `market_context_high->crypto_major_4h` score `0.7456` n `137` status `ready` deltaP `13.656` edge `0.1429` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `0.6422` n `137` status `ready` deltaP `11.3139` edge `0.0352` maxDD `-2.5689`
- `market_context_high->equity_1h` score `0.4645` n `137` status `ready` deltaP `7.2346` edge `0.0764` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.2845` n `137` status `ready` deltaP `6.6617` edge `0.0997` maxDD `-4.6323`
- `market_context_high->index_1h` score `0.2448` n `137` status `ready` deltaP `7.4265` edge `0.0139` maxDD `-0.7743`
- `market_context_high->equity_4h` score `0.2423` n `137` status `ready` deltaP `2.4855` edge `0.2547` maxDD `-9.5503`
- `market_context_high->fx_24h` score `-0.123` n `136` status `ready` deltaP `10.7834` edge `0.0211` maxDD `-3.0343`
- `market_context_high->crypto_alt_1h` score `-0.2066` n `137` status `ready` deltaP `2.1428` edge `0.0245` maxDD `-2.4803`
- `market_context_high->index_4h` score `-0.2439` n `137` status `ready` deltaP `11.161` edge `0.0427` maxDD `-1.5364`
- `market_context_high->commodity_1h` score `-0.3439` n `137` status `ready` deltaP `2.1963` edge `0.0026` maxDD `-0.6722`
- `market_context_high->fx_1h` score `-0.442` n `137` status `ready` deltaP `0.4066` edge `-0.0008` maxDD `-0.4331`
- `market_context_high->commodity_4h` score `-0.4515` n `137` status `ready` deltaP `1.759` edge `0.01` maxDD `-1.0817`
- `market_context_high->metal_1h` score `-0.5916` n `137` status `ready` deltaP `1.0381` edge `0.0178` maxDD `-0.7115`
- `market_context_high->metal_24h` score `-0.9814` n `137` status `ready` deltaP `0.7274` edge `0.1064` maxDD `-3.2993`
- `market_context_high->metal_4h` score `-1.1422` n `137` status `ready` deltaP `0.4295` edge `0.0678` maxDD `-2.3684`
- `market_context_high->unknown_1h` score `-1.2728` n `137` status `ready` deltaP `-0.0841` edge `-0.0465` maxDD `-1.054`
- `market_context_high->commodity_24h` score `-1.5321` n `136` status `ready` deltaP `6.2205` edge `-0.0108` maxDD `-7.0012`
- `market_context_high->fx_4h` score `-1.5656` n `137` status `ready` deltaP `-5.1284` edge `-0.0034` maxDD `-1.7166`
- `market_context_high->unknown_4h` score `-2.8419` n `137` status `ready` deltaP `13.4802` edge `-0.1762` maxDD `-2.373`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
