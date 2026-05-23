# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T05:37:17.591415+00:00`
- Price records: `672`
- Market context records: `1600`
- Flow alert records: `6519`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `14.2229` n `182` status `ready` deltaP `31.1088` edge `1.0779` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `13.1319` n `182` status `ready` deltaP `27.5183` edge `1.1125` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `11.151` n `182` status `ready` deltaP `27.2608` edge `0.8607` maxDD `-8.0553`
- `market_context_high->equity_24h` score `5.5179` n `182` status `ready` deltaP `21.7071` edge `0.5478` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.356` n `182` status `ready` deltaP `23.2105` edge `0.3169` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.1581` n `199` status `ready` deltaP `9.9691` edge `0.1395` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.1015` n `199` status `ready` deltaP `12.3399` edge `0.2627` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.0314` n `199` status `ready` deltaP `8.8223` edge `0.2161` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.1503` n `182` status `ready` deltaP `8.0223` edge `0.0389` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3581` n `199` status `ready` deltaP `0.5183` edge `0.053` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5348` n `199` status `ready` deltaP `1.063` edge `0.0292` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.6024` n `199` status `ready` deltaP `-1.5451` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6805` n `199` status `ready` deltaP `0.4747` edge `0.0033` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.722` n `199` status `ready` deltaP `5.2975` edge `0.0057` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.8029` n `199` status `ready` deltaP `-1.3954` edge `-0.0015` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.8778` n `199` status `ready` deltaP `-0.5935` edge `0.0271` maxDD `-6.1883`
- `market_context_high->index_4h` score `-0.9923` n `199` status `ready` deltaP `-0.6289` edge `0.0304` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3701` n `199` status `ready` deltaP `9.6014` edge `0.091` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3878` n `199` status `ready` deltaP `-10.5497` edge `-0.0147` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.2094` n `199` status `ready` deltaP `-14.3952` edge `-0.1092` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
