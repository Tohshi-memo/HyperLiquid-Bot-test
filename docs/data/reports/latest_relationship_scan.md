# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T15:22:26.750970+00:00`
- Price records: `672`
- Market context records: `5784`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8718`

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

- `market_context_high->equity_24h` score `0.4715` n `241` status `ready` deltaP `15.0206` edge `0.4682` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.0573` n `298` status `ready` deltaP `7.2363` edge `0.1204` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2552` n `305` status `ready` deltaP `2.2239` edge `0.001` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.6138` n `305` status `ready` deltaP `3.4417` edge `0.0266` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.6455` n `305` status `ready` deltaP `2.2092` edge `-0.001` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.7438` n `305` status `ready` deltaP `-1.4965` edge `-0.0049` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.9355` n `305` status `ready` deltaP `3.022` edge `0.034` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.9772` n `305` status `ready` deltaP `0.2705` edge `0.0036` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.9808` n `241` status `ready` deltaP `14.2058` edge `0.0402` maxDD `-3.852`
- `market_context_high->crypto_alt_1h` score `-1.0484` n `305` status `ready` deltaP `1.9172` edge `0.0333` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1999` n `298` status `ready` deltaP `0.6435` edge `0.0106` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.3913` n `298` status `ready` deltaP `0.977` edge `0.0042` maxDD `-1.793`
- `market_context_high->commodity_4h` score `-2.4654` n `298` status `ready` deltaP `-3.3925` edge `-0.0259` maxDD `-14.071`
- `market_context_high->index_24h` score `-2.858` n `241` status `ready` deltaP `2.7389` edge `0.0298` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.9242` n `298` status `ready` deltaP `7.5984` edge `0.1429` maxDD `-25.6458`
- `market_context_high->metal_4h` score `-3.8476` n `298` status `ready` deltaP `-5.5482` edge `-0.0477` maxDD `-11.5426`
- `market_context_high->crypto_alt_4h` score `-4.5137` n `298` status `ready` deltaP `5.3405` edge `0.0891` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-7.0857` n `241` status `ready` deltaP `-7.8896` edge `-0.2489` maxDD `-27.5543`
- `market_context_high->crypto_major_24h` score `-7.1101` n `241` status `ready` deltaP `1.9076` edge `-0.1012` maxDD `-29.6555`
- `market_context_high->commodity_24h` score `-10.9686` n `241` status `ready` deltaP `-14.1504` edge `-0.0821` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
