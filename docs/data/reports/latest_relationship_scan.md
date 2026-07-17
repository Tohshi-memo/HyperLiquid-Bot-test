# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T10:52:26.931778+00:00`
- Price records: `672`
- Market context records: `7020`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11529`

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

- `market_context_high->fx_1h` score `-0.2646` n `223` status `ready` deltaP `2.0213` edge `0.0011` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.6261` n `210` status `ready` deltaP `-6.3542` edge `0.4171` maxDD `-18.7342`
- `market_context_high->crypto_alt_1h` score `-0.6753` n `223` status `ready` deltaP `0.6693` edge `0.0257` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.6932` n `223` status `ready` deltaP `-1.8589` edge `0.0003` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.7305` n `223` status `ready` deltaP `-0.3659` edge `-0.0001` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.7621` n `223` status `ready` deltaP `2.3153` edge `0.0221` maxDD `-7.1523`
- `market_context_high->fx_4h` score `-0.9136` n `223` status `ready` deltaP `10.3932` edge `0.0062` maxDD `-2.0763`
- `market_context_high->commodity_1h` score `-1.3175` n `223` status `ready` deltaP `-3.0658` edge `-0.0172` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.3176` n `223` status `ready` deltaP `-2.6094` edge `-0.0023` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6754` n `223` status `ready` deltaP `-4.6628` edge `-0.0403` maxDD `-5.1394`
- `market_context_high->index_4h` score `-1.824` n `223` status `ready` deltaP `7.2097` edge `-0.012` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-1.9246` n `223` status `ready` deltaP `6.2213` edge `0.0101` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.35` n `223` status `ready` deltaP `-5.9308` edge `0.074` maxDD `-9.7569`
- `market_context_high->crypto_alt_4h` score `-2.7963` n `223` status `ready` deltaP `0.5913` edge `0.0161` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-2.836` n `210` status `ready` deltaP `-3.9384` edge `-0.0792` maxDD `-4.4704`
- `market_context_high->equity_1h` score `-3.0244` n `223` status `ready` deltaP `2.7725` edge `-0.0151` maxDD `-15.7664`
- `market_context_high->fx_24h` score `-4.0563` n `210` status `ready` deltaP `-4.8016` edge `-0.0148` maxDD `-4.6306`
- `market_context_high->crypto_major_4h` score `-4.9019` n `223` status `ready` deltaP `1.614` edge `0.0092` maxDD `-24.6094`
- `market_context_high->equity_4h` score `-11.6447` n `223` status `ready` deltaP `3.8281` edge `-0.0742` maxDD `-66.7371`
- `market_context_high->metal_24h` score `-13.4629` n `210` status `ready` deltaP `-10.4812` edge `-0.0551` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
