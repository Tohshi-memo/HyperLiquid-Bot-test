# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T12:07:28.333914+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8465`

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

- `market_context_high->unknown_24h` score `1497.6826` n `135` status `ready` deltaP `-3.7616` edge `124.9247` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `26.2998` n `148` status `ready` deltaP `4.7833` edge `2.175` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.7479` n `135` status `ready` deltaP `27.1875` edge `0.0332` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2656` n `149` status `ready` deltaP `8.3169` edge `0.0025` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0422` n `148` status `ready` deltaP `8.4542` edge `0.007` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0793` n `149` status `ready` deltaP `8.4767` edge `0.008` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3593` n `149` status `ready` deltaP `7.1294` edge `0.0347` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.4013` n `148` status `ready` deltaP `7.0863` edge `0.0412` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.4769` n `135` status `ready` deltaP `11.5625` edge `0.019` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.6413` n `148` status `ready` deltaP `10.6295` edge `0.001` maxDD `-4.6603`
- `market_context_high->commodity_1h` score `-0.6596` n `149` status `ready` deltaP `-0.4903` edge `0.0067` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7359` n `149` status `ready` deltaP `-3.4743` edge `-0.0029` maxDD `-1.4631`
- `market_context_high->equity_1h` score `-1.4755` n `149` status `ready` deltaP `0.4903` edge `-0.0012` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6118` n `149` status `ready` deltaP `2.5961` edge `0.0124` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.3262` n `135` status `ready` deltaP `8.0671` edge `0.0488` maxDD `-15.7143`
- `market_context_high->metal_24h` score `-2.3992` n `135` status `ready` deltaP `5.3356` edge `0.0423` maxDD `-8.2244`
- `market_context_high->index_4h` score `-3.0186` n `148` status `ready` deltaP `-9.0846` edge `-0.0288` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.3235` n `135` status `ready` deltaP `0.544` edge `0.056` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5123` n `148` status `ready` deltaP `3.5761` edge `-0.0422` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.4871` n `148` status `ready` deltaP `-4.3795` edge `-0.1509` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
