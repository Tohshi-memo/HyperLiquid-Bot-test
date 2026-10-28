# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T23:22:26.734367+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8280`

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

- `market_context_high->unknown_24h` score `1248.5763` n `148` status `ready` deltaP `-2.135` edge `104.155` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.258` n `149` status `ready` deltaP `4.385` edge `1.7575` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.9886` n `148` status `ready` deltaP `20.9366` edge `0.0116` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2572` n `149` status `ready` deltaP `8.3169` edge `0.0018` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0383` n `149` status `ready` deltaP `7.8388` edge `0.0044` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0995` n `149` status `ready` deltaP `8.327` edge `0.0064` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.3613` n `149` status `ready` deltaP `7.8112` edge `0.0397` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.3655` n `149` status `ready` deltaP `6.5306` edge `0.0379` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.6189` n `149` status `ready` deltaP `-0.1909` edge `0.0081` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7422` n `149` status `ready` deltaP `-3.624` edge `-0.0027` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.7902` n `148` status `ready` deltaP `10.4965` edge `0.0214` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.8666` n `149` status `ready` deltaP `7.227` edge `-0.0052` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.4038` n `149` status `ready` deltaP `1.0891` edge `0.004` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5798` n `149` status `ready` deltaP `2.7458` edge `0.0155` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0736` n `149` status `ready` deltaP `-9.6364` edge `-0.0297` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.4284` n `149` status `ready` deltaP `3.5092` edge `-0.031` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.5805` n `148` status `ready` deltaP `-0.2393` edge `0.0052` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-3.7685` n `148` status `ready` deltaP `-2.4493` edge `0.0189` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-4.417` n `148` status `ready` deltaP `3.4863` edge `-0.0949` maxDD `-15.7143`
- `market_context_high->equity_4h` score `-5.4704` n `149` status `ready` deltaP `-4.2396` edge `-0.1497` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
