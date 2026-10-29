# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T15:07:29.658316+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6784`

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

- `market_context_high->unknown_24h` score `1513.6103` n `138` status `ready` deltaP `-1.1549` edge `126.2031` maxDD `-2.5636`
- `market_context_high->unknown_4h` score `56.9783` n `138` status `ready` deltaP `7.1226` edge `4.714` maxDD `-0.3966`
- `market_context_high->index_24h` score `1.8464` n `138` status `ready` deltaP `24.0565` edge `0.0118` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `0.2583` n `138` status `ready` deltaP `13.081` edge `0.0562` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.0684` n `138` status `ready` deltaP `9.0666` edge `0.0079` maxDD `-0.7659`
- `market_context_high->fx_1h` score `-0.0271` n `138` status `ready` deltaP `5.0486` edge `-0.0001` maxDD `-0.1986`
- `market_context_high->metal_4h` score `-0.0854` n `138` status `ready` deltaP `12.0095` edge `0.0092` maxDD `-2.6836`
- `market_context_high->commodity_1h` score `-0.2673` n `138` status `ready` deltaP `2.0481` edge `0.0155` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.2824` n `138` status `ready` deltaP `3.5459` edge `0.0` maxDD `-0.4545`
- `market_context_high->equity_1h` score `-0.5779` n `138` status `ready` deltaP `0.5511` edge `0.0249` maxDD `-3.5462`
- `market_context_high->crypto_major_1h` score `-0.6917` n `138` status `ready` deltaP `5.0247` edge `0.0258` maxDD `-6.0219`
- `market_context_high->index_1h` score `-0.6999` n `138` status `ready` deltaP `-3.4431` edge `-0.0026` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-0.9059` n `138` status `ready` deltaP `6.5821` edge `0.0137` maxDD `-0.9792`
- `market_context_high->crypto_alt_1h` score `-1.319` n `138` status `ready` deltaP `1.9938` edge `0.0164` maxDD `-9.2367`
- `market_context_high->metal_24h` score `-1.8707` n `138` status `ready` deltaP `2.6494` edge `0.0072` maxDD `-10.5088`
- `market_context_high->equity_4h` score `-2.2304` n `138` status `ready` deltaP `-3.0864` edge `-0.0455` maxDD `-10.9236`
- `market_context_high->index_4h` score `-2.5832` n `138` status `ready` deltaP `-7.7744` edge `-0.0258` maxDD `-4.0109`
- `market_context_high->crypto_major_4h` score `-2.8384` n `138` status `ready` deltaP `3.6652` edge `-0.0361` maxDD `-20.8449`
- `market_context_high->equity_24h` score `-3.8445` n `138` status `ready` deltaP `6.6652` edge `-0.0891` maxDD `-14.0571`
- `market_context_high->crypto_major_24h` score `-4.0964` n `138` status `ready` deltaP `-5.1555` edge `-0.0051` maxDD `-29.1905`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
