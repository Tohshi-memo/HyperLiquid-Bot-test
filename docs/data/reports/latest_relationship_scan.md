# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T14:52:37.789948+00:00`
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

- `news_risk_high->unknown_24h` score `51.7325` n `50` status `ready` deltaP `11.5717` edge `4.2339` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.1444` n `50` status `ready` deltaP `37.6235` edge `1.472` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.7976` n `50` status `ready` deltaP `26.7744` edge `0.8979` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `4.6233` n `50` status `ready` deltaP `45.8411` edge `0.0839` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `4.5913` n `50` status `ready` deltaP `25.6235` edge `0.3046` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `4.0211` n `50` status `ready` deltaP `46.878` edge `0.0316` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `2.9739` n `140` status `ready` deltaP `22.7744` edge `0.1367` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.9647` n `50` status `ready` deltaP `16.976` edge `0.1695` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.6654` n `50` status `ready` deltaP `29.9689` edge `0.0374` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `2.3082` n `128` status `ready` deltaP `5.3217` edge `0.2301` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.5539` n `50` status `ready` deltaP `20.8024` edge `0.0078` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2433` n `50` status `ready` deltaP `17.5629` edge `0.0144` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `0.8412` n `148` status `ready` deltaP `9.2733` edge `0.0533` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.6475` n `50` status `ready` deltaP `17.9207` edge `0.0108` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5354` n `50` status `ready` deltaP `14.7485` edge `0.0016` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.181` n `50` status `ready` deltaP `8.4072` edge `0.0011` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1225` n `50` status `ready` deltaP `5.8503` edge `-0.0007` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0133` n `50` status `ready` deltaP `7.9207` edge `-0.0008` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.0733` n `50` status `ready` deltaP `5.2561` edge `-0.0015` maxDD `-0.1719`
- `market_context_high->fx_1h` score `-0.4937` n `148` status `ready` deltaP `1.5051` edge `-0.0001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
