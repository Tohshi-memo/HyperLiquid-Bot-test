# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T10:37:24.758595+00:00`
- Price records: `672`
- Market context records: `3065`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6969`

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

- `market_context_high->crypto_alt_24h` score `16.867` n `92` status `ready` deltaP `11.8207` edge `2.4753` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `14.5201` n `92` status `ready` deltaP `46.2561` edge `0.9257` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.3833` n `92` status `ready` deltaP `23.362` edge `1.006` maxDD `-1.7175`
- `market_context_high->index_24h` score `11.5856` n `92` status `ready` deltaP `29.212` edge `0.8671` maxDD `-4.7103`
- `market_context_high->equity_24h` score `10.5484` n `92` status `ready` deltaP `24.6376` edge `1.4633` maxDD `-18.3486`
- `market_context_high->commodity_4h` score `2.4087` n `128` status `ready` deltaP `16.5206` edge `0.1553` maxDD `-2.8438`
- `market_context_high->unknown_4h` score `-0.1663` n `128` status `ready` deltaP `3.0869` edge `0.0709` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.2531` n `129` status `ready` deltaP `-0.0348` edge `0.0214` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.5511` n `129` status `ready` deltaP `2.9592` edge `0.0159` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.6324` n `129` status `ready` deltaP `-6.3164` edge `-0.0017` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.7064` n `129` status `ready` deltaP `3.5847` edge `0.0985` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.7648` n `92` status `ready` deltaP `-0.1888` edge `-0.0096` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-1.0428` n `129` status `ready` deltaP `2.5472` edge `-0.0308` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-1.0447` n `129` status `ready` deltaP `0.564` edge `0.0077` maxDD `-8.6319`
- `market_context_high->crypto_major_1h` score `-1.0456` n `129` status `ready` deltaP `2.3766` edge `0.0764` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.2269` n `128` status `ready` deltaP `-10.0991` edge `-0.0056` maxDD `-1.0829`
- `market_context_high->metal_1h` score `-1.2988` n `129` status `ready` deltaP `-3.6752` edge `-0.0052` maxDD `-7.278`
- `market_context_high->index_4h` score `-1.365` n `128` status `ready` deltaP `8.9558` edge `0.0562` maxDD `-17.6057`
- `market_context_high->crypto_alt_4h` score `-3.0409` n `128` status `ready` deltaP `17.9878` edge `0.2947` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.5826` n `128` status `ready` deltaP `7.3171` edge `0.0113` maxDD `-35.8845`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
