# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T08:37:24.727496+00:00`
- Price records: `672`
- Market context records: `6373`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11118`

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

- `news_risk_high->crypto_alt_24h` score `14.4019` n `32` status `ready` deltaP `38.7153` edge `0.9568` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3184` n `32` status `ready` deltaP `52.4306` edge `0.177` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3223` n `32` status `ready` deltaP `17.5347` edge `0.5152` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `4.0844` n `32` status `ready` deltaP `35.4167` edge `0.1248` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.962` n `32` status `ready` deltaP `40.9299` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3859` n `32` status `ready` deltaP `28.7425` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5216` n `32` status `ready` deltaP `14.7268` edge `0.1436` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9057` n `32` status `ready` deltaP `11.3211` edge `0.0868` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.4854` n `216` status `ready` deltaP `15.0576` edge `0.0415` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.2882` n `220` status `ready` deltaP `-6.3255` edge `0.167` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.1481` n `216` status `ready` deltaP `8.7568` edge `0.0216` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.3136` n `32` status `ready` deltaP `6.2313` edge `-0.0332` maxDD `-0.7581`
- `market_context_high->metal_1h` score `-0.395` n `220` status `ready` deltaP `3.6636` edge `0.0027` maxDD `-1.8877`
- `market_context_high->metal_24h` score `-0.4407` n `138` status `ready` deltaP `17.4366` edge `0.0841` maxDD `-11.8809`
- `market_context_high->index_1h` score `-0.6401` n `220` status `ready` deltaP `-1.9515` edge `0.0029` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.6502` n `220` status `ready` deltaP `0.1061` edge `-0.0015` maxDD `-0.9376`
- `market_context_high->commodity_24h` score `-0.6787` n `138` status `ready` deltaP `-4.7554` edge `0.1311` maxDD `-6.2457`
- `news_risk_high->metal_1h` score `-0.7014` n `32` status `ready` deltaP `-2.2455` edge `-0.0252` maxDD `-1.6464`
- `news_risk_high->index_24h` score `-0.7245` n `32` status `ready` deltaP `0.5208` edge `-0.0092` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.8943` n `216` status `ready` deltaP `6.984` edge `0.0488` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
