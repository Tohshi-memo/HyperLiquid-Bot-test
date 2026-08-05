# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T11:52:41.958213+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11648`

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

- `market_context_high->unknown_24h` score `13.9874` n `89` status `ready` deltaP `9.4667` edge `1.1068` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4239` n `92` status `ready` deltaP `2.2402` edge `0.5366` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.7783` n `92` status `ready` deltaP `18.4384` edge `0.1099` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.1817` n `89` status `ready` deltaP `27.8812` edge `0.0862` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.8901` n `89` status `ready` deltaP `1.6268` edge `0.2201` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.4465` n `98` status `ready` deltaP `7.592` edge `0.0282` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.0677` n `92` status `ready` deltaP `13.1363` edge `0.0071` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.048` n `98` status `ready` deltaP `6.3394` edge `-0.0033` maxDD `-0.7973`
- `market_context_high->metal_1h` score `-0.5715` n `98` status `ready` deltaP `-2.0286` edge `-0.0103` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6574` n `98` status `ready` deltaP `-1.8117` edge `-0.0188` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.9164` n `92` status `ready` deltaP `1.4382` edge `-0.0036` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.9448` n `98` status `ready` deltaP `-4.2863` edge `-0.0215` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.4383` n `89` status `ready` deltaP `0.6768` edge `-0.0446` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.5703` n `92` status `ready` deltaP `-0.8749` edge `-0.0565` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7785` n `98` status `ready` deltaP `2.5144` edge `-0.0912` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1532` n `92` status `ready` deltaP `-13.3219` edge `-0.0618` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.4477` n `89` status `ready` deltaP `-10.6079` edge `-0.0236` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.1649` n `98` status `ready` deltaP `4.598` edge `-0.2497` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.62` n `98` status `ready` deltaP `-13.2653` edge `-0.0759` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.0644` n `89` status `ready` deltaP `10.6507` edge `-0.0335` maxDD `-50.8663`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
