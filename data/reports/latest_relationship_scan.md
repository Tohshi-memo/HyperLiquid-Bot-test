# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T18:37:32.938676+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11713`

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

- `news_risk_high->unknown_4h` score `366.1428` n `83` status `ready` deltaP `-20.9007` edge `30.7407` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `19.5665` n `82` status `ready` deltaP `43.5171` edge `1.4734` maxDD `-8.9708`
- `news_risk_high->crypto_major_24h` score `17.8983` n `82` status `ready` deltaP `35.8529` edge `1.452` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `13.9136` n `82` status `ready` deltaP `45.0415` edge `1.0366` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.2172` n `82` status `ready` deltaP `50.3007` edge `0.2837` maxDD `-0.075`
- `risk_on_high->commodity_24h` score `6.0473` n `52` status `ready` deltaP `37.3264` edge `0.2551` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0473` n `52` status `ready` deltaP `37.3264` edge `0.2551` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.6131` n `82` status `ready` deltaP `33.5959` edge `0.2892` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.7482` n `149` status `ready` deltaP `30.615` edge `0.2441` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.4072` n `52` status `ready` deltaP `32.1047` edge `-0.0092` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4072` n `52` status `ready` deltaP `32.1047` edge `-0.0092` maxDD `-0.0054`
- `risk_on_high->commodity_4h` score `2.3376` n `52` status `ready` deltaP `29.1862` edge `0.0352` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.3376` n `52` status `ready` deltaP `29.1862` edge `0.0352` maxDD `-0.1313`
- `market_context_high->fx_24h` score `2.2723` n `149` status `ready` deltaP `29.3298` edge `0.0154` maxDD `-0.0593`
- `market_context_high->commodity_4h` score `2.2373` n `149` status `ready` deltaP `25.6885` edge `0.057` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9024` n `149` status `ready` deltaP `14.1151` edge `0.0188` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3669` n `83` status `ready` deltaP `12.0408` edge `0.0296` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.3357` n `52` status `ready` deltaP `9.5451` edge `0.1409` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.3357` n `52` status `ready` deltaP `9.5451` edge `0.1409` maxDD `-6.2526`
- `risk_on_high->commodity_1h` score `0.2792` n `52` status `ready` deltaP `7.1972` edge `0.0105` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
