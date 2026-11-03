# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T08:37:29.541962+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4490`

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

- `news_risk_high->crypto_alt_4h` score `0.2537` n `146` status `ready` deltaP `6.0851` edge `0.2556` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4152` n `146` status `ready` deltaP `2.1819` edge `0.055` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6288` n `146` status `ready` deltaP `-1.175` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8927` n `146` status `ready` deltaP `1.3473` edge `-0.0034` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2556` n `146` status `ready` deltaP `-4.4992` edge `-0.0088` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.2697` n `146` status `ready` deltaP `-3.9634` edge `-0.0112` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.7724` n `142` status `ready` deltaP `9.5975` edge `0.118` maxDD `-14.3748`
- `news_risk_high->index_4h` score `-2.0293` n `146` status `ready` deltaP `-2.6646` edge `-0.0123` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.2579` n `142` status `ready` deltaP `-3.7926` edge `0.02` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.382` n `142` status `ready` deltaP `-17.2071` edge `-0.0198` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4055` n `146` status `ready` deltaP `-9.2261` edge `-0.0023` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6898` n `146` status `ready` deltaP `-6.7857` edge `-0.032` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2343` n `146` status `ready` deltaP `-8.3053` edge `-0.0416` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.9839` n `146` status `ready` deltaP `-13.3896` edge `-0.0073` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.6927` n `146` status `ready` deltaP `-6.3857` edge `-0.028` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.5873` n `142` status `ready` deltaP `19.0215` edge `0.7296` maxDD `-109.8188`
- `news_risk_high->crypto_major_4h` score `-6.9428` n `146` status `ready` deltaP `-13.7738` edge `-0.0848` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.5576` n `142` status `ready` deltaP `14.1604` edge `0.4518` maxDD `-87.0803`
- `news_risk_high->equity_4h` score `-11.3408` n `146` status `ready` deltaP `-0.8353` edge `-0.1034` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.8869` n `142` status `ready` deltaP `-24.1784` edge `-0.0981` maxDD `-42.8365`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
