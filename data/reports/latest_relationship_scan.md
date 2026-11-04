# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T09:37:29.238727+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.2306` n `146` status `ready` deltaP `8.3716` edge `0.2374` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4239` n `146` status `ready` deltaP `2.631` edge `0.0509` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7191` n `146` status `ready` deltaP `-2.8217` edge `-0.0033` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8508` n `146` status `ready` deltaP `1.6467` edge `-0.0019` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3328` n `146` status `ready` deltaP `-5.3974` edge `-0.0127` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4693` n `146` status `ready` deltaP `-7.622` edge `-0.0124` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.7932` n `146` status `ready` deltaP `0.509` edge `0.0509` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.8185` n `146` status `ready` deltaP `0.3842` edge `-0.0056` maxDD `-4.0745`
- `news_risk_high->metal_24h` score `-1.9666` n `146` status `ready` deltaP `9.3465` edge `0.132` maxDD `-16.6552`
- `news_risk_high->fx_24h` score `-2.3563` n `146` status `ready` deltaP `-17.8534` edge `-0.0122` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4486` n `146` status `ready` deltaP `-9.8249` edge `-0.0019` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.5917` n `146` status `ready` deltaP `-5.5881` edge `-0.0274` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.0761` n `146` status `ready` deltaP `-7.1077` edge `-0.0364` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8604` n `146` status `ready` deltaP `-12.475` edge `-0.0031` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.643` n `146` status `ready` deltaP `-4.0991` edge `-0.0391` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.5531` n `146` status `ready` deltaP `-11.1824` edge `-0.0696` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-7.8483` n `146` status `ready` deltaP `17.9795` edge `0.5734` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-10.0273` n `146` status `ready` deltaP `15.5489` edge `0.5111` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.1639` n `146` status `ready` deltaP `-0.378` edge `-0.0917` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.3039` n `146` status `ready` deltaP `-20.7834` edge `-0.0607` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
