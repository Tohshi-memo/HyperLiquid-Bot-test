# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T06:22:15.249656+00:00`
- Price records: `672`
- Market context records: `1708`
- Flow alert records: `6825`
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

- `market_context_high->unknown_24h` score `8.3335` n `139` status `ready` deltaP `17.9097` edge `1.1071` maxDD `-35.8966`
- `market_context_high->metal_24h` score `6.5478` n `139` status `ready` deltaP `25.3578` edge `0.6192` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.9844` n `197` status `ready` deltaP `21.5233` edge `0.5383` maxDD `-16.3135`
- `market_context_high->crypto_major_4h` score `4.1628` n `197` status `ready` deltaP `23.3982` edge `0.4618` maxDD `-13.3376`
- `market_context_high->index_24h` score `3.6604` n `139` status `ready` deltaP `16.6251` edge `0.332` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.0056` n `197` status `ready` deltaP `16.4882` edge `0.25` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.4069` n `139` status `ready` deltaP `15.4775` edge `0.5039` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.8957` n `197` status `ready` deltaP `7.8612` edge `0.1246` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.4888` n `197` status `ready` deltaP `8.3145` edge `0.0942` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.2457` n `197` status `ready` deltaP `5.2061` edge `0.0934` maxDD `-3.9439`
- `market_context_high->crypto_alt_24h` score `0.2024` n `139` status `ready` deltaP `23.8468` edge `1.0388` maxDD `-88.8062`
- `market_context_high->equity_1h` score `-0.0172` n `197` status `ready` deltaP `4.203` edge `0.0514` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.2605` n `197` status `ready` deltaP `13.0478` edge `0.1488` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.4951` n `197` status `ready` deltaP `0.6171` edge `0.0178` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.524` n `197` status `ready` deltaP `5.6552` edge `0.0287` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6511` n `197` status `ready` deltaP `-2.8572` edge `-0.0012` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.8309` n `139` status `ready` deltaP `4.3601` edge `0.0066` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-0.9495` n `139` status `ready` deltaP `22.0433` edge `0.5899` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.7751` n `197` status `ready` deltaP `-6.7553` edge `-0.01` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.038` n `197` status `ready` deltaP `0.2796` edge `-0.0177` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
