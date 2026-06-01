# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T21:22:22.294061+00:00`
- Price records: `672`
- Market context records: `2598`
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

- `market_context_high->unknown_24h` score `7.7237` n `135` status `ready` deltaP `17.9051` edge `0.5571` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.4527` n `146` status `ready` deltaP `25.3488` edge `0.5533` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.73` n `146` status `ready` deltaP `15.8307` edge `0.3863` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `1.5028` n `135` status `ready` deltaP `3.4144` edge `0.7403` maxDD `-39.0265`
- `market_context_high->crypto_alt_1h` score `1.4252` n `146` status `ready` deltaP `11.5803` edge `0.1603` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.9408` n `135` status `ready` deltaP `9.3865` edge `0.1139` maxDD `-2.5127`
- `market_context_high->unknown_4h` score `0.8851` n `146` status `ready` deltaP `7.6846` edge `0.1275` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.8204` n `146` status `ready` deltaP `9.3122` edge `0.1257` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.194` n `146` status `ready` deltaP `8.8227` edge `0.0415` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1144` n `146` status `ready` deltaP `4.2408` edge `0.0116` maxDD `-1.2855`
- `market_context_high->equity_24h` score `-0.2003` n `135` status `ready` deltaP `14.8842` edge `-0.0489` maxDD `-2.3615`
- `market_context_high->unknown_1h` score `-0.3217` n `146` status `ready` deltaP `2.3993` edge `0.0235` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4422` n `146` status `ready` deltaP `5.2026` edge `0.0163` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.5841` n `146` status `ready` deltaP `1.5606` edge `0.0157` maxDD `-2.9823`
- `market_context_high->metal_4h` score `-0.651` n `146` status `ready` deltaP `4.3497` edge `0.0555` maxDD `-4.7664`
- `market_context_high->fx_1h` score `-0.6641` n `146` status `ready` deltaP `-0.8346` edge `0.0037` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.7881` n `146` status `ready` deltaP `-0.0779` edge `0.0187` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.9144` n `146` status `ready` deltaP `-0.378` edge `0.0121` maxDD `-0.8621`
- `market_context_high->fx_24h` score `-0.9697` n `135` status `ready` deltaP `2.8588` edge `-0.0005` maxDD `-1.6157`
- `market_context_high->commodity_4h` score `-1.1441` n `146` status `ready` deltaP `2.5768` edge `0.0304` maxDD `-10.2078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
