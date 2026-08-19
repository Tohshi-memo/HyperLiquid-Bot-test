# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T13:37:26.677245+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11762`

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

- `market_context_high->equity_4h` score `2.0545` n `96` status `ready` deltaP `11.1534` edge `0.1857` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7408` n `96` status `ready` deltaP `14.8516` edge `0.0762` maxDD `-0.4112`
- `market_context_high->crypto_major_24h` score `1.6382` n `96` status `ready` deltaP `4.8611` edge `0.2249` maxDD `-4.9964`
- `market_context_high->metal_4h` score `1.1164` n `96` status `ready` deltaP `17.3272` edge `0.0351` maxDD `-1.273`
- `market_context_high->index_1h` score `0.951` n `96` status `ready` deltaP `16.2113` edge `0.0099` maxDD `-0.0982`
- `market_context_high->commodity_24h` score `0.6919` n `96` status `ready` deltaP `10.0694` edge `0.2049` maxDD `-4.666`
- `market_context_high->crypto_major_4h` score `0.6888` n `96` status `ready` deltaP `9.629` edge `0.0953` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `0.3264` n `96` status `ready` deltaP `18.2291` edge `-0.0437` maxDD `-1.0505`
- `market_context_high->unknown_1h` score `0.1785` n `96` status `ready` deltaP `8.009` edge `-0.0158` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.1515` n `96` status `ready` deltaP `9.4766` edge `0.0065` maxDD `-0.3539`
- `market_context_high->index_4h` score `0.1324` n `96` status `ready` deltaP `8.1046` edge `0.0225` maxDD `-0.5728`
- `market_context_high->metal_1h` score `0.0877` n `96` status `ready` deltaP `5.5202` edge `0.0092` maxDD `-0.4291`
- `market_context_high->crypto_alt_4h` score `-0.1409` n `96` status `ready` deltaP `7.9268` edge `0.0624` maxDD `-5.4926`
- `market_context_high->fx_1h` score `-0.3183` n `96` status `ready` deltaP `-1.1727` edge `0.0029` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4336` n `96` status `ready` deltaP `2.6821` edge `0.011` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.4782` n `96` status `ready` deltaP `1.4783` edge `0.009` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.6128` n `96` status `ready` deltaP `0.2795` edge `0.0046` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8978` n `96` status `ready` deltaP `-7.7408` edge `-0.0069` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2821` n `96` status `ready` deltaP `-4.1667` edge `0.066` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.8343` n `96` status `ready` deltaP `-21.5277` edge `-0.0177` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
