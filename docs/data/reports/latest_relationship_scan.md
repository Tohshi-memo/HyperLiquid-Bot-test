# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T21:37:32.361918+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.2254` n `146` status `ready` deltaP `8.6765` edge `0.2347` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.3935` n `146` status `ready` deltaP `3.3795` edge `0.0498` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6646` n `146` status `ready` deltaP `-1.9235` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8233` n `146` status `ready` deltaP `2.0958` edge `-0.0026` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4153` n `146` status `ready` deltaP `-6.7447` edge `-0.0143` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4822` n `146` status `ready` deltaP `-8.0793` edge `-0.011` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8971` n `146` status `ready` deltaP `-0.378` edge `-0.0106` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1909` n `146` status `ready` deltaP `-8.0285` edge `0.0076` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.3531` n `146` status `ready` deltaP `-6.9725` edge `0.029` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4574` n `146` status `ready` deltaP `-18.8368` edge `-0.0186` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6087` n `146` status `ready` deltaP `-6.4863` edge `-0.0236` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1529` n `146` status `ready` deltaP `-6.5089` edge `-0.0468` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.2564` n `146` status `ready` deltaP `-10.3408` edge `0.033` maxDD `-9.5011`
- `news_risk_high->metal_24h` score `-4.1683` n `146` status `ready` deltaP `1.1897` edge `0.0029` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-4.9555` n `146` status `ready` deltaP `-6.3857` edge `-0.0499` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0379` n `146` status `ready` deltaP `-11.1824` edge `-0.11` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-9.7869` n `146` status `ready` deltaP `12.9189` edge `0.3586` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-10.9509` n `146` status `ready` deltaP `0.0793` edge `-0.077` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.7031` n `146` status `ready` deltaP `11.8809` edge `0.3959` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-11.7785` n `146` status `ready` deltaP `-20.6807` edge `-0.0176` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
