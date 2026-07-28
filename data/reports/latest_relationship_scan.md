# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T13:37:39.686234+00:00`
- Price records: `672`
- Market context records: `8201`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5904`

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

- `news_risk_high->unknown_24h` score `8289.4287` n `43` status `ready` deltaP `36.9792` edge `690.5392` maxDD `0.0`
- `market_context_high->equity_24h` score `22.0658` n `40` status `ready` deltaP `44.8264` edge `1.631` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.3557` n `41` status `ready` deltaP `46.4939` edge `0.5573` maxDD `-0.0094`
- `market_context_high->metal_24h` score `9.0761` n `40` status `ready` deltaP `46.7014` edge `0.445` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `7.6253` n `40` status `ready` deltaP `19.0625` edge `1.0126` maxDD `-6.9664`
- `news_risk_high->equity_4h` score `6.7551` n `54` status `ready` deltaP `24.8588` edge `0.4569` maxDD `-3.4427`
- `market_context_high->crypto_major_24h` score `5.4283` n `40` status `ready` deltaP `18.5417` edge `0.872` maxDD `-17.9744`
- `market_context_high->index_4h` score `4.1968` n `41` status `ready` deltaP `38.567` edge `0.0969` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.9087` n `41` status `ready` deltaP `37.9573` edge `0.0905` maxDD `-0.0926`
- `market_context_high->equity_1h` score `3.5927` n `41` status `ready` deltaP `18.7856` edge `0.1888` maxDD `-0.1718`
- `news_risk_high->equity_1h` score `2.9981` n `54` status `ready` deltaP `22.128` edge `0.1332` maxDD `-1.1366`
- `market_context_high->index_24h` score `2.8747` n `40` status `ready` deltaP `26.3889` edge `0.2546` maxDD `-0.9576`
- `news_risk_high->crypto_major_4h` score `2.7178` n `54` status `ready` deltaP `13.8325` edge `0.3256` maxDD `-2.8833`
- `news_risk_high->index_4h` score `2.5998` n `54` status `ready` deltaP `21.81` edge `0.0903` maxDD `-0.191`
- `news_risk_high->crypto_major_1h` score `1.9985` n `54` status `ready` deltaP `13.6006` edge `0.1156` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.8566` n `54` status `ready` deltaP `15.0033` edge `0.0981` maxDD `-1.1388`
- `market_context_high->fx_24h` score `1.8082` n `40` status `ready` deltaP `34.0278` edge `0.0698` maxDD `-0.5196`
- `market_context_high->crypto_alt_4h` score `1.5348` n `41` status `ready` deltaP `8.2317` edge `0.2006` maxDD `-2.0305`
- `market_context_high->metal_1h` score `1.4815` n `41` status `ready` deltaP `16.7957` edge `0.0293` maxDD `-0.0917`
- `news_risk_high->crypto_alt_4h` score `1.4448` n `54` status `ready` deltaP `17.5362` edge `0.2075` maxDD `-5.8012`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
