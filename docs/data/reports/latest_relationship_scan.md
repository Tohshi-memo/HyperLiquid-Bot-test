# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T00:37:22.982875+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.4351` n `146` status `ready` deltaP `8.5241` edge `0.2626` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.3724` n `146` status `ready` deltaP `2.631` edge `0.0575` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7105` n `146` status `ready` deltaP `-2.672` edge `-0.0032` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8508` n `146` status `ready` deltaP `1.6467` edge `-0.0019` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1653` n `146` status `ready` deltaP `-3.1519` edge `-0.0062` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.4028` n `146` status `ready` deltaP `12.2979` edge `0.1593` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.4685` n `146` status `ready` deltaP `-7.622` edge `-0.0123` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.7303` n `146` status `ready` deltaP `1.8979` edge `0.0497` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.948` n `146` status `ready` deltaP `-1.5975` edge `-0.009` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2326` n `146` status `ready` deltaP `-16.4645` edge `-0.0056` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.5577` n `146` status `ready` deltaP `-11.0225` edge `-0.003` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6602` n `146` status `ready` deltaP `-6.7857` edge `-0.0282` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.0988` n `146` status `ready` deltaP `-7.5568` edge `-0.0353` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.0799` n `146` status `ready` deltaP `-14.3043` edge `-0.0092` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.3092` n `146` status `ready` deltaP `-3.0321` edge `-0.0184` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.9679` n `146` status `ready` deltaP `22.1462` edge `0.7867` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.6307` n `146` status `ready` deltaP `-11.7921` edge `-0.072` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.3282` n `146` status `ready` deltaP `18.8476` edge `0.6307` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.4114` n `146` status `ready` deltaP `-1.5975` edge `-0.1042` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2669` n `146` status `ready` deltaP `-19.9153` edge `-0.0634` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
