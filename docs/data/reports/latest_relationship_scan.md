# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T16:22:33.664652+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4951`

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

- `news_risk_high->crypto_alt_4h` score `-0.1236` n `146` status `ready` deltaP `4.5607` edge `0.2174` maxDD `-14.0916`
- `news_risk_high->fx_1h` score `-0.5183` n `146` status `ready` deltaP `0.9208` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->crypto_alt_1h` score `-0.5244` n `146` status `ready` deltaP `1.4334` edge `0.046` maxDD `-5.8225`
- `news_risk_high->metal_24h` score `-0.8562` n `126` status `ready` deltaP `12.5744` edge `0.132` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0784` n `146` status `ready` deltaP `-0.5988` edge `-0.0059` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1674` n `146` status `ready` deltaP `-1.9817` edge `-0.0113` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3351` n `146` status `ready` deltaP `-5.6968` edge `-0.011` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-2.0944` n `126` status `ready` deltaP `-14.7074` edge `0.0004` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2458` n `146` status `ready` deltaP `-5.1036` edge `-0.0238` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2654` n `146` status `ready` deltaP `-7.7291` edge `-0.0006` maxDD `-3.2657`
- `news_risk_high->crypto_alt_24h` score `-2.3755` n `126` status `ready` deltaP `14.9801` edge `0.5461` maxDD `-65.3749`
- `news_risk_high->index_24h` score `-2.5546` n `126` status `ready` deltaP `-6.4237` edge `-0.0005` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.8255` n `146` status `ready` deltaP `-7.2348` edge `-0.0464` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2871` n `146` status `ready` deltaP `-8.3053` edge `-0.046` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8008` n `146` status `ready` deltaP `-10.9506` edge `-0.0083` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.7087` n `146` status `ready` deltaP `-5.776` edge `-0.0334` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-4.802` n `126` status `ready` deltaP `10.119` edge `0.3264` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.2992` n `146` status `ready` deltaP `-14.6885` edge `-0.1084` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-11.894` n `126` status `ready` deltaP `-21.0069` edge `-0.1701` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-12.2838` n `126` status `ready` deltaP `-26.4881` edge `-0.1582` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
