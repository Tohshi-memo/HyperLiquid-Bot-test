# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T15:52:19.493141+00:00`
- Price records: `672`
- Market context records: `1541`
- Flow alert records: `6347`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8803`

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

- `market_context_high->metal_24h` score `12.5638` n `179` status `ready` deltaP `23.1349` edge `0.9928` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.474` n `179` status `ready` deltaP `28.1851` edge `0.9699` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.6724` n `179` status `ready` deltaP `27.5731` edge `0.7354` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.1129` n `179` status `ready` deltaP `20.651` edge `0.3137` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6668` n `179` status `ready` deltaP `13.5931` edge `0.3643` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.7556` n `179` status `ready` deltaP `17.1855` edge `0.0533` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.1823` n `199` status `ready` deltaP `4.1764` edge `0.0968` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.4036` n `199` status `ready` deltaP `11.8826` edge `0.201` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.4857` n `199` status `ready` deltaP `7.9077` edge `0.1559` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.5133` n `199` status `ready` deltaP `0.0692` edge `0.0361` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.607` n `199` status `ready` deltaP `-1.6948` edge `-0.0033` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.7515` n `199` status `ready` deltaP `-0.6469` edge `0.0001` maxDD `-4.7041`
- `market_context_high->index_1h` score `-0.7704` n `199` status `ready` deltaP `-0.1241` edge `-0.0002` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7726` n `199` status `ready` deltaP `4.6987` edge `0.0032` maxDD `-6.3532`
- `market_context_high->equity_1h` score `-0.8751` n `199` status `ready` deltaP `-1.6316` edge `0.0188` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.0377` n `199` status `ready` deltaP `-1.342` edge `0.0116` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.3016` n `199` status `ready` deltaP `-9.1777` edge `-0.0128` maxDD `-1.4313`
- `market_context_high->index_4h` score `-1.4126` n `199` status `ready` deltaP `-4.5923` edge `0.0218` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.4433` n `199` status `ready` deltaP `9.6014` edge `0.0849` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-5.2926` n `199` status `ready` deltaP `-15.9196` edge `-0.1097` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
