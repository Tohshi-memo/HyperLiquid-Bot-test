# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T12:18:04.980073+00:00`
- Price records: `672`
- Market context records: `1116`
- Flow alert records: `5118`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8704`

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

- `market_context_high->crypto_major_24h` score `18.3613` n `150` status `ready` deltaP `39.6389` edge `1.3122` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `8.0` n `150` status `ready` deltaP `16.0` edge `0.6834` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.5997` n `150` status `ready` deltaP `16.5208` edge `0.4895` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.5679` n `150` status `ready` deltaP `-1.8889` edge `0.6433` maxDD `-6.3373`
- `market_context_high->index_24h` score `5.2511` n `150` status `ready` deltaP `15.4791` edge `0.3652` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.5701` n `168` status `ready` deltaP `8.9649` edge `0.1374` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.8462` n `168` status `ready` deltaP `7.8324` edge `0.0866` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4881` n `168` status `ready` deltaP `7.6454` edge `0.0214` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2153` n `168` status `ready` deltaP `2.2811` edge `0.0405` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1352` n `168` status `ready` deltaP `8.3155` edge `0.0014` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.0079` n `168` status `ready` deltaP `7.9994` edge `0.1398` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `-0.0098` n `168` status `ready` deltaP `6.8328` edge `0.0302` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.2352` n `168` status `ready` deltaP `6.8007` edge `-0.0039` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.3473` n `168` status `ready` deltaP `2.495` edge `0.0387` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.7057` n `168` status `ready` deltaP `1.2412` edge `0.0009` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7349` n `168` status `ready` deltaP `-1.9247` edge `-0.0006` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.0482` n `168` status `ready` deltaP `5.3862` edge `0.1262` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.4384` n `168` status `ready` deltaP `6.0903` edge `-0.0484` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1582` n `168` status `ready` deltaP `-11.1208` edge `-0.014` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.3479` n `168` status `ready` deltaP `9.0085` edge `-0.2174` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
