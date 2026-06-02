# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T07:22:20.393236+00:00`
- Price records: `672`
- Market context records: `2641`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.5768` n `136` status `ready` deltaP `17.9432` edge `0.5446` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.2345` n `136` status `ready` deltaP `25.0358` edge `0.5372` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.6508` n `136` status `ready` deltaP `14.8852` edge `0.386` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `3.456` n `136` status `ready` deltaP `6.536` edge `0.7495` maxDD `-31.7395`
- `market_context_high->index_24h` score `1.2076` n `136` status `ready` deltaP `11.5809` edge `0.1215` maxDD `-2.5127`
- `market_context_high->crypto_alt_1h` score `1.0848` n `136` status `ready` deltaP `9.845` edge `0.1435` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.0036` n `136` status `ready` deltaP `6.2858` edge `0.1467` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.5522` n `136` status `ready` deltaP `7.0403` edge `0.1185` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.5174` n `136` status `ready` deltaP `11.1998` edge `0.0526` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0433` n `136` status `ready` deltaP `3.6236` edge `0.0336` maxDD `-1.665`
- `market_context_high->index_1h` score `-0.2176` n `136` status `ready` deltaP `3.0248` edge `0.0111` maxDD `-1.2855`
- `market_context_high->metal_4h` score `-0.3178` n `136` status `ready` deltaP `4.1159` edge `0.0277` maxDD `-2.5301`
- `market_context_high->commodity_1h` score `-0.3891` n `136` status `ready` deltaP `5.4465` edge `0.0191` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.4285` n `136` status `ready` deltaP `0.4491` edge `0.006` maxDD `-2.114`
- `market_context_high->fx_1h` score `-0.4848` n `136` status `ready` deltaP `0.1101` edge `0.0035` maxDD `-0.2373`
- `market_context_high->fx_24h` score `-0.752` n `136` status `ready` deltaP `4.2994` edge `-0.0012` maxDD `-0.8768`
- `market_context_high->fx_4h` score `-0.9084` n `136` status `ready` deltaP `-0.5111` edge `0.0108` maxDD `-0.6474`
- `market_context_high->equity_1h` score `-0.9707` n `136` status `ready` deltaP `-1.8052` edge `0.015` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-1.0575` n `136` status `ready` deltaP `4.4835` edge `0.0288` maxDD `-10.2078`
- `market_context_high->equity_4h` score `-1.2674` n `136` status `ready` deltaP `2.7797` edge `0.0163` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
