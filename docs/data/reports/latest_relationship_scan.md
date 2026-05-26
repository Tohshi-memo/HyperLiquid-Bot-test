# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T16:07:19.704969+00:00`
- Price records: `672`
- Market context records: `1953`
- Flow alert records: `7518`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7547`

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

- `market_context_high->crypto_alt_4h` score `7.0253` n `232` status `ready` deltaP `21.7364` edge `0.555` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4803` n `232` status `ready` deltaP `25.414` edge `0.4952` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.3527` n `232` status `ready` deltaP `13.3424` edge `0.3095` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.0776` n `232` status `ready` deltaP `14.1874` edge `0.188` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.0438` n `199` status `ready` deltaP `16.249` edge `0.5107` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.8301` n `234` status `ready` deltaP `8.3538` edge `0.1121` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.6624` n `234` status `ready` deltaP `7.6463` edge `0.1156` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.3307` n `199` status `ready` deltaP `12.1584` edge `0.1891` maxDD `-12.7414`
- `market_context_high->index_4h` score `0.1364` n `232` status `ready` deltaP `8.3797` edge `0.0644` maxDD `-3.7119`
- `market_context_high->index_24h` score `0.1297` n `199` status `ready` deltaP `4.1922` edge `0.1057` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.2362` n `234` status `ready` deltaP `4.6497` edge `0.0287` maxDD `-2.6836`
- `market_context_high->equity_24h` score `-0.2405` n `199` status `ready` deltaP `10.6655` edge `0.3987` maxDD `-33.1875`
- `market_context_high->fx_24h` score `-0.2603` n `199` status `ready` deltaP `9.9323` edge `0.017` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6353` n `234` status `ready` deltaP `0.6347` edge `0.006` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6421` n `234` status `ready` deltaP `-2.8635` edge `0.0` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0707` n `232` status `ready` deltaP `-6.8166` edge `-0.003` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.234` n `234` status `ready` deltaP `3.5468` edge `0.0071` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.5563` n `234` status `ready` deltaP `0.3596` edge `-0.0369` maxDD `-3.6151`
- `market_context_high->crypto_major_24h` score `-1.6644` n `199` status `ready` deltaP `15.2071` edge `0.6185` maxDD `-62.3533`
- `market_context_high->metal_4h` score `-1.8347` n `232` status `ready` deltaP `6.7944` edge `0.071` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
