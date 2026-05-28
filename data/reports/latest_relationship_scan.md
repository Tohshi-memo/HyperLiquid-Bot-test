# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T13:07:25.860012+00:00`
- Price records: `672`
- Market context records: `2144`
- Flow alert records: `8068`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9158`

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

- `market_context_high->crypto_alt_4h` score `13.286` n `157` status `ready` deltaP `37.3049` edge `0.9521` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.8291` n `157` status `ready` deltaP `41.3333` edge `0.7632` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.571` n `157` status `ready` deltaP `25.4098` edge `0.4531` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `6.2286` n `33` status `ready` deltaP `28.1966` edge `0.3982` maxDD `-3.0367`
- `market_context_high->equity_4h` score `4.9683` n `157` status `ready` deltaP `26.2312` edge `0.3486` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.8234` n `156` status `ready` deltaP `15.3979` edge `0.3388` maxDD `-4.1604`
- `market_context_high->equity_24h` score `3.2651` n `156` status `ready` deltaP `26.8697` edge `0.5828` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `3.2628` n `157` status `ready` deltaP `17.4015` edge `0.2036` maxDD `-1.817`
- `market_context_high->metal_4h` score `3.1105` n `157` status `ready` deltaP `21.5337` edge `0.2544` maxDD `-4.7664`
- `market_context_high->crypto_alt_1h` score `3.0679` n `157` status `ready` deltaP `15.9045` edge `0.236` maxDD `-4.9097`
- `market_context_high->index_4h` score `3.031` n `157` status `ready` deltaP `22.1318` edge `0.1734` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.9273` n `156` status `ready` deltaP `27.4172` edge `0.5932` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.4017` n `33` status `ready` deltaP `31.19` edge `0.0106` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.1836` n `156` status `ready` deltaP `22.1154` edge `0.9911` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.4653` n `33` status `ready` deltaP `18.1911` edge `0.1389` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.1205` n `39` status `ready` deltaP `20.8967` edge `0.001` maxDD `-1.7548`
- `market_context_high->equity_1h` score `0.8062` n `157` status `ready` deltaP `9.9928` edge `0.0794` maxDD `-2.6402`
- `news_risk_high->fx_1h` score `0.596` n `39` status `ready` deltaP `9.5732` edge `0.0115` maxDD `-0.0524`
- `market_context_high->metal_1h` score `0.5925` n `157` status `ready` deltaP `9.0097` edge `0.0563` maxDD `-2.3594`
- `market_context_high->metal_24h` score `0.5754` n `156` status `ready` deltaP `13.0476` edge `0.3769` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
