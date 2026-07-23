# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T20:33:34.183258+00:00`
- Price records: `672`
- Market context records: `7704`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `3.6255` n `132` status `ready` deltaP `19.396` edge `0.307` maxDD `-6.0681`
- `market_context_high->crypto_major_4h` score `1.2776` n `133` status `ready` deltaP `15.5659` edge `0.1745` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0957` n `133` status `ready` deltaP `13.1579` edge `0.0477` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.8245` n `133` status `ready` deltaP `8.8093` edge `0.1217` maxDD `-3.9374`
- `market_context_high->equity_4h` score `0.8088` n `133` status `ready` deltaP `3.1926` edge `0.2737` maxDD `-6.9701`
- `market_context_high->equity_1h` score `0.6506` n `133` status `ready` deltaP `8.6466` edge `0.0825` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.3854` n `133` status `ready` deltaP `8.9447` edge `0.0155` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1413` n `133` status `ready` deltaP `3.5298` edge `0.0315` maxDD `-1.4603`
- `market_context_high->fx_24h` score `-0.0471` n `132` status `ready` deltaP `11.9444` edge `0.0231` maxDD `-3.0343`
- `market_context_high->index_4h` score `-0.1145` n `133` status `ready` deltaP `12.5463` edge `0.0475` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `-0.2036` n `133` status `ready` deltaP `3.3948` edge `0.0063` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.2896` n `133` status `ready` deltaP `3.2581` edge `0.0135` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.5311` n `133` status `ready` deltaP `-0.6773` edge `-0.001` maxDD `-0.4331`
- `market_context_high->metal_24h` score `-0.5794` n `133` status `ready` deltaP `3.0284` edge `0.1406` maxDD `-2.3927`
- `market_context_high->metal_1h` score `-0.8399` n `133` status `ready` deltaP `1.5668` edge `0.0199` maxDD `-0.6936`
- `market_context_high->unknown_1h` score `-1.3009` n `133` status `ready` deltaP `-0.5256` edge `-0.0459` maxDD `-1.054`
- `market_context_high->metal_4h` score `-1.4101` n `133` status `ready` deltaP `1.7479` edge `0.0763` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5703` n `133` status `ready` deltaP `-5.2321` edge `-0.0036` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7357` n `132` status `ready` deltaP `5.6858` edge `-0.0242` maxDD `-7.0012`
- `market_context_high->unknown_4h` score `-2.2519` n `133` status `ready` deltaP `15.3023` edge `-0.164` maxDD `-1.7206`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
