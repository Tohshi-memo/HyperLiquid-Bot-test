# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T13:52:16.855918+00:00`
- Price records: `672`
- Market context records: `1532`
- Flow alert records: `6323`
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

- `market_context_high->metal_24h` score `13.2534` n `172` status `ready` deltaP `23.5949` edge `1.0472` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.8248` n `172` status `ready` deltaP `28.985` edge `0.9938` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.3621` n `172` status `ready` deltaP `28.3955` edge `0.7874` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.953` n `172` status `ready` deltaP `20.3327` edge `0.3025` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7249` n `172` status `ready` deltaP `13.6144` edge `0.369` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.8596` n `172` status `ready` deltaP `18.0515` edge `0.0562` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.1901` n `197` status `ready` deltaP `4.0934` edge `0.098` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.5779` n `197` status `ready` deltaP `10.9609` edge `0.1848` maxDD `-19.5565`
- `market_context_high->fx_1h` score `-0.5829` n `199` status `ready` deltaP `-1.2457` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.6037` n `199` status `ready` deltaP `-0.3799` edge `0.0275` maxDD `-4.1892`
- `market_context_high->crypto_major_4h` score `-0.6405` n `197` status `ready` deltaP `6.5951` edge `0.1448` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-0.7523` n `199` status `ready` deltaP `-0.6469` edge `0.0` maxDD `-4.7041`
- `market_context_high->index_1h` score `-0.7656` n `199` status `ready` deltaP `-0.1241` edge `0.0002` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7703` n `199` status `ready` deltaP `4.8484` edge `0.0025` maxDD `-6.3532`
- `market_context_high->equity_1h` score `-0.9159` n `199` status `ready` deltaP `-1.7813` edge `0.0164` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.1055` n `199` status `ready` deltaP `-1.7911` edge `0.0059` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.424` n `197` status `ready` deltaP `-4.9902` edge `0.0235` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.4611` n `197` status `ready` deltaP `9.2887` edge `0.0855` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.939` n `197` status `ready` deltaP `-8.4291` edge `-0.0125` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.2635` n `197` status `ready` deltaP `-16.3451` edge `-0.1143` maxDD `-23.7898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
