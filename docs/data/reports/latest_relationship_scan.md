# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T09:52:26.440600+00:00`
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

- `news_risk_high->unknown_24h` score `50.8553` n `50` status `ready` deltaP `11.5717` edge `4.1608` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.796` n `50` status `ready` deltaP `37.6235` edge `1.2763` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6136` n `50` status `ready` deltaP `26.4695` edge `0.8846` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `4.9045` n `50` status `ready` deltaP `25.6235` edge `0.3307` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `4.0357` n `50` status `ready` deltaP `47.0305` edge `0.0318` maxDD `-0.0559`
- `news_risk_high->metal_24h` score `3.8298` n `50` status `ready` deltaP `42.3869` edge `0.0408` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `3.583` n `130` status `ready` deltaP `24.7772` edge `0.1741` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.9035` n `50` status `ready` deltaP `16.5269` edge `0.1674` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.789` n `50` status `ready` deltaP `30.6598` edge `0.0431` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `1.6269` n `129` status `ready` deltaP `5.3701` edge `0.173` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.5084` n `50` status `ready` deltaP `20.2036` edge `0.008` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.3511` n `135` status `ready` deltaP `11.3417` edge `0.082` maxDD `-1.6015`
- `news_risk_high->equity_1h` score `1.1751` n `50` status `ready` deltaP `16.515` edge `0.0157` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `0.8753` n `50` status `ready` deltaP `18.6829` edge `0.0247` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.6024` n `50` status `ready` deltaP `15.6467` edge `0.0042` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1421` n `50` status `ready` deltaP `7.6587` edge `0.0011` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0937` n `50` status `ready` deltaP `5.4012` edge `-0.0014` maxDD `-0.1413`
- `news_risk_high->index_4h` score `-0.0637` n `50` status `ready` deltaP `5.2561` edge `-0.0007` maxDD `-0.1719`
- `news_risk_high->metal_4h` score `-0.2628` n `50` status `ready` deltaP `6.0915` edge `-0.0094` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4606` n `135` status `ready` deltaP `2.2777` edge `-0.001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
