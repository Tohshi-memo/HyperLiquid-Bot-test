# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T06:07:18.590907+00:00`
- Price records: `672`
- Market context records: `1707`
- Flow alert records: `6822`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->unknown_24h` score `8.3857` n `139` status `ready` deltaP `18.0827` edge `1.1103` maxDD `-35.8966`
- `market_context_high->metal_24h` score `6.519` n `139` status `ready` deltaP `25.3578` edge `0.6168` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.9578` n `197` status `ready` deltaP `21.3709` edge `0.5371` maxDD `-16.3135`
- `market_context_high->crypto_major_4h` score `4.1242` n `197` status `ready` deltaP `23.2458` edge `0.4596` maxDD `-13.3376`
- `market_context_high->index_24h` score `3.6796` n `139` status `ready` deltaP `16.6251` edge `0.3336` maxDD `-5.3574`
- `market_context_high->equity_4h` score `2.9922` n `197` status `ready` deltaP `16.3357` edge `0.2499` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.4525` n `139` status `ready` deltaP `15.4775` edge `0.5077` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.8945` n `197` status `ready` deltaP `7.8612` edge `0.1245` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.4718` n `197` status `ready` deltaP `8.162` edge `0.0938` maxDD `-3.7119`
- `market_context_high->crypto_alt_24h` score `0.2348` n `139` status `ready` deltaP `23.8468` edge `1.0415` maxDD `-88.8062`
- `market_context_high->crypto_major_1h` score `0.2229` n `197` status `ready` deltaP `5.2061` edge `0.0915` maxDD `-3.9439`
- `market_context_high->equity_1h` score `-0.0315` n `197` status `ready` deltaP `4.0533` edge `0.0512` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.2902` n `197` status `ready` deltaP `13.0478` edge `0.145` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.5119` n `197` status `ready` deltaP `0.4674` edge `0.0174` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.5536` n `197` status `ready` deltaP `5.6552` edge `0.0249` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6542` n `197` status `ready` deltaP `-2.8572` edge `-0.0016` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.8369` n `139` status `ready` deltaP `4.3601` edge `0.0061` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-0.9331` n `139` status `ready` deltaP `22.0433` edge `0.592` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.7811` n `197` status `ready` deltaP `-6.7553` edge `-0.0105` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.0762` n `197` status `ready` deltaP `0.1299` edge `-0.0216` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
