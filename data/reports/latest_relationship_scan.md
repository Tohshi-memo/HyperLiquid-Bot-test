# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T21:07:33.413170+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11235`

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

- `news_risk_high->unknown_4h` score `369.8712` n `83` status `ready` deltaP `-20.9007` edge `31.0514` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `18.5151` n `83` status `ready` deltaP `42.1708` edge `1.3997` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `16.9784` n `83` status `ready` deltaP `34.5842` edge `1.3838` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `13.3404` n `83` status `ready` deltaP `43.817` edge `0.997` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.0465` n `83` status `ready` deltaP `49.247` edge `0.2765` maxDD `-0.075`
- `risk_on_high->commodity_24h` score `6.5234` n `52` status `ready` deltaP `39.0625` edge `0.2832` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.5234` n `52` status `ready` deltaP `39.0625` edge `0.2832` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.281` n `83` status `ready` deltaP `32.6849` edge `0.2676` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `5.2243` n `149` status `ready` deltaP `32.3511` edge `0.2722` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.4628` n `52` status `ready` deltaP `30.4057` edge `0.0375` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.4628` n `52` status `ready` deltaP `30.4057` edge `0.0375` maxDD `-0.1313`
- `risk_on_high->fx_24h` score `2.4144` n `52` status `ready` deltaP `32.1047` edge `-0.0086` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4144` n `52` status `ready` deltaP `32.1047` edge `-0.0086` maxDD `-0.0054`
- `market_context_high->commodity_4h` score `2.3625` n `149` status `ready` deltaP `26.908` edge `0.0593` maxDD `-0.345`
- `market_context_high->fx_24h` score `2.2795` n `149` status `ready` deltaP `29.3298` edge `0.016` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `0.9432` n `149` status `ready` deltaP `14.5642` edge `0.0192` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.4195` n `83` status `ready` deltaP `12.4982` edge `0.0333` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3199` n `52` status `ready` deltaP `7.6463` edge `0.0109` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3199` n `52` status `ready` deltaP `7.6463` edge `0.0109` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1716` n `52` status `ready` deltaP `6.5638` edge `0.0088` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
