# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T07:22:30.953208+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8682`

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

- `news_risk_high->unknown_4h` score `384.676` n `83` status `ready` deltaP `-21.5105` edge `32.2892` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `14.8199` n `83` status `ready` deltaP `35.3999` edge `1.1369` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `13.6837` n `83` status `ready` deltaP `27.4661` edge `1.1567` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `10.0386` n `83` status `ready` deltaP `36.6989` edge `0.7693` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `8.4788` n `52` status `ready` deltaP `46.1806` edge `0.3987` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.4788` n `52` status `ready` deltaP `46.1806` edge `0.3987` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.1797` n `149` status `ready` deltaP `39.4692` edge `0.3877` maxDD `-0.8682`
- `news_risk_high->index_24h` score `6.1183` n `83` status `ready` deltaP `42.1289` edge `0.2466` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.3122` n `83` status `ready` deltaP `31.9905` edge `0.1915` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.6205` n `52` status `ready` deltaP `33.8408` edge `-0.003` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.6205` n `52` status `ready` deltaP `33.8408` edge `-0.003` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4856` n `149` status `ready` deltaP `31.0659` edge `0.0216` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.2852` n `52` status `ready` deltaP `28.5764` edge `0.0349` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2852` n `52` status `ready` deltaP `28.5764` edge `0.0349` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.1849` n `149` status `ready` deltaP `25.0787` edge `0.0567` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9515` n `149` status `ready` deltaP `14.7139` edge `0.0189` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.373` n `83` status `ready` deltaP `11.8884` edge `0.0314` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3283` n `52` status `ready` deltaP `7.796` edge `0.0106` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3283` n `52` status `ready` deltaP `7.796` edge `0.0106` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1062` n `52` status `ready` deltaP `5.6656` edge `0.0064` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
