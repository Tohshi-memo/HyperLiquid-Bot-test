# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T01:52:23.634829+00:00`
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

- `market_context_high->equity_24h` score `8.3133` n `34` status `ready` deltaP `15.6046` edge `0.9028` maxDD `-22.7914`
- `market_context_high->index_24h` score `1.2293` n `34` status `ready` deltaP `15.2267` edge `0.1142` maxDD `-2.6491`
- `market_context_high->commodity_24h` score `1.1653` n `34` status `ready` deltaP `6.5768` edge `0.1731` maxDD `-2.4036`
- `market_context_high->metal_1h` score `0.7798` n `65` status `ready` deltaP `9.8503` edge `0.0321` maxDD `-0.6226`
- `market_context_high->fx_24h` score `0.7122` n `34` status `ready` deltaP `10.6618` edge `-0.0029` maxDD `-0.0397`
- `market_context_high->commodity_4h` score `0.3033` n `53` status `ready` deltaP `1.9731` edge `0.051` maxDD `-1.1102`
- `market_context_high->equity_1h` score `0.1685` n `65` status `ready` deltaP `2.7153` edge `0.1232` maxDD `-5.5762`
- `market_context_high->metal_4h` score `-0.0203` n `53` status `ready` deltaP `5.2692` edge `0.0148` maxDD `-1.2025`
- `market_context_high->index_4h` score `-0.2941` n `53` status `ready` deltaP `7.8808` edge `0.0026` maxDD `-2.4279`
- `market_context_high->commodity_1h` score `-0.4504` n `65` status `ready` deltaP `2.3906` edge `0.0053` maxDD `-1.7019`
- `market_context_high->fx_4h` score `-0.511` n `53` status `ready` deltaP `2.4506` edge `0.0072` maxDD `-0.7904`
- `market_context_high->index_1h` score `-0.6407` n `65` status `ready` deltaP `-2.0498` edge `0.0186` maxDD `-0.6664`
- `market_context_high->fx_1h` score `-0.6487` n `65` status `ready` deltaP `-6.7987` edge `0.0001` maxDD `-0.3682`
- `market_context_high->crypto_alt_1h` score `-0.7083` n `65` status `ready` deltaP `9.2354` edge `0.0369` maxDD `-10.1421`
- `market_context_high->crypto_major_1h` score `-1.9029` n `65` status `ready` deltaP `2.6739` edge `-0.0519` maxDD `-11.7911`
- `market_context_high->metal_24h` score `-1.9395` n `34` status `ready` deltaP `4.1667` edge `-0.1341` maxDD `-1.4245`
- `market_context_high->equity_4h` score `-6.203` n `53` status `ready` deltaP `2.4103` edge `-0.155` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-6.2481` n `34` status `ready` deltaP `-6.6993` edge `-0.0646` maxDD `-26.9129`
- `market_context_high->crypto_alt_4h` score `-10.2585` n `53` status `ready` deltaP `-0.5264` edge `-0.3763` maxDD `-31.3386`
- `market_context_high->crypto_alt_24h` score `-11.1185` n `34` status `ready` deltaP `-20.0368` edge `-0.2599` maxDD `-35.9782`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
