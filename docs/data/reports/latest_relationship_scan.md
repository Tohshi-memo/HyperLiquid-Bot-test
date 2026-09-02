# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T23:07:33.087659+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11521`

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

- `risk_on_high->unknown_4h` score `6.2899` n `107` status `ready` deltaP `18.2386` edge `0.4644` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `6.2899` n `107` status `ready` deltaP `18.2386` edge `0.4644` maxDD `-2.2797`
- `risk_on_high->equity_24h` score `6.0336` n `107` status `ready` deltaP `26.1325` edge `0.7431` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `6.0336` n `107` status `ready` deltaP `26.1325` edge `0.7431` maxDD `-19.828`
- `market_context_high->unknown_4h` score `4.3706` n `147` status `ready` deltaP `13.9726` edge `0.3406` maxDD `-2.563`
- `news_risk_high->equity_24h` score `3.0337` n `59` status `ready` deltaP `12.0821` edge `0.419` maxDD `-15.4056`
- `market_context_high->equity_24h` score `2.2672` n `147` status `ready` deltaP `22.1017` edge `0.6242` maxDD `-24.4698`
- `risk_on_high->crypto_alt_24h` score `2.087` n `107` status `ready` deltaP `20.3888` edge `0.822` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.087` n `107` status `ready` deltaP `20.3888` edge `0.822` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.058` n `59` status `ready` deltaP `20.3096` edge `0.4219` maxDD `-19.4761`
- `news_risk_high->crypto_major_24h` score `0.3051` n `59` status `ready` deltaP `13.1327` edge `0.3762` maxDD `-30.7329`
- `market_context_high->crypto_alt_24h` score `0.2337` n `147` status `ready` deltaP `14.4062` edge `0.6838` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.2222` n `67` status `ready` deltaP `5.4901` edge `0.0278` maxDD `-0.8733`
- `risk_on_high->index_1h` score `0.1283` n `107` status `ready` deltaP `8.393` edge `0.005` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1283` n `107` status `ready` deltaP `8.393` edge `0.005` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.0914` n `107` status `ready` deltaP `20.0208` edge `0.0113` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0914` n `107` status `ready` deltaP `20.0208` edge `0.0113` maxDD `-3.6448`
- `risk_on_high->crypto_major_24h` score `0.046` n `107` status `ready` deltaP `19.4688` edge `0.7505` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.046` n `107` status `ready` deltaP `19.4688` edge `0.7505` maxDD `-56.9519`
- `news_risk_high->index_1h` score `0.0279` n `67` status `ready` deltaP `5.673` edge `0.0011` maxDD `-0.8275`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
