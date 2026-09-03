# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T00:07:30.296125+00:00`
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

- `risk_on_high->equity_24h` score `5.8448` n `107` status `ready` deltaP `25.4381` edge `0.732` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.8448` n `107` status `ready` deltaP `25.4381` edge `0.732` maxDD `-19.828`
- `risk_on_high->unknown_4h` score `5.7395` n `107` status `ready` deltaP `18.5435` edge `0.4165` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `5.7395` n `107` status `ready` deltaP `18.5435` edge `0.4165` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `3.8201` n `147` status `ready` deltaP `14.2775` edge `0.2927` maxDD `-2.563`
- `news_risk_high->equity_24h` score `2.845` n `59` status `ready` deltaP `11.3877` edge `0.4079` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `2.1858` n `107` status `ready` deltaP `20.9096` edge `0.8312` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.1858` n `107` status `ready` deltaP `20.9096` edge `0.8312` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.1568` n `59` status `ready` deltaP `20.8304` edge `0.4311` maxDD `-19.4761`
- `market_context_high->equity_24h` score `2.1446` n `147` status `ready` deltaP `21.4073` edge `0.6131` maxDD `-24.4698`
- `news_risk_high->crypto_major_24h` score `0.6018` n `59` status `ready` deltaP `13.8271` edge `0.3963` maxDD `-30.7329`
- `market_context_high->crypto_alt_24h` score `0.3326` n `147` status `ready` deltaP `14.927` edge `0.693` maxDD `-46.3234`
- `risk_on_high->crypto_major_24h` score `0.2389` n `107` status `ready` deltaP `20.1632` edge `0.7706` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.2389` n `107` status `ready` deltaP `20.1632` edge `0.7706` maxDD `-56.9519`
- `news_risk_high->commodity_4h` score `0.2309` n `67` status `ready` deltaP `5.6425` edge `0.0279` maxDD `-0.8733`
- `risk_on_high->index_1h` score `0.108` n `107` status `ready` deltaP `8.0936` edge `0.0044` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.108` n `107` status `ready` deltaP `8.0936` edge `0.0044` maxDD `-0.5605`
- `market_context_high->crypto_major_24h` score `0.0763` n `147` status `ready` deltaP `23.1895` edge `0.8016` maxDD `-61.3797`
- `risk_on_high->index_4h` score `0.0629` n `107` status `ready` deltaP `19.5635` edge `0.0107` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0629` n `107` status `ready` deltaP `19.5635` edge `0.0107` maxDD `-3.6448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
