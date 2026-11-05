# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T22:07:34.380598+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4268`

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

- `news_risk_high->crypto_alt_4h` score `-0.2641` n `146` status `ready` deltaP `7.1521` edge `0.1821` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4676` n `146` status `ready` deltaP `3.0801` edge `0.0423` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6506` n `146` status `ready` deltaP `3.2934` edge `0.0038` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7129` n `146` status `ready` deltaP `-2.8217` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4267` n `146` status `ready` deltaP `-7.0122` edge `-0.011` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5166` n `146` status `ready` deltaP `-8.092` edge `-0.0183` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6405` n `146` status `ready` deltaP `1.4513` edge `0.0101` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.2937` n `146` status `ready` deltaP `-5.2887` edge `0.0088` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4582` n `146` status `ready` deltaP `-10.4237` edge `0.0013` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.5534` n `146` status `ready` deltaP `-20.339` edge `-0.0209` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.7063` n `146` status `ready` deltaP `-12.2504` edge `0.0189` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-2.8267` n `146` status `ready` deltaP `-5.3113` edge `-0.0276` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8713` n `146` status `ready` deltaP `-14.4567` edge `0.0092` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.6809` n `146` status `ready` deltaP `-12.4833` edge `-0.0697` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.2225` n `146` status `ready` deltaP `-9.8104` edge `-0.0512` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-8.7764` n `146` status `ready` deltaP `-15.5362` edge `-0.2696` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.0899` n `146` status `ready` deltaP `-14.4928` edge `0.1652` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.4361` n `146` status `ready` deltaP `2.2135` edge `0.035` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-12.8073` n `146` status `ready` deltaP `9.8989` edge `0.3171` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.7518` n `146` status `ready` deltaP `2.1` edge `-0.334` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
