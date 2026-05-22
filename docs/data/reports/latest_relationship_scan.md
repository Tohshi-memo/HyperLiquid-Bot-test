# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T02:07:19.253856+00:00`
- Price records: `672`
- Market context records: `1483`
- Flow alert records: `6178`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8810`

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

- `market_context_high->crypto_alt_24h` score `12.4116` n `172` status `ready` deltaP `28.985` edge `1.0427` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `11.324` n `172` status `ready` deltaP `27.3538` edge `0.8745` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.0532` n `172` status `ready` deltaP `16.0126` edge `0.9769` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.1666` n `172` status `ready` deltaP `20.3327` edge `0.3203` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.0917` n `172` status `ready` deltaP `13.6144` edge `0.4829` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5777` n `211` status `ready` deltaP `7.1957` edge `0.1665` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.5623` n `172` status `ready` deltaP `15.3545` edge `0.0494` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `0.1603` n `211` status `ready` deltaP `12.4371` edge `0.2624` maxDD `-19.5565`
- `market_context_high->equity_1h` score `-0.0196` n `211` status `ready` deltaP `2.8776` edge `0.0392` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1195` n `211` status `ready` deltaP `3.4268` edge `0.0137` maxDD `-1.7205`
- `market_context_high->crypto_alt_1h` score `-0.4818` n `211` status `ready` deltaP `1.8326` edge `0.05` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.5683` n `211` status `ready` deltaP `-0.9358` edge `-0.0034` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.5916` n `211` status `ready` deltaP `0.0896` edge `0.059` maxDD `-3.7119`
- `market_context_high->crypto_major_4h` score `-0.6807` n `211` status `ready` deltaP `7.2238` edge `0.166` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.0206` n `211` status `ready` deltaP `-4.2834` edge `-0.0094` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-1.1869` n `211` status `ready` deltaP `-0.9855` edge `-0.0002` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.193` n `211` status `ready` deltaP `5.1998` edge `-0.0005` maxDD `-6.3532`
- `market_context_high->crypto_major_1h` score `-1.5519` n `211` status `ready` deltaP `-0.8613` edge `0.0121` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7413` n `211` status `ready` deltaP `8.1414` edge `0.0698` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.086` n `211` status `ready` deltaP `-12.2876` edge `-0.0703` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
