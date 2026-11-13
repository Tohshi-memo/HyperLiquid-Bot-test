# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T17:07:26.973651+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10554`

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

- `market_context_high->unknown_24h` score `370.8079` n `75` status `ready` deltaP `3.7569` edge `30.8897` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `33.2893` n `53` status `ready` deltaP `32.105` edge `2.6307` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.0556` n `75` status `ready` deltaP `26.6458` edge `2.0645` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `17.6386` n `75` status `ready` deltaP `49.4931` edge `1.3914` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.3327` n `53` status `ready` deltaP `42.0434` edge `1.7538` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.606` n `53` status `ready` deltaP `33.9536` edge `0.7705` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.5781` n `53` status `ready` deltaP `36.1111` edge `0.2241` maxDD `0.0`
- `market_context_high->index_24h` score `4.8044` n `75` status `ready` deltaP `25.5625` edge `0.2391` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.6796` n `53` status `ready` deltaP `44.4145` edge `0.1315` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1234` n `53` status `ready` deltaP `23.575` edge `0.2168` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.902` n `75` status `ready` deltaP `39.0764` edge `0.3289` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.487` n `53` status `ready` deltaP `17.7155` edge `0.2355` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0719` n `53` status `ready` deltaP `28.2358` edge `0.0931` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.0429` n `53` status `ready` deltaP `19.2189` edge `0.2742` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.2592` n `53` status `ready` deltaP `16.3358` edge `0.6313` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1715` n `53` status `ready` deltaP `25.4406` edge `0.0368` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.974` n `53` status `ready` deltaP `19.9839` edge `0.0749` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.7373` n `53` status `ready` deltaP `25.8887` edge `0.214` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2334` n `53` status `ready` deltaP `16.5772` edge `0.0224` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6525` n `53` status `ready` deltaP `17.2946` edge `0.0663` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
