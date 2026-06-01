# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T06:07:20.167282+00:00`
- Price records: `672`
- Market context records: `2535`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9252`

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

- `market_context_high->crypto_alt_4h` score `5.1436` n `160` status `ready` deltaP `23.75` edge `0.5382` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `4.5749` n `117` status `ready` deltaP `19.4044` edge `0.2847` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.634` n `160` status `ready` deltaP `17.2104` edge `0.3691` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.6997` n `117` status `ready` deltaP `12.7137` edge `0.6183` maxDD `-23.222`
- `market_context_high->unknown_4h` score `2.011` n `160` status `ready` deltaP `11.814` edge `0.1938` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.2376` n `160` status `ready` deltaP `9.9551` edge `0.1555` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.7538` n `160` status `ready` deltaP `8.5554` edge `0.1252` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `-0.0326` n `117` status `ready` deltaP `0.1201` edge `0.6842` maxDD `-43.1346`
- `market_context_high->index_4h` score `-0.0517` n `160` status `ready` deltaP `6.9207` edge `0.0337` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.0596` n `117` status `ready` deltaP `17.2142` edge `0.0186` maxDD `-6.3993`
- `market_context_high->index_24h` score `-0.1464` n `117` status `ready` deltaP `2.711` edge `0.0678` maxDD `-2.5127`
- `market_context_high->index_1h` score `-0.336` n `160` status `ready` deltaP `1.9349` edge `0.0085` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.342` n `160` status `ready` deltaP `4.3039` edge `0.0153` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.3624` n `160` status `ready` deltaP `2.7021` edge `0.0208` maxDD `-2.8543`
- `market_context_high->fx_1h` score `-0.4748` n `160` status `ready` deltaP `1.4259` edge `0.0044` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.4919` n `160` status `ready` deltaP `0.7485` edge `0.0079` maxDD `-3.0759`
- `market_context_high->fx_4h` score `-0.7866` n `160` status `ready` deltaP `1.1128` edge `0.013` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.8041` n `160` status `ready` deltaP `0.0225` edge `0.0167` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8818` n `117` status `ready` deltaP `2.6976` edge `0.0039` maxDD `-2.4611`
- `market_context_high->metal_4h` score `-0.9135` n `160` status `ready` deltaP `3.003` edge `0.0426` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
