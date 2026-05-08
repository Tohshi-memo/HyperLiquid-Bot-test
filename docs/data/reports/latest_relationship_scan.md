# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T05:22:21.549916+00:00`
- Price records: `617`
- Market context records: `722`
- Flow alert records: `2040`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `11.6356` n `146` status `ready` deltaP `28.2491` edge `0.8147` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.3314` n `146` status `ready` deltaP `7.9523` edge `0.4794` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.3083` n `149` status `ready` deltaP `5.7918` edge `0.009` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.4116` n `152` status `ready` deltaP `2.8725` edge `0.044` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.4471` n `152` status `ready` deltaP `2.7223` edge `0.0024` maxDD `-0.291`
- `market_context_high->index_24h` score `-0.4849` n `146` status `ready` deltaP `-0.8095` edge `0.1645` maxDD `-5.9609`
- `market_context_high->index_1h` score `-0.6325` n `152` status `ready` deltaP `0.2636` edge `0.0025` maxDD `-2.8282`
- `market_context_high->crypto_major_4h` score `-0.9964` n `149` status `ready` deltaP `17.558` edge `0.1258` maxDD `-22.648`
- `market_context_high->equity_1h` score `-1.1163` n `152` status `ready` deltaP `-1.2143` edge `-0.0039` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2528` n `152` status `ready` deltaP `-4.3445` edge `-0.0151` maxDD `-2.1602`
- `market_context_high->equity_24h` score `-1.3759` n `146` status `ready` deltaP `-2.6072` edge `0.1632` maxDD `-10.5047`
- `market_context_high->crypto_alt_1h` score `-1.4572` n `152` status `ready` deltaP `3.9356` edge `-0.0162` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.6904` n `152` status `ready` deltaP `5.3608` edge `-0.0043` maxDD `-11.4508`
- `market_context_high->index_4h` score `-1.8341` n `149` status `ready` deltaP `1.2793` edge `-0.0091` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-1.9821` n `149` status `ready` deltaP `3.4204` edge `0.069` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.7813` n `149` status `ready` deltaP `-1.7357` edge `-0.005` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.414` n `152` status `ready` deltaP `-5.2911` edge `-0.0533` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6318` n `149` status `ready` deltaP `-5.468` edge `0.0839` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.0458` n `149` status `ready` deltaP `4.1798` edge `-0.1772` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.187` n `146` status `ready` deltaP `-13.5927` edge `-0.0572` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
