# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T13:22:28.732745+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4300`

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

- `news_risk_high->crypto_alt_4h` score `0.2516` n `146` status `ready` deltaP `6.3899` edge `0.2533` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5501` n `146` status `ready` deltaP `0.9843` edge `0.0457` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6374` n `146` status `ready` deltaP `-1.3247` edge `-0.0028` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9299` n `146` status `ready` deltaP `0.8982` edge `-0.0035` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2284` n `146` status `ready` deltaP `-4.0501` edge `-0.0083` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.3456` n `146` status `ready` deltaP `-5.1829` edge `-0.0128` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.8335` n `146` status `ready` deltaP `11.4298` edge `0.1292` maxDD `-16.6552`
- `news_risk_high->index_4h` score `-2.0152` n `146` status `ready` deltaP `-2.6646` edge `-0.0105` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.0271` n `146` status `ready` deltaP `-1.5744` edge `0.0348` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.3474` n `146` status `ready` deltaP `-16.8117` edge `-0.018` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4942` n `146` status `ready` deltaP `-10.1243` edge `-0.0037` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6992` n `146` status `ready` deltaP `-6.9354` edge `-0.0322` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.3254` n `146` status `ready` deltaP `-8.9041` edge `-0.0452` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.3049` n `146` status `ready` deltaP `-15.6762` edge `-0.0188` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.3936` n `146` status `ready` deltaP `-4.2516` edge `-0.0173` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-6.0066` n `146` status `ready` deltaP `20.7573` edge `0.791` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.8478` n `146` status `ready` deltaP `-13.6214` edge `-0.0779` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-9.2556` n `146` status `ready` deltaP `15.8962` edge `0.5779` maxDD `-102.7472`
- `news_risk_high->equity_4h` score `-11.1966` n `146` status `ready` deltaP `-0.6828` edge `-0.0924` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.7332` n `146` status `ready` deltaP `-22.5195` edge `-0.0849` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
