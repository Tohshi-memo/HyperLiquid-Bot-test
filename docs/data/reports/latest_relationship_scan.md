# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T12:00:25.256053+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11471`

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

- `news_risk_high->unknown_4h` score `367.6306` n `83` status `ready` deltaP `-21.0531` edge `30.8657` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `23.8215` n `78` status `ready` deltaP `47.7698` edge `1.7057` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `21.0073` n `78` status `ready` deltaP `39.7303` edge `1.6328` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.0648` n `78` status `ready` deltaP `47.5961` edge `1.1155` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.7561` n `78` status `ready` deltaP `54.1266` edge `0.3031` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.5801` n `78` status `ready` deltaP `37.7938` edge `0.3418` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.3478` n `52` status `ready` deltaP `34.0278` edge `0.2188` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.3478` n `52` status `ready` deltaP `34.0278` edge `0.2188` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.0487` n `149` status `ready` deltaP `27.3164` edge `0.2078` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3645` n `52` status `ready` deltaP `31.9311` edge `-0.0116` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3645` n `52` status `ready` deltaP `31.9311` edge `-0.0116` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2296` n `149` status `ready` deltaP `29.1562` edge `0.013` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1306` n `52` status `ready` deltaP `27.8143` edge `0.0271` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1306` n `52` status `ready` deltaP `27.8143` edge `0.0271` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.0304` n `149` status `ready` deltaP `24.3166` edge `0.0489` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8964` n `149` status `ready` deltaP `14.2648` edge `0.0173` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5386` n `83` status `ready` deltaP `14.9372` edge `0.0323` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.5332` n `52` status `ready` deltaP `10.6121` edge `0.1591` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.5332` n `52` status `ready` deltaP `10.6121` edge `0.1591` maxDD `-6.2526`
- `risk_on_high->commodity_1h` score `0.2731` n `52` status `ready` deltaP `7.3469` edge `0.009` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
