# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T15:07:28.829877+00:00`
- Price records: `672`
- Market context records: `7785`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `7.5203` n `132` status `ready` deltaP `28.1068` edge `0.5735` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.5221` n `133` status `ready` deltaP `14.3131` edge `0.2405` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `1.0465` n `133` status `ready` deltaP `13.1579` edge `0.0436` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `0.9285` n `133` status `ready` deltaP `13.7367` edge `0.1576` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.896` n `133` status `ready` deltaP `3.0397` edge `0.2859` maxDD `-6.9701`
- `market_context_high->fx_24h` score `0.7718` n `132` status `ready` deltaP `24.6622` edge `0.0433` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `0.7314` n `133` status `ready` deltaP `8.1996` edge `0.118` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.695` n `133` status `ready` deltaP `8.046` edge `0.0902` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.3458` n `133` status `ready` deltaP `8.3441` edge `0.0162` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2204` n `133` status `ready` deltaP `4.5777` edge `0.0311` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `0.2195` n `133` status `ready` deltaP `6.622` edge `0.0335` maxDD `-1.0817`
- `market_context_high->commodity_1h` score `-0.0499` n `133` status `ready` deltaP `4.7461` edge `0.0101` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1822` n `133` status `ready` deltaP `11.1701` edge `0.048` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3618` n `133` status `ready` deltaP `1.2746` edge `0.0001` maxDD `-0.4331`
- `market_context_high->commodity_24h` score `-0.6091` n `132` status `ready` deltaP `10.7381` edge `0.036` maxDD `-7.0012`
- `market_context_high->metal_1h` score `-0.9345` n `133` status `ready` deltaP `0.5189` edge `0.019` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3366` n `133` status `ready` deltaP `-1.5624` edge `0.0019` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5293` n `133` status `ready` deltaP `0.5283` edge `0.0745` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.7372` n `132` status `ready` deltaP `-10.614` edge `0.0583` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.445` n `133` status `ready` deltaP `14.6643` edge `0.1183` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
