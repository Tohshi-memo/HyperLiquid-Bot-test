# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T11:52:27.892643+00:00`
- Price records: `672`
- Market context records: `7136`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11692`

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

- `market_context_high->fx_4h` score `0.7735` n `139` status `ready` deltaP `17.8584` edge `0.0154` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1748` n `151` status `ready` deltaP `4.1777` edge `0.0027` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.4738` n `151` status `ready` deltaP `-2.6986` edge `0.0427` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6213` n `151` status `ready` deltaP `-0.1814` edge `0.0246` maxDD `-5.91`
- `market_context_high->crypto_major_1h` score `-0.6683` n `151` status `ready` deltaP `3.1298` edge `0.0345` maxDD `-7.6171`
- `market_context_high->index_1h` score `-0.6706` n `151` status `ready` deltaP `2.3228` edge `-0.0049` maxDD `-2.3175`
- `market_context_high->commodity_1h` score `-0.6948` n `151` status `ready` deltaP `-1.5743` edge `-0.0165` maxDD `-1.9668`
- `market_context_high->metal_1h` score `-1.3369` n `151` status `ready` deltaP `-4.5128` edge `-0.0052` maxDD `-2.0897`
- `market_context_high->commodity_4h` score `-2.1877` n `139` status `ready` deltaP `-5.7565` edge `-0.0404` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-2.2038` n `139` status `ready` deltaP `-5.2115` edge `0.0201` maxDD `-5.1872`
- `market_context_high->crypto_major_4h` score `-3.4255` n `139` status `ready` deltaP `0.0066` edge `-0.0092` maxDD `-24.734`
- `market_context_high->equity_1h` score `-3.5032` n `151` status `ready` deltaP `-0.0674` edge `-0.0457` maxDD `-14.9961`
- `market_context_high->index_4h` score `-4.0383` n `139` status `ready` deltaP `-2.3283` edge `-0.0511` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.3073` n `139` status `ready` deltaP `-7.7229` edge `-0.0126` maxDD `-5.2551`
- `market_context_high->commodity_24h` score `-4.488` n `133` status `ready` deltaP `-13.4581` edge `-0.1534` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.9851` n `133` status `ready` deltaP `-16.0518` edge `-0.0257` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-5.5528` n `139` status `ready` deltaP `-3.9865` edge `-0.0462` maxDD `-23.1965`
- `market_context_high->unknown_24h` score `-10.1263` n `133` status `ready` deltaP `-32.8765` edge `-0.11` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.9437` n `139` status `ready` deltaP `-1.5902` edge `-0.2578` maxDD `-64.4856`
- `market_context_high->metal_24h` score `-14.4104` n `133` status `ready` deltaP `-29.3455` edge `-0.1871` maxDD `-40.7836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
