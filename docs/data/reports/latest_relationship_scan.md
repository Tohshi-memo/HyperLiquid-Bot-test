# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T09:37:25.215093+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4042`

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

- `news_risk_high->crypto_alt_4h` score `-0.3503` n `132` status `ready` deltaP `5.4508` edge `0.1824` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4923` n `132` status `ready` deltaP `2.6946` edge `0.0417` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7284` n `132` status `ready` deltaP `-3.1346` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7933` n `132` status `ready` deltaP `1.9279` edge `-0.0001` maxDD `-1.3086`
- `news_risk_high->index_4h` score `-0.9102` n `132` status `ready` deltaP `4.7071` edge `0.0111` maxDD `-3.0674`
- `news_risk_high->fx_4h` score `-1.2652` n `132` status `ready` deltaP `-7.16` edge `-0.0113` maxDD `-1.587`
- `news_risk_high->index_24h` score `-1.3664` n `132` status `ready` deltaP `-8.0948` edge `0.0956` maxDD `-6.6786`
- `news_risk_high->metal_1h` score `-1.4341` n `132` status `ready` deltaP `-7.4351` edge `-0.0191` maxDD `-2.5487`
- `news_risk_high->crypto_major_1h` score `-1.9729` n `132` status `ready` deltaP `-4.2914` edge `-0.0048` maxDD `-6.1465`
- `news_risk_high->fx_24h` score `-2.0289` n `132` status `ready` deltaP `-21.0181` edge `-0.0195` maxDD `-1.373`
- `news_risk_high->equity_1h` score `-2.1491` n `132` status `ready` deltaP `-5.0127` edge `-0.0016` maxDD `-14.2401`
- `news_risk_high->commodity_1h` score `-2.6839` n `132` status `ready` deltaP `-12.5703` edge `-0.0032` maxDD `-3.2657`
- `news_risk_high->crypto_major_4h` score `-2.9021` n `132` status `ready` deltaP `-5.5756` edge `0.0366` maxDD `-13.9683`
- `news_risk_high->equity_24h` score `-3.0667` n `132` status `ready` deltaP `15.8619` edge `0.8265` maxDD `-86.0244`
- `news_risk_high->metal_4h` score `-4.4846` n `132` status `ready` deltaP `-10.0194` edge `-0.0688` maxDD `-7.3831`
- `news_risk_high->commodity_4h` score `-4.6192` n `132` status `ready` deltaP `-20.7456` edge `-0.0112` maxDD `-9.5011`
- `news_risk_high->equity_4h` score `-6.3412` n `132` status `ready` deltaP `5.1644` edge `0.0534` maxDD `-39.301`
- `news_risk_high->metal_24h` score `-6.5311` n `132` status `ready` deltaP `-11.4553` edge `-0.2566` maxDD `-9.57`
- `news_risk_high->commodity_24h` score `-10.6821` n `132` status `ready` deltaP `-21.6866` edge `0.0421` maxDD `-42.6822`
- `news_risk_high->crypto_alt_24h` score `-12.3971` n `132` status `ready` deltaP `5.0829` edge `0.0762` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
