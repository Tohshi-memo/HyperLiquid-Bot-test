# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T17:52:33.967248+00:00`
- Price records: `672`
- Market context records: `4540`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9932`

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

- `market_context_high->unknown_1h` score `55.225` n `174` status `ready` deltaP `7.535` edge `4.6019` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `30.3244` n `172` status `ready` deltaP `8.4196` edge `2.6275` maxDD `-7.5275`
- `market_context_high->fx_4h` score `-0.5066` n `172` status `ready` deltaP `6.1933` edge `0.002` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.5752` n `174` status `ready` deltaP `0.4921` edge `0.0149` maxDD `-3.0206`
- `market_context_high->fx_1h` score `-0.6843` n `174` status `ready` deltaP `0.2942` edge `-0.0031` maxDD `-1.1377`
- `market_context_high->equity_4h` score `-1.019` n `172` status `ready` deltaP `4.0059` edge `0.0653` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.0332` n `174` status `ready` deltaP `-3.1196` edge `-0.0108` maxDD `-2.7358`
- `market_context_high->equity_1h` score `-1.063` n `174` status `ready` deltaP `-1.4677` edge `0.0199` maxDD `-5.5624`
- `market_context_high->index_4h` score `-1.2097` n `172` status `ready` deltaP `-0.3509` edge `-0.0113` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.4979` n `172` status `ready` deltaP `1.4074` edge `0.0193` maxDD `-9.9906`
- `market_context_high->unknown_24h` score `-2.7333` n `172` status `ready` deltaP `2.2892` edge `-0.1507` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-4.4597` n `174` status `ready` deltaP `-4.5495` edge `-0.0734` maxDD `-18.0993`
- `market_context_high->crypto_alt_1h` score `-5.306` n `174` status `ready` deltaP `-2.9458` edge `-0.0938` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.4977` n `172` status `ready` deltaP `-13.6225` edge `-0.0161` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.6947` n `172` status `ready` deltaP `-8.5957` edge `-0.1353` maxDD `-29.3321`
- `market_context_high->crypto_major_1h` score `-6.2254` n `174` status `ready` deltaP `-4.0953` edge `-0.1162` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-8.3966` n `172` status `ready` deltaP `4.1344` edge `0.0135` maxDD `-46.5954`
- `market_context_high->crypto_alt_4h` score `-13.2598` n `172` status `ready` deltaP `-1.5244` edge `-0.2291` maxDD `-63.9243`
- `market_context_high->equity_24h` score `-13.5257` n `172` status `ready` deltaP `-0.7954` edge `-0.2608` maxDD `-102.1031`
- `market_context_high->metal_4h` score `-15.558` n `172` status `ready` deltaP `-7.5297` edge `-0.3114` maxDD `-68.4587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
