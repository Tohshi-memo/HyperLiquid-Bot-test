# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T09:52:32.916254+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3582`

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

- `news_risk_high->crypto_alt_4h` score `-0.3343` n `146` status `ready` deltaP `6.2375` edge `0.1792` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6336` n `146` status `ready` deltaP `2.0322` edge `0.028` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7074` n `146` status `ready` deltaP `-2.672` edge `-0.0028` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7274` n `146` status `ready` deltaP `2.994` edge `-0.0006` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.5066` n `146` status `ready` deltaP `-8.3841` edge `-0.0121` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5625` n `146` status `ready` deltaP `-8.8405` edge `-0.0192` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7292` n `146` status `ready` deltaP `1.7562` edge `-0.0033` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1862` n `146` status `ready` deltaP `-7.8788` edge `0.007` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.3796` n `146` status `ready` deltaP `-17.9718` edge `-0.0144` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5713` n `146` status `ready` deltaP `-6.0372` edge `-0.0218` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.8928` n `146` status `ready` deltaP `-12.1628` edge `-0.0056` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.333` n `146` status `ready` deltaP `-11.103` edge `0.0317` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.394` n `146` status `ready` deltaP `-7.4071` edge `-0.0609` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.5164` n `146` status `ready` deltaP `-10.5016` edge `-0.0692` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-6.8073` n `146` status `ready` deltaP `-7.2878` edge `-0.1605` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.3087` n `146` status `ready` deltaP `-11.7921` edge `-0.1285` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-9.8815` n `146` status `ready` deltaP `-18.7776` edge `0.1278` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.7273` n `146` status `ready` deltaP `1.2989` edge `-0.0665` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.8738` n `146` status `ready` deltaP `9.9778` edge `0.2277` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-14.8797` n `146` status `ready` deltaP `4.4414` edge `-0.2378` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
