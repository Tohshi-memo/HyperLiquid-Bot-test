# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T21:07:37.027357+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4068`

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

- `news_risk_high->equity_4h` score `1.5686` n `86` status `ready` deltaP `13.7053` edge `0.2003` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.75` n `86` status `ready` deltaP `13.4962` edge `0.0203` maxDD `-0.4888`
- `news_risk_high->index_1h` score `0.3199` n `86` status `ready` deltaP `12.2615` edge `0.0046` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `0.2088` n `86` status `ready` deltaP `3.753` edge `0.0567` maxDD `-1.396`
- `news_risk_high->fx_4h` score `-0.0863` n `86` status `ready` deltaP `4.8639` edge `0.0011` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.304` n `86` status `ready` deltaP `0.1149` edge `-0.004` maxDD `-0.5256`
- `news_risk_high->index_24h` score `-0.3166` n `86` status `ready` deltaP `-0.8303` edge `0.1401` maxDD `-6.6786`
- `news_risk_high->fx_1h` score `-0.341` n `86` status `ready` deltaP `-0.5535` edge `-0.0002` maxDD `-0.1858`
- `news_risk_high->crypto_alt_1h` score `-0.5979` n `86` status `ready` deltaP `3.2586` edge `0.0244` maxDD `-5.8225`
- `news_risk_high->fx_24h` score `-0.6185` n `86` status `ready` deltaP `-5.0521` edge `0.0264` maxDD `-0.2073`
- `news_risk_high->crypto_major_4h` score `-0.6875` n `86` status `ready` deltaP `0.2659` edge `0.0787` maxDD `-9.1553`
- `news_risk_high->crypto_major_1h` score `-0.7771` n `86` status `ready` deltaP `-1.9566` edge `0.0073` maxDD `-4.1772`
- `news_risk_high->metal_4h` score `-1.0285` n `86` status `ready` deltaP `-1.1415` edge `-0.0337` maxDD `-1.5773`
- `news_risk_high->equity_24h` score `-1.4414` n `86` status `ready` deltaP `26.1658` edge `0.7994` maxDD `-86.0244`
- `news_risk_high->crypto_alt_4h` score `-1.8274` n `86` status `ready` deltaP `-3.336` edge `0.0516` maxDD `-14.0916`
- `news_risk_high->commodity_1h` score `-2.854` n `86` status `ready` deltaP `-17.0276` edge `-0.0062` maxDD `-1.7824`
- `news_risk_high->metal_24h` score `-2.9505` n `86` status `ready` deltaP `4.2058` edge `-0.2167` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.0972` n `86` status `ready` deltaP `-26.2302` edge `-0.0022` maxDD `-4.4823`
- `news_risk_high->crypto_major_24h` score `-7.1942` n `86` status `ready` deltaP `-20.6421` edge `0.0656` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-9.2625` n `86` status `ready` deltaP `-25.8293` edge `-0.0203` maxDD `-29.0172`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
