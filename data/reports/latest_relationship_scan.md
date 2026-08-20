# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T05:37:24.093790+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10829`

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

- `market_context_high->equity_4h` score `1.8901` n `96` status `ready` deltaP `10.2388` edge `0.1781` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.8236` n `96` status `ready` deltaP `15.151` edge `0.0811` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9186` n `96` status `ready` deltaP `15.7622` edge `0.0102` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.3102` n `96` status `ready` deltaP `11.8394` edge `0.0045` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.1022` n `96` status `ready` deltaP `6.4236` edge `0.1536` maxDD `-4.666`
- `market_context_high->index_4h` score `0.0805` n `96` status `ready` deltaP `7.7998` edge `0.0202` maxDD `-0.5728`
- `market_context_high->unknown_1h` score `0.0168` n `96` status `ready` deltaP `5.9132` edge `-0.0153` maxDD `-0.4843`
- `market_context_high->fx_4h` score `-0.0011` n `96` status `ready` deltaP `7.0376` edge `0.0032` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.1388` n `96` status `ready` deltaP `3.4244` edge `0.0043` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3743` n `96` status `ready` deltaP `-2.0709` edge `0.0017` maxDD `-0.2043`
- `market_context_high->unknown_24h` score `-0.3957` n `96` status `ready` deltaP `17.7083` edge `-0.1004` maxDD `-1.0505`
- `market_context_high->commodity_4h` score `-0.7421` n `96` status `ready` deltaP `-2.312` edge `0.0053` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.7986` n `96` status `ready` deltaP `0.131` edge `-0.0231` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.8626` n `96` status `ready` deltaP `1.9336` edge `-0.039` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9055` n `96` status `ready` deltaP `-8.0402` edge `-0.0059` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.9296` n `96` status `ready` deltaP `4.5732` edge `-0.0643` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.9562` n `96` status `ready` deltaP `7.6473` edge `-0.1119` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.1737` n `96` status `ready` deltaP `-15.625` edge `-0.002` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.8084` n `96` status `ready` deltaP `-0.8681` edge `-0.0657` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.1749` n `96` status `ready` deltaP `-15.2778` edge `-0.1026` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
