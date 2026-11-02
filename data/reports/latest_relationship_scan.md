# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T18:22:32.658170+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4954`

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

- `news_risk_high->crypto_alt_4h` score `-0.0947` n `146` status `ready` deltaP `4.5607` edge `0.2211` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4682` n `146` status `ready` deltaP `1.7328` edge `0.0512` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.558` n `146` status `ready` deltaP `0.1723` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8859` n `126` status `ready` deltaP `12.5744` edge `0.1282` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0353` n `146` status `ready` deltaP `-0.1497` edge `-0.0053` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2347` n `146` status `ready` deltaP `-3.2012` edge `-0.0118` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3444` n `146` status `ready` deltaP `-5.8465` edge `-0.0112` maxDD `-3.1082`
- `news_risk_high->crypto_alt_24h` score `-1.9687` n `126` status `ready` deltaP `16.369` edge `0.589` maxDD `-65.3749`
- `news_risk_high->fx_24h` score `-2.2033` n `126` status `ready` deltaP `-16.0963` edge `-0.0043` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.227` n `146` status `ready` deltaP `-7.4297` edge `0.0006` maxDD `-3.2657`
- `news_risk_high->index_4h` score `-2.268` n `146` status `ready` deltaP `-5.5609` edge `-0.0236` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.5336` n `126` status `ready` deltaP `-6.4237` edge `0.0022` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.7343` n `146` status `ready` deltaP `-6.636` edge `-0.0387` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1803` n `146` status `ready` deltaP `-7.8562` edge `-0.0401` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7384` n `146` status `ready` deltaP `-10.9506` edge `-0.0031` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-4.4513` n `126` status `ready` deltaP `11.5079` edge `0.3621` maxDD `-67.0937`
- `news_risk_high->metal_4h` score `-4.8603` n `146` status `ready` deltaP `-6.9955` edge `-0.0379` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.2596` n `146` status `ready` deltaP `-14.6885` edge `-0.1051` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-11.4133` n `126` status `ready` deltaP `-19.618` edge `-0.1393` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-12.1734` n `126` status `ready` deltaP `-26.4881` edge `-0.149` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
