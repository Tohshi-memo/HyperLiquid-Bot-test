# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T12:52:26.292404+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10803`

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

- `market_context_high->equity_4h` score `0.8509` n `103` status `ready` deltaP `7.619` edge `0.1582` maxDD `-6.3801`
- `market_context_high->equity_1h` score `0.3568` n `105` status `ready` deltaP `9.0191` edge `0.0511` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3059` n `105` status `ready` deltaP `10.2581` edge `0.0058` maxDD `-0.5622`
- `market_context_high->metal_4h` score `0.2419` n `103` status `ready` deltaP `12.9144` edge `0.0025` maxDD `-1.273`
- `market_context_high->fx_4h` score `0.0292` n `103` status `ready` deltaP `7.1853` edge `0.0061` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.028` n `105` status `ready` deltaP `4.7348` edge `0.0048` maxDD `-0.4291`
- `market_context_high->commodity_24h` score `-0.1225` n `96` status `ready` deltaP `3.9931` edge `0.141` maxDD `-4.666`
- `market_context_high->index_4h` score `-0.1776` n `103` status `ready` deltaP `6.0621` edge `0.0182` maxDD `-1.5103`
- `market_context_high->fx_1h` score `-0.1944` n `105` status `ready` deltaP `1.075` edge `0.0038` maxDD `-0.2043`
- `market_context_high->unknown_1h` score `-0.333` n `105` status `ready` deltaP `7.4808` edge `-0.0549` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.3864` n `105` status `ready` deltaP `2.1486` edge `0.0163` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.5245` n `105` status `ready` deltaP `2.4351` edge `0.001` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7453` n `103` status `ready` deltaP `-2.7631` edge `0.0079` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8125` n `105` status `ready` deltaP `-6.7764` edge `-0.0024` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-0.9641` n `103` status `ready` deltaP `5.9022` edge `0.0073` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `-1.1793` n `96` status `ready` deltaP `17.7083` edge `-0.1657` maxDD `-1.0505`
- `market_context_high->crypto_major_4h` score `-1.2335` n `103` status `ready` deltaP `7.9801` edge `-0.0539` maxDD `-3.1677`
- `market_context_high->index_24h` score `-3.6586` n `96` status `ready` deltaP `0.3472` edge `-0.0546` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.6735` n `96` status `ready` deltaP `-20.3125` edge `-0.0124` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.8665` n `96` status `ready` deltaP `-20.3125` edge `-0.1577` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
