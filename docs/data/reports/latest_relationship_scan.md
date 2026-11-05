# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T14:52:31.254276+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4094`

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

- `news_risk_high->crypto_alt_4h` score `0.3299` n `146` status `ready` deltaP `8.6765` edge `0.2481` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.3452` n `146` status `ready` deltaP `3.9783` edge `0.052` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6973` n `146` status `ready` deltaP `-2.5223` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.719` n `146` status `ready` deltaP `2.994` edge `0.0001` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.4427` n `146` status `ready` deltaP `-7.4695` edge `-0.01` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5882` n `146` status `ready` deltaP `-9.1399` edge `-0.0205` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7356` n `146` status `ready` deltaP `1.6037` edge `-0.0031` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2276` n `146` status `ready` deltaP `-15.4229` edge `-0.0119` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.3344` n `146` status `ready` deltaP `-4.2408` edge `-0.0034` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4114` n `146` status `ready` deltaP `-9.8249` edge `0.0012` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.8724` n `146` status `ready` deltaP `-5.0119` edge `-0.0334` maxDD `-9.4709`
- `news_risk_high->index_24h` score `-2.9425` n `146` status `ready` deltaP `-12.3382` edge `-0.0108` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.6943` n `146` status `ready` deltaP `-13.0847` edge `0.0148` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.7423` n `146` status `ready` deltaP `-12.6357` edge `-0.0738` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.2524` n `146` status `ready` deltaP `-9.658` edge `-0.0547` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-7.6474` n `146` status `ready` deltaP `-10.6188` edge `-0.2083` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.0834` n `146` status `ready` deltaP `-15.4015` edge `0.1718` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.1987` n `146` status `ready` deltaP `2.6708` edge `-0.0316` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-14.3388` n `146` status `ready` deltaP `9.8198` edge `0.19` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-16.0831` n `146` status `ready` deltaP `1.8337` edge `-0.3747` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
