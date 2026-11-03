# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T15:07:39.695270+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4324`

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

- `news_risk_high->crypto_alt_4h` score `0.229` n `146` status `ready` deltaP `6.3899` edge `0.2504` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4869` n `146` status `ready` deltaP `1.4334` edge `0.0508` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6553` n `146` status `ready` deltaP `-1.6241` edge `-0.0031` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8975` n `146` status `ready` deltaP `1.1976` edge `-0.0028` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1996` n `146` status `ready` deltaP `-3.601` edge `-0.0076` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.3796` n `146` status `ready` deltaP `-5.7927` edge `-0.0131` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.751` n `146` status `ready` deltaP `11.9506` edge `0.1326` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-1.9195` n `146` status `ready` deltaP `-0.3591` edge `0.0405` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.0129` n `146` status `ready` deltaP `-2.6646` edge `-0.0102` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3153` n `146` status `ready` deltaP `-16.4645` edge `-0.0162` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4654` n `146` status `ready` deltaP `-9.9746` edge `-0.0023` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6875` n `146` status `ready` deltaP `-6.9354` edge `-0.0307` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2714` n `146` status `ready` deltaP `-8.6047` edge `-0.0427` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.2485` n `146` status `ready` deltaP `-15.6762` edge `-0.0141` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.4528` n `146` status `ready` deltaP `-4.5565` edge `-0.0202` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.8295` n `146` status `ready` deltaP `21.9726` edge `0.8056` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.8598` n `146` status `ready` deltaP `-13.6214` edge `-0.0789` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.6616` n `146` status `ready` deltaP `17.1114` edge `0.6193` maxDD `-102.7472`
- `news_risk_high->equity_4h` score `-11.2014` n `146` status `ready` deltaP `-0.6828` edge `-0.0928` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.4908` n `146` status `ready` deltaP `-21.3042` edge `-0.0728` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
