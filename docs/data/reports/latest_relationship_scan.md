# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T17:22:31.869896+00:00`
- Price records: `672`
- Market context records: `4849`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7632`

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

- `market_context_high->unknown_1h` score `13.4982` n `110` status `ready` deltaP `10.4709` edge `1.0968` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.6692` n `99` status `ready` deltaP `28.674` edge `0.8344` maxDD `-1.917`
- `market_context_high->unknown_24h` score `5.3361` n `88` status `ready` deltaP `25.7892` edge `0.307` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.2211` n `99` status `ready` deltaP `18.0771` edge `0.4498` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `5.1275` n `99` status `ready` deltaP `14.551` edge `0.4527` maxDD `-7.1265`
- `market_context_high->metal_4h` score `1.5589` n `99` status `ready` deltaP `11.9011` edge `0.1168` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.6268` n `99` status `ready` deltaP `10.8155` edge `0.1464` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.4874` n `99` status `ready` deltaP `10.5676` edge `0.0383` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4321` n `110` status `ready` deltaP `6.1704` edge `0.1181` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.43` n `110` status `ready` deltaP `8.1709` edge `0.1029` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2082` n `110` status `ready` deltaP `4.2352` edge `0.0582` maxDD `-2.779`
- `market_context_high->fx_4h` score `-0.1284` n `99` status `ready` deltaP `6.3178` edge `0.0096` maxDD `-0.788`
- `market_context_high->commodity_1h` score `-0.2246` n `110` status `ready` deltaP `3.2825` edge `0.0153` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.2398` n `110` status `ready` deltaP `-0.3539` edge `0.0296` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.5258` n `110` status `ready` deltaP `-0.2885` edge `0.01` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.6731` n `99` status `ready` deltaP `8.0885` edge `0.0072` maxDD `-4.377`
- `market_context_high->fx_1h` score `-1.331` n `110` status `ready` deltaP `-6.8672` edge `-0.0038` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.9282` n `88` status `ready` deltaP `-7.1181` edge `-0.0122` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.8465` n `88` status `ready` deltaP `-9.0435` edge `-0.16` maxDD `-24.085`
- `market_context_high->commodity_24h` score `-5.542` n `88` status `ready` deltaP `10.1326` edge `-0.0185` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
