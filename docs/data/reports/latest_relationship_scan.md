# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T01:22:27.942306+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.004` n `146` status `ready` deltaP `4.1033` edge `0.2368` maxDD `-14.0916`
- `news_risk_high->crypto_alt_24h` score `-0.2339` n `126` status `ready` deltaP `21.2301` edge `0.779` maxDD `-65.3749`
- `news_risk_high->crypto_alt_1h` score `-0.4924` n `146` status `ready` deltaP `1.2837` edge `0.0511` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5883` n `146` status `ready` deltaP `-0.4265` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8703` n `126` status `ready` deltaP `12.5744` edge `0.1302` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9323` n `146` status `ready` deltaP `0.8982` edge `-0.0037` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2411` n `146` status `ready` deltaP `-3.3537` edge `-0.0116` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3273` n `146` status `ready` deltaP `-5.5471` edge `-0.011` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.0836` n `146` status `ready` deltaP `-3.2743` edge `-0.0152` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.246` n `126` status `ready` deltaP `-3.8195` edge `0.0217` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.3349` n `146` status `ready` deltaP `-8.4776` edge `-0.0014` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.5441` n `126` status `ready` deltaP `-20.6102` edge `-0.0179` maxDD `-2.336`
- `news_risk_high->equity_24h` score `-2.5871` n `126` status `ready` deltaP `16.369` edge `0.5687` maxDD `-67.0937`
- `news_risk_high->equity_1h` score `-2.64` n `146` status `ready` deltaP `-6.1869` edge `-0.0296` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2283` n `146` status `ready` deltaP `-8.1556` edge `-0.0421` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.812` n `146` status `ready` deltaP `-12.1701` edge `-0.0011` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.9009` n `146` status `ready` deltaP `-7.7577` edge `-0.0362` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.066` n `146` status `ready` deltaP `-14.3836` edge `-0.091` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-9.3768` n `126` status `ready` deltaP `-14.7569` edge `-0.002` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-11.5151` n `126` status `ready` deltaP `-26.3144` edge `-0.0953` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
