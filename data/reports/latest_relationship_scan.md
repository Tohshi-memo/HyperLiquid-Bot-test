# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T02:07:29.220030+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6545`

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

- `market_context_high->equity_24h` score `8.2214` n `34` status `ready` deltaP `15.431` edge `0.8963` maxDD `-22.7914`
- `market_context_high->index_24h` score `1.2179` n `34` status `ready` deltaP `15.0531` edge `0.1139` maxDD `-2.6491`
- `market_context_high->commodity_24h` score `1.1497` n `34` status `ready` deltaP `6.5768` edge `0.1711` maxDD `-2.4036`
- `market_context_high->metal_1h` score `0.8403` n `66` status `ready` deltaP `10.3067` edge `0.0341` maxDD `-0.6226`
- `market_context_high->fx_24h` score `0.7297` n `34` status `ready` deltaP `10.8354` edge `-0.0026` maxDD `-0.0397`
- `market_context_high->equity_1h` score `0.2744` n `66` status `ready` deltaP `3.3116` edge `0.1328` maxDD `-5.5762`
- `market_context_high->commodity_4h` score `0.1947` n `54` status `ready` deltaP `0.9598` edge `0.0487` maxDD `-1.1102`
- `market_context_high->metal_4h` score `0.103` n `54` status `ready` deltaP `5.9903` edge `0.0258` maxDD `-1.2025`
- `market_context_high->index_4h` score `-0.2237` n `54` status `ready` deltaP `8.6495` edge `0.0065` maxDD `-2.4279`
- `market_context_high->commodity_1h` score `-0.3951` n `66` status `ready` deltaP `2.9169` edge `0.0064` maxDD `-1.7019`
- `market_context_high->index_1h` score `-0.5671` n `66` status `ready` deltaP `-1.2339` edge `0.0193` maxDD `-0.6664`
- `market_context_high->fx_4h` score `-0.6038` n `54` status `ready` deltaP `1.4849` edge `0.0064` maxDD `-0.8305`
- `market_context_high->crypto_alt_1h` score `-0.6602` n `66` status `ready` deltaP `9.9347` edge `0.0384` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-0.6816` n `66` status `ready` deltaP `-7.3716` edge `-0.0003` maxDD `-0.3682`
- `market_context_high->crypto_major_1h` score `-1.9324` n `66` status `ready` deltaP `2.0776` edge `-0.0517` maxDD `-11.7911`
- `market_context_high->metal_24h` score `-1.9515` n `34` status `ready` deltaP `4.1667` edge `-0.1351` maxDD `-1.4245`
- `market_context_high->equity_4h` score `-5.7531` n `54` status `ready` deltaP `3.3537` edge `-0.1238` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-6.2385` n `34` status `ready` deltaP `-6.6993` edge `-0.0638` maxDD `-26.9129`
- `market_context_high->crypto_alt_4h` score `-9.642` n `54` status `ready` deltaP `0.4743` edge `-0.3316` maxDD `-31.3386`
- `market_context_high->crypto_alt_24h` score `-11.1437` n `34` status `ready` deltaP `-20.0368` edge `-0.262` maxDD `-35.9782`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
