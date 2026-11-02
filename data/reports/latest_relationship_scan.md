# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T23:52:28.959545+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4836`

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

- `news_risk_high->crypto_alt_4h` score `0.135` n `146` status `ready` deltaP `5.018` edge `0.2475` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4339` n `146` status `ready` deltaP `1.8825` edge `0.0546` maxDD `-5.8225`
- `news_risk_high->crypto_alt_24h` score `-0.579` n `126` status `ready` deltaP `20.1885` edge `0.7417` maxDD `-65.3749`
- `news_risk_high->fx_1h` score `-0.5977` n `146` status `ready` deltaP `-0.5762` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8804` n `126` status `ready` deltaP `12.5744` edge `0.1289` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9191` n `146` status `ready` deltaP `1.0479` edge `-0.0036` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2593` n `146` status `ready` deltaP `-3.6585` edge `-0.0119` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.307` n `146` status `ready` deltaP `-5.2477` edge `-0.0104` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.0543` n `146` status `ready` deltaP `-2.817` edge `-0.0145` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3001` n `146` status `ready` deltaP `-8.1782` edge `-0.0005` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.3369` n `126` status `ready` deltaP `-4.8612` edge `0.017` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4963` n `126` status `ready` deltaP `-19.9157` edge `-0.0164` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6049` n `146` status `ready` deltaP `-5.7378` edge `-0.0281` maxDD `-16.4088`
- `news_risk_high->equity_24h` score `-3.0001` n `126` status `ready` deltaP `15.3274` edge `0.5227` maxDD `-67.0937`
- `news_risk_high->crypto_major_1h` score `-3.1336` n `146` status `ready` deltaP `-7.5568` edge `-0.0382` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7488` n `146` status `ready` deltaP `-11.5604` edge `0.0001` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8133` n `146` status `ready` deltaP `-6.843` edge `-0.035` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.8656` n `146` status `ready` deltaP `-13.469` edge `-0.0804` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-9.7637` n `126` status `ready` deltaP `-15.7986` edge `-0.0273` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-11.3654` n `146` status `ready` deltaP `-1.2926` edge `-0.1024` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
