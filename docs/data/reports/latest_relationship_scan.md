# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T15:07:32.546284+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11625`

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

- `risk_on_high->unknown_4h` score `34.2942` n `133` status `ready` deltaP `12.657` edge `2.8353` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `34.2942` n `133` status `ready` deltaP `12.657` edge `2.8353` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `27.5292` n `167` status `ready` deltaP `14.2553` edge `2.2686` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `18.2285` n `133` status `ready` deltaP `1.1919` edge `1.5688` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `18.2285` n `133` status `ready` deltaP `1.1919` edge `1.5688` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.7486` n `167` status `ready` deltaP `1.6467` edge `1.1978` maxDD `-2.0446`
- `market_context_high->equity_24h` score `3.3358` n `127` status `ready` deltaP `21.3377` edge `0.5703` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `3.2586` n `67` status `ready` deltaP `20.9136` edge `0.5718` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `2.8529` n `107` status `ready` deltaP `16.5839` edge `0.5417` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `2.8529` n `107` status `ready` deltaP `16.5839` edge `0.5417` maxDD `-19.828`
- `news_risk_high->crypto_major_24h` score `2.7919` n `67` status `ready` deltaP `17.4104` edge `0.6802` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.653` n `67` status `ready` deltaP `9.0096` edge `0.3986` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `1.0058` n `107` status `ready` deltaP `16.7429` edge `0.7077` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.0058` n `107` status `ready` deltaP `16.7429` edge `0.7077` maxDD `-42.8959`
- `market_context_high->crypto_alt_24h` score `0.7268` n `127` status `ready` deltaP `18.3986` edge `0.7204` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.271` n `67` status `ready` deltaP `6.0998` edge `0.03` maxDD `-0.8733`
- `news_risk_high->fx_4h` score `0.0555` n `67` status `ready` deltaP `9.8039` edge `0.0049` maxDD `-1.2507`
- `risk_on_high->metal_1h` score `0.0385` n `133` status `ready` deltaP `11.2152` edge `0.0014` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0385` n `133` status `ready` deltaP `11.2152` edge `0.0014` maxDD `-1.699`
- `risk_on_high->crypto_alt_1h` score `-0.0267` n `133` status `ready` deltaP `5.4995` edge `0.0628` maxDD `-5.4685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
