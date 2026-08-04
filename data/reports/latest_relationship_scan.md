# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T19:22:42.886708+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9856`

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

- `market_context_high->unknown_24h` score `23.5804` n `66` status `ready` deltaP `20.3598` edge `1.8336` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.5294` n `89` status `ready` deltaP `1.8498` edge `0.548` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.4018` n `89` status `ready` deltaP `16.597` edge `0.0908` maxDD `-2.7703`
- `market_context_high->crypto_alt_24h` score `1.1167` n `66` status `ready` deltaP `11.1584` edge `0.1492` maxDD `-3.7755`
- `market_context_high->fx_24h` score `0.1877` n `66` status `ready` deltaP `12.4369` edge `0.0533` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.1719` n `90` status `ready` deltaP `4.8935` edge `0.0233` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1494` n `90` status `ready` deltaP `7.6048` edge `-0.0034` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.1351` n `89` status `ready` deltaP `14.3721` edge `0.0075` maxDD `-1.8797`
- `market_context_high->metal_24h` score `-0.084` n `66` status `ready` deltaP `-8.2544` edge `0.1611` maxDD `-2.6802`
- `market_context_high->metal_1h` score `-0.5418` n `90` status `ready` deltaP `-1.6068` edge `-0.0093` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5651` n `90` status `ready` deltaP `-0.0066` edge `-0.019` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.7273` n `90` status `ready` deltaP `-2.3087` edge `-0.0068` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.7912` n `89` status `ready` deltaP `1.9852` edge `0.0088` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9019` n `89` status `ready` deltaP `4.0285` edge `-0.0035` maxDD `-5.7857`
- `market_context_high->commodity_24h` score `-1.548` n `66` status `ready` deltaP `15.2462` edge `0.061` maxDD `-22.2219`
- `market_context_high->equity_1h` score `-1.7251` n `90` status `ready` deltaP `4.3513` edge `-0.0966` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0385` n `89` status `ready` deltaP `-11.9553` edge `-0.0562` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.7826` n `66` status `ready` deltaP `-12.8945` edge `-0.0513` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.4368` n `90` status `ready` deltaP `-11.8596` edge `-0.07` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4624` n `90` status `ready` deltaP `2.1989` edge `-0.2585` maxDD `-1.2421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
