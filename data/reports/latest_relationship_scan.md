# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T13:22:21.079170+00:00`
- Price records: `649`
- Market context records: `759`
- Flow alert records: `2140`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1117`

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

- `market_context_high->crypto_major_24h` score `13.4141` n `146` status `ready` deltaP `31.9255` edge `0.9384` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.775` n `146` status `ready` deltaP `7.4525` edge `0.5197` maxDD `-0.0508`
- `risk_on_high->metal_1h` score `1.32` n `32` status `ready` deltaP `15.2859` edge `0.0311` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.32` n `32` status `ready` deltaP `15.2859` edge `0.0311` maxDD `-0.5074`
- `market_context_high->index_24h` score `0.5862` n `146` status `ready` deltaP `3.4296` edge `0.2255` maxDD `-5.9609`
- `risk_on_high->fx_1h` score `0.4171` n `32` status `ready` deltaP `10.3988` edge `0.0031` maxDD `-0.1827`
- `risk_on_and_context->fx_1h` score `0.4171` n `32` status `ready` deltaP `10.3988` edge `0.0031` maxDD `-0.1827`
- `risk_on_high->commodity_1h` score `0.2152` n `32` status `ready` deltaP `6.7911` edge `0.0199` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2152` n `32` status `ready` deltaP `6.7911` edge `0.0199` maxDD `-0.6739`
- `risk_on_high->crypto_major_1h` score `0.13` n `32` status `ready` deltaP `6.9719` edge `-0.0013` maxDD `-0.948`
- `risk_on_and_context->crypto_major_1h` score `0.13` n `32` status `ready` deltaP `6.9719` edge `-0.0013` maxDD `-0.948`
- `market_context_high->equity_24h` score `0.0448` n `146` status `ready` deltaP `1.9363` edge `0.2513` maxDD `-10.5047`
- `risk_on_high->index_1h` score `-0.3365` n `32` status `ready` deltaP `-1.4674` edge `0.0101` maxDD `-0.2687`
- `risk_on_and_context->index_1h` score `-0.3365` n `32` status `ready` deltaP `-1.4674` edge `0.0101` maxDD `-0.2687`
- `risk_on_high->crypto_alt_1h` score `-0.3428` n `32` status `ready` deltaP `3.7403` edge `-0.0211` maxDD `-0.9258`
- `risk_on_and_context->crypto_alt_1h` score `-0.3428` n `32` status `ready` deltaP `3.7403` edge `-0.0211` maxDD `-0.9258`
- `market_context_high->fx_1h` score `-0.4682` n `175` status `ready` deltaP `2.4881` edge `0.0022` maxDD `-0.291`
- `market_context_high->fx_4h` score `-0.4874` n `163` status `ready` deltaP `5.6141` edge `0.0091` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.5801` n `175` status `ready` deltaP `1.6661` edge `0.038` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.6666` n `175` status `ready` deltaP `-0.8442` edge `0.0012` maxDD `-4.4826`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
