# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T11:52:25.506813+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4288`

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

- `news_risk_high->crypto_alt_4h` score `0.3046` n `146` status `ready` deltaP `6.3899` edge `0.2601` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4908` n `146` status `ready` deltaP `1.4334` edge `0.0503` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6374` n `146` status `ready` deltaP `-1.3247` edge `-0.0028` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8879` n `146` status `ready` deltaP `1.3473` edge `-0.003` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2315` n `146` status `ready` deltaP `-4.1998` edge `-0.0077` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.2934` n `146` status `ready` deltaP `-4.2683` edge `-0.0122` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.984` n `146` status `ready` deltaP `10.3881` edge `0.1236` maxDD `-16.6552`
- `news_risk_high->index_4h` score `-2.023` n `146` status `ready` deltaP `-2.6646` edge `-0.0115` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.1281` n `146` status `ready` deltaP `-2.616` edge `0.0288` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.3748` n `146` status `ready` deltaP `-17.159` edge `-0.0192` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.499` n `146` status `ready` deltaP `-9.9746` edge `-0.0051` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6851` n `146` status `ready` deltaP `-6.7857` edge `-0.0314` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2822` n `146` status `ready` deltaP `-8.9041` edge `-0.0416` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.2673` n `146` status `ready` deltaP `-15.3713` edge `-0.0177` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.4202` n `146` status `ready` deltaP `-4.404` edge `-0.0185` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-6.1988` n `146` status `ready` deltaP `19.7156` edge `0.7733` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.8178` n `146` status `ready` deltaP `-13.6214` edge `-0.0754` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-10.0241` n `146` status `ready` deltaP `14.8545` edge `0.5208` maxDD `-102.7472`
- `news_risk_high->equity_4h` score `-11.265` n `146` status `ready` deltaP `-0.6828` edge `-0.0981` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.8934` n `146` status `ready` deltaP `-23.5612` edge `-0.0913` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
