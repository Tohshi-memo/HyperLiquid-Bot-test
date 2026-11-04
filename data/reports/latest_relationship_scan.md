# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T12:52:29.359859+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4038`

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

- `news_risk_high->crypto_alt_4h` score `-0.0331` n `146` status `ready` deltaP `7.1554` edge `0.2117` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5033` n `146` status `ready` deltaP `1.8825` edge `0.0457` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.709` n `146` status `ready` deltaP `-2.672` edge `-0.003` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.84` n `146` status `ready` deltaP `1.7964` edge `-0.002` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3226` n `146` status `ready` deltaP `-5.2477` edge `-0.0124` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4729` n `146` status `ready` deltaP `-7.7508` edge `-0.012` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.877` n `146` status `ready` deltaP `-0.2311` edge `-0.009` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-1.9224` n `146` status `ready` deltaP `-1.0902` edge `0.045` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.3504` n `146` status `ready` deltaP `-8.9267` edge `0.0003` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.3804` n `146` status `ready` deltaP `-17.9718` edge `-0.0145` maxDD `-2.336`
- `news_risk_high->metal_24h` score `-2.5379` n `146` status `ready` deltaP `7.2451` edge `0.0984` maxDD `-16.6552`
- `news_risk_high->equity_1h` score `-2.622` n `146` status `ready` deltaP `-6.1869` edge `-0.0273` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2079` n `146` status `ready` deltaP `-8.0059` edge `-0.0414` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.6232` n `146` status `ready` deltaP `-10.8153` edge `0.0056` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8055` n `146` status `ready` deltaP `-5.3358` edge `-0.0444` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0231` n `146` status `ready` deltaP `-12.4079` edge `-0.1006` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-8.6418` n `146` status `ready` deltaP `15.8601` edge `0.4858` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-11.1681` n `146` status `ready` deltaP `13.438` edge `0.4301` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.5543` n `146` status `ready` deltaP `-1.5989` edge `-0.1161` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2057` n `146` status `ready` deltaP `-20.6807` edge `-0.0532` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
