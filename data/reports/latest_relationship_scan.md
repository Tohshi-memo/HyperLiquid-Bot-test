# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T18:09:47.020704+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4500`

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

- `news_risk_high->crypto_alt_4h` score `0.2669` n `146` status `ready` deltaP `6.9997` edge `0.2512` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4262` n `146` status `ready` deltaP `2.3316` edge `0.0526` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7043` n `146` status `ready` deltaP `-2.5223` edge `-0.0034` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9227` n `146` status `ready` deltaP `0.8982` edge `-0.0029` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1786` n `146` status `ready` deltaP `-3.3016` edge `-0.0069` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4754` n `146` status `ready` deltaP `-7.4695` edge `-0.0142` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.643` n `146` status `ready` deltaP `11.9506` edge `0.1416` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-1.7656` n `146` status `ready` deltaP `1.5506` edge `0.0475` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.0491` n `146` status `ready` deltaP `-3.1219` edge `-0.0118` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2833` n `146` status `ready` deltaP `-16.4645` edge `-0.0121` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.5924` n `146` status `ready` deltaP `-11.3219` edge `-0.0039` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.7054` n `146` status `ready` deltaP `-7.2348` edge `-0.031` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2391` n `146` status `ready` deltaP `-8.3053` edge `-0.042` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.0875` n `146` status `ready` deltaP `-14.6091` edge `-0.0078` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.3834` n `146` status `ready` deltaP `-3.7943` edge `-0.0195` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.8498` n `146` status `ready` deltaP `21.9726` edge `0.803` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.9574` n `146` status `ready` deltaP `-13.9263` edge `-0.085` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.015` n `146` status `ready` deltaP `18.8476` edge `0.6568` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.5368` n `146` status `ready` deltaP `-2.0548` edge `-0.1116` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2057` n `146` status `ready` deltaP `-19.9153` edge `-0.0583` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
