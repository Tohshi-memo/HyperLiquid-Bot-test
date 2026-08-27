# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T16:37:30.127201+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14761`

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

- `news_risk_high->unknown_24h` score `51.9594` n `50` status `ready` deltaP `11.6319` edge `4.2524` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.9274` n `50` status `ready` deltaP `37.8403` edge `1.5358` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `13.0577` n `50` status `ready` deltaP `27.5366` edge `0.9145` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `4.7188` n `50` status `ready` deltaP `46.0903` edge `0.0902` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `4.5835` n `50` status `ready` deltaP `25.8403` edge `0.3025` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `4.0223` n `50` status `ready` deltaP `46.878` edge `0.0317` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `3.0474` n `50` status `ready` deltaP `17.4251` edge `0.1734` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.6431` n `50` status `ready` deltaP `29.8403` edge `0.0364` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.6401` n `147` status `ready` deltaP `20.6114` edge `0.1233` maxDD `-0.5894`
- `market_context_high->unknown_24h` score `2.535` n `128` status `ready` deltaP `5.3819` edge `0.2486` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.5815` n `50` status `ready` deltaP `21.1018` edge `0.0081` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1918` n `50` status `ready` deltaP `17.1138` edge `0.0131` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `0.924` n `148` status `ready` deltaP `9.7224` edge `0.0572` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.6935` n `50` status `ready` deltaP `18.2256` edge `0.0126` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.551` n `50` status `ready` deltaP `14.8982` edge `0.0026` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1553` n `50` status `ready` deltaP `7.9581` edge `0.0008` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0882` n `50` status `ready` deltaP `5.2515` edge `-0.0011` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0595` n `50` status `ready` deltaP `7.4634` edge `-0.0016` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.0903` n `50` status `ready` deltaP `5.1037` edge `-0.0019` maxDD `-0.1719`
- `market_context_high->metal_4h` score `-0.4518` n `147` status `ready` deltaP `6.0893` edge `-0.0068` maxDD `-3.3377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
