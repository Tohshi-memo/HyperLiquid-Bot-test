# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T03:52:30.398417+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5751`

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

- `market_context_high->unknown_4h` score `43.0796` n `86` status `ready` deltaP `-6.6967` edge `3.6885` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.9405` n `86` status `ready` deltaP `38.3196` edge `0.6158` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.0633` n `86` status `ready` deltaP `18.972` edge `1.3503` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.5655` n `86` status `ready` deltaP `18.0517` edge `0.2134` maxDD `-6.9761`
- `market_context_high->crypto_alt_24h` score `0.3346` n `86` status `ready` deltaP `7.5339` edge `0.6039` maxDD `-35.5652`
- `market_context_high->fx_1h` score `0.314` n `97` status `ready` deltaP `7.3477` edge `0.0014` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1512` n `97` status `ready` deltaP `9.3108` edge `0.0462` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.1235` n `86` status `ready` deltaP `10.848` edge `0.0084` maxDD `-0.3007`
- `market_context_high->commodity_1h` score `-0.2202` n `97` status `ready` deltaP `0.747` edge `0.0044` maxDD `-0.3417`
- `market_context_high->metal_1h` score `-0.3184` n `97` status `ready` deltaP `1.3627` edge `0.0013` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.3573` n `86` status `ready` deltaP `8.0023` edge `0.0918` maxDD `-1.9432`
- `market_context_high->metal_24h` score `-0.417` n `86` status `ready` deltaP `6.246` edge `0.0534` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.4962` n `86` status `ready` deltaP `-0.4928` edge `-0.007` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `-0.6718` n `97` status `ready` deltaP `0.0154` edge `0.0276` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.8361` n `97` status `ready` deltaP `-2.6961` edge `-0.0044` maxDD `-2.1184`
- `market_context_high->crypto_alt_4h` score `-1.1376` n `86` status `ready` deltaP `-7.9091` edge `0.1002` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-1.1417` n `86` status `ready` deltaP `-8.9407` edge `0.014` maxDD `-1.0609`
- `market_context_high->equity_4h` score `-1.2928` n `86` status `ready` deltaP `-3.6762` edge `0.0057` maxDD `-5.4217`
- `market_context_high->index_1h` score `-1.64` n `97` status `ready` deltaP `-7.1501` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.803` n `86` status `ready` deltaP `-8.7493` edge `0.0013` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
