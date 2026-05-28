# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T14:07:25.620824+00:00`
- Price records: `672`
- Market context records: `2148`
- Flow alert records: `8080`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9168`

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

- `market_context_high->crypto_alt_4h` score `13.6105` n `153` status `ready` deltaP `38.0161` edge `0.9744` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `12.0431` n `153` status `ready` deltaP `42.1778` edge `0.7754` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.499` n `153` status `ready` deltaP `25.1843` edge `0.4486` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `6.202` n `33` status `ready` deltaP `28.0442` edge `0.397` maxDD `-3.0367`
- `market_context_high->equity_4h` score `5.0691` n `153` status `ready` deltaP `26.366` edge `0.3561` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.7692` n `153` status `ready` deltaP `14.9612` edge `0.3372` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.5404` n `153` status `ready` deltaP `18.967` edge `0.2163` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.2884` n `153` status `ready` deltaP `16.9661` edge `0.2473` maxDD `-4.9097`
- `market_context_high->metal_4h` score `3.246` n `153` status `ready` deltaP `22.1773` edge `0.2614` maxDD `-4.7664`
- `market_context_high->index_4h` score `3.2041` n `153` status `ready` deltaP `23.1857` edge `0.1808` maxDD `-1.8022`
- `market_context_high->equity_24h` score `3.1587` n `153` status `ready` deltaP `26.4706` edge `0.5766` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.7706` n `153` status `ready` deltaP `27.0936` edge `0.5823` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.3421` n `33` status `ready` deltaP `30.5802` edge `0.0097` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.1578` n `153` status `ready` deltaP `21.3643` edge `0.9928` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.5429` n `33` status `ready` deltaP `18.6484` edge `0.1458` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.0231` n `42` status `ready` deltaP `18.2991` edge `0.0102` maxDD `-1.7548`
- `news_risk_high->commodity_1h` score `0.9242` n `42` status `ready` deltaP `11.7551` edge `0.1081` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.8607` n `153` status `ready` deltaP `10.4341` edge `0.081` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.6595` n `153` status `ready` deltaP `9.3675` edge `0.0595` maxDD `-2.3594`
- `news_risk_high->fx_1h` score `0.6076` n `42` status `ready` deltaP `9.8232` edge `0.0108` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
