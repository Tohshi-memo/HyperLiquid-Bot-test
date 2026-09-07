# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T12:07:31.507750+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10333`

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

- `risk_on_high->unknown_24h` score `402.1164` n `93` status `ready` deltaP `25.6944` edge `33.3384` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `402.1164` n `93` status `ready` deltaP `25.6944` edge `33.3384` maxDD `0.0`
- `market_context_high->unknown_1h` score `24.2291` n `241` status `ready` deltaP `-2.0784` edge `2.1054` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `22.2496` n `93` status `ready` deltaP `38.2393` edge `1.6509` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `22.2496` n `93` status `ready` deltaP `38.2393` edge `1.6509` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.1742` n `93` status `ready` deltaP `32.1181` edge `1.0504` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.1742` n `93` status `ready` deltaP `32.1181` edge `1.0504` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.7485` n `192` status `ready` deltaP `24.3056` edge `0.6245` maxDD `-2.5998`
- `market_context_high->equity_24h` score `5.8147` n `192` status `ready` deltaP `20.1389` edge `0.3503` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.3651` n `117` status `ready` deltaP `28.9582` edge `0.2912` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.3651` n `117` status `ready` deltaP `28.9582` edge `0.2912` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `4.8403` n `93` status `ready` deltaP `20.1389` edge `0.2691` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.8403` n `93` status `ready` deltaP `20.1389` edge `0.2691` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.3665` n `117` status `ready` deltaP `24.4567` edge `0.2867` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3665` n `117` status `ready` deltaP `24.4567` edge `0.2867` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.4413` n `93` status `ready` deltaP `20.9061` edge `0.0683` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.4413` n `93` status `ready` deltaP `20.9061` edge `0.0683` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.9663` n `192` status `ready` deltaP `16.3194` edge `0.0812` maxDD `-0.0907`
- `risk_on_high->crypto_alt_1h` score `0.8949` n `117` status `ready` deltaP `4.2467` edge `0.0815` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8949` n `117` status `ready` deltaP `4.2467` edge `0.0815` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
