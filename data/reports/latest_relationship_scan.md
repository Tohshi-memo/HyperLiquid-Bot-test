# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T14:22:37.121435+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4038`

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

- `news_risk_high->crypto_alt_4h` score `0.0108` n `146` status `ready` deltaP `7.4593` edge `0.2153` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.494` n `146` status `ready` deltaP `2.1819` edge `0.0449` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6996` n `146` status `ready` deltaP `-2.5223` edge `-0.0028` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.852` n `146` status `ready` deltaP `1.6467` edge `-0.002` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3429` n `146` status `ready` deltaP `-5.5471` edge `-0.013` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4587` n `146` status `ready` deltaP `-7.5988` edge `-0.0112` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8399` n `146` status `ready` deltaP `0.3768` edge `-0.0083` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-1.9896` n `146` status `ready` deltaP `-2.1282` edge `0.0433` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.2521` n `146` status `ready` deltaP `-8.0285` edge `0.0025` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4222` n `146` status `ready` deltaP `-18.4908` edge `-0.0164` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6384` n `146` status `ready` deltaP `-6.4863` edge `-0.0274` maxDD `-16.4088`
- `news_risk_high->metal_24h` score `-2.7769` n `146` status `ready` deltaP `6.207` edge `0.0854` maxDD `-16.6552`
- `news_risk_high->crypto_major_1h` score `-3.2463` n `146` status `ready` deltaP `-8.1556` edge `-0.0436` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.506` n `146` status `ready` deltaP `-10.0554` edge `0.0103` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8249` n `146` status `ready` deltaP `-5.4878` edge `-0.045` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.9786` n `146` status `ready` deltaP `-12.2559` edge `-0.0979` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-8.7742` n `146` status `ready` deltaP `14.9951` edge `0.4746` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-11.3449` n `146` status `ready` deltaP `-0.991` edge `-0.1027` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.3687` n `146` status `ready` deltaP `12.7459` edge `0.418` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-12.2525` n `146` status `ready` deltaP `-20.6807` edge `-0.0571` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
