# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T16:22:21.435942+00:00`
- Price records: `672`
- Market context records: `1543`
- Flow alert records: `6354`
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

- `market_context_high->metal_24h` score `12.6204` n `179` status `ready` deltaP `23.4821` edge `0.9952` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.3874` n `179` status `ready` deltaP `27.8379` edge `0.965` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.7217` n `179` status `ready` deltaP `27.9203` edge `0.7372` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0769` n `179` status `ready` deltaP `20.651` edge `0.3107` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6656` n `179` status `ready` deltaP `13.5931` edge `0.3642` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.7345` n `179` status `ready` deltaP `17.0119` edge `0.0527` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.2005` n `199` status `ready` deltaP `4.3288` edge `0.0973` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.3386` n `199` status `ready` deltaP `12.1875` edge `0.2073` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.4215` n `199` status `ready` deltaP `8.2125` edge `0.1621` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.4829` n `199` status `ready` deltaP `0.3686` edge `0.038` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6234` n `199` status `ready` deltaP `-1.9942` edge `-0.0034` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.7445` n `199` status `ready` deltaP `-0.6469` edge `0.001` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7734` n `199` status `ready` deltaP `4.6987` edge `0.0031` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.786` n `199` status `ready` deltaP `-0.2738` edge `-0.0005` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.8727` n `199` status `ready` deltaP `-1.6316` edge `0.019` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.0073` n `199` status `ready` deltaP `-1.0426` edge `0.0135` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.3183` n `199` status `ready` deltaP `-9.4826` edge `-0.0129` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.4021` n `199` status `ready` deltaP `9.9063` edge `0.0863` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.4234` n `199` status `ready` deltaP `-4.5923` edge `0.0209` maxDD `-3.7119`
- `market_context_high->commodity_4h` score `-5.2627` n `199` status `ready` deltaP `-15.6147` edge `-0.1079` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
