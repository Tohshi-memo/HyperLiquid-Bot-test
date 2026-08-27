# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T13:07:27.544284+00:00`
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

- `news_risk_high->unknown_24h` score `51.3797` n `50` status `ready` deltaP `11.5717` edge `4.2045` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.332` n `50` status `ready` deltaP `37.6235` edge `1.4043` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6338` n `50` status `ready` deltaP `26.3171` edge `0.8873` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `4.6141` n `50` status `ready` deltaP `25.6235` edge `0.3065` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.355` n `50` status `ready` deltaP `44.6321` edge `0.0696` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.0235` n `50` status `ready` deltaP `46.878` edge `0.0318` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.2822` n `134` status `ready` deltaP `24.1081` edge `0.1535` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.9611` n `50` status `ready` deltaP `16.976` edge `0.1692` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.6864` n `50` status `ready` deltaP `30.1416` edge `0.038` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `1.9554` n `128` status `ready` deltaP `5.3217` edge `0.2007` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.5695` n `50` status `ready` deltaP `20.9521` edge `0.0081` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1726` n `50` status `ready` deltaP `17.1138` edge `0.0115` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `1.0593` n `145` status `ready` deltaP `10.7691` edge `0.0615` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5814` n `50` status `ready` deltaP `15.3473` edge `0.0035` maxDD `-0.5024`
- `news_risk_high->equity_4h` score `0.5799` n `50` status `ready` deltaP `17.6159` edge `0.0072` maxDD `-2.105`
- `news_risk_high->index_1h` score `0.1429` n `50` status `ready` deltaP `7.8084` edge `0.0002` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0991` n `50` status `ready` deltaP `5.5509` edge `-0.0017` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0871` n `50` status `ready` deltaP `7.4634` edge `-0.0039` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.1439` n `50` status `ready` deltaP `4.4939` edge `-0.0023` maxDD `-0.1719`
- `market_context_high->fx_1h` score `-0.5446` n `145` status `ready` deltaP `0.6762` edge `-0.0011` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
