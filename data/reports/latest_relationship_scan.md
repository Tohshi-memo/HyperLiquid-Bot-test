# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T13:22:36.143345+00:00`
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

- `market_context_high->unknown_24h` score `48.9567` n `161` status `ready` deltaP `-23.6898` edge `4.5289` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `18.0681` n `32` status `ready` deltaP `-42.1875` edge `2.6727` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `18.0681` n `32` status `ready` deltaP `-42.1875` edge `2.6727` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `8.3251` n `31` status `ready` deltaP `7.3813` edge `0.6825` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.9242` n `36` status `ready` deltaP `36.7378` edge `0.3321` maxDD `0.0`
- `risk_on_high->commodity_24h` score `3.661` n `32` status `ready` deltaP `26.5625` edge `0.128` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `3.661` n `32` status `ready` deltaP `26.5625` edge `0.128` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.5898` n `32` status `ready` deltaP `18.3689` edge `0.1116` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.5898` n `32` status `ready` deltaP `18.3689` edge `0.1116` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.4886` n `31` status `ready` deltaP `15.9722` edge `0.1009` maxDD `0.0`
- `risk_on_high->fx_24h` score `2.0362` n `32` status `ready` deltaP `22.7431` edge `0.0365` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `2.0362` n `32` status `ready` deltaP `22.7431` edge `0.0365` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.8289` n `36` status `ready` deltaP `20.8333` edge `0.0267` maxDD `-0.0546`
- `market_context_high->commodity_24h` score `1.692` n `161` status `ready` deltaP `16.6246` edge `0.1105` maxDD `-2.4263`
- `news_risk_high->equity_1h` score `1.5536` n `36` status `ready` deltaP `7.535` edge `0.1111` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.4083` n `161` status `ready` deltaP `16.0203` edge `0.0744` maxDD `-2.1077`
- `risk_on_high->crypto_major_24h` score `1.342` n `32` status `ready` deltaP `12.8472` edge `0.202` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.342` n `32` status `ready` deltaP `12.8472` edge `0.202` maxDD `-6.2481`
- `risk_on_high->commodity_1h` score `1.2` n `32` status `ready` deltaP `12.9117` edge `0.0372` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2` n `32` status `ready` deltaP `12.9117` edge `0.0372` maxDD `-0.1957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
