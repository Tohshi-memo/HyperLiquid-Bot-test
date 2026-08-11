# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T15:52:42.985614+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `20.1829` n `135` status `ready` deltaP `-20.0526` edge `2.061` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `2.8622` n `32` status `ready` deltaP `19.2835` edge `0.1282` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8622` n `32` status `ready` deltaP `19.2835` edge `0.1282` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.3079` n `32` status `ready` deltaP `13.2111` edge `0.0442` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3079` n `32` status `ready` deltaP `13.2111` edge `0.0442` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `1.0412` n `32` status `ready` deltaP `11.9665` edge `0.0211` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0412` n `32` status `ready` deltaP `11.9665` edge `0.0211` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.8687` n `182` status `ready` deltaP `12.0376` edge `0.0636` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7931` n `182` status `ready` deltaP `10.3952` edge `0.0305` maxDD `-0.6965`
- `market_context_high->commodity_24h` score `0.7356` n `135` status `ready` deltaP `9.7785` edge `0.0848` maxDD `-3.0953`
- `market_context_high->fx_24h` score `0.258` n `135` status `ready` deltaP `13.1613` edge `0.0261` maxDD `-1.4613`
- `risk_on_high->index_1h` score `0.2299` n `32` status `ready` deltaP `8.9072` edge `0.0076` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2299` n `32` status `ready` deltaP `8.9072` edge `0.0076` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.2281` n `32` status `ready` deltaP `5.8009` edge `0.0031` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2281` n `32` status `ready` deltaP `5.8009` edge `0.0031` maxDD `-0.1547`
- `market_context_high->fx_1h` score `-0.0594` n `182` status `ready` deltaP `5.0454` edge `0.0011` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.0992` n `182` status `ready` deltaP `6.2316` edge `0.0062` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.488` n `32` status `ready` deltaP `-1.2957` edge `0.0043` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.488` n `32` status `ready` deltaP `-1.2957` edge `0.0043` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.7848` n `32` status `ready` deltaP `-4.5097` edge `-0.0162` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
