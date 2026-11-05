# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T17:22:29.565739+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4172`

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

- `news_risk_high->crypto_alt_4h` score `0.6607` n `146` status `ready` deltaP `8.7519` edge `0.29` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.1139` n `146` status `ready` deltaP `4.4966` edge `0.0782` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6678` n `146` status `ready` deltaP `3.2138` edge `0.0029` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7094` n `146` status `ready` deltaP `-2.7407` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4689` n `146` status `ready` deltaP `-7.8387` edge `-0.0109` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5727` n `146` status `ready` deltaP `-8.9164` edge `-0.02` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6703` n `146` status `ready` deltaP `1.6743` edge `0.0048` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.156` n `146` status `ready` deltaP `-4.3204` edge `0.02` maxDD `-16.4088`
- `news_risk_high->fx_24h` score `-2.3338` n `146` status `ready` deltaP `-17.0461` edge `-0.0147` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.3923` n `146` status `ready` deltaP `-9.7508` edge `0.0023` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.5586` n `146` status `ready` deltaP `-4.4945` edge `-0.0107` maxDD `-9.4709`
- `news_risk_high->index_24h` score `-2.8732` n `146` status `ready` deltaP `-12.2504` edge `-0.0025` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.7068` n `146` status `ready` deltaP `-13.1659` edge `0.0143` maxDD `-9.5011`
- `news_risk_high->crypto_major_4h` score `-5.6935` n `146` status `ready` deltaP `-9.4369` edge `-0.0096` maxDD `-24.1554`
- `news_risk_high->metal_4h` score `-5.7496` n `146` status `ready` deltaP `-12.8615` edge `-0.0729` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-8.0449` n `146` status `ready` deltaP `-12.2433` edge `-0.2306` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-8.9015` n `146` status `ready` deltaP `-14.4928` edge `0.1809` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.3364` n `146` status `ready` deltaP `2.7397` edge `0.0398` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.8429` n `146` status `ready` deltaP `9.8989` edge `0.2308` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.9457` n `146` status `ready` deltaP `1.9266` edge `-0.3577` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
