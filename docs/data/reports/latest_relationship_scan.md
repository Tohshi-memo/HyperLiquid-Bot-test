# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T00:07:25.137470+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `news_risk_high->unknown_24h` score `52.4226` n `50` status `ready` deltaP `11.6319` edge `4.291` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `24.0054` n `50` status `ready` deltaP `37.8403` edge `1.7923` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.687` n `50` status `ready` deltaP `24.7927` edge `0.9019` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `4.9727` n `50` status `ready` deltaP `46.2639` edge `0.1102` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `4.9474` n `50` status `ready` deltaP `27.75` edge `0.3201` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.7618` n `50` status `ready` deltaP `43.9817` edge `0.0293` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `2.9982` n `128` status `ready` deltaP `5.3819` edge `0.2872` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.9444` n `50` status `ready` deltaP `16.2275` edge `0.1728` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.8282` n `50` status `ready` deltaP `31.75` edge `0.0391` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.244` n `148` status `ready` deltaP `17.9549` edge `0.108` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.518` n `50` status `ready` deltaP `20.3533` edge `0.0078` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2841` n `50` status `ready` deltaP `17.8623` edge `0.0158` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.126` n `50` status `ready` deltaP `20.5122` edge `0.0334` maxDD `-2.105`
- `market_context_high->unknown_1h` score `0.821` n `148` status `ready` deltaP `8.5248` edge `0.0566` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5082` n `50` status `ready` deltaP `14.1497` edge `0.0021` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1452` n `50` status `ready` deltaP `7.8084` edge `0.0005` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0968` n `50` status `ready` deltaP `5.4012` edge `-0.001` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0031` n `50` status `ready` deltaP `8.378` edge `-0.003` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.0795` n `50` status `ready` deltaP `5.1037` edge `-0.001` maxDD `-0.1719`
- `market_context_high->metal_4h` score `-0.3833` n `148` status `ready` deltaP `7.2429` edge `-0.0057` maxDD `-3.3377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
