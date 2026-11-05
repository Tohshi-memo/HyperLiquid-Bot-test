# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T21:37:32.030580+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4256`

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

- `news_risk_high->crypto_alt_4h` score `-0.1477` n `146` status `ready` deltaP `7.457` edge `0.195` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4559` n `146` status `ready` deltaP `3.0801` edge `0.0438` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6542` n `146` status `ready` deltaP `3.2934` edge `0.0035` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7129` n `146` status `ready` deltaP `-2.8217` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4441` n `146` status `ready` deltaP `-7.3171` edge `-0.0112` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5353` n `146` status `ready` deltaP `-8.3914` edge `-0.0187` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6413` n `146` status `ready` deltaP `1.4513` edge `0.01` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.2844` n `146` status `ready` deltaP `-5.139` edge `0.009` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4414` n `146` status `ready` deltaP `-10.274` edge `0.0017` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.5307` n `146` status `ready` deltaP `-19.9924` edge `-0.0203` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.7336` n `146` status `ready` deltaP `-12.2504` edge `0.0154` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-2.8363` n `146` status `ready` deltaP `-5.3113` edge `-0.0284` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8385` n `146` status `ready` deltaP `-14.1518` edge `0.0099` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.6785` n `146` status `ready` deltaP `-12.4833` edge `-0.0695` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.1336` n `146` status `ready` deltaP `-9.658` edge `-0.0448` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-8.7066` n `146` status `ready` deltaP `-15.1896` edge `-0.2661` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.0515` n `146` status `ready` deltaP `-14.4928` edge `0.1684` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.3699` n `146` status `ready` deltaP `2.3659` edge `0.0395` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.0281` n `146` status `ready` deltaP `9.8989` edge `0.2987` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.8766` n `146` status `ready` deltaP `2.1` edge `-0.35` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
