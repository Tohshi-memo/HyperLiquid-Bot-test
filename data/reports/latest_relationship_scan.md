# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T15:22:25.584748+00:00`
- Price records: `672`
- Market context records: `7997`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11806`

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

- `market_context_high->equity_24h` score `15.9994` n `89` status `ready` deltaP `25.9753` edge `1.2943` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.8238` n `89` status `ready` deltaP `35.9375` edge `0.4124` maxDD `0.0`
- `market_context_high->equity_4h` score `6.2034` n `104` status `ready` deltaP `25.0703` edge `0.4391` maxDD `-5.1426`
- `market_context_high->metal_4h` score `2.5795` n `104` status `ready` deltaP `24.015` edge `0.1171` maxDD `-0.979`
- `market_context_high->index_4h` score `2.462` n `104` status `ready` deltaP `25.8678` edge `0.0687` maxDD `-0.8791`
- `market_context_high->commodity_24h` score `2.3941` n `89` status `ready` deltaP `22.1656` edge `0.205` maxDD `-6.5945`
- `market_context_high->index_24h` score `2.0365` n `89` status `ready` deltaP `12.1548` edge `0.1557` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.6523` n `104` status `ready` deltaP `14.0776` edge `0.1256` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.2149` n `89` status `ready` deltaP `26.0104` edge `0.0366` maxDD `-3.0343`
- `market_context_high->index_1h` score `0.9121` n `104` status `ready` deltaP `14.7628` edge `0.0206` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.784` n `104` status `ready` deltaP `10.5652` edge `0.1667` maxDD `-6.7444`
- `market_context_high->metal_1h` score `0.7057` n `104` status `ready` deltaP `10.1912` edge `0.0287` maxDD `-0.6936`
- `market_context_high->crypto_alt_4h` score `0.6987` n `104` status `ready` deltaP `7.0708` edge `0.1228` maxDD `-3.9374`
- `market_context_high->crypto_major_1h` score `0.5498` n `104` status `ready` deltaP `10.79` edge `0.0396` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.045` n `104` status `ready` deltaP `0.7485` edge `0.0325` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.273` n `104` status `ready` deltaP `0.1094` edge `0.001` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.4277` n `104` status `ready` deltaP `5.2533` edge `0.0041` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.5553` n `104` status `ready` deltaP `-0.6852` edge `-0.0043` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.1754` n `104` status `ready` deltaP `0.598` edge `-0.0045` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.9598` n `104` status `ready` deltaP `6.7538` edge `-0.166` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
