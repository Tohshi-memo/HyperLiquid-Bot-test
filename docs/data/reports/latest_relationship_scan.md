# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T10:58:12.767401+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11798`

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

- `market_context_high->unknown_24h` score `196.6671` n `88` status `ready` deltaP `-21.512` edge `25.6255` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `14.2693` n `33` status `ready` deltaP `24.6844` edge `1.0521` maxDD `-0.8711`
- `news_risk_high->equity_4h` score `7.8294` n `33` status `ready` deltaP `37.0427` edge `0.4055` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5061` n `88` status `ready` deltaP `41.3037` edge `0.3559` maxDD `-0.1266`
- `news_risk_high->index_24h` score `3.8304` n `33` status `ready` deltaP `30.5556` edge `0.1155` maxDD `0.0`
- `market_context_high->commodity_4h` score `1.9186` n `113` status `ready` deltaP `18.2684` edge `0.0852` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.8255` n `33` status `ready` deltaP `20.6717` edge `0.0275` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.8068` n `33` status `ready` deltaP `7.3853` edge `0.1332` maxDD `-0.5496`
- `news_risk_high->fx_4h` score `0.0919` n `33` status `ready` deltaP `6.0144` edge `-0.0064` maxDD `-0.0863`
- `news_risk_high->index_1h` score `0.0071` n `33` status `ready` deltaP `1.1387` edge `0.0156` maxDD `-0.141`
- `market_context_high->fx_4h` score `-0.044` n `113` status `ready` deltaP `6.9798` edge `0.0083` maxDD `-0.504`
- `market_context_high->commodity_1h` score `-0.0472` n `125` status `ready` deltaP `2.5054` edge `0.0205` maxDD `-0.624`
- `news_risk_high->fx_1h` score `-0.1272` n `33` status `ready` deltaP `2.4497` edge `-0.0017` maxDD `-0.1414`
- `market_context_high->fx_1h` score `-0.1721` n `125` status `ready` deltaP `0.7042` edge `0.0014` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.5354` n `125` status `ready` deltaP `1.3545` edge `-0.0061` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.6531` n `33` status `ready` deltaP `-6.791` edge `-0.0116` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.7858` n `125` status `ready` deltaP `-6.8371` edge `-0.003` maxDD `-0.5064`
- `news_risk_high->commodity_1h` score `-0.9537` n `33` status `ready` deltaP `-4.2098` edge `-0.0211` maxDD `-0.7581`
- `market_context_high->metal_4h` score `-1.1341` n `113` status `ready` deltaP `4.1982` edge `-0.016` maxDD `-4.5909`
- `news_risk_high->metal_4h` score `-1.1488` n `33` status `ready` deltaP `-3.9542` edge `-0.0316` maxDD `-2.4791`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
