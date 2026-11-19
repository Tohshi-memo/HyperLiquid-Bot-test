# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T16:07:47.921669+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2600`

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

- `market_context_high->unknown_1h` score `12131.4063` n `107` status `ready` deltaP `0.5751` edge `1010.9665` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `8047.3714` n `102` status `ready` deltaP `-0.3736` edge `670.6452` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `25.0777` n `88` status `ready` deltaP `45.4545` edge `1.8461` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.7079` n `88` status `ready` deltaP `23.5322` edge `1.4834` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.9927` n `102` status `ready` deltaP `3.8767` edge `0.4221` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.37` n `102` status `ready` deltaP `4.7914` edge `0.2898` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.5253` n `102` status `ready` deltaP `18.5348` edge `0.0492` maxDD `-5.9858`
- `market_context_high->metal_24h` score `0.3859` n `88` status `ready` deltaP `18.7184` edge `0.2162` maxDD `-14.7068`
- `market_context_high->metal_1h` score `-0.234` n `107` status `ready` deltaP `3.611` edge `0.0124` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.3004` n `107` status `ready` deltaP `4.1328` edge `0.0736` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.3397` n `107` status `ready` deltaP `2.2273` edge `0.0028` maxDD `-1.2295`
- `market_context_high->index_4h` score `-1.2013` n `102` status `ready` deltaP `-2.9203` edge `-0.0002` maxDD `-4.7471`
- `market_context_high->crypto_alt_1h` score `-1.3411` n `107` status `ready` deltaP `-2.8583` edge `0.0295` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.63` n `107` status `ready` deltaP `5.031` edge `0.0085` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6519` n `107` status `ready` deltaP `-11.9775` edge `-0.0021` maxDD `-0.4566`
- `market_context_high->fx_4h` score `-2.3772` n `102` status `ready` deltaP `-14.9061` edge `-0.0038` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4991` n `107` status `ready` deltaP `-10.3713` edge `-0.0313` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-7.1214` n `88` status `ready` deltaP `-23.4217` edge `-0.01` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.3614` n `102` status `ready` deltaP `-31.0049` edge `-0.1282` maxDD `-14.9509`
- `market_context_high->equity_4h` score `-9.188` n `102` status `ready` deltaP `-7.9328` edge `-0.0451` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
