# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T09:22:30.873459+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4040`

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

- `news_risk_high->crypto_alt_4h` score `0.2619` n `146` status `ready` deltaP `8.5241` edge `0.2404` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4363` n `146` status `ready` deltaP `2.4813` edge `0.0503` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7098` n `146` status `ready` deltaP `-2.672` edge `-0.0031` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8508` n `146` status `ready` deltaP `1.6467` edge `-0.0019` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3226` n `146` status `ready` deltaP `-5.2477` edge `-0.0124` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4685` n `146` status `ready` deltaP `-7.622` edge `-0.0123` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.7901` n `146` status `ready` deltaP `0.509` edge `0.0513` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.8161` n `146` status `ready` deltaP `0.3842` edge `-0.0053` maxDD `-4.0745`
- `news_risk_high->metal_24h` score `-1.9191` n `146` status `ready` deltaP `9.5201` edge `0.1348` maxDD `-16.6552`
- `news_risk_high->fx_24h` score `-2.3547` n `146` status `ready` deltaP `-17.8534` edge `-0.012` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.463` n `146` status `ready` deltaP `-9.9746` edge `-0.0021` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.5932` n `146` status `ready` deltaP `-5.5881` edge `-0.0276` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.0928` n `146` status `ready` deltaP `-7.2574` edge `-0.0368` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.864` n `146` status `ready` deltaP `-12.475` edge `-0.0034` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.6188` n `146` status `ready` deltaP `-3.9467` edge `-0.0381` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.5097` n `146` status `ready` deltaP `-11.0299` edge `-0.067` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-7.7683` n `146` status `ready` deltaP `18.1531` edge `0.5825` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-9.9354` n `146` status `ready` deltaP `15.7226` edge `0.5176` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.1133` n `146` status `ready` deltaP `-0.2255` edge `-0.0885` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.3123` n `146` status `ready` deltaP `-20.7834` edge `-0.0614` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
