# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T07:52:30.749092+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4510`

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

- `news_risk_high->crypto_alt_4h` score `0.2191` n `146` status `ready` deltaP `5.7802` edge `0.2532` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4028` n `146` status `ready` deltaP `2.3316` edge `0.0556` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6031` n `146` status `ready` deltaP `-0.7259` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8927` n `146` status `ready` deltaP `1.3473` edge `-0.0034` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2594` n `146` status `ready` deltaP `-3.811` edge `-0.0109` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2743` n `146` status `ready` deltaP `-4.7986` edge `-0.0092` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.6367` n `139` status `ready` deltaP `10.2319` edge `0.121` maxDD `-14.0483`
- `news_risk_high->index_4h` score `-2.0347` n `146` status `ready` deltaP `-2.6646` edge `-0.013` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.2298` n `139` status `ready` deltaP `-3.4622` edge `0.0214` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.39` n `146` status `ready` deltaP `-9.0764` edge `-0.002` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4373` n `139` status `ready` deltaP `-18.3166` edge `-0.0195` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6883` n `146` status `ready` deltaP `-6.7857` edge `-0.0318` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2187` n `146` status `ready` deltaP `-8.1556` edge `-0.0413` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.9089` n `146` status `ready` deltaP `-12.9323` edge `-0.0041` maxDD `-9.5011`
- `news_risk_high->crypto_alt_24h` score `-4.4874` n `139` status `ready` deltaP `19.7317` edge `0.7546` maxDD `-101.9162`
- `news_risk_high->metal_4h` score `-4.7533` n `146` status `ready` deltaP `-6.843` edge `-0.03` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-6.2077` n `139` status `ready` deltaP `14.8706` edge `0.4863` maxDD `-74.5529`
- `news_risk_high->crypto_major_4h` score `-6.9886` n `146` status `ready` deltaP `-13.9263` edge `-0.0876` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-11.4422` n `146` status `ready` deltaP `-1.2926` edge `-0.1088` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.6795` n `139` status `ready` deltaP `-23.9808` edge `-0.0967` maxDD `-41.6709`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
