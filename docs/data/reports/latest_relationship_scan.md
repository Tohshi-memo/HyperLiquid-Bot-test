# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T05:52:30.717854+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6754`

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

- `market_context_high->unknown_1h` score `324.6052` n `50` status `ready` deltaP `6.8323` edge `27.0098` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.9936` n `50` status `ready` deltaP `6.8598` edge `23.3704` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.2777` n `129` status `ready` deltaP `29.1788` edge `1.4329` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.8257` n `50` status `ready` deltaP `18.4573` edge `0.5161` maxDD `-3.294`
- `market_context_high->crypto_major_24h` score `6.6587` n `32` status `ready` deltaP `26.0417` edge `0.5229` maxDD `-9.3299`
- `news_risk_high->crypto_major_24h` score `6.4511` n `129` status `ready` deltaP `23.1105` edge `0.6989` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.1669` n `129` status `ready` deltaP `23.8049` edge `0.5901` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.7229` n `50` status `ready` deltaP `13.75` edge `0.3479` maxDD `-7.6792`
- `news_risk_high->equity_4h` score `3.5898` n `129` status `ready` deltaP `25.8946` edge `0.1946` maxDD `-2.78`
- `market_context_high->crypto_major_1h` score `2.9291` n `50` status `ready` deltaP `14.7485` edge `0.1908` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8693` n `50` status `ready` deltaP `32.3841` edge `0.0367` maxDD `-0.0791`
- `market_context_high->crypto_alt_24h` score `2.6852` n `32` status `ready` deltaP `8.8542` edge `0.3357` maxDD `-11.6768`
- `news_risk_high->index_24h` score `2.6477` n `129` status `ready` deltaP `25.1332` edge `0.1009` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.6267` n `50` status `ready` deltaP `12.8563` edge `0.1995` maxDD `-3.6387`
- `news_risk_high->crypto_alt_4h` score `2.0026` n `129` status `ready` deltaP `10.4167` edge `0.2981` maxDD `-10.7193`
- `news_risk_high->metal_24h` score `2.0008` n `129` status `ready` deltaP `23.5667` edge `0.2268` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4304` n `50` status `ready` deltaP `20.1916` edge `0.011` maxDD `-0.113`
- `market_context_high->equity_24h` score `0.9553` n `32` status `ready` deltaP `1.7361` edge `0.2971` maxDD `-11.8957`
- `news_risk_high->equity_1h` score `0.7744` n `129` status `ready` deltaP `7.3481` edge `0.0692` maxDD `-0.9592`
- `news_risk_high->crypto_alt_1h` score `0.609` n `129` status `ready` deltaP `7.3214` edge `0.093` maxDD `-4.2849`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
