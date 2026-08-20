# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T10:37:36.581772+00:00`
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

- `market_context_high->equity_4h` score `1.9059` n `97` status `ready` deltaP `10.1505` edge `0.18` maxDD `-2.4411`
- `market_context_high->equity_1h` score `0.5966` n `103` status `ready` deltaP `9.6593` edge `0.0503` maxDD `-2.5318`
- `market_context_high->metal_4h` score `0.4658` n `97` status `ready` deltaP `13.4241` edge `0.0069` maxDD `-1.273`
- `market_context_high->index_1h` score `0.3984` n `103` status `ready` deltaP `10.7116` edge `0.0052` maxDD `-0.4726`
- `market_context_high->index_4h` score `0.12` n `97` status `ready` deltaP `8.2332` edge `0.0215` maxDD `-0.6441`
- `market_context_high->commodity_24h` score `-0.0097` n `96` status `ready` deltaP `5.3819` edge `0.1462` maxDD `-4.666`
- `market_context_high->fx_4h` score `-0.0548` n `97` status `ready` deltaP `5.975` edge `0.0034` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.129` n `103` status `ready` deltaP `3.6975` edge `0.0033` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.1891` n `103` status `ready` deltaP `1.1613` edge `0.0039` maxDD `-0.2043`
- `market_context_high->unknown_1h` score `-0.3167` n `103` status `ready` deltaP `6.9647` edge `-0.0501` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.4283` n `103` status `ready` deltaP `1.4476` edge `0.0156` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.4628` n `103` status `ready` deltaP `3.1713` edge `0.004` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8345` n `103` status `ready` deltaP `-7.2132` edge `-0.0023` maxDD `-1.1941`
- `market_context_high->unknown_24h` score `-0.8769` n `96` status `ready` deltaP `17.7083` edge `-0.1405` maxDD `-1.0505`
- `market_context_high->commodity_4h` score `-0.9439` n `97` status `ready` deltaP `-4.768` edge `-0.0042` maxDD `-2.4692`
- `market_context_high->crypto_alt_4h` score `-2.1699` n `97` status `ready` deltaP `4.0451` edge `-0.0808` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.5259` n `97` status `ready` deltaP `5.9106` edge `-0.1478` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.4957` n `96` status `ready` deltaP `-18.75` edge `-0.008` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.7536` n `96` status `ready` deltaP `-0.5209` edge `-0.061` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.6792` n `96` status `ready` deltaP `-18.75` edge `-0.1441` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
