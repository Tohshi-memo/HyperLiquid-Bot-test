# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T23:52:24.681414+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `market_context_high->unknown_24h` score `12.7096` n `90` status `ready` deltaP `4.4445` edge `1.0338` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `2.8859` n `109` status `ready` deltaP `-2.26` edge `0.3551` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1974` n `109` status `ready` deltaP `14.0566` edge `0.0907` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8704` n `90` status `ready` deltaP `2.0139` edge `0.215` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.817` n `90` status `ready` deltaP `24.7223` edge `0.0605` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4239` n `109` status `ready` deltaP `7.7597` edge `0.0252` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0416` n `109` status `ready` deltaP `6.1322` edge `-0.0024` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1209` n `109` status `ready` deltaP `9.3142` edge `0.0084` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5129` n `109` status `ready` deltaP `-1.4105` edge `-0.0069` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7721` n `109` status `ready` deltaP `2.9369` edge `0.0049` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.7735` n `109` status `ready` deltaP `-3.8057` edge `-0.0204` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-1.2995` n `90` status `ready` deltaP `0.5555` edge `-0.026` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.5061` n `109` status `ready` deltaP `-4.8385` edge `-0.0222` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.8549` n `109` status `ready` deltaP `0.82` edge `-0.0897` maxDD `-10.619`
- `market_context_high->index_24h` score `-2.0145` n `90` status `ready` deltaP `-7.257` edge `0.0096` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.1722` n `109` status `ready` deltaP `-13.5825` edge `-0.0625` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.2059` n `109` status `ready` deltaP `0.7747` edge `-0.05` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-3.3199` n `109` status `ready` deltaP `-11.1493` edge `-0.065` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.5429` n `109` status `ready` deltaP `1.7332` edge `-0.2621` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0871` n `90` status `ready` deltaP `10.3125` edge `-0.0277` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
