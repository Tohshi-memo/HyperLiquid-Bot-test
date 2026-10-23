# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T21:22:36.552347+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6270`

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

- `market_context_high->commodity_24h` score `1.1111` n `85` status `ready` deltaP `17.6185` edge `0.0827` maxDD `-3.6055`
- `risk_on_high->equity_1h` score `0.6278` n `37` status `ready` deltaP `15.2978` edge `0.0208` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.6278` n `37` status `ready` deltaP `15.2978` edge `0.0208` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.5145` n `37` status `ready` deltaP `13.202` edge `0.005` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5145` n `37` status `ready` deltaP `13.202` edge `0.005` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.2041` n `37` status `ready` deltaP `11.1956` edge `0.0313` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2041` n `37` status `ready` deltaP `11.1956` edge `0.0313` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1219` n `37` status `ready` deltaP `5.8505` edge `0.0025` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1219` n `37` status `ready` deltaP `5.8505` edge `0.0025` maxDD `-0.0698`
- `market_context_high->fx_1h` score `-0.0976` n `85` status `ready` deltaP `3.5611` edge `0.0036` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.1048` n `85` status `ready` deltaP `6.4042` edge `0.0092` maxDD `-0.5168`
- `risk_on_high->fx_4h` score `-0.1199` n `37` status `ready` deltaP `0.9352` edge `0.0048` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1199` n `37` status `ready` deltaP `0.9352` edge `0.0048` maxDD `-0.1126`
- `market_context_high->index_1h` score `-0.2104` n `85` status `ready` deltaP `4.3307` edge `-0.0022` maxDD `-0.9588`
- `risk_on_high->index_4h` score `-0.265` n `37` status `ready` deltaP `7.1441` edge `0.0029` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.265` n `37` status `ready` deltaP `7.1441` edge `0.0029` maxDD `-0.7604`
- `risk_on_high->metal_1h` score `-0.4487` n `37` status `ready` deltaP `-2.723` edge `0.0068` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4487` n `37` status `ready` deltaP `-2.723` edge `0.0068` maxDD `-0.0831`
- `market_context_high->commodity_1h` score `-0.5174` n `85` status `ready` deltaP `0.0757` edge `-0.0001` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.682` n `85` status `ready` deltaP `-5.6164` edge `-0.004` maxDD `-1.3465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
