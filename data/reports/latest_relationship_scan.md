# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T03:52:16.513063+00:00`
- Price records: `672`
- Market context records: `1697`
- Flow alert records: `6794`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->unknown_24h` score `8.8481` n `139` status `ready` deltaP `19.4668` edge `1.1396` maxDD `-35.8966`
- `market_context_high->metal_24h` score `6.2442` n `139` status `ready` deltaP `25.3578` edge `0.5939` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.0175` n `193` status `ready` deltaP `21.4718` edge `0.5414` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.8584` n `139` status `ready` deltaP `16.6251` edge `0.3485` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `3.8429` n `193` status `ready` deltaP `22.294` edge `0.4425` maxDD `-13.3376`
- `market_context_high->equity_4h` score `3.007` n `193` status `ready` deltaP `15.8307` edge `0.2545` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.8665` n `139` status `ready` deltaP `15.4775` edge `0.5422` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7507` n `197` status `ready` deltaP `6.963` edge `0.1185` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.458` n `139` status `ready` deltaP `23.8468` edge `1.0601` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.4016` n `193` status `ready` deltaP `7.5097` edge `0.0923` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.1006` n `197` status `ready` deltaP `4.6073` edge `0.0853` maxDD `-3.9439`
- `market_context_high->equity_1h` score `-0.016` n `197` status `ready` deltaP `4.203` edge `0.0515` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.5323` n `197` status `ready` deltaP `0.3177` edge `0.0167` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.6123` n `193` status `ready` deltaP `12.2377` edge `0.1091` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.6371` n `197` status `ready` deltaP `-2.4081` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.6519` n `197` status `ready` deltaP `5.0564` edge `0.0163` maxDD `-6.3532`
- `market_context_high->crypto_major_24h` score `-0.8372` n `139` status `ready` deltaP `22.0433` edge `0.6043` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.8825` n `139` status `ready` deltaP `4.3601` edge `0.0023` maxDD `-1.3925`
- `market_context_high->fx_4h` score `-1.2221` n `193` status `ready` deltaP `-7.4229` edge `-0.0143` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.1355` n `197` status `ready` deltaP `0.1299` edge `-0.0292` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
