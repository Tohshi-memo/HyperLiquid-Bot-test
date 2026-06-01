# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T06:37:17.226128+00:00`
- Price records: `672`
- Market context records: `2537`
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

- `market_context_high->crypto_alt_4h` score `5.1198` n `158` status `ready` deltaP `23.7226` edge `0.5364` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `4.6638` n `116` status `ready` deltaP `19.3307` edge `0.2926` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.5961` n `158` status `ready` deltaP `17.1117` edge `0.3666` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `3.0056` n `116` status `ready` deltaP `13.2663` edge `0.6296` maxDD `-21.6171`
- `market_context_high->unknown_4h` score `1.9255` n `158` status `ready` deltaP `11.2998` edge `0.1901` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1707` n `158` status `ready` deltaP `9.7798` edge `0.1511` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6834` n `158` status `ready` deltaP `8.3643` edge `0.1206` maxDD `-4.2199`
- `market_context_high->equity_24h` score `0.4239` n `116` status `ready` deltaP `18.4806` edge `0.032` maxDD `-5.5904`
- `market_context_high->crypto_alt_24h` score `0.0306` n `116` status `ready` deltaP `0.5328` edge `0.6842` maxDD `-42.7063`
- `market_context_high->index_24h` score `-0.0574` n `116` status `ready` deltaP `3.1489` edge `0.0723` maxDD `-2.5127`
- `market_context_high->index_4h` score `-0.1076` n `158` status `ready` deltaP `6.4777` edge `0.032` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.2959` n `158` status `ready` deltaP `3.0831` edge `0.0238` maxDD `-2.8543`
- `market_context_high->index_1h` score `-0.3315` n `158` status `ready` deltaP `2.0219` edge `0.0083` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.348` n `158` status `ready` deltaP `4.2333` edge `0.015` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4163` n `158` status `ready` deltaP `2.0825` edge `0.0049` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.517` n `158` status `ready` deltaP `0.415` edge `0.0069` maxDD `-3.0759`
- `market_context_high->fx_4h` score `-0.8121` n `158` status `ready` deltaP `0.8085` edge `0.0129` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.823` n `158` status `ready` deltaP `-0.1686` edge `0.0164` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8567` n `116` status `ready` deltaP `3.125` edge `0.0039` maxDD `-2.432`
- `market_context_high->metal_4h` score `-0.9405` n `158` status `ready` deltaP `2.6513` edge `0.0427` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
