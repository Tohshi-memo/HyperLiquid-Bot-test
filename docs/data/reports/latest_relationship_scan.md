# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T03:22:27.544128+00:00`
- Price records: `672`
- Market context records: `6879`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `0.9362` n `179` status `ready` deltaP `-3.6385` edge `0.5195` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2487` n `224` status `ready` deltaP `2.2375` edge `0.0017` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5853` n `224` status `ready` deltaP `1.9114` edge `0.0149` maxDD `-3.7803`
- `market_context_high->commodity_1h` score `-0.6143` n `224` status `ready` deltaP `-0.8982` edge `-0.0043` maxDD `-2.1443`
- `market_context_high->crypto_major_1h` score `-0.6221` n `224` status `ready` deltaP `3.5474` edge `0.0149` maxDD `-4.2314`
- `market_context_high->index_1h` score `-0.8149` n `224` status `ready` deltaP `-1.628` edge `-0.0025` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8838` n `224` status `ready` deltaP `-4.4429` edge `-0.0069` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9434` n `224` status `ready` deltaP `11.8685` edge `0.0063` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3439` n `224` status `ready` deltaP `-2.3411` edge `-0.0077` maxDD `-5.5853`
- `market_context_high->commodity_24h` score `-1.3884` n `179` status `ready` deltaP `3.318` edge `0.049` maxDD `-5.2791`
- `market_context_high->unknown_1h` score `-1.6194` n `224` status `ready` deltaP `-3.1116` edge `-0.0241` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.8518` n `224` status `ready` deltaP `1.0372` edge `-0.0263` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.982` n `224` status `ready` deltaP `3.9417` edge `-0.0224` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.3794` n `224` status `ready` deltaP `0.49` edge `-0.01` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0789` n `224` status `ready` deltaP `-1.3066` edge `-0.0533` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1104` n `224` status `ready` deltaP `-0.2287` edge `-0.0389` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.1929` n `224` status `ready` deltaP `-9.6472` edge `0.0348` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4514` n `179` status `ready` deltaP `-8.6132` edge `-0.0099` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.3331` n `224` status `ready` deltaP `1.4917` edge `-0.1556` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.8501` n `179` status `ready` deltaP `-17.3194` edge `-0.1606` maxDD `-28.352`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
