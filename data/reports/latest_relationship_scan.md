# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T02:07:36.163161+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4411`

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

- `news_risk_high->crypto_alt_4h` score `0.5501` n `146` status `ready` deltaP `8.9814` edge `0.2743` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.2952` n `146` status `ready` deltaP `3.2298` edge `0.0634` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6739` n `146` status `ready` deltaP `-2.0732` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7777` n `146` status `ready` deltaP `2.2455` edge `0.0002` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.205` n `146` status `ready` deltaP `-3.7507` edge `-0.0073` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.3644` n `146` status `ready` deltaP `12.2979` edge `0.1625` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.4654` n `146` status `ready` deltaP `-7.622` edge `-0.0119` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.7096` n `146` status `ready` deltaP `2.0715` edge `0.0512` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.8834` n `146` status `ready` deltaP `-0.8353` edge `-0.0058` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2569` n `146` status `ready` deltaP `-16.8117` edge `-0.0064` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.5061` n `146` status `ready` deltaP `-10.5734` edge `-0.0017` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.523` n `146` status `ready` deltaP `-5.8875` edge `-0.0166` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-2.9837` n `146` status `ready` deltaP `-6.958` edge `-0.0297` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.9961` n `146` status `ready` deltaP `-13.5421` edge `-0.0073` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.3808` n `146` status `ready` deltaP `-3.6418` edge `-0.0203` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-6.0296` n `146` status `ready` deltaP `22.1462` edge `0.7788` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.4019` n `146` status `ready` deltaP `-11.1824` edge `-0.057` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.3275` n `146` status `ready` deltaP `19.0212` edge `0.6296` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.0766` n `146` status `ready` deltaP `-0.6828` edge `-0.0824` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.3139` n `146` status `ready` deltaP `-20.2626` edge `-0.065` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
