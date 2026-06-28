# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T15:37:33.540452+00:00`
- Price records: `672`
- Market context records: `5054`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10292`

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

- `market_context_high->unknown_1h` score `12.0976` n `100` status `ready` deltaP `3.9042` edge `1.0322` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.9018` n `98` status `ready` deltaP `21.441` edge `0.7011` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.5178` n `98` status `ready` deltaP `16.3608` edge `0.4891` maxDD `-7.7348`
- `market_context_high->crypto_major_4h` score `5.3339` n `98` status `ready` deltaP `16.9238` edge `0.4901` maxDD `-8.3416`
- `market_context_high->metal_4h` score `0.9078` n `98` status `ready` deltaP `10.0267` edge `0.1167` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.8831` n `100` status `ready` deltaP `7.491` edge `0.1124` maxDD `-4.4335`
- `market_context_high->equity_1h` score `0.5001` n `100` status `ready` deltaP `7.7485` edge `0.0698` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.4684` n `98` status `ready` deltaP `4.1749` edge `0.1662` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3818` n `100` status `ready` deltaP `6.7904` edge `0.0362` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.2154` n `100` status `ready` deltaP `5.6467` edge `0.0905` maxDD `-5.3758`
- `market_context_high->fx_24h` score `-0.0619` n `76` status `ready` deltaP `8.9638` edge `0.0085` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.0637` n `98` status `ready` deltaP `4.8314` edge `0.0386` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3554` n `100` status `ready` deltaP `0.9461` edge `0.0141` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4859` n `100` status `ready` deltaP `0.0` edge `0.0118` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.5656` n `98` status `ready` deltaP `6.9531` edge `0.0064` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.975` n `98` status `ready` deltaP `-3.5652` edge `-0.0023` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.4779` n `100` status `ready` deltaP `-8.6048` edge `-0.0048` maxDD `-0.5464`
- `market_context_high->unknown_24h` score `-2.9558` n `76` status `ready` deltaP `27.3209` edge `-0.3942` maxDD `-1.4072`
- `market_context_high->metal_24h` score `-3.551` n `76` status `ready` deltaP `6.049` edge `0.0499` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.4986` n `76` status `ready` deltaP `0.6579` edge `-0.0845` maxDD `-26.7306`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
