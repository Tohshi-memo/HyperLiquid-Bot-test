# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T20:22:26.479813+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12779`

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

- `market_context_high->unknown_24h` score `10875.1632` n `74` status `ready` deltaP `12.7487` edge `906.1838` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `9949.1833` n `34` status `ready` deltaP `15.4514` edge `828.9956` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `9949.1833` n `34` status `ready` deltaP `15.4514` edge `828.9956` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.4916` n `82` status `ready` deltaP `-5.4002` edge `32.0358` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `19.9389` n `71` status `ready` deltaP `43.6498` edge `1.4981` maxDD `-7.5349`
- `news_risk_high->crypto_alt_24h` score `17.2397` n `71` status `ready` deltaP `30.4553` edge `1.2824` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `14.7452` n `34` status `ready` deltaP `35.4677` edge `1.0153` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `14.7452` n `34` status `ready` deltaP `35.4677` edge `1.0153` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `13.3969` n `74` status `ready` deltaP `28.552` edge `1.0088` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `10.0995` n `34` status `ready` deltaP `42.7083` edge `0.5569` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `10.0995` n `34` status `ready` deltaP `42.7083` edge `0.5569` maxDD `0.0`
- `market_context_high->equity_24h` score `9.6567` n `74` status `ready` deltaP `42.7083` edge `0.52` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.741` n `71` status `ready` deltaP `22.99` edge `0.6703` maxDD `-3.6123`
- `news_risk_high->index_24h` score `6.6324` n `71` status `ready` deltaP `44.0947` edge `0.2764` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `6.1135` n `71` status `ready` deltaP `37.8056` edge `0.3015` maxDD `-0.526`
- `risk_on_high->index_24h` score `5.3632` n `34` status `ready` deltaP `53.8296` edge `0.0923` maxDD `-0.005`
- `risk_on_and_context->index_24h` score `5.3632` n `34` status `ready` deltaP `53.8296` edge `0.0923` maxDD `-0.005`
- `risk_on_high->crypto_alt_4h` score `5.3075` n `47` status `ready` deltaP `26.1384` edge `0.3388` maxDD `-2.9944`
- `risk_on_and_context->crypto_alt_4h` score `5.3075` n `47` status `ready` deltaP `26.1384` edge `0.3388` maxDD `-2.9944`
- `market_context_high->index_24h` score `3.3634` n `74` status `ready` deltaP `36.5005` edge `0.0763` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
