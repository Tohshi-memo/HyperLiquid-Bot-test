# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T22:52:32.547371+00:00`
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

- `risk_on_high->unknown_4h` score `6.2839` n `107` status `ready` deltaP `18.2386` edge `0.4639` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `6.2839` n `107` status `ready` deltaP `18.2386` edge `0.4639` maxDD `-2.2797`
- `risk_on_high->equity_24h` score `6.0763` n `107` status `ready` deltaP `26.3062` edge `0.7455` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `6.0763` n `107` status `ready` deltaP `26.3062` edge `0.7455` maxDD `-19.828`
- `market_context_high->unknown_4h` score `4.3646` n `147` status `ready` deltaP `13.9726` edge `0.3401` maxDD `-2.563`
- `news_risk_high->equity_24h` score `3.0764` n `59` status `ready` deltaP `12.2558` edge `0.4214` maxDD `-15.4056`
- `market_context_high->equity_24h` score `2.295` n `147` status `ready` deltaP `22.2754` edge `0.6266` maxDD `-24.4698`
- `risk_on_high->crypto_alt_24h` score `2.0553` n `107` status `ready` deltaP `20.2152` edge `0.8191` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.0553` n `107` status `ready` deltaP `20.2152` edge `0.8191` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.0264` n `59` status `ready` deltaP `20.136` edge `0.419` maxDD `-19.4761`
- `news_risk_high->commodity_4h` score `0.2309` n `67` status `ready` deltaP `5.6425` edge `0.0279` maxDD `-0.8733`
- `news_risk_high->crypto_major_24h` score `0.224` n `59` status `ready` deltaP `12.9591` edge `0.3706` maxDD `-30.7329`
- `market_context_high->crypto_alt_24h` score `0.2021` n `147` status `ready` deltaP `14.2326` edge `0.6809` maxDD `-46.3234`
- `risk_on_high->index_1h` score `0.1283` n `107` status `ready` deltaP `8.393` edge `0.005` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1283` n `107` status `ready` deltaP `8.393` edge `0.005` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.1001` n `107` status `ready` deltaP `20.1733` edge `0.0114` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1001` n `107` status `ready` deltaP `20.1733` edge `0.0114` maxDD `-3.6448`
- `news_risk_high->index_1h` score `0.0279` n `67` status `ready` deltaP `5.673` edge `0.0011` maxDD `-0.8275`
- `risk_on_high->crypto_major_24h` score `-0.0067` n `107` status `ready` deltaP `19.2952` edge `0.7449` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `-0.0067` n `107` status `ready` deltaP `19.2952` edge `0.7449` maxDD `-56.9519`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
