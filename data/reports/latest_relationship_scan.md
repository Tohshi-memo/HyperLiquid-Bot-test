# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T23:36:02.975507+00:00`
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

- `market_context_high->unknown_24h` score `12.7336` n `90` status `ready` deltaP `4.4445` edge `1.0358` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `2.904` n `109` status `ready` deltaP `-2.1076` edge `0.3556` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1998` n `109` status `ready` deltaP `14.0566` edge `0.0909` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8774` n `90` status `ready` deltaP `2.0139` edge `0.2159` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.8217` n `90` status `ready` deltaP `24.7223` edge `0.0611` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4239` n `109` status `ready` deltaP `7.7597` edge `0.0252` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0428` n `109` status `ready` deltaP `6.1322` edge `-0.0023` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1122` n `109` status `ready` deltaP `9.4666` edge `0.0085` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5012` n `109` status `ready` deltaP `-1.2608` edge `-0.0064` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7587` n `109` status `ready` deltaP `3.0894` edge `0.0056` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.7743` n `109` status `ready` deltaP `-3.8057` edge `-0.0205` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-1.3065` n `90` status `ready` deltaP `0.5555` edge `-0.0269` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.4918` n `109` status `ready` deltaP `-4.6888` edge `-0.022` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.8689` n `109` status `ready` deltaP `0.6703` edge `-0.0905` maxDD `-10.619`
- `market_context_high->index_24h` score `-2.0375` n `90` status `ready` deltaP `-7.4306` edge `0.0078` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.1817` n `109` status `ready` deltaP `-13.7349` edge `-0.0627` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.2301` n `109` status `ready` deltaP `0.6223` edge `-0.051` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-3.3044` n `109` status `ready` deltaP `-10.9996` edge `-0.0647` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.5237` n `109` status `ready` deltaP `1.8829` edge `-0.2615` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0871` n `90` status `ready` deltaP `10.3125` edge `-0.0277` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
