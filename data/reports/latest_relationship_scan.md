# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T14:07:20.993254+00:00`
- Price records: `672`
- Market context records: `1533`
- Flow alert records: `6326`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8792`

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

- `market_context_high->metal_24h` score `13.165` n `173` status `ready` deltaP `23.6151` edge `1.0397` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.8057` n `173` status `ready` deltaP `28.8215` edge `0.9933` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.31` n `173` status `ready` deltaP `28.4191` edge `0.7829` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.964` n `173` status `ready` deltaP `20.3797` edge `0.3031` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7172` n `173` status `ready` deltaP `13.6681` edge `0.368` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.8459` n `173` status `ready` deltaP `17.9552` edge `0.0557` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.1965` n `198` status `ready` deltaP `4.2344` edge `0.0976` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.5623` n `198` status `ready` deltaP `11.1404` edge `0.1856` maxDD `-19.5565`
- `market_context_high->fx_1h` score `-0.5907` n `199` status `ready` deltaP `-1.3954` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5951` n `199` status `ready` deltaP `-0.3799` edge `0.0286` maxDD `-4.1892`
- `market_context_high->crypto_major_4h` score `-0.6208` n `198` status `ready` deltaP `6.7951` edge `0.146` maxDD `-13.3376`
- `market_context_high->index_1h` score `-0.7656` n `199` status `ready` deltaP `-0.1241` edge `0.0002` maxDD `-1.7205`
- `market_context_high->commodity_1h` score `-0.7663` n `199` status `ready` deltaP `-0.7966` edge `-0.0008` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7672` n `199` status `ready` deltaP `4.8484` edge `0.0029` maxDD `-6.3532`
- `market_context_high->equity_1h` score `-0.9111` n `199` status `ready` deltaP `-1.7813` edge `0.0168` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.1031` n `199` status `ready` deltaP `-1.7911` edge `0.0062` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.4008` n `198` status `ready` deltaP `-4.7902` edge `0.0241` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.5261` n `198` status `ready` deltaP `8.9862` edge `0.0821` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.9581` n `198` status `ready` deltaP `-8.6521` edge `-0.0126` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.3258` n `198` status `ready` deltaP `-16.5143` edge `-0.1158` maxDD `-24.2185`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
