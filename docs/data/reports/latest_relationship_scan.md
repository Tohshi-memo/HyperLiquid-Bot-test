# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T00:37:36.227017+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5062`

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

- `market_context_high->unknown_4h` score `29.8989` n `113` status `ready` deltaP `-0.7487` edge `2.5301` maxDD `-1.016`
- `market_context_high->crypto_major_24h` score `0.0888` n `89` status `ready` deltaP `5.302` edge `0.0746` maxDD `-4.5369`
- `market_context_high->fx_1h` score `-0.0918` n `113` status `ready` deltaP `3.1106` edge `0.0024` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.1132` n `113` status `ready` deltaP `6.3917` edge `0.0078` maxDD `-0.4545`
- `market_context_high->fx_24h` score `-0.1305` n `89` status `ready` deltaP `17.4743` edge `0.024` maxDD `-1.2451`
- `market_context_high->metal_24h` score `-0.3426` n `89` status `ready` deltaP `15.7966` edge `0.1178` maxDD `-7.3625`
- `market_context_high->commodity_1h` score `-0.4175` n `113` status `ready` deltaP `0.5657` edge `0.0115` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6287` n `113` status `ready` deltaP `4.7838` edge `-0.0051` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6339` n `113` status `ready` deltaP `-1.5871` edge `-0.0055` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.6858` n `113` status `ready` deltaP `-0.4088` edge `0.0377` maxDD `-1.165`
- `market_context_high->index_24h` score `-0.772` n `89` status `ready` deltaP `11.7685` edge `-0.0492` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.2569` n `113` status `ready` deltaP `3.9955` edge `-0.0297` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.0034` n `113` status `ready` deltaP `3.699` edge `-0.0206` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1522` n `113` status `ready` deltaP `-7.7676` edge `-0.0367` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1104` n `113` status `ready` deltaP `-1.1115` edge `-0.0644` maxDD `-11.3243`
- `market_context_high->commodity_24h` score `-3.2122` n `89` status `ready` deltaP `-10.1631` edge `-0.0629` maxDD `-9.8267`
- `market_context_high->equity_1h` score `-3.8236` n `113` status `ready` deltaP `-0.2398` edge `-0.0897` maxDD `-12.1865`
- `market_context_high->equity_24h` score `-7.2798` n `89` status `ready` deltaP `1.584` edge `-0.4155` maxDD `-36.6024`
- `market_context_high->crypto_alt_24h` score `-7.8349` n `89` status `ready` deltaP `-5.9145` edge `-0.2797` maxDD `-45.4946`
- `market_context_high->crypto_major_4h` score `-9.9476` n `113` status `ready` deltaP `-12.7428` edge `-0.2442` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
