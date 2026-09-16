# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T20:07:28.213320+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11059`

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

- `news_risk_high->unknown_4h` score `369.1248` n `83` status `ready` deltaP `-20.9007` edge `30.9892` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `18.8381` n `83` status `ready` deltaP `42.518` edge `1.4243` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `17.3375` n `83` status `ready` deltaP `35.2786` edge `1.4091` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `13.6384` n `83` status `ready` deltaP `44.5114` edge `1.0172` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.1321` n `83` status `ready` deltaP `49.9414` edge `0.279` maxDD `-0.075`
- `risk_on_high->commodity_24h` score `6.3298` n `52` status `ready` deltaP `38.3681` edge `0.2717` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.3298` n `52` status `ready` deltaP `38.3681` edge `0.2717` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.3638` n `83` status `ready` deltaP `32.6849` edge `0.2745` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `5.0307` n `149` status `ready` deltaP `31.6567` edge `0.2607` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.412` n `52` status `ready` deltaP `32.1047` edge `-0.0088` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.412` n `52` status `ready` deltaP `32.1047` edge `-0.0088` maxDD `-0.0054`
- `risk_on_high->commodity_4h` score `2.4044` n `52` status `ready` deltaP `29.796` edge `0.0367` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.4044` n `52` status `ready` deltaP `29.796` edge `0.0367` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.3041` n `149` status `ready` deltaP `26.2983` edge `0.0585` maxDD `-0.345`
- `market_context_high->fx_24h` score `2.2771` n `149` status `ready` deltaP `29.3298` edge `0.0158` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `0.93` n `149` status `ready` deltaP `14.4145` edge `0.0191` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3943` n `83` status `ready` deltaP `12.1933` edge `0.0321` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3067` n `52` status `ready` deltaP `7.4966` edge `0.0108` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3067` n `52` status `ready` deltaP `7.4966` edge `0.0108` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1988` n `52` status `ready` deltaP `7.0129` edge `0.0093` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
