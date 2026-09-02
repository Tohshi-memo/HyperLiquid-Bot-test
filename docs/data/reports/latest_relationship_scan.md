# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T23:32:21.354774+00:00`
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

- `risk_on_high->unknown_4h` score `6.3359` n `107` status `ready` deltaP `18.5435` edge `0.4662` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `6.3359` n `107` status `ready` deltaP `18.5435` edge `0.4662` maxDD `-2.2797`
- `risk_on_high->equity_24h` score `5.9422` n `107` status `ready` deltaP `25.7853` edge `0.7378` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.9422` n `107` status `ready` deltaP `25.7853` edge `0.7378` maxDD `-19.828`
- `market_context_high->unknown_4h` score `4.4165` n `147` status `ready` deltaP `14.2775` edge `0.3424` maxDD `-2.563`
- `news_risk_high->equity_24h` score `2.9424` n `59` status `ready` deltaP `11.7349` edge `0.4137` maxDD `-15.4056`
- `market_context_high->equity_24h` score `2.2078` n `147` status `ready` deltaP `21.7545` edge `0.6189` maxDD `-24.4698`
- `risk_on_high->crypto_alt_24h` score `2.1397` n `107` status `ready` deltaP `20.5624` edge `0.8276` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.1397` n `107` status `ready` deltaP `20.5624` edge `0.8276` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.1107` n `59` status `ready` deltaP `20.4832` edge `0.4275` maxDD `-19.4761`
- `news_risk_high->crypto_major_24h` score `0.4721` n `59` status `ready` deltaP `13.4799` edge `0.3878` maxDD `-30.7329`
- `market_context_high->crypto_alt_24h` score `0.2864` n `147` status `ready` deltaP `14.5798` edge `0.6894` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.223` n `67` status `ready` deltaP `5.4901` edge `0.0279` maxDD `-0.8733`
- `risk_on_high->crypto_major_24h` score `0.1545` n `107` status `ready` deltaP `19.816` edge `0.7621` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.1545` n `107` status `ready` deltaP `19.816` edge `0.7621` maxDD `-56.9519`
- `risk_on_high->index_1h` score `0.1197` n `107` status `ready` deltaP `8.2433` edge `0.0049` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1197` n `107` status `ready` deltaP `8.2433` edge `0.0049` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.0732` n `107` status `ready` deltaP `19.7159` edge `0.011` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0732` n `107` status `ready` deltaP `19.7159` edge `0.011` maxDD `-3.6448`
- `news_risk_high->index_1h` score `0.0193` n `67` status `ready` deltaP `5.5233` edge `0.001` maxDD `-0.8275`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
