# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T11:52:29.297661+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.0198` n `146` status `ready` deltaP `7.1554` edge `0.2134` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4956` n `146` status `ready` deltaP `1.9555` edge `0.0462` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6962` n `146` status `ready` deltaP `-2.4418` edge `-0.0029` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.851` n `146` status `ready` deltaP `1.719` edge `-0.0024` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3385` n `146` status `ready` deltaP `-5.4784` edge `-0.0129` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4744` n `146` status `ready` deltaP `-7.7508` edge `-0.0122` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.8731` n `146` status `ready` deltaP `-0.3981` edge `0.0467` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.8754` n `146` status `ready` deltaP `-0.2311` edge `-0.0088` maxDD `-4.0745`
- `news_risk_high->metal_24h` score `-2.3565` n `146` status `ready` deltaP `7.9372` edge `0.1089` maxDD `-16.6552`
- `news_risk_high->fx_24h` score `-2.3734` n `146` status `ready` deltaP `-17.9718` edge `-0.0136` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.3864` n `146` status `ready` deltaP `-9.3024` edge `-0.0002` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6557` n `146` status `ready` deltaP `-6.1142` edge `-0.0321` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2008` n `146` status `ready` deltaP `-7.9325` edge `-0.0413` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.715` n `146` status `ready` deltaP `-11.4232` edge `0.002` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.7413` n `146` status `ready` deltaP `-4.7279` edge `-0.0431` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.9751` n `146` status `ready` deltaP `-12.4079` edge `-0.0966` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-8.4631` n `146` status `ready` deltaP `16.5522` edge `0.5041` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-10.8944` n `146` status `ready` deltaP `14.13` edge `0.4483` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.5711` n `146` status `ready` deltaP `-1.5989` edge `-0.1175` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2309` n `146` status `ready` deltaP `-20.6807` edge `-0.0553` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
