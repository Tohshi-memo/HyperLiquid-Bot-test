# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T03:52:33.747899+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4314`

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

- `news_risk_high->crypto_alt_4h` score `-0.2245` n `146` status `ready` deltaP `6.9997` edge `0.1882` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5955` n `146` status `ready` deltaP `2.9304` edge `0.0269` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6926` n `146` status `ready` deltaP `3.1437` edge `0.0013` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7144` n `146` status `ready` deltaP `-2.8217` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.467` n `146` status `ready` deltaP `-7.622` edge `-0.0121` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5329` n `146` status `ready` deltaP `-8.2417` edge `-0.0194` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6838` n `146` status `ready` deltaP `0.994` edge `0.0076` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.4076` n `146` status `ready` deltaP `-5.7378` edge `-0.0028` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.4241` n `146` status `ready` deltaP `-12.1628` edge `0.0545` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.5169` n `146` status `ready` deltaP `-11.0225` edge `0.0004` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.8142` n `146` status `ready` deltaP `-24.2001` edge `-0.0286` maxDD `-2.336`
- `news_risk_high->crypto_major_1h` score `-2.8819` n `146` status `ready` deltaP `-5.3113` edge `-0.0322` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.9697` n `146` status `ready` deltaP `-15.3713` edge `0.0071` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.7607` n `146` status `ready` deltaP `-12.9406` edge `-0.0733` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-5.851` n `146` status `ready` deltaP `-9.2007` edge `-0.0243` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-9.1736` n `146` status `ready` deltaP `-16.9763` edge `-0.2931` maxDD `-16.6552`
- `news_risk_high->equity_4h` score `-9.6415` n `146` status `ready` deltaP `2.0611` edge `0.0189` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-9.765` n `146` status `ready` deltaP `-15.8364` edge `0.1179` maxDD `-43.7525`
- `news_risk_high->equity_24h` score `-10.401` n `146` status `ready` deltaP `9.9778` edge `0.5171` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-13.1432` n `146` status `ready` deltaP `5.8255` edge `-0.0244` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
