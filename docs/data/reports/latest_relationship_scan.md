# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T17:37:22.700911+00:00`
- Price records: `672`
- Market context records: `2582`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `market_context_high->unknown_24h` score `6.5625` n `125` status `ready` deltaP `18.7056` edge `0.455` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.1649` n `146` status `ready` deltaP `26.7207` edge `0.6035` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.369` n `146` status `ready` deltaP `18.1173` edge `0.4243` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.4492` n `146` status `ready` deltaP `11.73` edge `0.1613` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.2234` n `146` status `ready` deltaP `9.5139` edge `0.1435` maxDD `-3.7312`
- `market_context_high->crypto_major_24h` score `1.0633` n `125` status `ready` deltaP `8.7847` edge `0.4926` maxDD `-27.6709`
- `market_context_high->crypto_major_1h` score `0.9654` n `146` status `ready` deltaP `10.3601` edge `0.1308` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.8175` n `125` status `ready` deltaP `2.1667` edge `0.7282` maxDD `-39.0265`
- `market_context_high->index_24h` score `0.7101` n `125` status `ready` deltaP `7.6722` edge `0.1061` maxDD `-2.5127`
- `market_context_high->equity_24h` score `0.6246` n `125` status `ready` deltaP `17.725` edge `0.0009` maxDD `-2.3615`
- `market_context_high->index_4h` score `0.3448` n `146` status `ready` deltaP `9.4325` edge `0.05` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1671` n `146` status `ready` deltaP `3.642` edge `0.0112` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4176` n `146` status `ready` deltaP `1.8005` edge `0.0195` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4362` n `146` status `ready` deltaP `5.2026` edge `0.0168` maxDD `-4.3601`
- `market_context_high->metal_4h` score `-0.4904` n `146` status `ready` deltaP `5.1119` edge `0.0638` maxDD `-4.7664`
- `market_context_high->metal_1h` score `-0.6368` n `146` status `ready` deltaP `0.9618` edge `0.0153` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.6629` n `146` status `ready` deltaP `-0.8346` edge `0.0038` maxDD `-0.278`
- `market_context_high->fx_4h` score `-0.8646` n `146` status `ready` deltaP `0.0793` edge `0.0132` maxDD `-0.8621`
- `market_context_high->equity_1h` score `-0.8648` n `146` status `ready` deltaP `-0.6767` edge `0.0163` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-1.036` n `125` status `ready` deltaP `1.7889` edge `0.0011` maxDD `-1.6157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
