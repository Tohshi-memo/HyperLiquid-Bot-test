# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T01:52:25.900816+00:00`
- Price records: `672`
- Market context records: `5204`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5644`

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

- `market_context_high->unknown_24h` score `17.0355` n `98` status `ready` deltaP `33.7656` edge `1.2135` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.8423` n `98` status `ready` deltaP `30.063` edge `1.4026` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `10.7809` n `98` status `ready` deltaP `30.3465` edge `1.0348` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.2585` n `155` status `ready` deltaP `18.9644` edge `0.414` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.6511` n `155` status `ready` deltaP `13.8464` edge `0.4552` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.4874` n `155` status `ready` deltaP `14.0696` edge `0.5094` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.4237` n `155` status `ready` deltaP `8.5387` edge `0.2092` maxDD `-2.7986`
- `market_context_high->equity_4h` score `0.706` n `155` status `ready` deltaP `8.1599` edge `0.1683` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.6536` n `155` status `ready` deltaP `4.9527` edge `0.1176` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.6448` n `155` status `ready` deltaP `7.0021` edge `0.1316` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.5191` n `98` status `ready` deltaP `13.1838` edge `0.0449` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.0859` n `155` status `ready` deltaP `6.5675` edge `0.0599` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.0755` n `155` status `ready` deltaP `4.7102` edge `0.0181` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.0792` n `155` status `ready` deltaP `4.7354` edge `0.0122` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.2923` n `155` status `ready` deltaP `1.2102` edge `-0.0003` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.5726` n `155` status `ready` deltaP `5.4485` edge `0.0277` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-0.5891` n `155` status `ready` deltaP `0.875` edge `-0.0005` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.5923` n `155` status `ready` deltaP `3.3389` edge `0.0052` maxDD `-1.6047`
- `market_context_high->index_24h` score `-0.7434` n `98` status `ready` deltaP `11.3981` edge `-0.0078` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.3597` n `155` status `ready` deltaP `-0.1023` edge `0.0267` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
