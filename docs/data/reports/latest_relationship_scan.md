# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T16:22:36.221217+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8829`

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

- `market_context_high->equity_4h` score `2.3259` n `96` status `ready` deltaP `12.2205` edge `0.2012` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.8548` n `96` status `ready` deltaP `15.3007` edge `0.0827` maxDD `-0.4112`
- `market_context_high->crypto_major_24h` score `1.0591` n `96` status `ready` deltaP `4.6875` edge `0.1778` maxDD `-4.9964`
- `market_context_high->index_1h` score `0.9091` n `96` status `ready` deltaP `15.6125` edge `0.0104` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.8023` n `96` status `ready` deltaP `15.6504` edge `0.0201` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.4709` n `96` status `ready` deltaP `8.1597` edge `0.1893` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.3504` n `96` status `ready` deltaP `18.2291` edge `-0.0417` maxDD `-1.0505`
- `market_context_high->index_4h` score `0.1312` n `96` status `ready` deltaP `8.1046` edge `0.0224` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.0905` n `96` status `ready` deltaP `8.4095` edge `0.0058` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `0.085` n `96` status `ready` deltaP `7.2605` edge `-0.0186` maxDD `-0.4843`
- `market_context_high->crypto_major_4h` score `0.0552` n `96` status `ready` deltaP `8.7144` edge `0.0486` maxDD `-3.1677`
- `market_context_high->metal_1h` score `-0.0549` n `96` status `ready` deltaP `4.1729` edge `0.0063` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3525` n `96` status `ready` deltaP `-1.7715` edge `0.0025` maxDD `-0.2043`
- `market_context_high->crypto_alt_4h` score `-0.6191` n `96` status `ready` deltaP `6.5549` edge `0.0317` maxDD `-5.4926`
- `market_context_high->commodity_4h` score `-0.6436` n `96` status `ready` deltaP `-0.1778` edge `0.0037` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.6591` n `96` status `ready` deltaP `0.5801` edge `-0.0082` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.6676` n `96` status `ready` deltaP `2.0833` edge `-0.015` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9087` n `96` status `ready` deltaP `-7.8905` edge `-0.0073` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.5506` n `96` status `ready` deltaP `-6.0764` edge `0.0443` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.6903` n `96` status `ready` deltaP `-20.3125` edge `-0.0138` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
