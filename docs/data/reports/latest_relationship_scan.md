# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T03:37:17.687008+00:00`
- Price records: `672`
- Market context records: `1591`
- Flow alert records: `6495`
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

- `market_context_high->metal_24h` score `13.8634` n `182` status `ready` deltaP `29.7199` edge `1.0572` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `12.4753` n `182` status `ready` deltaP `27.171` edge `1.0601` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.7224` n `182` status `ready` deltaP `26.9135` edge `0.8273` maxDD `-8.0553`
- `market_context_high->equity_24h` score `4.928` n `182` status `ready` deltaP `20.3182` edge `0.5079` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.194` n `182` status `ready` deltaP `21.9952` edge `0.3115` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.1167` n `199` status `ready` deltaP `9.5117` edge `0.1391` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.219` n `199` status `ready` deltaP `12.9496` edge `0.2737` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.0926` n `199` status `ready` deltaP `9.2796` edge `0.2209` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.0272` n `182` status `ready` deltaP `9.4112` edge `0.0399` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3441` n `199` status `ready` deltaP `0.668` edge `0.0538` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5779` n `199` status `ready` deltaP `0.6139` edge `0.0286` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.6024` n `199` status `ready` deltaP `-1.5451` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7105` n `199` status `ready` deltaP `0.1753` edge `0.0028` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7142` n `199` status `ready` deltaP `5.4472` edge `0.0057` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.8224` n `199` status `ready` deltaP `-1.6948` edge `-0.002` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.8592` n `199` status `ready` deltaP `-0.2941` edge `0.0275` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.0569` n `199` status `ready` deltaP `-1.3911` edge `0.0301` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.2862` n `199` status `ready` deltaP `10.516` edge `0.0919` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3712` n `199` status `ready` deltaP `-10.2448` edge `-0.0146` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.2526` n `199` status `ready` deltaP `-14.7001` edge `-0.1127` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
