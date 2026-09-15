# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T00:37:33.486164+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10788`

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

- `news_risk_high->unknown_4h` score `397.8776` n `78` status `ready` deltaP `-22.4554` edge `33.3955` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `24.5719` n `78` status `ready` deltaP `18.9236` edge `1.9215` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.282` n `78` status `ready` deltaP `44.2976` edge `1.5173` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.7445` n `78` status `ready` deltaP `32.265` edge `1.244` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.1539` n `78` status `ready` deltaP `43.9503` edge `1.0645` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6929` n `78` status `ready` deltaP `61.5918` edge `0.3314` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4529` n `78` status `ready` deltaP `37.7938` edge `0.3312` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.9793` n `52` status `ready` deltaP `38.0208` edge `0.2448` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9793` n `52` status `ready` deltaP `38.0208` edge `0.2448` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.6823` n `137` status `ready` deltaP `30.7215` edge `0.2379` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `4.2471` n `52` status `ready` deltaP `47.9033` edge `0.0388` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.2471` n `52` status `ready` deltaP `47.9033` edge `0.0388` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.8501` n `137` status `ready` deltaP `44.7169` edge `0.0443` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9391` n `52` status `ready` deltaP `25.3752` edge `0.0274` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9391` n `52` status `ready` deltaP `25.3752` edge `0.0274` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7395` n `137` status `ready` deltaP `20.7851` edge `0.0482` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.7269` n `78` status `ready` deltaP `17.2686` edge `0.0409` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.7238` n `138` status `ready` deltaP `12.1518` edge `0.017` maxDD `-0.3491`
- `risk_on_high->metal_1h` score `0.223` n `52` status `ready` deltaP `7.6117` edge `0.0084` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.223` n `52` status `ready` deltaP `7.6117` edge `0.0084` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
