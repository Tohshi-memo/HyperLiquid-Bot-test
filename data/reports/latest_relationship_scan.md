# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T17:22:25.516682+00:00`
- Price records: `672`
- Market context records: `2989`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6970`

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

- `market_context_high->crypto_alt_24h` score `16.6636` n `98` status `ready` deltaP `5.1162` edge `1.7462` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.0618` n `98` status `ready` deltaP `41.773` edge `0.7377` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `11.3674` n `98` status `ready` deltaP `17.5277` edge `0.8769` maxDD `-1.7175`
- `market_context_high->equity_24h` score `7.4932` n `98` status `ready` deltaP `15.9156` edge `0.7187` maxDD `-12.6963`
- `market_context_high->index_24h` score `4.7357` n `98` status `ready` deltaP `15.873` edge `0.3869` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.4849` n `99` status `ready` deltaP `15.0669` edge `0.2289` maxDD `-0.7819`
- `market_context_high->index_4h` score `2.4281` n `99` status `ready` deltaP `19.6015` edge `0.1505` maxDD `-1.9733`
- `market_context_high->commodity_4h` score `2.3912` n `99` status `ready` deltaP `17.4874` edge `0.1474` maxDD `-2.8438`
- `market_context_high->crypto_alt_4h` score `0.9598` n `99` status `ready` deltaP `24.4026` edge `0.4165` maxDD `-30.8239`
- `market_context_high->index_1h` score `0.3594` n `102` status `ready` deltaP `6.8627` edge `0.0311` maxDD `-1.4189`
- `market_context_high->equity_1h` score `0.0823` n `102` status `ready` deltaP `5.3804` edge `0.0448` maxDD `-3.609`
- `market_context_high->commodity_1h` score `-0.2125` n `102` status `ready` deltaP `-0.3669` edge `0.0177` maxDD `-0.9706`
- `market_context_high->fx_1h` score `-0.4924` n `102` status `ready` deltaP `-1.6467` edge `0.0012` maxDD `-0.1672`
- `market_context_high->crypto_alt_1h` score `-1.0136` n `102` status `ready` deltaP `7.9928` edge `0.0375` maxDD `-11.6869`
- `market_context_high->fx_4h` score `-1.0336` n `99` status `ready` deltaP `-8.5859` edge `0.0026` maxDD `-0.5631`
- `market_context_high->metal_1h` score `-1.0611` n `102` status `ready` deltaP `-2.4393` edge `-0.0063` maxDD `-5.4112`
- `market_context_high->crypto_major_1h` score `-1.0615` n `102` status `ready` deltaP `5.4039` edge `0.011` maxDD `-11.9831`
- `market_context_high->unknown_4h` score `-1.1116` n `99` status `ready` deltaP `-0.3141` edge `0.0148` maxDD `-3.7602`
- `market_context_high->unknown_1h` score `-1.721` n `102` status `ready` deltaP `1.8258` edge `-0.0825` maxDD `-3.1801`
- `market_context_high->crypto_major_4h` score `-1.8662` n `99` status `ready` deltaP `9.6128` edge `0.2092` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
