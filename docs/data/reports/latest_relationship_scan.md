# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T13:37:28.912441+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.0144` n `146` status `ready` deltaP `5.4753` edge `0.2253` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5485` n `146` status `ready` deltaP `1.134` edge `0.0449` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5509` n `146` status `ready` deltaP `0.322` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8774` n `124` status `ready` deltaP `12.108` edge `0.1324` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0712` n `146` status `ready` deltaP `-0.4491` edge `-0.0063` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1421` n `146` status `ready` deltaP `-1.5244` edge `-0.0111` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2845` n `146` status `ready` deltaP `-4.9483` edge `-0.0095` maxDD `-3.1082`
- `news_risk_high->crypto_alt_24h` score `-1.9491` n `124` status `ready` deltaP `15.149` edge `0.5399` maxDD `-61.262`
- `news_risk_high->fx_24h` score `-2.0188` n `124` status `ready` deltaP `-13.6425` edge `0.003` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2244` n `146` status `ready` deltaP `-4.6463` edge `-0.0241` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3781` n `146` status `ready` deltaP `-8.4776` edge `-0.005` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.648` n `124` status `ready` deltaP `-7.3197` edge `-0.0065` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.9082` n `146` status `ready` deltaP `-7.3845` edge `-0.056` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.3494` n `146` status `ready` deltaP `-8.7544` edge `-0.0482` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.963` n `146` status `ready` deltaP `-12.0177` edge `-0.0147` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.5598` n `146` status `ready` deltaP `-4.7089` edge `-0.0281` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-5.215` n `124` status `ready` deltaP `8.3278` edge `0.2854` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.2796` n `146` status `ready` deltaP `-14.3836` edge `-0.1088` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-12.0206` n `124` status `ready` deltaP `-26.3217` edge `-0.1585` maxDD `-31.0857`
- `news_risk_high->crypto_major_24h` score `-12.0993` n `124` status `ready` deltaP `-22.295` edge `-0.1901` maxDD `-42.2297`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
