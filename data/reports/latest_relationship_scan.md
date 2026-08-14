# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T15:37:29.807079+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `119.5582` n `135` status `ready` deltaP `-33.4606` edge `10.4775` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.8362` n `32` status `ready` deltaP `-45.6597` edge `4.5892` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.8362` n `32` status `ready` deltaP `-45.6597` edge `4.5892` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.7909` n `36` status `ready` deltaP `10.7639` edge `0.7821` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.2722` n `36` status `ready` deltaP `38.5671` edge `0.3489` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7594` n `32` status `ready` deltaP `32.1181` edge `0.1825` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7594` n `32` status `ready` deltaP `32.1181` edge `0.1825` maxDD `0.0`
- `market_context_high->commodity_24h` score `3.8245` n `135` status `ready` deltaP `24.7107` edge `0.2044` maxDD `-1.701`
- `risk_on_high->commodity_4h` score `2.9188` n `32` status `ready` deltaP `20.3506` edge `0.1258` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9188` n `32` status `ready` deltaP `20.3506` edge `0.1258` maxDD `-0.1258`
- `risk_on_high->crypto_major_24h` score `2.1624` n `32` status `ready` deltaP `17.0139` edge `0.2794` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.1624` n `32` status `ready` deltaP `17.0139` edge `0.2794` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.1255` n `36` status `ready` deltaP `14.5833` edge `0.0799` maxDD `0.0`
- `news_risk_high->equity_1h` score `1.7561` n `36` status `ready` deltaP `8.8823` edge `0.119` maxDD `-0.5496`
- `news_risk_high->index_4h` score `1.7127` n `36` status `ready` deltaP `20.0711` edge `0.0221` maxDD `-0.0546`
- `risk_on_high->commodity_1h` score `1.2803` n `32` status `ready` deltaP `13.5105` edge `0.0399` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2803` n `32` status `ready` deltaP `13.5105` edge `0.0399` maxDD `-0.1957`
- `market_context_high->commodity_4h` score `1.2531` n `135` status `ready` deltaP `14.8182` edge `0.0666` maxDD `-1.8769`
- `risk_on_high->fx_24h` score `1.173` n `32` status `ready` deltaP `13.8889` edge `0.0236` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.173` n `32` status `ready` deltaP `13.8889` edge `0.0236` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
