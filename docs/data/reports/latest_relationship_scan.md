# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T21:07:25.683012+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `89.402` n `151` status `ready` deltaP `-27.1179` edge `7.9222` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.7225` n `32` status `ready` deltaP `-41.6667` edge `4.6762` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.7225` n `32` status `ready` deltaP `-41.6667` edge `4.6762` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.5938` n `36` status `ready` deltaP `10.0694` edge `0.7703` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.6179` n `36` status `ready` deltaP `35.5183` edge `0.3147` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.5896` n `32` status `ready` deltaP `31.9444` edge `0.1695` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.5896` n `32` status `ready` deltaP `31.9444` edge `0.1695` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9142` n `32` status `ready` deltaP `20.503` edge `0.1244` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9142` n `32` status `ready` deltaP `20.503` edge `0.1244` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `2.5799` n `151` status `ready` deltaP `21.3484` edge `0.153` maxDD `-2.4263`
- `news_risk_high->index_24h` score `2.404` n `36` status `ready` deltaP `14.9306` edge `0.1008` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.6598` n `32` status `ready` deltaP `18.9236` edge `0.0306` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.6598` n `32` status `ready` deltaP `18.9236` edge `0.0306` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.6105` n `36` status `ready` deltaP `19.004` edge `0.0207` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.5624` n `151` status `ready` deltaP `17.2124` edge `0.0793` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.496` n `36` status `ready` deltaP `7.0859` edge `0.1093` maxDD `-0.5496`
- `risk_on_high->crypto_major_24h` score `1.3326` n `32` status `ready` deltaP `12.8472` edge `0.2008` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.3326` n `32` status `ready` deltaP `12.8472` edge `0.2008` maxDD `-6.2481`
- `risk_on_high->commodity_1h` score `1.3234` n `32` status `ready` deltaP `14.1093` edge `0.0395` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3234` n `32` status `ready` deltaP `14.1093` edge `0.0395` maxDD `-0.1957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
