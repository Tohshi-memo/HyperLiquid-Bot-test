# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T02:52:27.162249+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.6024` n `146` status `ready` deltaP `8.9814` edge `0.281` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.2687` n `146` status `ready` deltaP `3.5292` edge `0.0648` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6576` n `146` status `ready` deltaP `-1.7738` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7321` n `146` status `ready` deltaP `2.6946` edge `0.001` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1887` n `146` status `ready` deltaP `-3.601` edge `-0.0062` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.3428` n `146` status `ready` deltaP `12.2979` edge `0.1643` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.4654` n `146` status `ready` deltaP `-7.622` edge `-0.0119` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.7003` n `146` status `ready` deltaP `2.0715` edge `0.0524` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.8386` n `146` status `ready` deltaP `-0.378` edge `-0.0031` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2608` n `146` status `ready` deltaP `-16.8117` edge `-0.0069` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.4653` n `146` status `ready` deltaP `-5.4384` edge `-0.0122` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.481` n `146` status `ready` deltaP `-10.4237` edge `-0.0006` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.9225` n `146` status `ready` deltaP `-6.5089` edge `-0.0276` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.9283` n `146` status `ready` deltaP `-13.0847` edge `-0.0047` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.3796` n `146` status `ready` deltaP `-3.6418` edge `-0.0202` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-6.1475` n `146` status `ready` deltaP `21.7989` edge `0.766` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.2803` n `146` status `ready` deltaP `-10.8775` edge `-0.0489` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.3335` n `146` status `ready` deltaP `19.0212` edge `0.6291` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-10.8493` n `146` status `ready` deltaP `-0.2255` edge `-0.0665` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.3055` n `146` status `ready` deltaP `-20.2626` edge `-0.0643` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
