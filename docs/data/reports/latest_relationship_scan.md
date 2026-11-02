# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T12:22:47.837451+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4861`

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

- `news_risk_high->crypto_alt_4h` score `0.2846` n `141` status `ready` deltaP `6.5257` edge `0.2364` maxDD `-12.4736`
- `news_risk_high->crypto_alt_24h` score `0.0104` n `119` status `ready` deltaP `17.5464` edge `0.6135` maxDD `-49.9981`
- `news_risk_high->fx_1h` score `-0.526` n `146` status `ready` deltaP `0.7711` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->crypto_alt_1h` score `-0.5407` n `146` status `ready` deltaP `1.2837` edge `0.0449` maxDD `-5.8225`
- `news_risk_high->metal_24h` score `-0.7895` n `119` status `ready` deltaP `13.9487` edge `0.1314` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0964` n `146` status `ready` deltaP `-0.7485` edge `-0.0064` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1795` n `141` status `ready` deltaP `-2.1839` edge `-0.0115` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.279` n `146` status `ready` deltaP `-4.9483` edge `-0.0088` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-2.1492` n `119` status `ready` deltaP `-15.0108` edge `-0.0046` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2139` n `141` status `ready` deltaP `-4.265` edge `-0.0253` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3745` n `146` status `ready` deltaP `-8.4776` edge `-0.0047` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.8611` n `119` status `ready` deltaP `-9.6916` edge `-0.018` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.9159` n `146` status `ready` deltaP `-7.5342` edge `-0.056` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.3362` n `146` status `ready` deltaP `-8.7544` edge `-0.0471` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.1561` n `141` status `ready` deltaP `-13.8168` edge `-0.0188` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.5179` n `141` status `ready` deltaP `-4.1861` edge `-0.0281` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-5.5017` n `119` status `ready` deltaP `6.803` edge `0.2588` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.1757` n `141` status `ready` deltaP `-14.1347` edge `-0.1018` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-8.3012` n `141` status `ready` deltaP `-3.0985` edge `-0.2075` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.4811` n `119` status `ready` deltaP `-25.8812` edge `-0.1497` maxDD `-28.4283`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
