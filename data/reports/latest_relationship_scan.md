# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T21:28:13.419461+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11856`

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

- `risk_on_high->commodity_4h` score `2.3389` n `32` status `ready` deltaP `16.3872` edge `0.1039` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.3389` n `32` status `ready` deltaP `16.3872` edge `0.1039` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.1281` n `32` status `ready` deltaP `12.3129` edge `0.0352` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1281` n `32` status `ready` deltaP `12.3129` edge `0.0352` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9913` n `32` status `ready` deltaP `11.3567` edge `0.021` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9913` n `32` status `ready` deltaP `11.3567` edge `0.021` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.6882` n `181` status `ready` deltaP `9.8612` edge `0.0238` maxDD `-0.5752`
- `market_context_high->commodity_4h` score `0.5641` n `181` status `ready` deltaP `9.5329` edge `0.0473` maxDD `-2.1077`
- `risk_on_high->index_1h` score `0.3475` n `32` status `ready` deltaP `10.7036` edge `0.0107` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3475` n `32` status `ready` deltaP `10.7036` edge `0.0107` maxDD `-0.3343`
- `market_context_high->commodity_24h` score `0.2601` n `145` status `ready` deltaP `7.3651` edge `0.0529` maxDD `-2.4263`
- `risk_on_high->fx_1h` score `0.1514` n `32` status `ready` deltaP `4.9027` edge `0.0027` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.1514` n `32` status `ready` deltaP `4.9027` edge `0.0027` maxDD `-0.1547`
- `market_context_high->fx_24h` score `-0.0299` n `145` status `ready` deltaP `10.7692` edge `0.0218` maxDD `-1.4613`
- `market_context_high->fx_1h` score `-0.0925` n `181` status `ready` deltaP `4.4538` edge `0.0008` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.1106` n `181` status `ready` deltaP `5.9527` edge `0.0066` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.2377` n `32` status `ready` deltaP `1.4482` edge `0.0181` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.2377` n `32` status `ready` deltaP `1.4482` edge `0.0181` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.6437` n `32` status `ready` deltaP `-3.3121` edge `-0.0061` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `-0.6437` n `32` status `ready` deltaP `-3.3121` edge `-0.0061` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
