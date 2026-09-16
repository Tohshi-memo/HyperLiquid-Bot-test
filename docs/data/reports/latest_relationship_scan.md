# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T19:07:33.873314+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11293`

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

- `news_risk_high->unknown_4h` score `367.3428` n `83` status `ready` deltaP `-20.9007` edge `30.8407` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `19.1105` n `83` status `ready` deltaP `42.518` edge `1.447` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `17.6804` n `83` status `ready` deltaP `35.7994` edge `1.4342` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `13.8745` n `83` status `ready` deltaP `45.0323` edge `1.0334` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.1838` n `83` status `ready` deltaP `50.2887` edge `0.281` maxDD `-0.075`
- `risk_on_high->commodity_24h` score `6.1399` n `52` status `ready` deltaP `37.6736` edge `0.2605` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1399` n `52` status `ready` deltaP `37.6736` edge `0.2605` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.4418` n `83` status `ready` deltaP `32.6849` edge `0.281` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.8407` n `149` status `ready` deltaP `30.9622` edge `0.2495` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.4096` n `52` status `ready` deltaP `32.1047` edge `-0.009` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4096` n `52` status `ready` deltaP `32.1047` edge `-0.009` maxDD `-0.0054`
- `risk_on_high->commodity_4h` score `2.357` n `52` status `ready` deltaP `29.3386` edge `0.0358` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.357` n `52` status `ready` deltaP `29.3386` edge `0.0358` maxDD `-0.1313`
- `market_context_high->fx_24h` score `2.2747` n `149` status `ready` deltaP `29.3298` edge `0.0156` maxDD `-0.0593`
- `market_context_high->commodity_4h` score `2.2567` n `149` status `ready` deltaP `25.8409` edge `0.0576` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9024` n `149` status `ready` deltaP `14.1151` edge `0.0188` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3716` n `83` status `ready` deltaP `12.0408` edge `0.0302` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2792` n `52` status `ready` deltaP `7.1972` edge `0.0105` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2792` n `52` status `ready` deltaP `7.1972` edge `0.0105` maxDD `-0.1507`
- `risk_on_high->crypto_alt_4h` score `0.2403` n `52` status `ready` deltaP `9.2402` edge `0.1307` maxDD `-6.2526`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
