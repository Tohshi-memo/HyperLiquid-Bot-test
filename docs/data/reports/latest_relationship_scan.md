# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T10:07:25.812266+00:00`
- Price records: `672`
- Market context records: `8185`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5904`

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

- `news_risk_high->unknown_24h` score `8627.7147` n `43` status `ready` deltaP `36.9792` edge `718.7297` maxDD `0.0`
- `market_context_high->equity_24h` score `19.8595` n `47` status `ready` deltaP `43.0481` edge `1.459` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.87` n `48` status `ready` deltaP `44.8679` edge `0.611` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.6369` n `47` status `ready` deltaP `44.2708` edge `0.4246` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.8655` n `50` status `ready` deltaP `28.9512` edge `0.4918` maxDD `-1.3479`
- `market_context_high->crypto_alt_24h` score `4.5031` n `47` status `ready` deltaP `10.871` edge `0.7662` maxDD `-12.5753`
- `market_context_high->index_4h` score `4.244` n `48` status `ready` deltaP `37.9573` edge `0.1049` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.2022` n `48` status `ready` deltaP `31.9106` edge `0.0759` maxDD `-0.4094`
- `market_context_high->equity_1h` score `3.1684` n `48` status `ready` deltaP `16.5045` edge `0.1729` maxDD `-0.512`
- `news_risk_high->crypto_major_4h` score `3.0712` n `50` status `ready` deltaP `16.2683` edge `0.3484` maxDD `-2.382`
- `news_risk_high->equity_1h` score `2.9082` n `54` status `ready` deltaP `21.8286` edge `0.1277` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.8143` n `50` status `ready` deltaP `24.2073` edge `0.0922` maxDD `-0.191`
- `market_context_high->index_24h` score `2.1487` n `47` status `ready` deltaP `19.0344` edge `0.215` maxDD `-1.3142`
- `news_risk_high->crypto_major_1h` score `1.9733` n `54` status `ready` deltaP `13.4509` edge `0.1145` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.8411` n `54` status `ready` deltaP `14.8536` edge `0.0978` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.3933` n `50` status `ready` deltaP `16.7256` edge `0.2063` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.3116` n `50` status `ready` deltaP `12.4939` edge `0.0728` maxDD `-0.7433`
- `market_context_high->fx_24h` score `1.2571` n `47` status `ready` deltaP `24.7193` edge `0.0612` maxDD `-0.5196`
- `market_context_high->index_1h` score `1.2179` n `48` status `ready` deltaP `21.5818` edge `0.0261` maxDD `-0.1069`
- `market_context_high->crypto_major_24h` score `1.0011` n `47` status `ready` deltaP `10.3502` edge `0.5282` maxDD `-29.1746`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
