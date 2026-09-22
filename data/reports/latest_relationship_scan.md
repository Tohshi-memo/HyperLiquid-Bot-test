# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T11:52:31.635497+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_4h` score `47.029` n `46` status `ready` deltaP `7.3171` edge `3.8703` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `31.9085` n `46` status `ready` deltaP `17.5272` edge `2.5578` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `16.9777` n `46` status `ready` deltaP `16.6667` edge `1.3037` maxDD `0.0`
- `market_context_high->equity_24h` score `16.4747` n `46` status `ready` deltaP `13.0133` edge `1.2962` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.5704` n `46` status `ready` deltaP `20.1314` edge `0.3387` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.1914` n `101` status `ready` deltaP `-7.828` edge `1.0873` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.1559` n `101` status `ready` deltaP `38.1274` edge `0.281` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.4309` n `101` status `ready` deltaP `12.2117` edge `0.2421` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.2618` n `101` status `ready` deltaP `13.8362` edge `0.1428` maxDD `-2.058`
- `market_context_high->index_4h` score `2.0829` n `46` status `ready` deltaP `24.2311` edge `0.0254` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `1.8945` n `101` status `ready` deltaP `15.4129` edge `0.1809` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.57` n `101` status `ready` deltaP `15.4829` edge `0.0799` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.3198` n `46` status `ready` deltaP `8.9011` edge `0.0813` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.0112` n `101` status `ready` deltaP `16.72` edge `0.0364` maxDD `-0.421`
- `market_context_high->equity_1h` score `0.984` n `46` status `ready` deltaP `7.8105` edge `0.0542` maxDD `-0.2751`
- `market_context_high->crypto_alt_4h` score `0.8753` n `46` status `ready` deltaP `7.9069` edge `0.0797` maxDD `-2.7574`
- `market_context_high->metal_24h` score `0.7552` n `46` status `ready` deltaP `20.3578` edge `-0.0494` maxDD `-0.2042`
- `market_context_high->index_1h` score `0.7358` n `46` status `ready` deltaP `11.2536` edge `0.0116` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.6113` n `101` status `ready` deltaP `14.598` edge `0.0138` maxDD `-0.8144`
- `news_risk_high->crypto_alt_24h` score `0.4967` n `101` status `ready` deltaP `-7.0957` edge `0.5768` maxDD `-32.7147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
