# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T04:07:17.020637+00:00`
- Price records: `672`
- Market context records: `1698`
- Flow alert records: `6797`
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

- `market_context_high->unknown_24h` score `8.8006` n `139` status `ready` deltaP `19.2938` edge `1.1368` maxDD `-35.8966`
- `market_context_high->metal_24h` score `6.2766` n `139` status `ready` deltaP `25.3578` edge `0.5966` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.9626` n `194` status `ready` deltaP `21.2503` edge `0.5383` maxDD `-16.3135`
- `market_context_high->crypto_major_4h` score `3.8721` n `194` status `ready` deltaP `22.4195` edge `0.4441` maxDD `-13.3376`
- `market_context_high->index_24h` score `3.8404` n `139` status `ready` deltaP `16.6251` edge `0.347` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.0041` n `194` status `ready` deltaP `15.9589` edge `0.2534` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.8269` n `139` status `ready` deltaP `15.4775` edge `0.5389` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7555` n `197` status `ready` deltaP `6.963` edge `0.1189` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.44` n `139` status `ready` deltaP `23.8468` edge `1.0586` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.4208` n `194` status `ready` deltaP `7.6753` edge `0.0928` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.115` n `197` status `ready` deltaP `4.757` edge `0.0855` maxDD `-3.9439`
- `market_context_high->equity_1h` score `-0.0016` n `197` status `ready` deltaP `4.3527` edge `0.0517` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.5311` n `197` status `ready` deltaP `0.3177` edge `0.0168` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.565` n `194` status `ready` deltaP `12.4434` edge `0.1138` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.6449` n `197` status `ready` deltaP `-2.5578` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.6526` n `197` status `ready` deltaP `5.0564` edge `0.0162` maxDD `-6.3532`
- `market_context_high->crypto_major_24h` score `-0.8426` n `139` status `ready` deltaP `22.0433` edge `0.6036` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.8777` n `139` status `ready` deltaP `4.3601` edge `0.0027` maxDD `-1.3925`
- `market_context_high->fx_4h` score `-1.8826` n `194` status `ready` deltaP `-7.5135` edge `-0.0139` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.1324` n `197` status `ready` deltaP `0.1299` edge `-0.0288` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
