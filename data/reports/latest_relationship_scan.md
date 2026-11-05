# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T17:07:45.410759+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4098`

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

- `news_risk_high->crypto_alt_4h` score `0.6474` n `146` status `ready` deltaP `8.7519` edge `0.2883` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.1225` n `146` status `ready` deltaP `4.4966` edge `0.0771` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.669` n `146` status `ready` deltaP `3.2138` edge `0.0028` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7094` n `146` status `ready` deltaP `-2.7407` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4681` n `146` status `ready` deltaP `-7.8387` edge `-0.0108` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5805` n `146` status `ready` deltaP `-9.0658` edge `-0.02` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6765` n `146` status `ready` deltaP `1.6743` edge `0.004` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.1654` n `146` status `ready` deltaP `-4.3204` edge `0.0188` maxDD `-16.4088`
- `news_risk_high->fx_24h` score `-2.3217` n `146` status `ready` deltaP `-16.8728` edge `-0.0143` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.3947` n `146` status `ready` deltaP `-9.7508` edge `0.0021` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.5718` n `146` status `ready` deltaP `-4.4945` edge `-0.0118` maxDD `-9.4709`
- `news_risk_high->index_24h` score `-2.881` n `146` status `ready` deltaP `-12.2504` edge `-0.0035` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.7068` n `146` status `ready` deltaP `-13.1659` edge `0.0143` maxDD `-9.5011`
- `news_risk_high->crypto_major_4h` score `-5.7163` n `146` status `ready` deltaP `-9.4369` edge `-0.0115` maxDD `-24.1554`
- `news_risk_high->metal_4h` score `-5.7629` n `146` status `ready` deltaP `-13.0137` edge `-0.073` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-8.0047` n `146` status `ready` deltaP `-12.07` edge `-0.2284` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-8.8943` n `146` status `ready` deltaP `-14.4928` edge `0.1815` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.4072` n `146` status `ready` deltaP `2.7397` edge `0.0339` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.8837` n `146` status `ready` deltaP `9.8989` edge `0.2274` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.9472` n `146` status `ready` deltaP `1.9266` edge `-0.3579` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
