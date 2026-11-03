# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T16:37:46.344043+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4374`

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

- `news_risk_high->crypto_alt_4h` score `0.2339` n `146` status `ready` deltaP `6.6948` edge `0.249` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4682` n `146` status `ready` deltaP `1.7328` edge `0.0512` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6716` n `146` status `ready` deltaP `-1.9235` edge `-0.0032` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9107` n `146` status `ready` deltaP `1.0479` edge `-0.0029` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1715` n `146` status `ready` deltaP `-3.1519` edge `-0.007` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4216` n `146` status `ready` deltaP `-6.5549` edge `-0.0134` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.6994` n `146` status `ready` deltaP `11.9506` edge `0.1369` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-1.8364` n `146` status `ready` deltaP `0.6826` edge `0.0442` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.0547` n `146` status `ready` deltaP `-3.2743` edge `-0.0115` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2997` n `146` status `ready` deltaP `-16.4645` edge `-0.0142` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.5086` n `146` status `ready` deltaP `-10.4237` edge `-0.0029` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6968` n `146` status `ready` deltaP `-7.0851` edge `-0.0309` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2367` n `146` status `ready` deltaP `-8.3053` edge `-0.0418` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.1361` n `146` status `ready` deltaP `-15.0664` edge `-0.0088` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.483` n `146` status `ready` deltaP `-4.7089` edge `-0.0217` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.7576` n `146` status `ready` deltaP `22.667` edge `0.8102` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.9188` n `146` status `ready` deltaP `-13.7738` edge `-0.0828` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.2397` n `146` status `ready` deltaP `18.1531` edge `0.6427` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.3772` n `146` status `ready` deltaP `-1.1402` edge `-0.1044` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2935` n `146` status `ready` deltaP `-20.2626` edge `-0.0633` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
