# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T23:22:31.273461+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4256`

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

- `market_context_high->unknown_1h` score `381.2899` n `50` status `ready` deltaP `12.8204` edge `31.6936` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `321.6632` n `50` status `ready` deltaP `12.8049` edge `26.7199` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.3548` n `50` status `ready` deltaP `29.286` edge `1.088` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.2886` n `50` status `ready` deltaP `36.2461` edge `0.8407` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.6724` n `62` status `ready` deltaP `29.4376` edge `0.7416` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.5114` n `68` status `ready` deltaP `38.4864` edge `0.6397` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.3052` n `68` status `ready` deltaP `26.1568` edge `0.5688` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.1115` n `50` status `ready` deltaP `16.7805` edge `0.5511` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.5886` n `50` status `ready` deltaP `15.2744` edge `0.4928` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.5005` n `62` status `ready` deltaP `32.5963` edge `0.1736` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8291` n `68` status `ready` deltaP `26.9637` edge `0.2006` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.066` n `50` status `ready` deltaP `13.1557` edge `0.2341` maxDD `-3.6376`
- `market_context_high->fx_4h` score `3.009` n `50` status `ready` deltaP `33.7561` edge `0.0392` maxDD `-0.0791`
- `news_risk_high->index_4h` score `2.9473` n `68` status `ready` deltaP `32.2364` edge `0.0569` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9115` n `68` status `ready` deltaP `13.0592` edge `0.1911` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.8467` n `50` status `ready` deltaP `12.3533` edge `0.1999` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.399` n `68` status `ready` deltaP `20.4448` edge `0.1052` maxDD `-0.993`
- `news_risk_high->index_1h` score `1.9719` n `68` status `ready` deltaP `24.3484` edge `0.017` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.5214` n `50` status `ready` deltaP `21.2395` edge `0.0116` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.5092` n `50` status `ready` deltaP `8.7279` edge `0.3215` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
