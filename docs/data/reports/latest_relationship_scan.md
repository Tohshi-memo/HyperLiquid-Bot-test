# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T01:07:25.048364+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `4893.6574` n `58` status `ready` deltaP `23.4853` edge `407.6903` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `14.6806` n `40` status `ready` deltaP `51.6319` edge `0.9189` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.2278` n `40` status `ready` deltaP `51.3194` edge `0.6063` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.3065` n `58` status `ready` deltaP `12.6209` edge `0.3511` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.737` n `58` status `ready` deltaP `16.7263` edge `0.0713` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.9572` n `41` status `ready` deltaP `12.6525` edge `0.123` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.7063` n `41` status `ready` deltaP `7.6219` edge `0.1303` maxDD `-4.9116`
- `news_risk_high->equity_1h` score `0.676` n `58` status `ready` deltaP `9.0027` edge `0.0786` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.6217` n `41` status `ready` deltaP `19.8171` edge `0.0272` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.365` n `47` status `ready` deltaP `7.5646` edge `0.0338` maxDD `-1.3282`
- `news_risk_high->metal_4h` score `0.1114` n `58` status `ready` deltaP `5.0673` edge `0.0156` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0453` n `58` status `ready` deltaP `4.3517` edge `0.0091` maxDD `-0.5845`
- `market_context_high->fx_1h` score `-0.0123` n `47` status `ready` deltaP `6.9658` edge `-0.0091` maxDD `-0.7804`
- `news_risk_high->crypto_alt_1h` score `-0.0151` n `58` status `ready` deltaP `7.3457` edge `0.0173` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.1332` n `58` status `ready` deltaP `1.6467` edge `0.0042` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `-0.1332` n `58` status `ready` deltaP `8.5471` edge `0.0217` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.2662` n `58` status `ready` deltaP `0.6762` edge `0.0017` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.3373` n `58` status `ready` deltaP `2.772` edge `0.0103` maxDD `-3.762`
- `news_risk_high->commodity_1h` score `-0.6962` n `58` status `ready` deltaP `3.9696` edge `-0.0167` maxDD `-2.0891`
- `market_context_high->fx_24h` score `-0.7415` n `40` status `ready` deltaP `0.6597` edge `0.0318` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
