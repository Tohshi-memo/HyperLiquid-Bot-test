# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T19:22:26.729363+00:00`
- Price records: `672`
- Market context records: `7803`
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

- `market_context_high->equity_24h` score `8.1834` n `132` status `ready` deltaP `28.5507` edge `0.6258` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.3909` n `133` status `ready` deltaP `13.0178` edge `0.2382` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `1.1709` n `133` status `ready` deltaP `14.5764` edge `0.1722` maxDD `-6.7444`
- `market_context_high->equity_4h` score `1.1295` n `133` status `ready` deltaP `4.036` edge `0.3092` maxDD `-6.9701`
- `market_context_high->crypto_major_1h` score `1.1041` n `133` status `ready` deltaP `13.4573` edge `0.0464` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.8171` n `132` status `ready` deltaP `25.2187` edge `0.0454` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.8018` n `133` status `ready` deltaP `8.3463` edge `0.0971` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.7621` n `133` status `ready` deltaP `7.8186` edge `0.1231` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.5376` n `133` status `ready` deltaP `9.0088` edge `0.0441` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3938` n `133` status `ready` deltaP `8.7946` edge `0.0172` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2923` n `133` status `ready` deltaP `5.1765` edge `0.0331` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0473` n `133` status `ready` deltaP `5.4969` edge `0.0132` maxDD `-0.6722`
- `market_context_high->commodity_24h` score `-0.0154` n `132` status `ready` deltaP `13.6443` edge `0.0661` maxDD `-7.0012`
- `market_context_high->index_4h` score `-0.1511` n `133` status `ready` deltaP `11.7075` edge `0.0484` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.321` n `133` status `ready` deltaP `1.7251` edge `0.0005` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8662` n `133` status `ready` deltaP `1.2674` edge `0.0197` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3326` n `133` status `ready` deltaP `-1.5014` edge `0.002` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.624` n `133` status `ready` deltaP `-0.4612` edge `0.0732` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.628` n `132` status `ready` deltaP `-9.4875` edge `0.0648` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.3068` n `133` status `ready` deltaP `14.7431` edge `0.1355` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
