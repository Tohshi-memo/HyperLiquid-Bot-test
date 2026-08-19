# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T17:46:03.476231+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9828`

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

- `market_context_high->equity_4h` score `2.3859` n `96` status `ready` deltaP `12.2205` edge `0.2062` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.9411` n `96` status `ready` deltaP `15.7498` edge `0.0869` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9762` n `96` status `ready` deltaP `16.361` edge `0.011` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.6787` n `96` status `ready` deltaP `14.7357` edge `0.0159` maxDD `-1.273`
- `market_context_high->crypto_major_24h` score `0.3897` n `96` status `ready` deltaP `3.8194` edge `0.1278` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `0.3645` n `96` status `ready` deltaP `7.1181` edge `0.1826` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.3132` n `96` status `ready` deltaP `18.2291` edge `-0.0448` maxDD `-1.0505`
- `market_context_high->index_4h` score `0.2078` n `96` status `ready` deltaP `8.8668` edge `0.0237` maxDD `-0.5728`
- `market_context_high->unknown_1h` score `0.1449` n `96` status `ready` deltaP `7.7096` edge `-0.0166` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.0708` n `96` status `ready` deltaP `8.1046` edge `0.0053` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.0597` n `96` status `ready` deltaP `4.1729` edge `0.0059` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3198` n `96` status `ready` deltaP `-1.1727` edge `0.0027` maxDD `-0.2043`
- `market_context_high->crypto_major_4h` score `-0.4668` n `96` status `ready` deltaP `7.7998` edge `0.0112` maxDD `-3.1677`
- `market_context_high->crypto_major_1h` score `-0.62` n `96` status `ready` deltaP `2.5324` edge `-0.0119` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.631` n `96` status `ready` deltaP `0.8795` edge `-0.0066` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.6957` n `96` status `ready` deltaP `-0.94` edge `0.0021` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.9001` n `96` status `ready` deltaP `-7.7408` edge `-0.0072` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-0.9779` n `96` status `ready` deltaP `5.6402` edge `0.0079` maxDD `-5.4926`
- `market_context_high->metal_24h` score `-2.707` n `96` status `ready` deltaP `-7.1181` edge `0.0312` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.6258` n `96` status `ready` deltaP `-19.7916` edge `-0.0119` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
