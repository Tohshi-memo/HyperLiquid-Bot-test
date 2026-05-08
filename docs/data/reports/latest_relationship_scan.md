# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T13:52:21.505209+00:00`
- Price records: `651`
- Market context records: `761`
- Flow alert records: `2146`
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

- `market_context_high->crypto_major_24h` score `13.495` n `146` status `ready` deltaP `32.1412` edge `0.9437` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.8014` n `146` status `ready` deltaP `7.4232` edge `0.5221` maxDD `-0.0508`
- `risk_on_high->metal_1h` score `1.3104` n `32` status `ready` deltaP `15.1517` edge `0.0312` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.3104` n `32` status `ready` deltaP `15.1517` edge `0.0312` maxDD `-0.5074`
- `market_context_high->index_24h` score `0.5855` n `146` status `ready` deltaP `3.3153` edge `0.2262` maxDD `-5.9609`
- `risk_on_high->fx_1h` score `0.426` n `32` status `ready` deltaP `10.5706` edge `0.0031` maxDD `-0.1827`
- `risk_on_and_context->fx_1h` score `0.426` n `32` status `ready` deltaP `10.5706` edge `0.0031` maxDD `-0.1827`
- `risk_on_high->commodity_1h` score `0.2242` n `32` status `ready` deltaP `6.9353` edge `0.0201` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2242` n `32` status `ready` deltaP `6.9353` edge `0.0201` maxDD `-0.6739`
- `risk_on_high->crypto_major_1h` score `0.1454` n `32` status `ready` deltaP `7.1339` edge `-0.0004` maxDD `-0.948`
- `risk_on_and_context->crypto_major_1h` score `0.1454` n `32` status `ready` deltaP `7.1339` edge `-0.0004` maxDD `-0.948`
- `market_context_high->equity_24h` score `0.0527` n `146` status `ready` deltaP `1.8398` edge `0.2526` maxDD `-10.5047`
- `risk_on_high->crypto_alt_1h` score `-0.3187` n `32` status `ready` deltaP `3.9219` edge `-0.0203` maxDD `-0.9258`
- `risk_on_and_context->crypto_alt_1h` score `-0.3187` n `32` status `ready` deltaP `3.9219` edge `-0.0203` maxDD `-0.9258`
- `risk_on_high->index_1h` score `-0.3386` n `32` status `ready` deltaP `-1.4337` edge `0.0097` maxDD `-0.2687`
- `risk_on_and_context->index_1h` score `-0.3386` n `32` status `ready` deltaP `-1.4337` edge `0.0097` maxDD `-0.2687`
- `market_context_high->fx_1h` score `-0.5102` n `177` status `ready` deltaP `2.0077` edge `0.0019` maxDD `-0.291`
- `market_context_high->fx_4h` score `-0.5386` n `165` status `ready` deltaP `5.0637` edge `0.0085` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.624` n `177` status `ready` deltaP `1.2679` edge `0.037` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.6314` n `177` status `ready` deltaP `-0.5281` edge `0.0036` maxDD `-4.4826`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
