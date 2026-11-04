# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T15:07:27.042330+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4030`

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

- `news_risk_high->crypto_alt_4h` score `0.0538` n `146` status `ready` deltaP `7.7619` edge `0.2188` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5346` n `146` status `ready` deltaP `2.1819` edge `0.0397` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6747` n `146` status `ready` deltaP `-2.0732` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8568` n `146` status `ready` deltaP `1.6467` edge `-0.0024` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3538` n `146` status `ready` deltaP `-5.6968` edge `-0.0134` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4505` n `146` status `ready` deltaP `-7.4695` edge `-0.011` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8372` n `146` status `ready` deltaP `0.3842` edge `-0.008` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.0268` n `146` status `ready` deltaP `-2.6473` edge `0.042` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.2186` n `146` status `ready` deltaP `-7.7291` edge `0.0033` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4367` n `146` status `ready` deltaP `-18.6638` edge `-0.0171` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6563` n `146` status `ready` deltaP `-6.4863` edge `-0.0297` maxDD `-16.4088`
- `news_risk_high->metal_24h` score `-2.8988` n `146` status `ready` deltaP `5.688` edge `0.0787` maxDD `-16.6552`
- `news_risk_high->crypto_major_1h` score `-3.3519` n `146` status `ready` deltaP `-8.3053` edge `-0.0514` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.4948` n `146` status `ready` deltaP `-10.036` edge `0.0111` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8223` n `146` status `ready` deltaP `-5.4711` edge `-0.0449` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.9153` n `146` status `ready` deltaP `-11.9446` edge `-0.0947` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-8.8479` n `146` status `ready` deltaP `14.8221` edge `0.4663` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-11.2566` n `146` status `ready` deltaP `-0.6828` edge `-0.0974` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.4474` n `146` status `ready` deltaP `12.2269` edge `0.4149` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-12.2669` n `146` status `ready` deltaP `-20.6807` edge `-0.0583` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
