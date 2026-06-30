# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T16:22:26.798275+00:00`
- Price records: `672`
- Market context records: `5264`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9598`

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

- `market_context_high->unknown_24h` score `26.3277` n `147` status `ready` deltaP `29.8895` edge `2.0037` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `10.3599` n `147` status `ready` deltaP `28.4297` edge `1.0342` maxDD `-22.166`
- `market_context_high->crypto_alt_4h` score `4.1496` n `160` status `ready` deltaP `14.878` edge `0.4107` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.7491` n `160` status `ready` deltaP `13.811` edge `0.4496` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.4476` n `147` status `ready` deltaP `19.5118` edge `0.7201` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `1.6947` n `160` status `ready` deltaP `16.3262` edge `0.1346` maxDD `-5.5109`
- `market_context_high->equity_4h` score `0.6114` n `160` status `ready` deltaP `8.5823` edge `0.1576` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5185` n `147` status `ready` deltaP `12.6666` edge `0.0483` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.5174` n `172` status `ready` deltaP `4.8705` edge `0.1068` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.2719` n `172` status `ready` deltaP `5.8209` edge `0.1084` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.2283` n `147` status `ready` deltaP `21.0247` edge `0.0526` maxDD `-7.413`
- `market_context_high->crypto_alt_24h` score `0.0558` n `147` status `ready` deltaP `15.4018` edge `0.534` maxDD `-38.6949`
- `market_context_high->equity_1h` score `0.0268` n `172` status `ready` deltaP `6.1586` edge `0.0577` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0404` n `172` status `ready` deltaP `5.2952` edge `0.0117` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.2135` n `172` status `ready` deltaP `4.1394` edge `0.0138` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2514` n `172` status `ready` deltaP `1.8069` edge `0.0005` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.6998` n `160` status `ready` deltaP `4.9085` edge `0.0207` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.7752` n `160` status `ready` deltaP `0.3963` edge `0.0009` maxDD `-1.567`
- `market_context_high->unknown_1h` score `-1.1444` n `172` status `ready` deltaP `7.1369` edge `-0.0788` maxDD `-2.7986`
- `market_context_high->commodity_1h` score `-1.3959` n `172` status `ready` deltaP `-3.2238` edge `-0.0072` maxDD `-3.0104`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
