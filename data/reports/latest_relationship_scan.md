# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T18:07:34.330907+00:00`
- Price records: `672`
- Market context records: `5168`
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

- `market_context_high->unknown_24h` score `28.6882` n `67` status `ready` deltaP `32.9188` edge `2.1902` maxDD `-0.8515`
- `market_context_high->crypto_alt_24h` score `7.7642` n `67` status `ready` deltaP `21.0924` edge `0.8451` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.9205` n `143` status `ready` deltaP `20.0996` edge `0.4616` maxDD `-5.5109`
- `market_context_high->crypto_major_24h` score `5.1723` n `67` status `ready` deltaP `19.3926` edge `0.9` maxDD `-22.6266`
- `market_context_high->crypto_alt_4h` score `4.813` n `143` status `ready` deltaP `15.0446` edge `0.4607` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.2235` n `143` status `ready` deltaP `13.9509` edge `0.4882` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `3.5782` n `150` status `ready` deltaP `9.7545` edge `0.2973` maxDD `-2.7986`
- `market_context_high->equity_4h` score `0.8327` n `143` status `ready` deltaP `8.6784` edge `0.1754` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.8155` n `150` status `ready` deltaP `8.0559` edge `0.1388` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.7589` n `150` status `ready` deltaP `5.2794` edge `0.1242` maxDD `-5.0257`
- `market_context_high->commodity_24h` score `0.5716` n `67` status `ready` deltaP `16.5423` edge `0.1274` maxDD `-7.1525`
- `market_context_high->equity_1h` score `0.294` n `150` status `ready` deltaP `7.7146` edge `0.0696` maxDD `-5.0555`
- `market_context_high->metal_24h` score `0.1849` n `67` status `ready` deltaP `-1.3319` edge `0.208` maxDD `-7.7002`
- `market_context_high->index_1h` score `-0.053` n `150` status `ready` deltaP `4.8982` edge `0.0133` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0679` n `150` status `ready` deltaP `5.1577` edge `0.0161` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2146` n `150` status `ready` deltaP `2.5848` edge `0.0005` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.3691` n `143` status `ready` deltaP `5.0124` edge `0.031` maxDD `-2.9391`
- `market_context_high->fx_24h` score `-0.378` n `67` status `ready` deltaP `7.2347` edge `0.0098` maxDD `-0.8294`
- `market_context_high->fx_4h` score `-0.4798` n `143` status `ready` deltaP `5.1723` edge `0.0074` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.5349` n `150` status `ready` deltaP `1.6327` edge `0.0014` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
