# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T09:52:29.993871+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9426`

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

- `market_context_high->unknown_4h` score `87.4387` n `135` status `ready` deltaP `5.3094` edge `7.2664` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `15.3719` n `135` status `ready` deltaP `1.5181` edge `1.3198` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.8605` n `127` status `ready` deltaP `26.5097` edge `0.0471` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4979` n `135` status `ready` deltaP `11.0557` edge `0.0036` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4761` n `135` status `ready` deltaP `13.3537` edge `0.0105` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.0919` n `135` status `ready` deltaP `11.2442` edge `0.0115` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.3417` n `135` status `ready` deltaP `1.8286` edge `0.0094` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4817` n `135` status `ready` deltaP `5.5866` edge `0.0293` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5484` n `135` status `ready` deltaP `-0.0632` edge `-0.0016` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.6406` n `135` status `ready` deltaP `10.1479` edge `0.0043` maxDD `-4.6603`
- `market_context_high->fx_24h` score `-0.6747` n `127` status `ready` deltaP `7.7744` edge `0.0189` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.7195` n `135` status `ready` deltaP `4.0978` edge `0.0346` maxDD `-1.0837`
- `market_context_high->metal_24h` score `-0.8377` n `127` status `ready` deltaP `14.8051` edge `0.091` maxDD `-6.7607`
- `market_context_high->equity_1h` score `-1.3443` n `135` status `ready` deltaP `2.4894` edge `0.0023` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.9569` n `135` status `ready` deltaP `-1.191` edge `-0.0066` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.4692` n `135` status `ready` deltaP `-3.1166` edge `-0.0228` maxDD `-5.6417`
- `market_context_high->equity_24h` score `-2.7402` n `127` status `ready` deltaP `6.1463` edge `0.0271` maxDD `-15.7143`
- `market_context_high->crypto_major_4h` score `-3.594` n `135` status `ready` deltaP `4.2694` edge `-0.0573` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.5868` n `127` status `ready` deltaP `-0.9061` edge `-0.0963` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.7084` n `135` status `ready` deltaP `3.9194` edge `-0.1064` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
