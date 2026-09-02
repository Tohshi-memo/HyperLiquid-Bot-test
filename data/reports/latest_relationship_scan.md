# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T22:07:27.028455+00:00`
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

- `risk_on_high->unknown_4h` score `6.2357` n `107` status `ready` deltaP `18.0861` edge `0.4609` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `6.2357` n `107` status `ready` deltaP `18.0861` edge `0.4609` maxDD `-2.2797`
- `risk_on_high->equity_24h` score `6.1984` n `107` status `ready` deltaP `26.827` edge `0.7522` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `6.1984` n `107` status `ready` deltaP `26.827` edge `0.7522` maxDD `-19.828`
- `market_context_high->unknown_4h` score `4.3164` n `147` status `ready` deltaP `13.8201` edge `0.3371` maxDD `-2.563`
- `news_risk_high->equity_24h` score `3.1985` n `59` status `ready` deltaP `12.7766` edge `0.4281` maxDD `-15.4056`
- `market_context_high->equity_24h` score `2.3743` n `147` status `ready` deltaP `22.7962` edge `0.6333` maxDD `-24.4698`
- `risk_on_high->crypto_alt_24h` score `1.9534` n `107` status `ready` deltaP `19.6943` edge `0.8095` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.9534` n `107` status `ready` deltaP `19.6943` edge `0.8095` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `1.9244` n `59` status `ready` deltaP `19.6151` edge `0.4094` maxDD `-19.4761`
- `news_risk_high->commodity_4h` score `0.2419` n `67` status `ready` deltaP `5.795` edge `0.0283` maxDD `-0.8733`
- `risk_on_high->index_1h` score `0.1361` n `107` status `ready` deltaP `8.5427` edge `0.005` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1361` n `107` status `ready` deltaP `8.5427` edge `0.005` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.1198` n `107` status `ready` deltaP `20.4781` edge `0.0119` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1198` n `107` status `ready` deltaP `20.4781` edge `0.0119` maxDD `-3.6448`
- `market_context_high->crypto_alt_24h` score `0.1001` n `147` status `ready` deltaP `13.7117` edge `0.6713` maxDD `-46.3234`
- `news_risk_high->index_1h` score `0.0357` n `67` status `ready` deltaP `5.8227` edge `0.0011` maxDD `-0.8275`
- `news_risk_high->crypto_major_24h` score `-0.0049` n `59` status `ready` deltaP `12.4382` edge `0.355` maxDD `-30.7329`
- `risk_on_high->metal_1h` score `-0.0466` n `107` status `ready` deltaP `9.9992` edge `-0.0014` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.0466` n `107` status `ready` deltaP `9.9992` edge `-0.0014` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
