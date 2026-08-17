# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T00:37:25.429129+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->unknown_24h` score `61.6565` n `79` status `ready` deltaP `-35.8452` edge `8.412` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `4.6345` n `79` status `ready` deltaP `34.0937` edge `0.1938` maxDD `-0.4576`
- `market_context_high->commodity_4h` score `0.9649` n `107` status `ready` deltaP `11.1323` edge `0.0533` maxDD `-0.7687`
- `market_context_high->index_24h` score `0.1638` n `79` status `ready` deltaP `12.9637` edge `-0.0381` maxDD `-0.4405`
- `market_context_high->metal_4h` score `-0.1442` n `107` status `ready` deltaP `16.415` edge `0.0128` maxDD `-4.5909`
- `market_context_high->commodity_1h` score `-0.3552` n `112` status `ready` deltaP `0.4331` edge `0.011` maxDD `-0.8124`
- `market_context_high->metal_1h` score `-0.384` n `112` status `ready` deltaP `3.5607` edge `-0.0014` maxDD `-1.7257`
- `market_context_high->fx_1h` score `-0.4978` n `112` status `ready` deltaP `-0.7485` edge `0.0` maxDD `-0.2527`
- `market_context_high->crypto_major_24h` score `-0.5664` n `79` status `ready` deltaP `-2.4702` edge `0.1603` maxDD `-11.9823`
- `market_context_high->index_1h` score `-0.6604` n `112` status `ready` deltaP `-4.6514` edge `-0.0015` maxDD `-0.5064`
- `market_context_high->fx_4h` score `-0.6647` n `107` status `ready` deltaP `1.1968` edge `-0.0029` maxDD `-0.504`
- `market_context_high->crypto_major_4h` score `-0.9056` n `107` status `ready` deltaP `1.8592` edge `-0.0077` maxDD `-4.6638`
- `market_context_high->index_4h` score `-1.2366` n `107` status `ready` deltaP `-10.7932` edge `-0.0057` maxDD `-0.8045`
- `market_context_high->crypto_alt_1h` score `-1.9026` n `112` status `ready` deltaP `-5.6565` edge `-0.0169` maxDD `-4.6486`
- `market_context_high->crypto_major_1h` score `-1.9879` n `112` status `ready` deltaP `-6.25` edge `-0.0238` maxDD `-4.0151`
- `market_context_high->equity_1h` score `-2.4224` n `112` status `ready` deltaP `-9.8695` edge `-0.0428` maxDD `-4.1282`
- `market_context_high->metal_24h` score `-2.5862` n `79` status `ready` deltaP `-15.491` edge `0.0229` maxDD `-7.0954`
- `market_context_high->fx_24h` score `-2.6643` n `79` status `ready` deltaP `-23.3605` edge `-0.0251` maxDD `-1.8596`
- `market_context_high->equity_24h` score `-4.5386` n `79` status `ready` deltaP `7.0037` edge `-0.1904` maxDD `-14.4273`
- `market_context_high->crypto_alt_4h` score `-5.6246` n `107` status `ready` deltaP `-7.659` edge `-0.0495` maxDD `-16.786`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
