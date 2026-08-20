# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T12:37:29.686446+00:00`
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

- `market_context_high->equity_4h` score `0.7979` n `103` status `ready` deltaP `7.4666` edge `0.1548` maxDD `-6.3801`
- `market_context_high->equity_1h` score `0.3376` n `105` status `ready` deltaP `8.8694` edge `0.0505` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.2927` n `105` status `ready` deltaP `10.1084` edge `0.0057` maxDD `-0.5622`
- `market_context_high->metal_4h` score `0.2443` n `103` status `ready` deltaP `12.9144` edge `0.0028` maxDD `-1.273`
- `market_context_high->fx_4h` score `0.0379` n `103` status `ready` deltaP `7.3378` edge `0.0062` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.0136` n `105` status `ready` deltaP `4.8845` edge `0.005` maxDD `-0.4291`
- `market_context_high->commodity_24h` score `-0.1103` n `96` status `ready` deltaP `4.1667` edge `0.1414` maxDD `-4.666`
- `market_context_high->index_4h` score `-0.1902` n `103` status `ready` deltaP `5.9096` edge `0.0176` maxDD `-1.5103`
- `market_context_high->fx_1h` score `-0.2022` n `105` status `ready` deltaP `0.9253` edge `0.0038` maxDD `-0.2043`
- `market_context_high->unknown_1h` score `-0.3474` n `105` status `ready` deltaP `7.3311` edge `-0.0551` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.3965` n `105` status `ready` deltaP `1.9989` edge `0.016` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.5362` n `105` status `ready` deltaP `2.2854` edge `0.0005` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7461` n `103` status `ready` deltaP `-2.7631` edge `0.0078` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8117` n `105` status `ready` deltaP `-6.7764` edge `-0.0023` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-0.9387` n `103` status `ready` deltaP `6.0546` edge `0.0084` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `-1.1445` n `96` status `ready` deltaP `17.7083` edge `-0.1628` maxDD `-1.0505`
- `market_context_high->crypto_major_4h` score `-1.2287` n `103` status `ready` deltaP `7.9801` edge `-0.0535` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.6536` n `96` status `ready` deltaP `-20.1389` edge `-0.0119` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.6754` n `96` status `ready` deltaP `0.1736` edge `-0.0556` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.8497` n `96` status `ready` deltaP `-20.1389` edge `-0.1567` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
