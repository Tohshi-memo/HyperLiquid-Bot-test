# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T10:37:27.555146+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14748`

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

- `news_risk_high->unknown_24h` score `50.9765` n `50` status `ready` deltaP `11.5717` edge `4.1709` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.0948` n `50` status `ready` deltaP `37.6235` edge `1.3012` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6328` n `50` status `ready` deltaP `26.4695` edge `0.8862` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `4.8145` n `50` status `ready` deltaP `25.6235` edge `0.3232` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `4.0478` n `50` status `ready` deltaP `47.1829` edge `0.0318` maxDD `-0.0559`
- `news_risk_high->metal_24h` score `3.9528` n `50` status `ready` deltaP `42.905` edge `0.0476` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `3.6022` n `130` status `ready` deltaP `24.7772` edge `0.1757` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.9023` n `50` status `ready` deltaP `16.5269` edge `0.1673` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.771` n `50` status `ready` deltaP `30.6598` edge `0.0416` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `1.7481` n `129` status `ready` deltaP `5.3701` edge `0.1831` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.5204` n `50` status `ready` deltaP `20.3533` edge `0.008` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.3397` n `137` status `ready` deltaP `11.7094` edge `0.0786` maxDD `-1.6015`
- `news_risk_high->equity_1h` score `1.2086` n `50` status `ready` deltaP `16.8144` edge `0.0165` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `0.7439` n `50` status `ready` deltaP `18.2256` edge `0.0168` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5752` n `50` status `ready` deltaP `15.1976` edge `0.0037` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1678` n `50` status `ready` deltaP `8.1078` edge `0.0014` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1131` n `50` status `ready` deltaP `5.7006` edge `-0.0009` maxDD `-0.1413`
- `news_risk_high->index_4h` score `-0.1111` n `50` status `ready` deltaP `4.7988` edge `-0.0016` maxDD `-0.1719`
- `news_risk_high->metal_4h` score `-0.2264` n `50` status `ready` deltaP `6.3963` edge `-0.0084` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4551` n `137` status `ready` deltaP `2.3679` edge `-0.0009` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
