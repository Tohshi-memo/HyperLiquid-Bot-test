# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T10:52:27.941766+00:00`
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

- `news_risk_high->crypto_alt_24h` score `2.253` n `113` status `ready` deltaP `20.987` edge `0.7042` maxDD `-38.0878`
- `news_risk_high->crypto_alt_4h` score `0.6756` n `135` status `ready` deltaP `7.6705` edge `0.24` maxDD `-11.0288`
- `news_risk_high->fx_1h` score `-0.5183` n `146` status `ready` deltaP `0.9208` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->crypto_alt_1h` score `-0.5462` n `146` status `ready` deltaP `1.2837` edge `0.0442` maxDD `-5.8225`
- `news_risk_high->metal_24h` score `-0.8261` n `113` status `ready` deltaP `13.6492` edge `0.1287` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.1275` n `146` status `ready` deltaP `-1.0479` edge `-0.007` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2899` n `146` status `ready` deltaP `-5.098` edge `-0.0092` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.3052` n `135` status `ready` deltaP `-4.4219` edge `-0.0127` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-2.2933` n `135` status `ready` deltaP `-5.358` edge `-0.0282` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3238` n `113` status `ready` deltaP `-16.914` edge `-0.0143` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4044` n `146` status `ready` deltaP `-8.777` edge `-0.0052` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.9822` n `146` status `ready` deltaP `-8.133` edge `-0.0605` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-3.1491` n `113` status `ready` deltaP `-12.815` edge `-0.0341` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.3578` n `146` status `ready` deltaP `-8.9041` edge `-0.0479` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.978` n `135` status `ready` deltaP `-13.313` edge `-0.0175` maxDD `-8.6862`
- `news_risk_high->metal_4h` score `-4.4497` n `135` status `ready` deltaP `-3.1831` edge `-0.0291` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-6.0531` n `113` status `ready` deltaP `4.7951` edge `0.2015` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.3212` n `135` status `ready` deltaP `-14.6183` edge `-0.1107` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-8.5475` n `135` status `ready` deltaP `-4.1599` edge `-0.232` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-10.7975` n `113` status `ready` deltaP `-25.3012` edge `-0.1375` maxDD `-25.1561`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
