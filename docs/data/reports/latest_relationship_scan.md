# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T07:52:25.727439+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4153`

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

- `news_risk_high->equity_4h` score `1.3181` n `62` status `ready` deltaP `12.5983` edge `0.1589` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.7787` n `62` status `ready` deltaP `13.69` edge `0.0214` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.3038` n `62` status `ready` deltaP `9.235` edge `0.1442` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `0.2003` n `62` status `ready` deltaP `-1.0081` edge `0.0676` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.0863` n `62` status `ready` deltaP `7.9486` edge `0.0034` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.0643` n `62` status `ready` deltaP `-0.1497` edge `0.0477` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1324` n `62` status `ready` deltaP `2.8588` edge `0.0025` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.2373` n `62` status `ready` deltaP `1.5096` edge `0.0041` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5478` n `62` status `ready` deltaP `-4.124` edge `-0.007` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.0307` n `62` status `ready` deltaP `-0.1033` edge `-0.0409` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.2397` n `62` status `ready` deltaP `-2.7429` edge `-0.0251` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.3068` n `62` status `ready` deltaP `-3.4667` edge `0.016` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.5967` n `62` status `ready` deltaP `-11.1744` edge `-0.0026` maxDD `-1.1434`
- `news_risk_high->crypto_major_1h` score `-1.9667` n `62` status `ready` deltaP `-7.881` edge `-0.0296` maxDD `-3.2066`
- `news_risk_high->crypto_alt_4h` score `-2.274` n `62` status `ready` deltaP `-3.4667` edge `-0.0064` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.8357` n `62` status `ready` deltaP `-5.9476` edge `-0.2625` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.5263` n `62` status `ready` deltaP `-31.2795` edge `-0.0115` maxDD `-3.9061`
- `news_risk_high->equity_24h` score `-4.9018` n `62` status `ready` deltaP `20.5197` edge `0.3934` maxDD `-86.0244`
- `news_risk_high->commodity_24h` score `-10.5937` n `62` status `ready` deltaP `-28.6178` edge `-0.126` maxDD `-27.9483`
- `news_risk_high->crypto_major_24h` score `-14.5579` n `62` status `ready` deltaP `-31.4908` edge `-0.1529` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
