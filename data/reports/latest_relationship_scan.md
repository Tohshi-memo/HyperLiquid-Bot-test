# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T00:07:32.281115+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3815`

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

- `news_risk_high->crypto_alt_4h` score `-0.1672` n `146` status `ready` deltaP `7.457` edge `0.1925` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4668` n `146` status `ready` deltaP `2.7807` edge `0.0444` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7066` n `146` status `ready` deltaP `-2.672` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8209` n `146` status `ready` deltaP `2.0958` edge `-0.0024` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.434` n `146` status `ready` deltaP `-7.0441` edge `-0.0147` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5612` n `146` status `ready` deltaP `-9.2988` edge `-0.013` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.9618` n `146` status `ready` deltaP `-1.2926` edge `-0.0128` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1885` n `146` status `ready` deltaP `-8.0285` edge `0.0078` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4574` n `146` status `ready` deltaP `-18.8368` edge `-0.0186` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.4785` n `146` status `ready` deltaP `-8.5296` edge `0.0233` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.5924` n `146` status `ready` deltaP `-6.3366` edge `-0.0225` maxDD `-16.4088`
- `news_risk_high->commodity_4h` score `-3.2224` n `146` status `ready` deltaP `-10.036` edge `0.0338` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.2393` n `146` status `ready` deltaP `-6.958` edge `-0.051` maxDD `-9.4709`
- `news_risk_high->metal_24h` score `-4.6823` n `146` status `ready` deltaP `-0.5404` edge `-0.0284` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-5.0307` n `146` status `ready` deltaP `-6.9955` edge `-0.0521` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.4749` n `146` status `ready` deltaP `-12.2495` edge `-0.1393` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-10.8761` n `146` status `ready` deltaP `11.1888` edge `0.2305` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-11.2112` n `146` status `ready` deltaP `-0.8353` edge `-0.0926` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.4413` n `146` status `ready` deltaP `-20.6807` edge `0.0105` maxDD `-43.7525`
- `news_risk_high->equity_24h` score `-12.0619` n `146` status `ready` deltaP `11.8809` edge `0.366` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
