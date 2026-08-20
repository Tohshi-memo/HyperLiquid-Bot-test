# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T08:07:29.739031+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10800`

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

- `market_context_high->equity_4h` score `1.773` n `96` status `ready` deltaP `9.629` edge `0.1724` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.3744` n `99` status `ready` deltaP `12.2876` edge `0.0677` maxDD `-0.807`
- `market_context_high->index_1h` score `0.6658` n `99` status `ready` deltaP `12.962` edge `0.0083` maxDD `-0.1383`
- `market_context_high->metal_4h` score `0.348` n `96` status `ready` deltaP `12.2967` edge `0.0046` maxDD `-1.273`
- `market_context_high->index_4h` score `0.0391` n `96` status `ready` deltaP `7.3424` edge `0.0198` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.0325` n `96` status `ready` deltaP `5.7292` edge `0.1493` maxDD `-4.666`
- `market_context_high->fx_4h` score `0.002` n `96` status `ready` deltaP `7.0376` edge `0.0036` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.176` n `99` status `ready` deltaP `2.2259` edge `0.0013` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.197` n `99` status `ready` deltaP `6.3011` edge `-0.0357` maxDD `-0.4843`
- `market_context_high->fx_1h` score `-0.2617` n `99` status `ready` deltaP `-0.1301` edge `0.0032` maxDD `-0.2043`
- `market_context_high->unknown_24h` score `-0.6009` n `96` status `ready` deltaP `17.7083` edge `-0.1175` maxDD `-1.0505`
- `market_context_high->crypto_alt_1h` score `-0.796` n `99` status `ready` deltaP `-0.0574` edge `-0.0215` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.8556` n `96` status `ready` deltaP `-3.6839` edge `-0.0001` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.8754` n `99` status `ready` deltaP `1.9265` edge `-0.0406` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9277` n `99` status `ready` deltaP `-8.5118` edge `-0.0056` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-2.0526` n `96` status `ready` deltaP `4.1159` edge `-0.0715` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.2529` n `96` status `ready` deltaP `6.4278` edge `-0.1285` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.3052` n `96` status `ready` deltaP `-17.0139` edge `-0.0037` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.8084` n `96` status `ready` deltaP `-0.8681` edge `-0.0657` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.4501` n `96` status `ready` deltaP `-17.0139` edge `-0.1263` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
