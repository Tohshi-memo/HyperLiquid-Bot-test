# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T04:22:18.355062+00:00`
- Price records: `672`
- Market context records: `1699`
- Flow alert records: `6800`
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

- `market_context_high->unknown_24h` score `8.752` n `139` status `ready` deltaP `19.1208` edge `1.1339` maxDD `-35.8966`
- `market_context_high->metal_24h` score `6.3102` n `139` status `ready` deltaP `25.3578` edge `0.5994` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.9188` n `195` status `ready` deltaP `21.0327` edge `0.5361` maxDD `-16.3135`
- `market_context_high->crypto_major_4h` score `3.9001` n `195` status `ready` deltaP `22.5437` edge `0.4456` maxDD `-13.3376`
- `market_context_high->index_24h` score `3.82` n `139` status `ready` deltaP `16.6251` edge `0.3453` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.0083` n `195` status `ready` deltaP `16.0858` edge `0.2529` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.7825` n `139` status `ready` deltaP `15.4775` edge `0.5352` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7698` n `197` status `ready` deltaP `7.1127` edge `0.1191` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.4376` n `195` status `ready` deltaP `7.8392` edge `0.0931` maxDD `-3.7119`
- `market_context_high->crypto_alt_24h` score `0.4148` n `139` status `ready` deltaP `23.8468` edge `1.0565` maxDD `-88.8062`
- `market_context_high->crypto_major_1h` score `0.1162` n `197` status `ready` deltaP `4.757` edge `0.0856` maxDD `-3.9439`
- `market_context_high->equity_1h` score `-0.0136` n `197` status `ready` deltaP `4.203` edge `0.0517` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.5201` n `195` status `ready` deltaP `12.6469` edge `0.1182` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.5323` n `197` status `ready` deltaP `0.3177` edge `0.0167` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.6433` n `197` status `ready` deltaP `5.2061` edge `0.0164` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6449` n `197` status `ready` deltaP `-2.5578` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->crypto_major_24h` score `-0.8512` n `139` status `ready` deltaP `22.0433` edge `0.6025` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.8717` n `139` status `ready` deltaP `4.3601` edge `0.0032` maxDD `-1.3925`
- `market_context_high->fx_4h` score `-1.886` n `195` status `ready` deltaP `-7.6016` edge `-0.0136` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.1308` n `197` status `ready` deltaP `0.1299` edge `-0.0286` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
