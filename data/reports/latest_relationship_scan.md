# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T05:52:12.351017+00:00`
- Price records: `672`
- Market context records: `1601`
- Flow alert records: `6522`
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

- `market_context_high->metal_24h` score `14.0625` n `183` status `ready` deltaP `30.769` edge `1.0668` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `12.822` n `183` status `ready` deltaP `27.1545` edge `1.0891` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.9092` n `183` status `ready` deltaP `26.924` edge `0.8428` maxDD `-8.0553`
- `market_context_high->equity_24h` score `5.3544` n `183` status `ready` deltaP `21.3883` edge `0.5363` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.2828` n `183` status `ready` deltaP `22.8797` edge `0.313` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.1739` n `199` status `ready` deltaP `10.1215` edge `0.1398` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.1133` n `199` status `ready` deltaP `12.4923` edge `0.2632` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.0314` n `199` status `ready` deltaP `8.8223` edge `0.2161` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.1659` n `183` status `ready` deltaP `7.9178` edge `0.0383` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3612` n `199` status `ready` deltaP `0.5183` edge `0.0526` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5348` n `199` status `ready` deltaP `1.063` edge `0.0292` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.6024` n `199` status `ready` deltaP `-1.5451` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6793` n `199` status `ready` deltaP `0.4747` edge `0.0034` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7228` n `199` status `ready` deltaP `5.2975` edge `0.0056` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.8014` n `199` status `ready` deltaP `-1.3954` edge `-0.0013` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.8903` n `199` status `ready` deltaP `-0.7432` edge `0.0265` maxDD `-6.1883`
- `market_context_high->index_4h` score `-0.9789` n `199` status `ready` deltaP `-0.4765` edge `0.0305` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3701` n `199` status `ready` deltaP `9.6014` edge `0.091` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3957` n `199` status `ready` deltaP `-10.7021` edge `-0.0147` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.1976` n `199` status `ready` deltaP `-14.2427` edge `-0.1087` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
