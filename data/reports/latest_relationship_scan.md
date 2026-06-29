# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T19:37:30.906354+00:00`
- Price records: `672`
- Market context records: `5175`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `25.9945` n `73` status `ready` deltaP `32.3677` edge `1.9694` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `9.9082` n `73` status `ready` deltaP `22.5219` edge `1.0417` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `8.8107` n `73` status `ready` deltaP `23.8536` edge `0.9139` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `6.1438` n `149` status `ready` deltaP `20.656` edge `0.4765` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.0917` n `149` status `ready` deltaP `15.6787` edge `0.4797` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.8151` n `149` status `ready` deltaP `14.6413` edge `0.5329` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.7151` n `155` status `ready` deltaP `10.0357` edge `0.2235` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.4794` n `149` status `ready` deltaP `9.397` edge `0.2245` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.5908` n `155` status `ready` deltaP `6.8524` edge `0.1281` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.5553` n `155` status `ready` deltaP `4.3539` edge `0.1134` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.3735` n `155` status `ready` deltaP `8.6633` edge `0.0699` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0502` n `155` status `ready` deltaP `6.0827` edge `0.014` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0522` n `155` status `ready` deltaP `5.1593` edge `0.0181` maxDD `-2.0682`
- `market_context_high->fx_24h` score `-0.1502` n `73` status `ready` deltaP `9.1372` edge `0.0161` maxDD `-0.8294`
- `market_context_high->fx_1h` score `-0.2324` n `155` status `ready` deltaP `2.2581` edge `0.0004` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.3702` n `149` status `ready` deltaP `6.3738` edge `0.0384` maxDD `-2.9391`
- `market_context_high->commodity_24h` score `-0.5828` n `73` status `ready` deltaP `11.758` edge `0.0806` maxDD `-10.6962`
- `market_context_high->fx_4h` score `-0.5867` n `149` status `ready` deltaP `3.236` edge `0.0066` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6039` n `155` status `ready` deltaP `0.5756` edge `-0.0004` maxDD `-2.4692`
- `market_context_high->metal_24h` score `-0.7578` n `73` status `ready` deltaP `-4.2761` edge `0.1661` maxDD `-10.4465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
