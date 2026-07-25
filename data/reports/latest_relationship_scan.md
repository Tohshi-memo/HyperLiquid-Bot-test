# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T19:37:26.287563+00:00`
- Price records: `672`
- Market context records: `7911`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14745`

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

- `market_context_high->equity_24h` score `15.9102` n `90` status `ready` deltaP `28.1598` edge `1.2723` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.7897` n `90` status `ready` deltaP `38.7503` edge `0.395` maxDD `-0.0021`
- `market_context_high->equity_4h` score `6.1871` n `98` status `ready` deltaP `22.8109` edge `0.4528` maxDD `-5.1426`
- `market_context_high->index_4h` score `2.5334` n `98` status `ready` deltaP `26.281` edge `0.0719` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.3225` n `98` status `ready` deltaP `20.7722` edge `0.1173` maxDD `-0.979`
- `market_context_high->commodity_24h` score `2.1599` n `90` status `ready` deltaP `20.5555` edge `0.2013` maxDD `-7.0012`
- `market_context_high->index_24h` score `1.6444` n `90` status `ready` deltaP `8.2292` edge `0.1492` maxDD `-1.3621`
- `market_context_high->crypto_alt_4h` score `1.5329` n `98` status `ready` deltaP `11.5885` edge `0.1622` maxDD `-3.9374`
- `market_context_high->equity_1h` score `1.4464` n `99` status `ready` deltaP `11.234` edge `0.1274` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `1.1839` n `98` status `ready` deltaP `12.7146` edge `0.1857` maxDD `-6.7444`
- `market_context_high->fx_24h` score `1.0891` n `90` status `ready` deltaP `30.7639` edge `0.0433` maxDD `-3.0343`
- `market_context_high->crypto_major_1h` score `0.9759` n `99` status `ready` deltaP `12.0275` edge `0.042` maxDD `-1.6021`
- `market_context_high->index_1h` score `0.916` n `99` status `ready` deltaP `14.6465` edge `0.0217` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.5551` n `99` status `ready` deltaP `8.3243` edge `0.0286` maxDD `-0.6936`
- `market_context_high->crypto_alt_1h` score `0.2577` n `99` status `ready` deltaP `5.5934` edge `0.039` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.1078` n `99` status `ready` deltaP `3.1669` edge `0.0018` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.15` n `98` status `ready` deltaP `7.3394` edge `0.0066` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.3368` n `98` status `ready` deltaP `2.9146` edge `0.0133` maxDD `-2.4066`
- `market_context_high->commodity_1h` score `-0.7421` n `99` status `ready` deltaP `-0.1774` edge `-0.0038` maxDD `-1.5486`
- `market_context_high->unknown_1h` score `-2.0668` n `99` status `ready` deltaP `7.1267` edge `-0.1774` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
