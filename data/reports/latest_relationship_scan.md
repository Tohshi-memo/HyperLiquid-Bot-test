# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T05:07:28.990873+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11210`

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

- `market_context_high->unknown_1h` score `86.1837` n `47` status `ready` deltaP `8.7687` edge `7.1306` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.9696` n `47` status `ready` deltaP `30.5962` edge `3.9161` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.9396` n `47` status `ready` deltaP `24.782` edge `2.5344` maxDD `-2.7051`
- `market_context_high->equity_24h` score `26.1058` n `47` status `ready` deltaP `34.7628` edge `1.9793` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.2803` n `47` status `ready` deltaP `39.1031` edge `0.4423` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.7267` n `47` status `ready` deltaP `39.9195` edge `0.1516` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.5835` n `54` status `ready` deltaP `30.3819` edge `0.1309` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9631` n `47` status `ready` deltaP `33.8739` edge `0.0365` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5691` n `47` status `ready` deltaP `17.1445` edge `0.1416` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `1.387` n `116` status `ready` deltaP `12.3065` edge `0.1246` maxDD `-4.2849`
- `market_context_high->equity_1h` score `0.975` n `47` status `ready` deltaP `11.7658` edge `0.0431` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `0.9606` n `47` status `ready` deltaP `9.0782` edge `0.0863` maxDD `-3.3417`
- `market_context_high->index_1h` score `0.9595` n `47` status `ready` deltaP `14.6101` edge `0.0104` maxDD `-0.2275`
- `news_risk_high->crypto_major_1h` score `0.5478` n `116` status `ready` deltaP `8.7033` edge `0.0622` maxDD `-3.2991`
- `market_context_high->fx_1h` score `0.3536` n `47` status `ready` deltaP `8.7622` edge `0.0067` maxDD `-0.1854`
- `news_risk_high->metal_1h` score `0.1825` n `116` status `ready` deltaP `9.2504` edge `0.0117` maxDD `-0.6526`
- `market_context_high->metal_1h` score `0.0492` n `47` status `ready` deltaP `3.8763` edge `0.0121` maxDD `-0.1976`
- `market_context_high->crypto_major_1h` score `-0.1361` n `47` status `ready` deltaP `2.357` edge `0.0547` maxDD `-4.5405`
- `news_risk_high->equity_1h` score `-0.2049` n `116` status `ready` deltaP `0.9808` edge `0.0252` maxDD `-2.6402`
- `market_context_high->metal_4h` score `-0.2621` n `47` status `ready` deltaP `-2.8672` edge `0.0239` maxDD `-0.404`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
