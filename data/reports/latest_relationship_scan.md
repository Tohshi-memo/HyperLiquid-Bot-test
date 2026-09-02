# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T23:52:23.022197+00:00`
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

- `risk_on_high->unknown_4h` score `6.0371` n `107` status `ready` deltaP `18.5435` edge `0.4413` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `6.0371` n `107` status `ready` deltaP `18.5435` edge `0.4413` maxDD `-2.2797`
- `risk_on_high->equity_24h` score `5.8947` n `107` status `ready` deltaP `25.6117` edge `0.735` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.8947` n `107` status `ready` deltaP `25.6117` edge `0.735` maxDD `-19.828`
- `market_context_high->unknown_4h` score `4.1178` n `147` status `ready` deltaP `14.2775` edge `0.3175` maxDD `-2.563`
- `news_risk_high->equity_24h` score `2.8949` n `59` status `ready` deltaP `11.5613` edge `0.4109` maxDD `-15.4056`
- `market_context_high->equity_24h` score `2.177` n `147` status `ready` deltaP `21.5809` edge `0.6161` maxDD `-24.4698`
- `risk_on_high->crypto_alt_24h` score `2.1666` n `107` status `ready` deltaP `20.736` edge `0.8299` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.1666` n `107` status `ready` deltaP `20.736` edge `0.8299` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.1377` n `59` status `ready` deltaP `20.6568` edge `0.4298` maxDD `-19.4761`
- `news_risk_high->crypto_major_24h` score `0.5399` n `59` status `ready` deltaP `13.6535` edge `0.3923` maxDD `-30.7329`
- `market_context_high->crypto_alt_24h` score `0.3134` n `147` status `ready` deltaP `14.7534` edge `0.6917` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.2317` n `67` status `ready` deltaP `5.6425` edge `0.028` maxDD `-0.8733`
- `risk_on_high->crypto_major_24h` score `0.1986` n `107` status `ready` deltaP `19.9896` edge `0.7666` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.1986` n `107` status `ready` deltaP `19.9896` edge `0.7666` maxDD `-56.9519`
- `risk_on_high->index_1h` score `0.1104` n `107` status `ready` deltaP `8.0936` edge `0.0047` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1104` n `107` status `ready` deltaP `8.0936` edge `0.0047` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.0637` n `107` status `ready` deltaP `19.5635` edge `0.0108` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0637` n `107` status `ready` deltaP `19.5635` edge `0.0108` maxDD `-3.6448`
- `market_context_high->crypto_major_24h` score `0.0361` n `147` status `ready` deltaP `23.0159` edge `0.7976` maxDD `-61.3797`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
