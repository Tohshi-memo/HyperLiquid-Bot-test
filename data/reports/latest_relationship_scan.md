# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T18:37:31.687638+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.0807` n `146` status `ready` deltaP `4.5607` edge `0.2229` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4667` n `146` status `ready` deltaP `1.7328` edge `0.0514` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.558` n `146` status `ready` deltaP `0.1723` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.889` n `126` status `ready` deltaP `12.5744` edge `0.1278` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0353` n `146` status `ready` deltaP `-0.1497` edge `-0.0053` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2347` n `146` status `ready` deltaP `-3.2012` edge `-0.0118` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3444` n `146` status `ready` deltaP `-5.8465` edge `-0.0112` maxDD `-3.1082`
- `news_risk_high->crypto_alt_24h` score `-1.9066` n `126` status `ready` deltaP `16.5426` edge `0.5958` maxDD `-65.3749`
- `news_risk_high->commodity_1h` score `-2.2127` n `146` status `ready` deltaP `-7.28` edge `0.0008` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.217` n `126` status `ready` deltaP `-16.2699` edge `-0.0049` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2601` n `146` status `ready` deltaP `-5.4085` edge `-0.0236` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.5312` n `126` status `ready` deltaP `-6.4237` edge `0.0025` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.7296` n `146` status `ready` deltaP `-6.636` edge `-0.0381` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1803` n `146` status `ready` deltaP `-7.8562` edge `-0.0401` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.73` n `146` status `ready` deltaP `-10.9506` edge `-0.0024` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-4.4018` n `126` status `ready` deltaP `11.6815` edge `0.3673` maxDD `-67.0937`
- `news_risk_high->metal_4h` score `-4.8615` n `146` status `ready` deltaP `-6.9955` edge `-0.038` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.244` n `146` status `ready` deltaP `-14.6885` edge `-0.1038` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-11.343` n `126` status `ready` deltaP `-19.4444` edge `-0.1346` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-12.1554` n `126` status `ready` deltaP `-26.4881` edge `-0.1475` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
