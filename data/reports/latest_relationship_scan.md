# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T13:52:29.180251+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3791`

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

- `news_risk_high->crypto_alt_4h` score `0.1953` n `146` status `ready` deltaP `8.0668` edge `0.2349` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.438` n `146` status `ready` deltaP `3.5292` edge `0.0431` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.716` n `146` status `ready` deltaP `-2.8217` edge `-0.0029` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7681` n `146` status `ready` deltaP `2.5449` edge `-0.001` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.4466` n `146` status `ready` deltaP `-7.4695` edge `-0.0105` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.589` n `146` status `ready` deltaP `-9.1399` edge `-0.0206` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7608` n `146` status `ready` deltaP `1.2989` edge `-0.0043` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2366` n `146` status `ready` deltaP `-15.5965` edge `-0.0119` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.3743` n `146` status `ready` deltaP `-9.5255` edge `0.0023` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.4381` n `146` status `ready` deltaP `-4.6899` edge `-0.0137` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.9456` n `146` status `ready` deltaP `-12.3382` edge `-0.0112` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.0295` n `146` status `ready` deltaP `-5.6107` edge `-0.0425` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.6907` n `146` status `ready` deltaP `-13.0847` edge `0.0151` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.7023` n `146` status `ready` deltaP `-12.3309` edge `-0.0725` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.4763` n `146` status `ready` deltaP `-10.2677` edge `-0.0693` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-7.4526` n `146` status `ready` deltaP `-9.9244` edge `-0.1967` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.2373` n `146` status `ready` deltaP `-16.0959` edge `0.1636` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.3753` n `146` status `ready` deltaP `2.5184` edge `-0.0453` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-14.3076` n `146` status `ready` deltaP `9.8198` edge `0.1926` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.8428` n `146` status `ready` deltaP `2.1809` edge `-0.3462` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
