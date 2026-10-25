# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T20:22:26.332957+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5098`

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

- `market_context_high->unknown_4h` score `29.8053` n `113` status `ready` deltaP `-0.7487` edge `2.5223` maxDD `-1.016`
- `market_context_high->crypto_major_24h` score `0.1413` n `72` status `ready` deltaP `1.5625` edge `0.1039` maxDD `-4.5369`
- `market_context_high->fx_4h` score `-0.0317` n `113` status `ready` deltaP `7.3063` edge `0.0085` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0661` n `113` status `ready` deltaP `3.5597` edge `0.0027` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.4799` n `113` status `ready` deltaP `0.1166` edge `0.0093` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6287` n `113` status `ready` deltaP `4.7838` edge `-0.0051` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.7095` n `113` status `ready` deltaP `-2.9344` edge `-0.0062` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.8087` n `113` status `ready` deltaP `-1.9332` edge `0.0321` maxDD `-1.165`
- `market_context_high->fx_24h` score `-0.9609` n `72` status `ready` deltaP `9.5487` edge `0.0135` maxDD `-1.2451`
- `market_context_high->commodity_24h` score `-0.9928` n `72` status `ready` deltaP `-0.3472` edge `0.0076` maxDD `-3.6055`
- `market_context_high->crypto_major_1h` score `-1.3574` n `113` status `ready` deltaP `2.9476` edge `-0.0356` maxDD `-9.3126`
- `market_context_high->index_24h` score `-1.4687` n `72` status `ready` deltaP `4.3403` edge `-0.089` maxDD `-4.925`
- `market_context_high->metal_24h` score `-1.4817` n `72` status `ready` deltaP `1.7361` edge `0.0655` maxDD `-7.3625`
- `market_context_high->metal_4h` score `-2.0072` n `113` status `ready` deltaP `3.5466` edge `-0.0199` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.2068` n `113` status `ready` deltaP `-8.6822` edge `-0.0376` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.2422` n `113` status `ready` deltaP `-1.86` edge `-0.0704` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.9841` n `113` status `ready` deltaP `-1.5871` edge `-0.0941` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-6.4146` n `72` status `ready` deltaP `1.3889` edge `-0.186` maxDD `-42.3182`
- `market_context_high->equity_24h` score `-9.5101` n `72` status `ready` deltaP `-9.0278` edge `-0.6307` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.3367` n `113` status `ready` deltaP `-14.8769` edge `-0.2624` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
