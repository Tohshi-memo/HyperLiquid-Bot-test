# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T21:52:32.403447+00:00`
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

- `risk_on_high->unknown_4h` score `6.2503` n `107` status `ready` deltaP `18.2386` edge `0.4611` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `6.2503` n `107` status `ready` deltaP `18.2386` edge `0.4611` maxDD `-2.2797`
- `risk_on_high->equity_24h` score `6.2362` n `107` status `ready` deltaP `27.0006` edge `0.7542` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `6.2362` n `107` status `ready` deltaP `27.0006` edge `0.7542` maxDD `-19.828`
- `market_context_high->unknown_4h` score `4.331` n `147` status `ready` deltaP `13.9726` edge `0.3373` maxDD `-2.563`
- `news_risk_high->equity_24h` score `3.2364` n `59` status `ready` deltaP `12.9502` edge `0.4301` maxDD `-15.4056`
- `market_context_high->equity_24h` score `2.399` n `147` status `ready` deltaP `22.9698` edge `0.6353` maxDD `-24.4698`
- `risk_on_high->crypto_alt_24h` score `1.9162` n `107` status `ready` deltaP `19.5207` edge `0.8059` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.9162` n `107` status `ready` deltaP `19.5207` edge `0.8059` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `1.8873` n `59` status `ready` deltaP `19.4415` edge `0.4058` maxDD `-19.4761`
- `news_risk_high->commodity_4h` score `0.2419` n `67` status `ready` deltaP `5.795` edge `0.0283` maxDD `-0.8733`
- `risk_on_high->index_1h` score `0.1353` n `107` status `ready` deltaP `8.5427` edge `0.0049` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1353` n `107` status `ready` deltaP `8.5427` edge `0.0049` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.1206` n `107` status `ready` deltaP `20.4781` edge `0.012` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1206` n `107` status `ready` deltaP `20.4781` edge `0.012` maxDD `-3.6448`
- `market_context_high->crypto_alt_24h` score `0.063` n `147` status `ready` deltaP `13.5381` edge `0.6677` maxDD `-46.3234`
- `news_risk_high->index_1h` score `0.0349` n `67` status `ready` deltaP `5.8227` edge `0.001` maxDD `-0.8275`
- `risk_on_high->metal_1h` score `-0.056` n `107` status `ready` deltaP `9.8495` edge `-0.0016` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.056` n `107` status `ready` deltaP `9.8495` edge `-0.0016` maxDD `-1.699`
- `news_risk_high->crypto_major_24h` score `-0.0836` n `59` status `ready` deltaP `12.2646` edge `0.3496` maxDD `-30.7329`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
