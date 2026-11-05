# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T10:22:25.755282+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3555`

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

- `news_risk_high->crypto_alt_4h` score `-0.3109` n `146` status `ready` deltaP `6.2375` edge `0.1822` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5978` n `146` status `ready` deltaP `2.3316` edge `0.0306` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6903` n `146` status `ready` deltaP `-2.3726` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7537` n `146` status `ready` deltaP `2.6946` edge `-0.0008` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.5058` n `146` status `ready` deltaP `-8.3841` edge `-0.012` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5446` n `146` status `ready` deltaP `-8.5411` edge `-0.0189` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7505` n `146` status `ready` deltaP `1.4513` edge `-0.004` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2197` n `146` status `ready` deltaP `-8.1782` edge `0.0062` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.3569` n `146` status `ready` deltaP `-17.6257` edge `-0.0138` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5729` n `146` status `ready` deltaP `-6.0372` edge `-0.022` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.8975` n `146` status `ready` deltaP `-12.1628` edge `-0.0062` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.364` n `146` status `ready` deltaP `-7.4071` edge `-0.0584` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.3958` n `146` status `ready` deltaP `-11.4079` edge `0.0285` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.5322` n `146` status `ready` deltaP `-10.654` edge `-0.0695` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-6.8782` n `146` status `ready` deltaP `-7.6338` edge `-0.1641` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.2463` n `146` status `ready` deltaP `-11.7921` edge `-0.1233` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-9.795` n `146` status `ready` deltaP `-18.4315` edge `0.1327` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.7587` n `146` status `ready` deltaP `1.1464` edge `-0.0681` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.8822` n `146` status `ready` deltaP `9.9778` edge `0.227` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.0116` n `146` status `ready` deltaP `4.0954` edge `-0.2524` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
