# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T23:52:26.487470+00:00`
- Price records: `672`
- Market context records: `5090`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10352`

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

- `market_context_high->unknown_24h` score `18.3011` n `77` status `ready` deltaP `27.4576` edge `1.3763` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `9.2688` n `110` status `ready` deltaP `2.8879` edge `0.8173` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `8.8623` n `98` status `ready` deltaP `22.4614` edge `0.691` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.3268` n `98` status `ready` deltaP `15.387` edge `0.4769` maxDD `-7.513`
- `market_context_high->crypto_major_4h` score `2.8689` n `98` status `ready` deltaP `14.8239` edge `0.4782` maxDD `-12.4039`
- `market_context_high->equity_4h` score `2.5829` n `98` status `ready` deltaP `14.8488` edge `0.2294` maxDD `-6.3852`
- `market_context_high->equity_1h` score `1.247` n `110` status `ready` deltaP `11.5188` edge `0.0803` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.6451` n `110` status `ready` deltaP `5.7322` edge `0.1117` maxDD `-5.0257`
- `market_context_high->index_4h` score `0.5847` n `98` status `ready` deltaP `11.1063` edge `0.0508` maxDD `-1.0893`
- `market_context_high->index_1h` score `0.3982` n `110` status `ready` deltaP `6.8236` edge `0.0175` maxDD `-0.3843`
- `market_context_high->metal_1h` score `0.3964` n `110` status `ready` deltaP `10.2558` edge `0.0321` maxDD `-1.3057`
- `market_context_high->crypto_major_1h` score `0.3916` n `110` status `ready` deltaP `7.0577` edge `0.1277` maxDD `-6.9639`
- `market_context_high->metal_4h` score `0.1079` n `98` status `ready` deltaP `6.4024` edge `0.0838` maxDD `-2.3457`
- `market_context_high->commodity_1h` score `-0.9718` n `110` status `ready` deltaP `-1.0915` edge `-0.0003` maxDD `-1.8723`
- `market_context_high->commodity_4h` score `-1.1585` n `98` status `ready` deltaP `6.3433` edge `-0.0091` maxDD `-5.3783`
- `market_context_high->fx_24h` score `-1.4315` n `77` status `ready` deltaP `-2.7192` edge `-0.0083` maxDD `-1.7626`
- `market_context_high->commodity_24h` score `-1.5103` n `77` status `ready` deltaP `8.9827` edge `0.0427` maxDD `-15.0303`
- `market_context_high->fx_1h` score `-1.7533` n `110` status `ready` deltaP `-11.5515` edge `-0.005` maxDD `-0.7944`
- `market_context_high->fx_4h` score `-2.2498` n `98` status `ready` deltaP `-10.4623` edge `-0.0109` maxDD `-1.8799`
- `market_context_high->metal_24h` score `-4.5004` n `77` status `ready` deltaP `-5.984` edge `0.0084` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
