# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T00:52:33.050666+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11041`

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

- `market_context_high->unknown_1h` score `83.882` n `47` status `ready` deltaP `9.5172` edge `6.9338` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.3261` n `47` status `ready` deltaP `30.4226` edge `3.7803` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.156` n `47` status `ready` deltaP `24.782` edge `2.4691` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.8423` n `47` status `ready` deltaP `34.5892` edge `1.9585` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `10.0341` n `114` status `ready` deltaP `-1.1398` edge `0.8682` maxDD `-0.9543`
- `market_context_high->index_24h` score `8.1868` n `47` status `ready` deltaP `38.2351` edge `0.4403` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.4368` n `47` status `ready` deltaP `37.3153` edge `0.1448` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.3667` n `66` status `ready` deltaP `31.392` edge `0.1061` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9499` n `47` status `ready` deltaP `33.8739` edge `0.0354` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.7813` n `114` status `ready` deltaP `14.7022` edge `0.1847` maxDD `-1.7416`
- `market_context_high->equity_4h` score `2.4347` n `47` status `ready` deltaP `17.1445` edge `0.1304` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `1.946` n `114` status `ready` deltaP `15.343` edge `0.1158` maxDD `-2.4737`
- `news_risk_high->metal_1h` score `1.1594` n `114` status `ready` deltaP `15.8735` edge `0.0193` maxDD `-0.6142`
- `market_context_high->index_1h` score `0.9319` n `47` status `ready` deltaP `14.3107` edge `0.0101` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8731` n `47` status `ready` deltaP `11.0173` edge `0.0396` maxDD `-1.5564`
- `news_risk_high->fx_4h` score `0.6749` n `102` status `ready` deltaP `14.135` edge `0.0256` maxDD `-0.421`
- `market_context_high->crypto_alt_4h` score `0.3257` n `47` status `ready` deltaP `7.0965` edge `0.0466` maxDD `-3.3417`
- `market_context_high->fx_1h` score `0.229` n `47` status `ready` deltaP `7.4149` edge `0.0053` maxDD `-0.1854`
- `news_risk_high->equity_1h` score `0.0545` n `114` status `ready` deltaP `3.8318` edge `0.037` maxDD `-2.6402`
- `news_risk_high->metal_24h` score `0.0002` n `66` status `ready` deltaP `17.3927` edge `0.0289` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
