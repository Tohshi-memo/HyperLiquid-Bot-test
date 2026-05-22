# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T16:07:25.126704+00:00`
- Price records: `672`
- Market context records: `1542`
- Flow alert records: `6350`
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

- `market_context_high->metal_24h` score `12.5945` n `179` status `ready` deltaP `23.3085` edge `0.9942` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.4301` n `179` status `ready` deltaP `28.0115` edge `0.9674` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.6982` n `179` status `ready` deltaP `27.7467` edge `0.7364` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0937` n `179` status `ready` deltaP `20.651` edge `0.3121` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6656` n `179` status `ready` deltaP `13.5931` edge `0.3642` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.752` n `179` status `ready` deltaP `17.1855` edge `0.053` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.1835` n `199` status `ready` deltaP `4.1764` edge `0.0969` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.3699` n `199` status `ready` deltaP `12.035` edge `0.2043` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.452` n `199` status `ready` deltaP `8.0601` edge `0.1592` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.4977` n `199` status `ready` deltaP `0.2189` edge `0.0371` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6156` n `199` status `ready` deltaP `-1.8445` edge `-0.0034` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.7476` n `199` status `ready` deltaP `-0.6469` edge `0.0006` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7742` n `199` status `ready` deltaP `4.6987` edge `0.003` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.7848` n `199` status `ready` deltaP `-0.2738` edge `-0.0004` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.8739` n `199` status `ready` deltaP `-1.6316` edge `0.0189` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.0213` n `199` status `ready` deltaP `-1.1923` edge `0.0127` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.3103` n `199` status `ready` deltaP `-9.3302` edge `-0.0129` maxDD `-1.4313`
- `market_context_high->index_4h` score `-1.4198` n `199` status `ready` deltaP `-4.5923` edge `0.0212` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.4203` n `199` status `ready` deltaP `9.7538` edge `0.0858` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-5.2753` n `199` status `ready` deltaP `-15.7671` edge `-0.1085` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
