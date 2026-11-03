# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T00:22:28.956445+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.0872` n `146` status `ready` deltaP `4.7131` edge `0.2434` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4612` n `146` status `ready` deltaP `1.5831` edge `0.0531` maxDD `-5.8225`
- `news_risk_high->crypto_alt_24h` score `-0.472` n `126` status `ready` deltaP `20.5357` edge `0.7531` maxDD `-65.3749`
- `news_risk_high->fx_1h` score `-0.5891` n `146` status `ready` deltaP `-0.4265` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8773` n `126` status `ready` deltaP `12.5744` edge `0.1293` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9191` n `146` status `ready` deltaP `1.0479` edge `-0.0036` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2427` n `146` status `ready` deltaP `-3.3537` edge `-0.0118` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3265` n `146` status `ready` deltaP `-5.5471` edge `-0.0109` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.0551` n `146` status `ready` deltaP `-2.817` edge `-0.0146` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2881` n `146` status `ready` deltaP `-8.0285` edge `-0.0005` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.3095` n `126` status `ready` deltaP `-4.5139` edge `0.0182` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.5206` n `126` status `ready` deltaP `-20.2629` edge `-0.0172` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6158` n `146` status `ready` deltaP `-5.8875` edge `-0.0285` maxDD `-16.4088`
- `news_risk_high->equity_24h` score `-2.8744` n `126` status `ready` deltaP `15.6746` edge `0.5365` maxDD `-67.0937`
- `news_risk_high->crypto_major_1h` score `-3.1408` n `146` status `ready` deltaP `-7.5568` edge `-0.0388` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.75` n `146` status `ready` deltaP `-11.5604` edge `0.0` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8413` n `146` status `ready` deltaP `-7.1479` edge `-0.0353` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.9224` n `146` status `ready` deltaP `-13.7738` edge `-0.0831` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-9.6363` n `126` status `ready` deltaP `-15.4514` edge `-0.019` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-11.3978` n `146` status `ready` deltaP `-1.2926` edge `-0.1051` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
