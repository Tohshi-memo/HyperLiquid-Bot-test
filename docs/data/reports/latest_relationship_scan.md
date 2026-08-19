# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T08:37:32.032013+00:00`
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

- `market_context_high->crypto_major_24h` score `2.2325` n `96` status `ready` deltaP `7.6389` edge `0.2559` maxDD `-4.9964`
- `market_context_high->equity_4h` score `1.7881` n `96` status `ready` deltaP `10.2388` edge `0.1696` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.6054` n `96` status `ready` deltaP `13.8037` edge `0.0719` maxDD `-0.4112`
- `market_context_high->metal_4h` score `1.3856` n `96` status `ready` deltaP `19.4613` edge `0.0433` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `1.1273` n `96` status `ready` deltaP `11.9156` edge `0.1166` maxDD `-3.1677`
- `market_context_high->commodity_24h` score `1.0776` n `96` status `ready` deltaP `13.5417` edge `0.2312` maxDD `-4.666`
- `market_context_high->index_1h` score `0.8863` n `96` status `ready` deltaP `15.4628` edge `0.0095` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.2073` n `96` status `ready` deltaP `8.1587` edge `-0.0144` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.1832` n `96` status `ready` deltaP `9.9085` edge `0.0762` maxDD `-5.4926`
- `market_context_high->metal_1h` score `0.1548` n `96` status `ready` deltaP `5.9693` edge `0.0118` maxDD `-0.4291`
- `market_context_high->index_4h` score `0.0971` n `96` status `ready` deltaP `7.6473` edge `0.0226` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.0684` n `96` status `ready` deltaP `8.1046` edge `0.005` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `-0.127` n `96` status `ready` deltaP `15.2777` edge `-0.0618` maxDD `-1.0505`
- `market_context_high->fx_1h` score `-0.3276` n `96` status `ready` deltaP `-1.3224` edge `0.0027` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4009` n `96` status `ready` deltaP `2.6821` edge `0.0152` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.4735` n `96` status `ready` deltaP `1.4783` edge `0.0096` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.5268` n `96` status `ready` deltaP `1.499` edge `0.0075` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8713` n `96` status `ready` deltaP `-7.4414` edge `-0.0055` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.1973` n `96` status `ready` deltaP `-3.6458` edge `0.0734` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-4.1966` n `96` status `ready` deltaP `-24.8264` edge `-0.0259` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
