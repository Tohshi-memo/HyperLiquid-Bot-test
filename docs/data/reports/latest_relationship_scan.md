# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T03:22:33.051092+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4836`

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

- `news_risk_high->crypto_alt_24h` score `0.4116` n `126` status `ready` deltaP `22.619` edge `0.8525` maxDD `-65.3749`
- `news_risk_high->crypto_alt_4h` score `0.0557` n `146` status `ready` deltaP `4.4082` edge `0.2414` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4674` n `146` status `ready` deltaP `1.5831` edge `0.0523` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5541` n `146` status `ready` deltaP `0.1723` edge `-0.0021` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8449` n `126` status `ready` deltaP `12.7481` edge `0.1323` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9586` n `146` status `ready` deltaP `0.5988` edge `-0.0039` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2277` n `146` status `ready` deltaP `-3.2012` edge `-0.0109` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2954` n `146` status `ready` deltaP `-5.098` edge `-0.0099` maxDD `-3.1082`
- `news_risk_high->equity_24h` score `-1.9314` n `126` status `ready` deltaP `17.7579` edge `0.6435` maxDD `-67.0937`
- `news_risk_high->index_24h` score `-2.1067` n `126` status `ready` deltaP `-2.4306` edge `0.0303` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.1579` n `146` status `ready` deltaP `-4.4938` edge `-0.0166` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.348` n `146` status `ready` deltaP `-8.6273` edge `-0.0015` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.5229` n `126` status `ready` deltaP `-20.2629` edge `-0.0175` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.7046` n `146` status `ready` deltaP `-6.9354` edge `-0.0329` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1971` n `146` status `ready` deltaP `-7.8562` edge `-0.0415` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.806` n `146` status `ready` deltaP `-12.1701` edge `-0.0006` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.9153` n `146` status `ready` deltaP `-7.7577` edge `-0.0374` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.1482` n `146` status `ready` deltaP `-14.8409` edge `-0.0948` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-8.6333` n `126` status `ready` deltaP `-13.368` edge `0.0507` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-11.2319` n `126` status `ready` deltaP `-25.0992` edge `-0.0798` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
