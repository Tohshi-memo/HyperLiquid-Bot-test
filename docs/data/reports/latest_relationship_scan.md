# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T10:07:15.559367+00:00`
- Price records: `672`
- Market context records: `1832`
- Flow alert records: `7172`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4488`

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

- `market_context_high->crypto_alt_4h` score `6.9241` n `192` status `ready` deltaP `22.7515` edge `0.5398` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.6213` n `178` status `ready` deltaP `26.2017` edge `0.6197` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.4667` n `192` status `ready` deltaP `26.3847` edge `0.4876` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.4357` n `192` status `ready` deltaP `17.0604` edge `0.4583` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.5374` n `178` status `ready` deltaP `17.8683` edge `0.2985` maxDD `-4.1604`
- `market_context_high->equity_4h` score `2.9805` n `192` status `ready` deltaP `16.654` edge `0.2468` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.7195` n `178` status `ready` deltaP `14.56` edge `0.6616` maxDD `-35.8966`
- `market_context_high->equity_24h` score `2.0197` n `178` status `ready` deltaP `15.3675` edge `0.5557` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.8302` n `192` status `ready` deltaP `12.0427` edge `0.0978` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.3882` n `196` status `ready` deltaP `5.8903` edge `0.0917` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.2522` n `196` status `ready` deltaP `6.0736` edge `0.0919` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `0.0977` n `178` status `ready` deltaP `18.8593` edge `0.741` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.0797` n `178` status `ready` deltaP `12.1294` edge `0.0174` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0867` n `196` status `ready` deltaP `4.433` edge `0.0426` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.557` n `196` status `ready` deltaP `2.7405` edge `0.0305` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.6158` n `196` status `ready` deltaP `5.2242` edge `0.0198` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.6202` n `196` status `ready` deltaP `-0.0764` edge `0.012` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.6946` n `192` status `ready` deltaP `12.3603` edge `0.1289` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.7402` n `196` status `ready` deltaP `-4.5857` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0597` n `192` status `ready` deltaP `-5.8562` edge `-0.008` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
