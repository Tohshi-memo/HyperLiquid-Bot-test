# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T21:52:28.384167+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4258`

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

- `news_risk_high->crypto_alt_4h` score `-0.2024` n `146` status `ready` deltaP `7.3046` edge `0.189` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4629` n `146` status `ready` deltaP `3.0801` edge `0.0429` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6518` n `146` status `ready` deltaP `3.2934` edge `0.0037` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7129` n `146` status `ready` deltaP `-2.8217` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4354` n `146` status `ready` deltaP `-7.1646` edge `-0.0111` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5251` n `146` status `ready` deltaP `-8.2417` edge `-0.0184` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6405` n `146` status `ready` deltaP `1.4513` edge `0.0101` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.2828` n `146` status `ready` deltaP `-5.139` edge `0.0092` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4546` n `146` status `ready` deltaP `-10.4237` edge `0.0016` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.5413` n `146` status `ready` deltaP `-20.1657` edge `-0.0205` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.7196` n `146` status `ready` deltaP `-12.2504` edge `0.0172` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-2.8255` n `146` status `ready` deltaP `-5.3113` edge `-0.0275` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8555` n `146` status `ready` deltaP `-14.3043` edge `0.0095` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.6797` n `146` status `ready` deltaP `-12.4833` edge `-0.0696` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.16` n `146` status `ready` deltaP `-9.658` edge `-0.047` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-8.7409` n `146` status `ready` deltaP `-15.3629` edge `-0.2678` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.0695` n `146` status `ready` deltaP `-14.4928` edge `0.1669` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.3975` n `146` status `ready` deltaP `2.3659` edge `0.0372` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-12.9237` n `146` status `ready` deltaP `9.8989` edge `0.3074` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.8165` n `146` status `ready` deltaP `2.1` edge `-0.3423` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
