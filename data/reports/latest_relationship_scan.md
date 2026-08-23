# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T13:52:29.428920+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_4h` score `14.1921` n `51` status `ready` deltaP `25.6307` edge `1.0164` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `4.823` n `33` status `ready` deltaP `-9.0773` edge `0.7237` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `4.823` n `33` status `ready` deltaP `-9.0773` edge `0.7237` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.4577` n `51` status `ready` deltaP `18.7301` edge `0.1937` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `2.9303` n `51` status `ready` deltaP `34.7292` edge `0.0261` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.7187` n `51` status `ready` deltaP `23.2694` edge `0.1487` maxDD `-2.1818`
- `risk_on_high->metal_4h` score `2.2888` n `33` status `ready` deltaP `30.4093` edge `-0.0032` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.2888` n `33` status `ready` deltaP `30.4093` edge `-0.0032` maxDD `-0.0367`
- `risk_on_high->equity_4h` score `1.6043` n `33` status `ready` deltaP `-1.686` edge `0.26` maxDD `-0.7794`
- `risk_on_and_context->equity_4h` score `1.6043` n `33` status `ready` deltaP `-1.686` edge `0.26` maxDD `-0.7794`
- `market_context_high->crypto_alt_4h` score `1.3217` n `128` status `ready` deltaP `9.4131` edge `0.1942` maxDD `-7.0785`
- `market_context_high->unknown_1h` score `1.1886` n `128` status `ready` deltaP `6.6897` edge `0.0993` maxDD `-1.5876`
- `news_risk_high->fx_1h` score `1.1631` n `51` status `ready` deltaP `16.0972` edge `0.0066` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `0.7477` n `128` status `ready` deltaP `21.3415` edge `-0.0628` maxDD `-0.3736`
- `news_risk_high->equity_1h` score `0.7099` n `51` status `ready` deltaP `16.0972` edge `0.0202` maxDD `-0.9204`
- `risk_on_high->fx_4h` score `0.6913` n `33` status `ready` deltaP `16.1909` edge `0.0039` maxDD `-0.1905`
- `risk_on_and_context->fx_4h` score `0.6913` n `33` status `ready` deltaP `16.1909` edge `0.0039` maxDD `-0.1905`
- `market_context_high->commodity_24h` score `0.5641` n `112` status `ready` deltaP `-0.9921` edge `0.1011` maxDD `-0.7984`
- `news_risk_high->index_4h` score `0.5484` n `51` status `ready` deltaP `9.8906` edge `0.0195` maxDD `-0.1788`
- `risk_on_high->index_4h` score `0.4075` n `33` status `ready` deltaP `8.6429` edge `0.0426` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
