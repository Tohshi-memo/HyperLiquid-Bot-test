# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T22:52:26.429078+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.0714` n `146` status `ready` deltaP `8.2192` edge `0.218` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4894` n `146` status `ready` deltaP `2.631` edge `0.0425` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6724` n `146` status `ready` deltaP `-2.0732` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8628` n `146` status `ready` deltaP `1.6467` edge `-0.0029` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4231` n `146` status `ready` deltaP `-6.8944` edge `-0.0143` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5137` n `146` status `ready` deltaP `-8.5366` edge `-0.012` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.9207` n `146` status `ready` deltaP `-0.6828` edge `-0.0116` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1873` n `146` status `ready` deltaP `-8.0285` edge `0.0079` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.4207` n `146` status `ready` deltaP `-7.8376` edge `0.0261` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4581` n `146` status `ready` deltaP `-18.8368` edge `-0.0187` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.65` n `146` status `ready` deltaP `-6.9354` edge `-0.0259` maxDD `-16.4088`
- `news_risk_high->commodity_4h` score `-3.209` n `146` status `ready` deltaP `-9.8835` edge `0.0339` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.2393` n `146` status `ready` deltaP `-6.958` edge `-0.051` maxDD `-9.4709`
- `news_risk_high->metal_24h` score `-4.4259` n `146` status `ready` deltaP `0.3247` edge `-0.0128` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-4.9725` n `146` status `ready` deltaP `-6.5382` edge `-0.0503` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.1895` n `146` status `ready` deltaP `-11.4873` edge `-0.1206` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-10.3296` n `146` status `ready` deltaP `12.0539` edge `0.2948` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-11.0714` n `146` status `ready` deltaP `-0.378` edge `-0.084` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.6069` n `146` status `ready` deltaP `-20.6807` edge `-0.0033` maxDD `-43.7525`
- `news_risk_high->equity_24h` score `-11.8879` n `146` status `ready` deltaP `11.8809` edge `0.3805` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
