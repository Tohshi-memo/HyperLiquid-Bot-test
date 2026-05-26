# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T23:37:16.368433+00:00`
- Price records: `672`
- Market context records: `1987`
- Flow alert records: `7611`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7584`

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

- `market_context_high->crypto_alt_4h` score `7.5778` n `231` status `ready` deltaP `23.1232` edge `0.5918` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.474` n `231` status `ready` deltaP `27.4278` edge `0.5331` maxDD `-3.4494`
- `market_context_high->unknown_4h` score `3.1285` n `231` status `ready` deltaP `14.6421` edge `0.3354` maxDD `-8.4514`
- `market_context_high->equity_4h` score `2.2597` n `231` status `ready` deltaP `14.1538` edge `0.2034` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.9539` n `196` status `ready` deltaP `16.5397` edge `0.5846` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.908` n `196` status `ready` deltaP `16.7703` edge `0.2898` maxDD `-12.7414`
- `market_context_high->equity_24h` score `1.2913` n `196` status `ready` deltaP `15.5333` edge `0.4939` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `1.1053` n `231` status `ready` deltaP `10.1732` edge `0.1229` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.8274` n `231` status `ready` deltaP `8.3282` edge `0.1248` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `0.5813` n `196` status `ready` deltaP `20.0133` edge `0.7736` maxDD `-62.3533`
- `market_context_high->index_24h` score `0.4243` n `196` status `ready` deltaP `3.8999` edge `0.1322` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.2872` n `231` status `ready` deltaP `7.3798` edge `0.0689` maxDD `-3.533`
- `market_context_high->fx_24h` score `0.1217` n `196` status `ready` deltaP `11.6228` edge `0.0226` maxDD `-1.1952`
- `market_context_high->equity_1h` score `-0.1998` n `231` status `ready` deltaP `4.0394` edge `0.0358` maxDD `-2.6836`
- `market_context_high->fx_1h` score `-0.6513` n `231` status `ready` deltaP `-2.996` edge `-0.0003` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7303` n `231` status `ready` deltaP `-0.8074` edge `0.0077` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.9408` n `231` status `ready` deltaP `1.7498` edge `0.0013` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.202` n `231` status `ready` deltaP `-9.1919` edge `-0.0041` maxDD `-1.0983`
- `market_context_high->unknown_1h` score `-1.3871` n `231` status `ready` deltaP `1.2359` edge `-0.0288` maxDD `-3.6022`
- `market_context_high->commodity_1h` score `-1.8962` n `231` status `ready` deltaP `1.8146` edge `0.0006` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
