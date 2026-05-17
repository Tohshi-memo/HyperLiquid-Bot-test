# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T12:52:12.913174+00:00`
- Price records: `672`
- Market context records: `1013`
- Flow alert records: `4826`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8634`

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

- `market_context_high->crypto_major_24h` score `13.339` n `199` status `ready` deltaP `32.27` edge `0.9553` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.2383` n `199` status `ready` deltaP `11.0537` edge `0.4029` maxDD `-9.5387`
- `market_context_high->index_24h` score `0.0426` n `199` status `ready` deltaP `5.4912` edge `0.1537` maxDD `-4.9405`
- `market_context_high->equity_24h` score `-0.0786` n `199` status `ready` deltaP `6.1478` edge `0.1766` maxDD `-9.5972`
- `market_context_high->fx_1h` score `-0.2751` n `199` status `ready` deltaP `2.1861` edge `-0.0001` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5069` n `199` status `ready` deltaP `2.6465` edge `0.0209` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.745` n `199` status `ready` deltaP `-0.392` edge `0.0174` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.7552` n `199` status `ready` deltaP `2.4629` edge `0.006` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-0.9666` n `199` status `ready` deltaP `2.5041` edge `0.0024` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.301` n `199` status `ready` deltaP `3.8862` edge `-0.0204` maxDD `-11.4508`
- `market_context_high->equity_4h` score `-1.3933` n `199` status `ready` deltaP `2.1441` edge `0.0848` maxDD `-10.5498`
- `market_context_high->crypto_alt_1h` score `-1.42` n `199` status `ready` deltaP `-1.9626` edge `-0.025` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.6114` n `199` status `ready` deltaP `-1.2662` edge `0.0218` maxDD `-6.1444`
- `market_context_high->metal_1h` score `-1.8001` n `199` status `ready` deltaP `0.5928` edge `-0.0388` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-2.975` n `199` status `ready` deltaP `6.643` edge `0.0784` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-3.1187` n `199` status `ready` deltaP `-1.182` edge `0.0258` maxDD `-15.2248`
- `market_context_high->commodity_4h` score `-3.125` n `199` status `ready` deltaP `-1.4937` edge `0.0663` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.3521` n `199` status `ready` deltaP `-0.0062` edge `-0.021` maxDD `-19.3643`
- `market_context_high->metal_4h` score `-4.5092` n `199` status `ready` deltaP `-3.4578` edge `-0.166` maxDD `-24.4577`
- `market_context_high->commodity_24h` score `-8.537` n `199` status `ready` deltaP `1.3944` edge `0.361` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
