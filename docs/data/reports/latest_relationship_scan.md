# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T03:37:20.979805+00:00`
- Price records: `672`
- Market context records: `1696`
- Flow alert records: `6791`
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

- `market_context_high->unknown_24h` score `8.9063` n `139` status `ready` deltaP `19.6398` edge `1.1433` maxDD `-35.8966`
- `market_context_high->metal_24h` score `6.2106` n `139` status `ready` deltaP `25.3578` edge `0.5911` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.0764` n `192` status `ready` deltaP `21.6972` edge `0.5448` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.8776` n `139` status `ready` deltaP `16.6251` edge `0.3501` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `3.8171` n `192` status `ready` deltaP `22.1671` edge `0.4412` maxDD `-13.3376`
- `market_context_high->equity_4h` score `3.0075` n `192` status `ready` deltaP `15.7012` edge `0.2554` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.9085` n `139` status `ready` deltaP `15.4775` edge `0.5457` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7435` n `197` status `ready` deltaP `6.963` edge `0.1179` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.4688` n `139` status `ready` deltaP `23.8468` edge `1.061` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.3834` n `192` status `ready` deltaP `7.3424` edge `0.0919` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.0994` n `197` status `ready` deltaP `4.6073` edge `0.0852` maxDD `-3.9439`
- `market_context_high->equity_1h` score `-0.0291` n `197` status `ready` deltaP `4.0533` edge `0.0514` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.5335` n `197` status `ready` deltaP `0.3177` edge `0.0166` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6371` n `197` status `ready` deltaP `-2.4081` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.6511` n `197` status `ready` deltaP `5.0564` edge `0.0164` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.6598` n `192` status `ready` deltaP `12.0299` edge `0.1044` maxDD `-12.5349`
- `market_context_high->crypto_major_24h` score `-0.8333` n `139` status `ready` deltaP `22.0433` edge `0.6048` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.8873` n `139` status `ready` deltaP `4.3601` edge `0.0019` maxDD `-1.3925`
- `market_context_high->fx_4h` score `-1.8763` n `192` status `ready` deltaP `-7.3298` edge `-0.0146` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.1386` n `197` status `ready` deltaP `0.1299` edge `-0.0296` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
