# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T01:07:25.024937+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4319`

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

- `news_risk_high->crypto_alt_4h` score `-0.439` n `146` status `ready` deltaP `6.9254` edge `0.1612` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.643` n `146` status `ready` deltaP `2.631` edge `0.0228` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6878` n `146` status `ready` deltaP `2.994` edge `0.0027` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.6965` n `146` status `ready` deltaP `-2.5223` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.415` n `146` status `ready` deltaP `-6.7732` edge `-0.0111` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5407` n `146` status `ready` deltaP `-8.3914` edge `-0.0194` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.648` n `146` status `ready` deltaP `1.2177` edge `0.0107` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.3834` n `146` status `ready` deltaP `-5.8875` edge `0.0013` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4474` n `146` status `ready` deltaP `-10.274` edge `0.0012` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.5395` n `146` status `ready` deltaP `-12.1628` edge `0.0397` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.688` n `146` status `ready` deltaP `-22.297` edge `-0.0251` maxDD `-2.336`
- `news_risk_high->crypto_major_1h` score `-3.0594` n `146` status `ready` deltaP `-6.0598` edge `-0.042` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.868` n `146` status `ready` deltaP `-14.5358` edge `0.01` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.7242` n `146` status `ready` deltaP `-12.7093` edge `-0.0718` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.2863` n `146` status `ready` deltaP `-9.4369` edge `-0.059` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-9.1064` n `146` status `ready` deltaP `-16.9763` edge `-0.2875` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.3297` n `146` status `ready` deltaP `-14.6253` edge `0.1461` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.4369` n `146` status `ready` deltaP `1.9787` edge `0.0365` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.3946` n `146` status `ready` deltaP `9.9778` edge `0.4343` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-14.5845` n `146` status `ready` deltaP `3.9224` edge `-0.1965` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
