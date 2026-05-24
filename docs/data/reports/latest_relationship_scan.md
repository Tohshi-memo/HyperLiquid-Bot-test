# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T05:22:17.298638+00:00`
- Price records: `672`
- Market context records: `1704`
- Flow alert records: `6812`
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

- `market_context_high->unknown_24h` score `8.5334` n `139` status `ready` deltaP `18.4288` edge `1.1203` maxDD `-35.8966`
- `market_context_high->metal_24h` score `6.4386` n `139` status `ready` deltaP `25.3578` edge `0.6101` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.0636` n `195` status `ready` deltaP `21.6425` edge `0.5441` maxDD `-16.3135`
- `market_context_high->crypto_major_4h` score `4.0528` n `195` status `ready` deltaP `22.8486` edge `0.4563` maxDD `-13.3376`
- `market_context_high->index_24h` score `3.742` n `139` status `ready` deltaP `16.6251` edge `0.3388` maxDD `-5.3574`
- `market_context_high->equity_4h` score `2.9987` n `195` status `ready` deltaP `16.0858` edge `0.2521` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.5965` n `139` status `ready` deltaP `15.4775` edge `0.5197` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.8274` n `197` status `ready` deltaP `7.4121` edge `0.1219` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.4448` n `195` status `ready` deltaP `7.8392` edge `0.0937` maxDD `-3.7119`
- `market_context_high->crypto_alt_24h` score `0.3224` n `139` status `ready` deltaP `23.8468` edge `1.0488` maxDD `-88.8062`
- `market_context_high->crypto_major_1h` score `0.1581` n `197` status `ready` deltaP `5.0564` edge `0.0871` maxDD `-3.9439`
- `market_context_high->equity_1h` score `-0.0327` n `197` status `ready` deltaP `4.0533` edge `0.0511` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.3976` n `195` status `ready` deltaP `12.6469` edge `0.1339` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.5203` n `197` status `ready` deltaP `0.4674` edge `0.0167` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.6106` n `197` status `ready` deltaP `5.6552` edge `0.0176` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6776` n `197` status `ready` deltaP `-3.1566` edge `-0.0026` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.8525` n `139` status `ready` deltaP `4.3601` edge `0.0048` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-0.8902` n `139` status `ready` deltaP `22.0433` edge `0.5975` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.8534` n `195` status `ready` deltaP `-7.4492` edge `-0.0119` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.1433` n `197` status `ready` deltaP `-0.0198` edge `-0.0292` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
