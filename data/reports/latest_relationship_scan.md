# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T12:52:34.493719+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7072`

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

- `market_context_high->unknown_24h` score `1340.3711` n `145` status `ready` deltaP `-2.4845` edge `111.8069` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `40.8922` n `145` status `ready` deltaP `5.7558` edge `3.3826` maxDD `-0.3966`
- `market_context_high->index_24h` score `1.1197` n `145` status `ready` deltaP `20.2347` edge `-0.0005` maxDD `-1.2875`
- `market_context_high->commodity_4h` score `0.0874` n `145` status `ready` deltaP `12.069` edge `0.0487` maxDD `-1.0837`
- `market_context_high->fx_1h` score `0.0369` n `145` status `ready` deltaP `5.8032` edge `0.0002` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.1382` n `145` status `ready` deltaP `7.4768` edge `0.0058` maxDD `-1.2025`
- `market_context_high->fx_4h` score `-0.165` n `145` status `ready` deltaP `5.5499` edge `0.0017` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.362` n `145` status `ready` deltaP `0.5534` edge `0.0083` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.5149` n `145` status `ready` deltaP `9.2809` edge `0.0016` maxDD `-4.0256`
- `market_context_high->index_1h` score `-0.7835` n `145` status `ready` deltaP `-4.1782` edge `-0.0043` maxDD `-1.4631`
- `market_context_high->crypto_major_1h` score `-0.8461` n `145` status `ready` deltaP `4.5736` edge `0.0273` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-1.1569` n `145` status `ready` deltaP `4.6516` edge `0.01` maxDD `-0.9934`
- `market_context_high->equity_1h` score `-1.4227` n `145` status `ready` deltaP `-0.0454` edge `0.0019` maxDD `-8.7199`
- `market_context_high->crypto_alt_1h` score `-1.6164` n `145` status `ready` deltaP `1.9275` edge `0.0107` maxDD `-11.7957`
- `market_context_high->metal_24h` score `-2.3157` n `145` status `ready` deltaP `0.5855` edge `-0.0111` maxDD `-10.5088`
- `market_context_high->index_4h` score `-3.0257` n `145` status `ready` deltaP `-10.1882` edge `-0.032` maxDD `-5.1773`
- `market_context_high->crypto_major_4h` score `-3.5016` n `145` status `ready` deltaP `2.2036` edge `-0.0376` maxDD `-26.7476`
- `market_context_high->crypto_major_24h` score `-3.7502` n `145` status `ready` deltaP `-3.1178` edge `0.0257` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.4841` n `145` status `ready` deltaP `-4.3156` edge `-0.123` maxDD `-27.1824`
- `market_context_high->commodity_24h` score `-4.6813` n `145` status `ready` deltaP `0.0072` edge `-0.0412` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
