# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T08:37:22.095380+00:00`
- Price records: `672`
- Market context records: `2953`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `17.1713` n `129` status `ready` deltaP `13.9979` edge `1.7293` maxDD `-22.6673`
- `market_context_high->equity_24h` score `8.1476` n `129` status `ready` deltaP `18.4109` edge `0.7566` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `8.0564` n `129` status `ready` deltaP `16.7757` edge `0.606` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `5.0528` n `129` status `ready` deltaP `22.4039` edge `0.4531` maxDD `-6.5117`
- `market_context_high->index_24h` score `3.1429` n `129` status `ready` deltaP `14.1876` edge `0.2654` maxDD `-2.5127`
- `market_context_high->equity_4h` score `2.5116` n `130` status `ready` deltaP `13.4592` edge `0.1854` maxDD `-2.9332`
- `market_context_high->crypto_alt_4h` score `1.3978` n `130` status `ready` deltaP `19.9226` edge `0.4398` maxDD `-30.8239`
- `market_context_high->index_4h` score `0.7049` n `130` status `ready` deltaP `13.9986` edge `0.0812` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.6765` n `130` status `ready` deltaP `5.5511` edge `0.1247` maxDD `-3.7602`
- `market_context_high->index_1h` score `0.0731` n `130` status `ready` deltaP `5.5758` edge `0.0216` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.1268` n `130` status `ready` deltaP `1.9622` edge `0.0518` maxDD `-2.0358`
- `market_context_high->fx_1h` score `-0.2273` n `130` status `ready` deltaP `1.1516` edge `0.0041` maxDD `-0.1244`
- `market_context_high->crypto_alt_1h` score `-0.4033` n `130` status `ready` deltaP `5.3846` edge `0.0884` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.5643` n `130` status `ready` deltaP `-1.0064` edge `-0.0031` maxDD `-3.3365`
- `market_context_high->metal_1h` score `-0.6034` n `130` status `ready` deltaP `0.6863` edge `0.0068` maxDD `-3.4325`
- `market_context_high->fx_4h` score `-0.6629` n `130` status `ready` deltaP `1.8645` edge `0.0102` maxDD `-0.5631`
- `market_context_high->crypto_major_1h` score `-0.6827` n `130` status `ready` deltaP `4.5325` edge `0.0692` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-0.8025` n `130` status `ready` deltaP `5.6074` edge `0.0387` maxDD `-8.9839`
- `market_context_high->unknown_1h` score `-0.9105` n `130` status `ready` deltaP `0.661` edge `-0.0072` maxDD `-3.1801`
- `market_context_high->crypto_major_4h` score `-1.035` n `130` status `ready` deltaP `9.9085` edge `0.3138` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
