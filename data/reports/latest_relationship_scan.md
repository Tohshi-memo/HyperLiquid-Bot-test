# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T15:22:52.707276+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4088`

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

- `news_risk_high->crypto_alt_4h` score `0.4017` n `146` status `ready` deltaP `8.6765` edge `0.2573` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.2423` n `146` status `ready` deltaP `4.2777` edge `0.0632` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6794` n `146` status `ready` deltaP `3.2934` edge `0.0014` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.6965` n `146` status `ready` deltaP `-2.5223` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4427` n `146` status `ready` deltaP `-7.4695` edge `-0.01` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5843` n `146` status `ready` deltaP `-9.1399` edge `-0.02` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7254` n `146` status `ready` deltaP `1.6037` edge `-0.0018` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.212` n `146` status `ready` deltaP `-3.9414` edge `0.0103` maxDD `-16.4088`
- `news_risk_high->fx_24h` score `-2.248` n `146` status `ready` deltaP `-15.7701` edge `-0.0122` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4246` n `146` status `ready` deltaP `-9.9746` edge `0.0011` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.7236` n `146` status `ready` deltaP `-4.7125` edge `-0.023` maxDD `-9.4709`
- `news_risk_high->index_24h` score `-2.9316` n `146` status `ready` deltaP `-12.3382` edge `-0.0094` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.6979` n `146` status `ready` deltaP `-13.0847` edge `0.0145` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.7557` n `146` status `ready` deltaP `-12.7882` edge `-0.0739` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.1094` n `146` status `ready` deltaP `-9.5056` edge `-0.0438` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-7.7376` n `146` status `ready` deltaP `-10.966` edge `-0.2135` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.004` n `146` status `ready` deltaP `-15.0542` edge `0.1761` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.0355` n `146` status `ready` deltaP `2.6708` edge `-0.018` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-14.2392` n `146` status `ready` deltaP `9.8198` edge `0.1983` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-16.0886` n `146` status `ready` deltaP `1.8337` edge `-0.3754` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
