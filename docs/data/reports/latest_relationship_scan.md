# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T09:52:29.814298+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8658`

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

- `news_risk_high->unknown_4h` score `384.6436` n `83` status `ready` deltaP `-21.5105` edge `32.2865` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `13.6922` n `83` status `ready` deltaP `33.6638` edge `1.0545` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `12.8356` n `83` status `ready` deltaP `25.73` edge `1.0976` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `9.3309` n `83` status `ready` deltaP `34.9628` edge `0.7219` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `8.8757` n `52` status `ready` deltaP `47.9167` edge `0.4202` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8757` n `52` status `ready` deltaP `47.9167` edge `0.4202` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5766` n `149` status `ready` deltaP `41.2053` edge `0.4092` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.911` n `83` status `ready` deltaP `40.3928` edge `0.2409` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.0834` n `83` status `ready` deltaP `31.4696` edge `0.1759` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.5819` n `52` status `ready` deltaP `33.4936` edge `-0.0039` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.5819` n `52` status `ready` deltaP `33.4936` edge `-0.0039` maxDD `-0.0054`
- `risk_on_high->commodity_4h` score `2.49` n `52` status `ready` deltaP `30.1008` edge `0.0418` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.49` n `52` status `ready` deltaP `30.1008` edge `0.0418` maxDD `-0.1313`
- `market_context_high->fx_24h` score `2.447` n `149` status `ready` deltaP `30.7187` edge `0.0207` maxDD `-0.0593`
- `market_context_high->commodity_4h` score `2.3897` n `149` status `ready` deltaP `26.6031` edge `0.0636` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9983` n `149` status `ready` deltaP `15.163` edge `0.0198` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.375` n `52` status `ready` deltaP `8.2451` edge `0.0115` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.375` n `52` status `ready` deltaP `8.2451` edge `0.0115` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.2759` n `83` status `ready` deltaP `10.5165` edge `0.0281` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.0672` n `52` status `ready` deltaP `5.0668` edge `0.0054` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
