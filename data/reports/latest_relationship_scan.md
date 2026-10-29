# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T11:07:30.436345+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7072`

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

- `market_context_high->unknown_24h` score `1254.0454` n `149` status `ready` deltaP `-2.0216` edge `104.61` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `31.8354` n `149` status `ready` deltaP `4.8423` edge `2.6359` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.5205` n `149` status `ready` deltaP `17.9204` edge `-0.0073` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.0907` n `149` status `ready` deltaP `6.3708` edge `0.0009` maxDD `-0.1986`
- `market_context_high->commodity_4h` score `-0.1121` n `149` status `ready` deltaP `10.2503` edge `0.0442` maxDD `-1.0837`
- `market_context_high->fx_4h` score `-0.1404` n `149` status `ready` deltaP `6.7718` edge `0.003` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1525` n `149` status `ready` deltaP `7.4288` edge `0.0056` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.4894` n `149` status `ready` deltaP `5.1833` edge `0.031` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.4907` n `149` status `ready` deltaP `1.1564` edge `0.0098` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.8123` n `149` status `ready` deltaP `7.8368` edge `-0.0023` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.8442` n `149` status `ready` deltaP `-5.2707` edge `-0.0048` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-1.4617` n `149` status `ready` deltaP `4.0385` edge `0.0085` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.5565` n `149` status `ready` deltaP `-0.7073` edge `-0.0036` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.7068` n `149` status `ready` deltaP `1.2488` edge `0.0092` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1717` n `149` status `ready` deltaP `-10.3986` edge `-0.0328` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.4115` n `149` status `ready` deltaP `2.2897` edge `-0.0207` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.6615` n `149` status `ready` deltaP `-1.9213` edge `0.0291` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.9761` n `149` status `ready` deltaP `-0.5069` edge `-0.0216` maxDD `-10.5088`
- `market_context_high->equity_4h` score `-5.5137` n `149` status `ready` deltaP `-4.6969` edge `-0.1522` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.9597` n `149` status `ready` deltaP `1.813` edge `-0.2123` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
