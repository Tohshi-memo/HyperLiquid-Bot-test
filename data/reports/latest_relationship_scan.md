# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T06:07:15.027269+00:00`
- Price records: `672`
- Market context records: `1602`
- Flow alert records: `6525`
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

- `market_context_high->metal_24h` score `14.1064` n `183` status `ready` deltaP `30.9426` edge `1.0693` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `12.9331` n `183` status `ready` deltaP `27.3281` edge `1.0972` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.9807` n `183` status `ready` deltaP `27.0976` edge `0.8476` maxDD `-8.0553`
- `market_context_high->equity_24h` score `5.4271` n `183` status `ready` deltaP `21.5619` edge `0.5412` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.3051` n `183` status `ready` deltaP `23.0533` edge `0.3137` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.1897` n `199` status `ready` deltaP `10.2739` edge `0.1401` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.1314` n `199` status `ready` deltaP `12.6448` edge `0.2645` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.033` n `199` status `ready` deltaP `8.8223` edge `0.2163` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.1809` n `183` status `ready` deltaP `7.7442` edge `0.0382` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3636` n `199` status `ready` deltaP `0.5183` edge `0.0523` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5467` n `199` status `ready` deltaP `0.9133` edge `0.0292` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.6024` n `199` status `ready` deltaP `-1.5451` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6793` n `199` status `ready` deltaP `0.4747` edge `0.0034` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7236` n `199` status `ready` deltaP `5.2975` edge `0.0055` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7897` n `199` status `ready` deltaP `-1.2457` edge `-0.0008` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.9028` n `199` status `ready` deltaP `-0.8929` edge `0.0259` maxDD `-6.1883`
- `market_context_high->index_4h` score `-0.9655` n `199` status `ready` deltaP `-0.324` edge `0.0306` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3823` n `199` status `ready` deltaP `9.4489` edge `0.091` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.4037` n `199` status `ready` deltaP `-10.8546` edge `-0.0147` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.1865` n `199` status `ready` deltaP `-14.0903` edge `-0.1083` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
