# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T10:07:34.091320+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.1648` n `146` status `ready` deltaP `8.0668` edge `0.231` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4324` n `146` status `ready` deltaP `2.4813` edge `0.0508` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7355` n `146` status `ready` deltaP `-3.1211` edge `-0.0034` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8532` n `146` status `ready` deltaP `1.6467` edge `-0.0021` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3515` n `146` status `ready` deltaP `-5.6968` edge `-0.0131` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4701` n `146` status `ready` deltaP `-7.622` edge `-0.0125` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.7979` n `146` status `ready` deltaP `0.509` edge `0.0503` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.8319` n `146` status `ready` deltaP `0.2318` edge `-0.0063` maxDD `-4.0745`
- `news_risk_high->metal_24h` score `-2.0591` n `146` status `ready` deltaP `8.9992` edge `0.1266` maxDD `-16.6552`
- `news_risk_high->fx_24h` score `-2.3602` n `146` status `ready` deltaP `-17.8534` edge `-0.0127` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4163` n `146` status `ready` deltaP `-9.5255` edge `-0.0012` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.5963` n `146` status `ready` deltaP `-5.5881` edge `-0.028` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.0773` n `146` status `ready` deltaP `-7.1077` edge `-0.0365` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8386` n `146` status `ready` deltaP `-12.3225` edge `-0.0023` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.6562` n `146` status `ready` deltaP `-4.0991` edge `-0.0402` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.6543` n `146` status `ready` deltaP `-11.4873` edge `-0.076` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-8.0068` n `146` status `ready` deltaP `17.6323` edge `0.5554` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-10.2087` n `146` status `ready` deltaP `15.2017` edge `0.4983` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.2566` n `146` status `ready` deltaP `-0.6828` edge `-0.0974` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2955` n `146` status `ready` deltaP `-20.7834` edge `-0.06` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
