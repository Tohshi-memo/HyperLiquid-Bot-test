# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T21:52:26.167125+00:00`
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

- `news_risk_high->unknown_4h` score `372.0838` n `83` status `ready` deltaP `-21.0531` edge `31.2368` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `18.2635` n `83` status `ready` deltaP `41.6499` edge `1.3822` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `16.7471` n `83` status `ready` deltaP `34.0633` edge `1.368` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `13.1068` n `83` status `ready` deltaP `43.2961` edge `0.981` maxDD `-6.5262`
- `news_risk_high->index_24h` score `6.982` n `83` status `ready` deltaP `48.7262` edge `0.2746` maxDD `-0.075`
- `risk_on_high->commodity_24h` score `6.6731` n `52` status `ready` deltaP `39.5833` edge `0.2922` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.6731` n `52` status `ready` deltaP `39.5833` edge `0.2922` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.3739` n `149` status `ready` deltaP `32.8719` edge `0.2812` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `5.2198` n `83` status `ready` deltaP `32.6849` edge `0.2625` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.4348` n `52` status `ready` deltaP `30.1008` edge `0.0372` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.4348` n `52` status `ready` deltaP `30.1008` edge `0.0372` maxDD `-0.1313`
- `risk_on_high->fx_24h` score `2.4156` n `52` status `ready` deltaP `32.1047` edge `-0.0085` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4156` n `52` status `ready` deltaP `32.1047` edge `-0.0085` maxDD `-0.0054`
- `market_context_high->commodity_4h` score `2.3345` n `149` status `ready` deltaP `26.6031` edge `0.059` maxDD `-0.345`
- `market_context_high->fx_24h` score `2.2807` n `149` status `ready` deltaP `29.3298` edge `0.0161` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `0.9312` n `149` status `ready` deltaP `14.4145` edge `0.0192` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.4416` n `83` status `ready` deltaP `12.803` edge `0.0341` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3079` n `52` status `ready` deltaP `7.4966` edge `0.0109` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3079` n `52` status `ready` deltaP `7.4966` edge `0.0109` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1794` n `52` status `ready` deltaP `6.7135` edge `0.0088` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
