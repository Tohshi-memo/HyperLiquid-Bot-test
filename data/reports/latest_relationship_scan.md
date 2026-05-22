# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T05:22:13.996540+00:00`
- Price records: `672`
- Market context records: `1496`
- Flow alert records: `6218`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8811`

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

- `market_context_high->metal_24h` score `12.4919` n `172` status `ready` deltaP `20.906` edge `1.01` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.4528` n `172` status `ready` deltaP `28.985` edge `0.9628` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.2908` n `172` status `ready` deltaP `27.3538` edge `0.7884` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.881` n `172` status `ready` deltaP `20.3327` edge `0.2965` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.1773` n `172` status `ready` deltaP `13.6144` edge `0.4067` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.2428` n `198` status `ready` deltaP `6.8937` edge `0.1406` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.9931` n `172` status `ready` deltaP `19.8401` edge `0.0554` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.2235` n `198` status `ready` deltaP `1.5287` edge `0.0312` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.2781` n `198` status `ready` deltaP `2.3151` edge `0.0079` maxDD `-1.7205`
- `market_context_high->crypto_alt_4h` score `-0.345` n `198` status `ready` deltaP `10.3212` edge `0.2344` maxDD `-19.5565`
- `market_context_high->crypto_alt_1h` score `-0.5181` n `198` status `ready` deltaP `1.5137` edge `0.0491` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.5254` n `198` status `ready` deltaP `-0.1693` edge `-0.003` maxDD `-0.3914`
- `market_context_high->crypto_major_4h` score `-0.7278` n `198` status `ready` deltaP `6.0806` edge `0.1697` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-0.7817` n `198` status `ready` deltaP `5.1987` edge `-0.0013` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-0.9595` n `198` status `ready` deltaP `-3.1534` edge `-0.0091` maxDD `-1.4313`
- `market_context_high->index_4h` score `-0.9649` n `198` status `ready` deltaP `-2.0263` edge `0.042` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-1.1248` n `198` status `ready` deltaP `-0.2994` edge `0.0004` maxDD `-4.7041`
- `market_context_high->metal_4h` score `-1.1873` n `198` status `ready` deltaP `11.5114` edge `0.0935` maxDD `-12.5349`
- `market_context_high->crypto_major_1h` score `-1.5345` n `198` status `ready` deltaP `-0.9738` edge `0.0143` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-4.3511` n `198` status `ready` deltaP `-14.4756` edge `-0.0897` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
