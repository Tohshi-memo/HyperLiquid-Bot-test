# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T20:37:26.846376+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14777`

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

- `news_risk_high->unknown_24h` score `52.245` n `50` status `ready` deltaP `11.6319` edge `4.2762` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `22.1394` n `50` status `ready` deltaP `37.8403` edge `1.6368` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.825` n `50` status `ready` deltaP `25.7073` edge `0.9073` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `4.8496` n `50` status `ready` deltaP `46.0903` edge `0.1011` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `4.4791` n `50` status `ready` deltaP `25.8403` edge `0.2938` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.9211` n `50` status `ready` deltaP `45.6585` edge `0.0314` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `2.9732` n `50` status `ready` deltaP `16.3772` edge `0.1742` maxDD `-0.8495`
- `market_context_high->unknown_24h` score `2.8206` n `128` status `ready` deltaP `5.3819` edge `0.2724` maxDD `-3.1917`
- `news_risk_high->index_24h` score `2.6239` n `50` status `ready` deltaP `29.8403` edge `0.0348` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.3819` n `148` status `ready` deltaP `18.8695` edge `0.1134` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5204` n `50` status `ready` deltaP `20.3533` edge `0.008` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1499` n `50` status `ready` deltaP `16.6647` edge `0.0126` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `0.8497` n `148` status `ready` deltaP `8.6745` edge `0.058` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.8277` n `50` status `ready` deltaP `18.9878` edge `0.0187` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5323` n `50` status `ready` deltaP `14.5988` edge `0.0022` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1125` n `50` status `ready` deltaP `7.2096` edge `0.0003` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0625` n `50` status `ready` deltaP `4.8024` edge `-0.0014` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.1123` n `50` status `ready` deltaP `7.4634` edge `-0.006` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.1695` n `50` status `ready` deltaP `4.189` edge `-0.0024` maxDD `-0.1719`
- `market_context_high->metal_4h` score `-0.4542` n `148` status `ready` deltaP `6.3283` edge `-0.0087` maxDD `-3.3377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
