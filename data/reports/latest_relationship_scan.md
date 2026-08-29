# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T15:22:27.964610+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11324`

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

- `news_risk_high->unknown_24h` score `44.6867` n `61` status `ready` deltaP `9.745` edge `3.7563` maxDD `-4.1232`
- `news_risk_high->crypto_alt_24h` score `20.0524` n `61` status `ready` deltaP `31.2927` edge `1.792` maxDD `-22.0332`
- `market_context_high->unknown_24h` score `8.7525` n `104` status `ready` deltaP `20.0855` edge `0.6687` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.4084` n `80` status `ready` deltaP `11.5854` edge `0.5158` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.5137` n `104` status `ready` deltaP `32.6789` edge `0.2602` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.5936` n `80` status `ready` deltaP `5.0749` edge `0.218` maxDD `-0.8558`
- `news_risk_high->fx_4h` score `2.5058` n `80` status `ready` deltaP `36.189` edge `0.0225` maxDD `-0.3953`
- `market_context_high->unknown_4h` score `2.3762` n `118` status `ready` deltaP `17.9413` edge `0.1216` maxDD `-0.7887`
- `news_risk_high->equity_24h` score `1.2071` n `61` status `ready` deltaP `19.8942` edge `0.2979` maxDD `-18.3954`
- `market_context_high->unknown_1h` score `1.099` n `130` status `ready` deltaP `9.8826` edge `0.0738` maxDD `-1.5148`
- `risk_on_high->crypto_alt_1h` score `0.7955` n `30` status `ready` deltaP `14.2715` edge `0.0544` maxDD `-2.1381`
- `risk_on_and_context->crypto_alt_1h` score `0.7955` n `30` status `ready` deltaP `14.2715` edge `0.0544` maxDD `-2.1381`
- `news_risk_high->fx_1h` score `0.7483` n `80` status `ready` deltaP `14.3413` edge `0.0056` maxDD `-0.108`
- `news_risk_high->metal_24h` score `0.7006` n `61` status `ready` deltaP `32.2376` edge `0.0089` maxDD `-7.0529`
- `risk_on_high->metal_1h` score `0.4786` n `30` status `ready` deltaP `8.0539` edge `0.0076` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `0.4786` n `30` status `ready` deltaP `8.0539` edge `0.0076` maxDD `-0.0463`
- `news_risk_high->commodity_1h` score `0.4073` n `80` status `ready` deltaP `11.9012` edge `0.0049` maxDD `-0.5618`
- `news_risk_high->index_24h` score `0.316` n `61` status `ready` deltaP `15.8811` edge `0.0106` maxDD `-2.0772`
- `news_risk_high->crypto_major_24h` score `0.247` n `61` status `ready` deltaP `16.2483` edge `0.2883` maxDD `-24.8633`
- `market_context_high->crypto_major_4h` score `0.0535` n `118` status `ready` deltaP `18.8146` edge `0.2241` maxDD `-20.9394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
