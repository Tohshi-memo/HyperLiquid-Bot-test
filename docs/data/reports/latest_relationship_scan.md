# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T09:37:25.170003+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11898`

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

- `risk_on_high->crypto_alt_24h` score `15.7761` n `91` status `ready` deltaP `32.8736` edge `1.1185` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `15.7761` n `91` status `ready` deltaP `32.8736` edge `1.1185` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `11.2937` n `202` status `ready` deltaP `24.5067` edge `0.8605` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.7122` n `91` status `ready` deltaP `39.202` edge `0.4185` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.7122` n `91` status `ready` deltaP `39.202` edge `0.4185` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.8424` n `91` status `ready` deltaP `29.0003` edge `0.3794` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.8424` n `91` status `ready` deltaP `29.0003` edge `0.3794` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `5.0071` n `91` status `ready` deltaP `21.7224` edge `0.9039` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.0071` n `91` status `ready` deltaP `21.7224` edge `0.9039` maxDD `-24.5429`
- `risk_on_high->index_24h` score `3.1874` n `91` status `ready` deltaP `33.6825` edge `0.0453` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.1874` n `91` status `ready` deltaP `33.6825` edge `0.0453` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.7806` n `202` status `ready` deltaP `17.8819` edge `0.1125` maxDD `0.0`
- `market_context_high->index_24h` score `2.3396` n `202` status `ready` deltaP `28.0683` edge `0.0472` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `1.9137` n `91` status `ready` deltaP `25.8761` edge `-0.0037` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `1.9137` n `91` status `ready` deltaP `25.8761` edge `-0.0037` maxDD `-0.0802`
- `risk_on_high->commodity_24h` score `1.908` n `91` status `ready` deltaP `18.2921` edge `0.0464` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.908` n `91` status `ready` deltaP `18.2921` edge `0.0464` maxDD `-0.0811`
- `market_context_high->commodity_24h` score `1.7707` n `202` status `ready` deltaP `18.1724` edge `0.0478` maxDD `-0.3779`
- `risk_on_high->equity_1h` score `1.121` n `91` status `ready` deltaP `17.8901` edge `0.002` maxDD `-0.228`
- `risk_on_and_context->equity_1h` score `1.121` n `91` status `ready` deltaP `17.8901` edge `0.002` maxDD `-0.228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
