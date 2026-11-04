# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T22:07:43.364707+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3872`

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

- `news_risk_high->crypto_alt_4h` score `0.2036` n `146` status `ready` deltaP `8.6765` edge `0.2319` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4262` n `146` status `ready` deltaP `3.0801` edge `0.0476` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6724` n `146` status `ready` deltaP `-2.0732` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8496` n `146` status `ready` deltaP `1.7964` edge `-0.0028` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4231` n `146` status `ready` deltaP `-6.8944` edge `-0.0143` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4932` n `146` status `ready` deltaP `-8.2317` edge `-0.0114` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8979` n `146` status `ready` deltaP `-0.378` edge `-0.0107` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1766` n `146` status `ready` deltaP `-7.8788` edge `0.0078` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.3796` n `146` status `ready` deltaP `-7.3185` edge `0.0279` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4574` n `146` status `ready` deltaP `-18.8368` edge `-0.0186` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6298` n `146` status `ready` deltaP `-6.636` edge `-0.0253` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1721` n `146` status `ready` deltaP `-6.6586` edge `-0.0474` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.2284` n `146` status `ready` deltaP `-10.036` edge `0.0333` maxDD `-9.5011`
- `news_risk_high->metal_24h` score `-4.2716` n `146` status `ready` deltaP `0.8437` edge `-0.0034` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-4.9421` n `146` status `ready` deltaP `-6.2333` edge `-0.0498` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0499` n `146` status `ready` deltaP `-11.1824` edge `-0.111` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-9.9726` n `146` status `ready` deltaP `12.5729` edge `0.3371` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-10.9581` n `146` status `ready` deltaP `0.0793` edge `-0.0776` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.7101` n `146` status `ready` deltaP `-20.6807` edge `-0.0119` maxDD `-43.7525`
- `news_risk_high->equity_24h` score `-11.7703` n `146` status `ready` deltaP `11.8809` edge `0.3903` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
