# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T04:07:27.004936+00:00`
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

- `news_risk_high->crypto_alt_24h` score `0.6899` n `126` status `ready` deltaP `23.1399` edge `0.8847` maxDD `-65.3749`
- `news_risk_high->crypto_alt_4h` score `0.1224` n `146` status `ready` deltaP `4.8655` edge `0.2469` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4511` n `146` status `ready` deltaP `1.7328` edge `0.0534` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.579` n `146` status `ready` deltaP `-0.2768` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8061` n `126` status `ready` deltaP `13.2689` edge `0.1338` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9323` n `146` status `ready` deltaP `0.8982` edge `-0.0037` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2262` n `146` status `ready` deltaP `-3.2012` edge `-0.0107` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2915` n `146` status `ready` deltaP `-5.098` edge `-0.0094` maxDD `-3.1082`
- `news_risk_high->equity_24h` score `-1.6126` n `126` status `ready` deltaP `18.2788` edge `0.6809` maxDD `-67.0937`
- `news_risk_high->index_24h` score `-2.0477` n `126` status `ready` deltaP `-1.9098` edge `0.0344` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.1587` n `146` status `ready` deltaP `-4.4938` edge `-0.0167` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3876` n `146` status `ready` deltaP `-9.0764` edge `-0.0018` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4912` n `126` status `ready` deltaP `-19.7421` edge `-0.0169` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.7062` n `146` status `ready` deltaP `-6.9354` edge `-0.0331` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1935` n `146` status `ready` deltaP `-7.8562` edge `-0.0412` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7976` n `146` status `ready` deltaP `-12.1701` edge `0.0001` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.9165` n `146` status `ready` deltaP `-7.7577` edge `-0.0375` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.1106` n `146` status `ready` deltaP `-14.536` edge `-0.0937` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-8.2928` n `126` status `ready` deltaP `-12.8472` edge `0.0756` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-11.1477` n `126` status `ready` deltaP `-24.7519` edge `-0.0751` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
