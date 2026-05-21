# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T05:37:17.142183+00:00`
- Price records: `672`
- Market context records: `1394`
- Flow alert records: `5925`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `12.8522` n `157` status `ready` deltaP `28.0067` edge `0.9975` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.5175` n `157` status `ready` deltaP `28.8184` edge `0.9693` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.3211` n `157` status `ready` deltaP `11.7359` edge `1.0319` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.0108` n `157` status `ready` deltaP `19.555` edge `0.3125` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.3622` n `157` status `ready` deltaP `12.7256` edge `0.3447` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5029` n `190` status `ready` deltaP `8.2702` edge `0.1531` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0535` n `157` status `ready` deltaP `9.8803` edge `0.0435` maxDD `-1.3925`
- `market_context_high->index_1h` score `0.0356` n `202` status `ready` deltaP `5.201` edge `0.0148` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0307` n `202` status `ready` deltaP `3.4045` edge `0.0306` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.3135` n `202` status `ready` deltaP `3.3957` edge `-0.0022` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.5034` n `190` status `ready` deltaP `0.8617` edge `0.0612` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.6103` n `202` status `ready` deltaP `5.1684` edge `-0.0013` maxDD `-4.5782`
- `market_context_high->metal_4h` score `-0.6514` n `190` status `ready` deltaP `8.1017` edge `0.0348` maxDD `-6.4478`
- `market_context_high->crypto_alt_1h` score `-0.6659` n `202` status `ready` deltaP `0.9545` edge `0.0252` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.9488` n `202` status `ready` deltaP `-2.1877` edge `-0.003` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.3309` n `190` status `ready` deltaP `7.6268` edge `0.1702` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.3666` n `190` status `ready` deltaP `4.8459` edge `0.1247` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.4013` n `202` status `ready` deltaP `-1.3132` edge `-0.0015` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.6135` n `190` status `ready` deltaP `-4.1848` edge `-0.0095` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-4.4088` n `190` status `ready` deltaP `-12.7696` edge `-0.0276` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
