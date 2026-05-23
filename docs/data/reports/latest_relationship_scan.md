# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T14:22:18.666307+00:00`
- Price records: `672`
- Market context records: `1638`
- Flow alert records: `6624`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `9.9068` n `178` status `ready` deltaP `27.2506` edge `0.8865` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.3977` n `178` status `ready` deltaP `19.3261` edge `0.2921` maxDD `-5.3574`
- `market_context_high->crypto_alt_4h` score `2.7425` n `185` status `ready` deltaP `18.5043` edge `0.3716` maxDD `-16.3135`
- `market_context_high->equity_4h` score `1.4471` n `185` status `ready` deltaP `11.5866` edge `0.1528` maxDD `-5.0894`
- `market_context_high->crypto_major_4h` score `1.3561` n `185` status `ready` deltaP `14.2638` edge `0.2888` maxDD `-13.3376`
- `market_context_high->equity_24h` score `0.9743` n `178` status `ready` deltaP `17.9454` edge `0.4514` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `-0.1332` n `195` status `ready` deltaP `2.2632` edge `0.0702` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `-0.2011` n `178` status `ready` deltaP `23.5693` edge `0.6847` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.3943` n `178` status `ready` deltaP `6.9675` edge `0.0256` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.5075` n `195` status `ready` deltaP `0.1896` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->equity_1h` score `-0.5516` n `195` status `ready` deltaP `0.7631` edge `0.0298` maxDD `-2.8014`
- `market_context_high->commodity_1h` score `-0.5759` n `195` status `ready` deltaP `1.986` edge `0.0009` maxDD `-4.7041`
- `market_context_high->index_1h` score `-0.6588` n `195` status `ready` deltaP `0.3555` edge `0.0059` maxDD `-1.7205`
- `market_context_high->crypto_major_1h` score `-0.8083` n `195` status `ready` deltaP `-0.8552` edge `0.0342` maxDD `-5.9032`
- `market_context_high->index_4h` score `-0.8401` n `185` status `ready` deltaP `-0.0009` edge `0.0389` maxDD `-3.7119`
- `market_context_high->crypto_alt_24h` score `-1.0772` n `178` status `ready` deltaP `23.946` edge `0.9315` maxDD `-88.8062`
- `market_context_high->metal_1h` score `-1.4264` n `195` status `ready` deltaP `1.7726` edge `0.0029` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.5113` n `185` status `ready` deltaP `7.3266` edge `0.0944` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-2.0388` n `185` status `ready` deltaP `-9.5413` edge `-0.0134` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.7134` n `185` status `ready` deltaP `8.4702` edge `-0.1388` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
