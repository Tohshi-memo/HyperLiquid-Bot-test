# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T19:45:18.570878+00:00`
- Price records: `672`
- Market context records: `6635`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11766`

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

- `market_context_high->unknown_1h` score `2.3411` n `203` status `ready` deltaP `-5.491` edge `0.3218` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `1.4618` n `189` status `ready` deltaP `-1.4958` edge `0.4481` maxDD `-12.3047`
- `market_context_high->commodity_24h` score `0.5703` n `189` status `ready` deltaP `10.1326` edge `0.1668` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.1111` n `203` status `ready` deltaP `8.8139` edge `0.0498` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1038` n `203` status `ready` deltaP `6.2011` edge `0.0431` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.222` n `203` status `ready` deltaP `3.2351` edge `0.0007` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.475` n `203` status `ready` deltaP `0.8208` edge `0.0054` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6731` n `203` status `ready` deltaP `-1.4387` edge `-0.0084` maxDD `-2.1314`
- `market_context_high->unknown_4h` score `-0.7249` n `203` status `ready` deltaP `-15.5766` edge `0.284` maxDD `-10.5788`
- `market_context_high->equity_1h` score `-0.7867` n `203` status `ready` deltaP `3.6511` edge `0.0128` maxDD `-3.8827`
- `market_context_high->index_4h` score `-0.8059` n `203` status `ready` deltaP `10.7788` edge `0.0128` maxDD `-5.7046`
- `market_context_high->crypto_major_4h` score `-1.0616` n `203` status `ready` deltaP `10.5671` edge `0.1249` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1125` n `203` status `ready` deltaP `-2.9077` edge `0.0008` maxDD `-1.5966`
- `market_context_high->commodity_4h` score `-1.3979` n `203` status `ready` deltaP `-1.3119` edge `-0.021` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.4552` n `203` status `ready` deltaP `7.4124` edge `0.1042` maxDD `-19.2145`
- `market_context_high->fx_4h` score `-1.4895` n `203` status `ready` deltaP `4.5371` edge `0.0` maxDD `-3.3635`
- `market_context_high->metal_4h` score `-1.9141` n `203` status `ready` deltaP `1.5221` edge `0.0305` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.3431` n `203` status `ready` deltaP `8.9834` edge `0.0051` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-5.5475` n `189` status `ready` deltaP `-2.8561` edge `0.026` maxDD `-22.4543`
- `market_context_high->fx_24h` score `-6.1522` n `189` status `ready` deltaP `-10.1124` edge `-0.006` maxDD `-10.475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
