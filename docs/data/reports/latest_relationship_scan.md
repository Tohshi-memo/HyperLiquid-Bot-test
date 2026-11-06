# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T12:52:30.989181+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3915`

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

- `news_risk_high->equity_24h` score `0.0437` n `119` status `ready` deltaP `22.5655` edge `1.0138` maxDD `-86.0244`
- `news_risk_high->index_4h` score `-0.2007` n `119` status `ready` deltaP `8.5186` edge `0.0117` maxDD `-2.2044`
- `news_risk_high->index_1h` score `-0.2331` n `119` status `ready` deltaP `6.3264` edge `0.0021` maxDD `-0.9325`
- `news_risk_high->fx_1h` score `-0.4717` n `119` status `ready` deltaP `-2.5399` edge `-0.0017` maxDD `-0.3475`
- `news_risk_high->crypto_alt_4h` score `-0.5194` n `119` status `ready` deltaP `4.7781` edge `0.1652` maxDD `-14.0916`
- `news_risk_high->index_24h` score `-0.6556` n `119` status `ready` deltaP `-3.4602` edge `0.1225` maxDD `-6.6786`
- `news_risk_high->crypto_alt_1h` score `-0.7552` n `119` status `ready` deltaP `0.2944` edge `0.024` maxDD `-5.8225`
- `news_risk_high->fx_4h` score `-0.7965` n `119` status `ready` deltaP `-2.8477` edge `-0.0022` maxDD `-0.4745`
- `news_risk_high->metal_1h` score `-1.1168` n `119` status `ready` deltaP `-3.6318` edge `-0.0129` maxDD `-1.4762`
- `news_risk_high->fx_24h` score `-1.3889` n `119` status `ready` deltaP `-16.263` edge `-0.0062` maxDD `-0.4086`
- `news_risk_high->equity_1h` score `-1.4456` n `119` status `ready` deltaP `-1.4102` edge `0.0151` maxDD `-10.283`
- `news_risk_high->crypto_major_1h` score `-1.6465` n `119` status `ready` deltaP `-4.1489` edge `-0.009` maxDD `-4.7103`
- `news_risk_high->crypto_major_4h` score `-1.8214` n `119` status `ready` deltaP `-3.9417` edge `0.0556` maxDD `-9.1553`
- `news_risk_high->metal_4h` score `-2.7305` n `119` status `ready` deltaP `-7.1313` edge `-0.0484` maxDD `-3.1947`
- `news_risk_high->commodity_1h` score `-2.8042` n `119` status `ready` deltaP `-13.624` edge `-0.0062` maxDD `-3.2657`
- `news_risk_high->equity_4h` score `-2.9319` n `119` status `ready` deltaP `8.9759` edge `0.0903` maxDD `-25.8902`
- `news_risk_high->metal_24h` score `-3.4752` n `119` status `ready` deltaP `-5.1656` edge `-0.2215` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.6888` n `119` status `ready` deltaP `-21.5106` edge `-0.0119` maxDD `-9.5011`
- `news_risk_high->crypto_major_24h` score `-6.4909` n `119` status `ready` deltaP `-17.647` edge `0.1358` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.2625` n `119` status `ready` deltaP `-23.3564` edge `0.0122` maxDD `-39.6028`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
