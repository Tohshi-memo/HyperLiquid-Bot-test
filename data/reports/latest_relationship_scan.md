# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T04:22:16.582340+00:00`
- Price records: `672`
- Market context records: `2007`
- Flow alert records: `7670`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9107`

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

- `market_context_high->crypto_major_4h` score `8.8117` n `212` status `ready` deltaP `30.5855` edge `0.5834` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.239` n `212` status `ready` deltaP `24.3529` edge `0.6387` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.6676` n `212` status `ready` deltaP `18.9168` edge `0.4211` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.7162` n `212` status `ready` deltaP `15.7501` edge `0.2308` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.4688` n `212` status `ready` deltaP `12.137` edge `0.1401` maxDD `-3.2225`
- `market_context_high->unknown_24h` score `1.2499` n `185` status `ready` deltaP `15.6599` edge `0.5318` maxDD `-35.8966`
- `market_context_high->crypto_alt_1h` score `1.1505` n `212` status `ready` deltaP `9.5921` edge `0.1433` maxDD `-4.9097`
- `market_context_high->index_4h` score `1.1179` n `212` status `ready` deltaP `10.7426` edge `0.0899` maxDD `-1.8022`
- `market_context_high->metal_24h` score `0.8443` n `185` status `ready` deltaP `14.5289` edge `0.2161` maxDD `-12.7414`
- `market_context_high->equity_24h` score `0.616` n `185` status `ready` deltaP `14.4715` edge `0.4447` maxDD `-33.1875`
- `market_context_high->fx_24h` score `0.5441` n `185` status `ready` deltaP `15.8951` edge `0.0285` maxDD `-1.7964`
- `market_context_high->equity_1h` score `0.0201` n `212` status `ready` deltaP `5.5361` edge `0.0436` maxDD `-2.6402`
- `market_context_high->index_24h` score `-0.0447` n `185` status `ready` deltaP `2.7472` edge `0.1008` maxDD `-4.1604`
- `market_context_high->index_1h` score `-0.4858` n `212` status `ready` deltaP `0.9237` edge `0.0124` maxDD `-1.3898`
- `market_context_high->unknown_1h` score `-0.6137` n `212` status `ready` deltaP `3.5279` edge `-0.0027` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.7369` n `212` status `ready` deltaP `2.576` edge `0.0071` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.7897` n `212` status `ready` deltaP `-0.5762` edge `0.0008` maxDD `-0.3548`
- `market_context_high->crypto_major_24h` score `-1.0082` n `185` status `ready` deltaP `18.2053` edge `0.6532` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.5781` n `212` status `ready` deltaP `-6.25` edge `-0.0017` maxDD `-1.0513`
- `market_context_high->metal_4h` score `-1.637` n `212` status `ready` deltaP `6.9518` edge `0.0795` maxDD `-11.9812`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
