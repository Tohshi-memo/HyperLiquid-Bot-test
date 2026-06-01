# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T05:37:18.213405+00:00`
- Price records: `672`
- Market context records: `2533`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9312`

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

- `market_context_high->crypto_alt_4h` score `5.0918` n `160` status `ready` deltaP `23.5976` edge `0.5349` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `4.6337` n `117` status `ready` deltaP `19.4044` edge `0.2896` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.5966` n `160` status `ready` deltaP `17.0579` edge `0.367` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.6981` n `117` status `ready` deltaP `12.7137` edge `0.6181` maxDD `-23.222`
- `market_context_high->unknown_4h` score `1.9698` n `160` status `ready` deltaP `11.5091` edge `0.1924` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.21` n `160` status `ready` deltaP `9.8054` edge `0.1542` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.7167` n `160` status `ready` deltaP `8.256` edge `0.1241` maxDD `-4.2199`
- `market_context_high->equity_24h` score `0.0054` n `117` status `ready` deltaP `17.5614` edge `0.0217` maxDD `-6.3993`
- `market_context_high->crypto_alt_24h` score `-0.0021` n `117` status `ready` deltaP `0.4674` edge `0.6858` maxDD `-43.1346`
- `market_context_high->index_4h` score `-0.0541` n `160` status `ready` deltaP `6.9207` edge `0.0335` maxDD `-2.3986`
- `market_context_high->index_24h` score `-0.1332` n `117` status `ready` deltaP `2.711` edge `0.0689` maxDD `-2.5127`
- `market_context_high->commodity_1h` score `-0.3303` n `160` status `ready` deltaP `4.4536` edge `0.0158` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.3792` n `160` status `ready` deltaP `1.6355` edge `0.0069` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.3888` n `160` status `ready` deltaP `2.5524` edge `0.0196` maxDD `-2.8543`
- `market_context_high->metal_1h` score `-0.4887` n `160` status `ready` deltaP `0.7485` edge `0.0083` maxDD `-3.0759`
- `market_context_high->fx_1h` score `-0.4892` n `160` status `ready` deltaP `1.2762` edge `0.0042` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.8065` n `160` status `ready` deltaP `0.0225` edge `0.0165` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8158` n `160` status `ready` deltaP `0.8079` edge `0.0126` maxDD `-0.8774`
- `market_context_high->fx_24h` score `-0.8825` n `117` status `ready` deltaP `2.6976` edge `0.0038` maxDD `-2.4611`
- `market_context_high->metal_4h` score `-0.8965` n `160` status `ready` deltaP `3.1555` edge `0.043` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
