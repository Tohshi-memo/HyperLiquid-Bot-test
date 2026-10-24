# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T18:45:27.775178+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7582`

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

- `market_context_high->unknown_4h` score `13.6199` n `107` status `ready` deltaP `-1.8107` edge `1.1806` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.7731` n `79` status `ready` deltaP `15.1789` edge `0.0583` maxDD `-3.6055`
- `risk_on_high->equity_1h` score `0.6174` n `35` status `ready` deltaP `17.9469` edge `0.0018` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.6174` n `35` status `ready` deltaP `17.9469` edge `0.0018` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.5045` n `35` status `ready` deltaP `13.4431` edge `0.0021` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5045` n `35` status `ready` deltaP `13.4431` edge `0.0021` maxDD `-0.1637`
- `risk_on_high->fx_1h` score `0.4378` n `35` status `ready` deltaP `10.586` edge `0.0031` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.4378` n `35` status `ready` deltaP `10.586` edge `0.0031` maxDD `-0.0698`
- `risk_on_high->commodity_24h` score `0.2191` n `35` status `ready` deltaP `10.9474` edge `0.024` maxDD `-1.5113`
- `risk_on_and_context->commodity_24h` score `0.2191` n `35` status `ready` deltaP `10.9474` edge `0.024` maxDD `-1.5113`
- `market_context_high->commodity_4h` score `0.1755` n `107` status `ready` deltaP `8.7731` edge `0.0334` maxDD `-2.181`
- `risk_on_high->fx_4h` score `0.0471` n `35` status `ready` deltaP `3.9068` edge `0.0064` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0471` n `35` status `ready` deltaP `3.9068` edge `0.0064` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.1916` n `113` status `ready` deltaP `1.2307` edge `0.0027` maxDD `-0.1712`
- `market_context_high->commodity_1h` score `-0.3458` n `113` status `ready` deltaP `2.5953` edge `0.0051` maxDD `-1.0053`
- `market_context_high->fx_4h` score `-0.4708` n `107` status `ready` deltaP `-0.7394` edge `0.0052` maxDD `-0.5168`
- `risk_on_high->index_4h` score `-0.537` n `35` status `ready` deltaP `4.0592` edge `-0.0114` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.537` n `35` status `ready` deltaP `4.0592` edge `-0.0114` maxDD `-0.7604`
- `market_context_high->index_1h` score `-0.6769` n `113` status `ready` deltaP `-2.3091` edge `-0.0062` maxDD `-1.2155`
- `risk_on_high->metal_1h` score `-0.7157` n `35` status `ready` deltaP `-5.9709` edge `0.0062` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
