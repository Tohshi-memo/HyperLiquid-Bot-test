# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T09:22:32.550207+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.3027` n `133` status `ready` deltaP `5.7812` edge `0.1863` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5056` n `133` status `ready` deltaP `2.4684` edge `0.0415` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7161` n `133` status `ready` deltaP `-2.9141` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8079` n `133` status `ready` deltaP `1.7131` edge `0.0002` maxDD `-1.3155`
- `news_risk_high->index_4h` score `-0.9652` n `133` status `ready` deltaP `4.4609` edge `0.011` maxDD `-3.1585`
- `news_risk_high->fx_4h` score `-1.3223` n `133` status `ready` deltaP `-7.5302` edge `-0.0117` maxDD `-1.6099`
- `news_risk_high->metal_1h` score `-1.4058` n `133` status `ready` deltaP `-6.9965` edge `-0.0184` maxDD `-2.5487`
- `news_risk_high->index_24h` score `-1.4311` n `133` status `ready` deltaP `-8.4137` edge `0.0936` maxDD `-6.6786`
- `news_risk_high->crypto_major_1h` score `-1.9908` n `133` status `ready` deltaP `-4.455` edge `-0.0052` maxDD `-6.1465`
- `news_risk_high->fx_24h` score `-2.0941` n `133` status `ready` deltaP `-21.4168` edge `-0.0203` maxDD `-1.432`
- `news_risk_high->commodity_1h` score `-2.7115` n `133` status `ready` deltaP `-12.8551` edge `-0.0036` maxDD `-3.2657`
- `news_risk_high->crypto_major_4h` score `-2.9357` n `133` status `ready` deltaP `-5.7194` edge `0.037` maxDD `-14.1477`
- `news_risk_high->equity_1h` score `-3.2365` n `133` status `ready` deltaP `-4.5912` edge `0.0014` maxDD `-14.2401`
- `news_risk_high->equity_24h` score `-3.3408` n `133` status `ready` deltaP `15.4006` edge `0.8109` maxDD `-86.0244`
- `news_risk_high->metal_4h` score `-4.5744` n `133` status `ready` deltaP `-10.1917` edge `-0.0689` maxDD `-7.5482`
- `news_risk_high->commodity_4h` score `-4.6416` n `133` status `ready` deltaP `-20.9506` edge `-0.0117` maxDD `-9.5011`
- `news_risk_high->equity_4h` score `-6.5725` n `133` status `ready` deltaP `4.9182` edge `0.0518` maxDD `-40.2507`
- `news_risk_high->metal_24h` score `-6.71` n `133` status `ready` deltaP `-11.8882` edge `-0.259` maxDD `-10.0065`
- `news_risk_high->commodity_24h` score `-10.7264` n `133` status `ready` deltaP `-21.5534` edge `0.0444` maxDD `-42.8998`
- `news_risk_high->crypto_alt_24h` score `-12.383` n `133` status `ready` deltaP `5.28` edge `0.0767` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
