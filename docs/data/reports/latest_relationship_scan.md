# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T15:22:49.633963+00:00`
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

- `news_risk_high->unknown_24h` score `51.7861` n `50` status `ready` deltaP `11.6118` edge `4.2381` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.4572` n `50` status `ready` deltaP `37.7678` edge `1.4971` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.8976` n `50` status `ready` deltaP `27.0793` edge `0.9042` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `4.6702` n `50` status `ready` deltaP `46.0069` edge `0.0867` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `4.6209` n `50` status `ready` deltaP `25.7678` edge `0.3061` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `4.0223` n `50` status `ready` deltaP `46.878` edge `0.0317` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `3.015` n `50` status `ready` deltaP `17.2754` edge `0.1717` maxDD `-0.8495`
- `market_context_high->unknown_4h` score `2.8513` n `142` status `ready` deltaP `21.8117` edge `0.1329` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.6469` n `50` status `ready` deltaP `29.7678` edge `0.0372` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `2.3618` n `128` status `ready` deltaP `5.3618` edge `0.2343` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.5671` n `50` status `ready` deltaP `20.9521` edge `0.0079` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2277` n `50` status `ready` deltaP `17.4132` edge `0.0141` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `0.8916` n `148` status `ready` deltaP `9.5727` edge `0.0555` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.6475` n `50` status `ready` deltaP `17.9207` edge `0.0108` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5494` n `50` status `ready` deltaP `14.8982` edge `0.0024` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1717` n `50` status `ready` deltaP `8.2575` edge `0.0009` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1272` n `50` status `ready` deltaP `5.8503` edge `-0.0001` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0073` n `50` status `ready` deltaP `7.9207` edge `-0.0003` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.0745` n `50` status `ready` deltaP `5.2561` edge `-0.0016` maxDD `-0.1719`
- `market_context_high->fx_1h` score `-0.4852` n `148` status `ready` deltaP `1.6548` edge `0.0` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
