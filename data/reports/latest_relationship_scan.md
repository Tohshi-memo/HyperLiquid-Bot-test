# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T04:52:24.627200+00:00`
- Price records: `672`
- Market context records: `2937`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6940`

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

- `market_context_high->crypto_alt_24h` score `16.1369` n `142` status `ready` deltaP `15.7229` edge `1.6316` maxDD `-22.6673`
- `market_context_high->equity_24h` score `7.7364` n `142` status `ready` deltaP `17.9357` edge `0.7255` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `6.7313` n `142` status `ready` deltaP `15.7961` edge `0.5021` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.7135` n `142` status `ready` deltaP `13.7104` edge `0.2328` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8053` n `142` status `ready` deltaP `15.378` edge `0.3573` maxDD `-12.4171`
- `market_context_high->equity_4h` score `0.8938` n `143` status `ready` deltaP `8.8116` edge `0.1537` maxDD `-5.7037`
- `market_context_high->index_4h` score `0.7393` n `143` status `ready` deltaP `15.1245` edge `0.0781` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.1789` n `143` status `ready` deltaP `4.3568` edge `0.0912` maxDD `-3.7602`
- `market_context_high->index_1h` score `0.0219` n `143` status `ready` deltaP `4.9967` edge `0.0189` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `0.0189` n `143` status `ready` deltaP `16.2108` edge `0.3538` maxDD `-30.8239`
- `market_context_high->equity_1h` score `-0.3405` n `143` status `ready` deltaP `1.2029` edge `0.0469` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4446` n `143` status `ready` deltaP `5.8949` edge `0.0797` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5458` n `143` status `ready` deltaP `-0.6469` edge `0.0032` maxDD `-0.2164`
- `market_context_high->unknown_1h` score `-0.5651` n `143` status `ready` deltaP `2.9993` edge `0.006` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-0.5962` n `143` status `ready` deltaP `6.0917` edge `0.0699` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6372` n `143` status `ready` deltaP `0.3967` edge `0.0044` maxDD `-3.4325`
- `market_context_high->commodity_1h` score `-0.6797` n `143` status `ready` deltaP `-1.5451` edge `-0.0015` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.9832` n `143` status `ready` deltaP `-1.5692` edge `0.0064` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2833` n `143` status `ready` deltaP `1.4242` edge `0.018` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.308` n `142` status `ready` deltaP `-1.7116` edge `-0.0104` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
