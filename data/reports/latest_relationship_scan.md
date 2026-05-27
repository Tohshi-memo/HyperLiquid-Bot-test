# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T03:52:19.080044+00:00`
- Price records: `672`
- Market context records: `2005`
- Flow alert records: `7664`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9107`

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

- `market_context_high->crypto_major_4h` score `8.7817` n `214` status `ready` deltaP `30.391` edge `0.5822` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.2113` n `214` status `ready` deltaP `24.2464` edge `0.6371` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.5705` n `214` status `ready` deltaP `18.6787` edge `0.4146` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.6902` n `214` status `ready` deltaP `15.7696` edge `0.2285` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.6555` n `185` status `ready` deltaP `15.6599` edge `0.5656` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `1.4173` n `214` status `ready` deltaP `11.8683` edge `0.1376` maxDD `-3.2225`
- `market_context_high->metal_24h` score `1.1206` n `185` status `ready` deltaP `15.2675` edge `0.2342` maxDD `-12.7414`
- `market_context_high->crypto_alt_1h` score `1.1026` n `214` status `ready` deltaP `9.3234` edge `0.1411` maxDD `-4.9097`
- `market_context_high->index_4h` score `1.0672` n `214` status `ready` deltaP `10.3345` edge `0.0884` maxDD `-1.8022`
- `market_context_high->equity_24h` score `0.784` n `185` status `ready` deltaP `14.4715` edge `0.4587` maxDD `-33.1875`
- `market_context_high->fx_24h` score `0.6552` n `185` status `ready` deltaP `16.2643` edge `0.0292` maxDD `-1.6425`
- `market_context_high->index_24h` score `0.0165` n `185` status `ready` deltaP `2.7472` edge `0.1059` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.0228` n `214` status `ready` deltaP `5.241` edge `0.042` maxDD `-2.6402`
- `market_context_high->index_1h` score `-0.5438` n `214` status `ready` deltaP `0.3638` edge `0.0113` maxDD `-1.3898`
- `market_context_high->crypto_major_24h` score `-0.5591` n `185` status `ready` deltaP `18.9439` edge `0.6857` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `-0.7051` n `214` status `ready` deltaP `3.1353` edge `-0.0077` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.7605` n `214` status `ready` deltaP `2.391` edge `0.0053` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8287` n `214` status `ready` deltaP `-1.0479` edge `0.0007` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.5927` n `214` status `ready` deltaP `-6.4024` edge `-0.0019` maxDD `-1.0513`
- `market_context_high->metal_4h` score `-1.6396` n `214` status `ready` deltaP `7.0392` edge `0.0787` maxDD `-11.9812`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
