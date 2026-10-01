# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T22:22:28.965872+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6574`

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

- `market_context_high->unknown_1h` score `338.1373` n `50` status `ready` deltaP `9.0778` edge `28.1225` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `286.8152` n `50` status `ready` deltaP `7.1646` edge `23.8535` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.3095` n `93` status `ready` deltaP `36.3912` edge `1.4708` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.487` n `50` status `ready` deltaP `34.4306` edge `0.786` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.3005` n `50` status `ready` deltaP `19.0671` edge `0.5516` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `6.015` n `50` status `ready` deltaP `12.5417` edge `0.5886` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.091` n `50` status `ready` deltaP `16.6463` edge `0.4426` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.49` n `93` status `ready` deltaP `18.022` edge `0.5694` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.7545` n `50` status `ready` deltaP `19.0417` edge `0.5406` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.1127` n `106` status `ready` deltaP `26.6538` edge `0.1513` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.0454` n `50` status `ready` deltaP `34.061` edge `0.0402` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0419` n `50` status `ready` deltaP `14.7485` edge `0.2002` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `3.0045` n `50` status `ready` deltaP `14.0539` edge `0.223` maxDD `-3.6387`
- `news_risk_high->equity_24h` score `2.5269` n `93` status `ready` deltaP `17.7084` edge `0.4408` maxDD `-9.4579`
- `news_risk_high->metal_24h` score `1.9256` n `93` status `ready` deltaP `21.9254` edge `0.2281` maxDD `-2.192`
- `news_risk_high->index_24h` score `1.9235` n `93` status `ready` deltaP `21.1358` edge `0.0672` maxDD `-0.4916`
- `market_context_high->fx_1h` score `1.4903` n `50` status `ready` deltaP `20.7904` edge `0.012` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.3771` n `93` status `ready` deltaP `23.5439` edge `0.132` maxDD `-3.9922`
- `market_context_high->index_24h` score `0.9097` n `50` status `ready` deltaP `14.7917` edge `0.0751` maxDD `-1.2338`
- `news_risk_high->equity_1h` score `0.5683` n `106` status `ready` deltaP `7.8777` edge `0.0485` maxDD `-0.9592`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
