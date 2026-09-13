# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T19:07:28.096831+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12738`

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

- `market_context_high->unknown_24h` score `17708.4108` n `56` status `ready` deltaP `10.2093` edge `1475.653` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `7811.5527` n `37` status `ready` deltaP `11.0298` edge `650.8957` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `7811.5527` n `37` status `ready` deltaP `11.0298` edge `650.8957` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `426.9411` n `82` status `ready` deltaP `-5.1008` edge `35.6546` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.6775` n `82` status `ready` deltaP `36.2027` edge `1.3639` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3724` n `82` status `ready` deltaP `38.0236` edge `1.4246` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.4211` n `82` status `ready` deltaP `27.6156` edge `0.779` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.1667` n `82` status `ready` deltaP `51.3877` edge `0.2723` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.752` n `82` status `ready` deltaP `26.3121` edge `0.266` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.631` n `37` status `ready` deltaP `39.8276` edge `0.1204` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.631` n `37` status `ready` deltaP `39.8276` edge `0.1204` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.4798` n `56` status `ready` deltaP `39.8276` edge `0.1078` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `2.5558` n `37` status `ready` deltaP `4.6273` edge `0.4304` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `2.5558` n `37` status `ready` deltaP `4.6273` edge `0.4304` maxDD `-7.0204`
- `market_context_high->crypto_alt_24h` score `2.5048` n `56` status `ready` deltaP `5.0616` edge `0.4535` maxDD `-9.6226`
- `risk_on_high->fx_24h` score `1.06` n `37` status `ready` deltaP `31.8174` edge `0.0042` maxDD `-1.767`
- `risk_on_and_context->fx_24h` score `1.06` n `37` status `ready` deltaP `31.8174` edge `0.0042` maxDD `-1.767`
- `risk_on_high->commodity_4h` score `0.634` n `59` status `ready` deltaP `12.2907` edge `0.0078` maxDD `-0.286`
- `risk_on_and_context->commodity_4h` score `0.634` n `59` status `ready` deltaP `12.2907` edge `0.0078` maxDD `-0.286`
- `market_context_high->commodity_4h` score `0.589` n `131` status `ready` deltaP `12.6012` edge `0.0113` maxDD `-0.3645`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
