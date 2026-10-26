# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T18:22:30.995477+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8092`

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

- `market_context_high->unknown_4h` score `95.5364` n `152` status `ready` deltaP `0.6178` edge `7.9908` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `28.3069` n `153` status `ready` deltaP `1.4745` edge `2.398` maxDD `-1.5807`
- `market_context_high->metal_24h` score `0.4039` n `112` status `ready` deltaP `25.6685` edge `0.1433` maxDD `-7.0108`
- `market_context_high->fx_1h` score `0.2303` n `153` status `ready` deltaP `7.8157` edge `0.0029` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1331` n `152` status `ready` deltaP `9.4111` edge `0.0082` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0051` n `112` status `ready` deltaP `16.3051` edge `0.0145` maxDD `-4.5747`
- `market_context_high->fx_24h` score `-0.1356` n `112` status `ready` deltaP `16.972` edge `0.0267` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.1408` n `153` status `ready` deltaP `8.1807` edge `0.0066` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.2762` n `153` status `ready` deltaP `2.1526` edge `0.0127` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5767` n `153` status `ready` deltaP `0.1624` edge `-0.0013` maxDD `-1.8971`
- `market_context_high->commodity_4h` score `-0.6994` n `152` status `ready` deltaP `4.2763` edge `0.0361` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.9309` n `153` status `ready` deltaP `3.7846` edge `0.0135` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9679` n `152` status `ready` deltaP `7.1726` edge `-0.0009` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.7957` n `153` status `ready` deltaP `1.7543` edge `-0.0143` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0271` n `153` status `ready` deltaP `-0.8747` edge `-0.0056` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.4206` n `152` status `ready` deltaP `-6.4666` edge `-0.0243` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.4102` n `112` status `ready` deltaP `-2.4449` edge `-0.0634` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.6985` n `152` status `ready` deltaP `-1.2596` edge `-0.09` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.0938` n `112` status `ready` deltaP `-3.5637` edge `-0.2142` maxDD `-35.4638`
- `market_context_high->commodity_24h` score `-6.3197` n `112` status `ready` deltaP `-16.9039` edge `-0.1386` maxDD `-24.0477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
