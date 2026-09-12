# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T01:07:25.624273+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11245`

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

- `news_risk_high->unknown_1h` score `383.2716` n `82` status `ready` deltaP `-3.1547` edge `32.0025` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `25.0303` n `91` status `ready` deltaP `43.1166` edge `1.8214` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `25.0303` n `91` status `ready` deltaP `43.1166` edge `1.8214` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `22.7515` n `45` status `ready` deltaP `52.3958` edge `1.6367` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `22.1208` n `151` status `ready` deltaP `38.0151` edge `1.6727` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `14.0618` n `45` status `ready` deltaP `24.1667` edge `1.0595` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `10.9278` n `45` status `ready` deltaP `32.5348` edge `0.7036` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.3051` n `91` status `ready` deltaP `36.9792` edge `0.5289` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.3051` n `91` status `ready` deltaP `36.9792` edge `0.5289` maxDD `0.0`
- `market_context_high->equity_24h` score `9.0159` n `151` status `ready` deltaP `36.9792` edge `0.5048` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.9398` n `91` status `ready` deltaP `43.9276` edge `0.4893` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9398` n `91` status `ready` deltaP `43.9276` edge `0.4893` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.0769` n `45` status `ready` deltaP `51.0417` edge `0.3328` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.8493` n `91` status `ready` deltaP `25.021` edge `1.2463` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.8493` n `91` status `ready` deltaP `25.021` edge `1.2463` maxDD `-24.5429`
- `news_risk_high->index_24h` score `7.825` n `45` status `ready` deltaP `50.4167` edge `0.3253` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `6.7713` n `91` status `ready` deltaP `31.8966` edge `0.4375` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.7713` n `91` status `ready` deltaP `31.8966` edge `0.4375` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.3188` n `91` status `ready` deltaP `51.5644` edge `0.1037` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.3188` n `91` status `ready` deltaP `51.5644` edge `0.1037` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
