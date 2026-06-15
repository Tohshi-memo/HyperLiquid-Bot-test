# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T12:07:34.432175+00:00`
- Price records: `672`
- Market context records: `3990`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10092`

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

- `risk_on_high->unknown_4h` score `147.0984` n `40` status `ready` deltaP `-1.7988` edge `12.4514` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `147.0984` n `40` status `ready` deltaP `-1.7988` edge `12.4514` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `37.1793` n `147` status `ready` deltaP `-5.9347` edge `3.5397` maxDD `-24.1486`
- `market_context_high->unknown_4h` score `21.9142` n `159` status `ready` deltaP `1.7075` edge `2.3557` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.3347` n `40` status `ready` deltaP `42.0139` edge `0.4978` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.3347` n `40` status `ready` deltaP `42.0139` edge `0.4978` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.9154` n `40` status `ready` deltaP `37.7439` edge `0.0794` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.9154` n `40` status `ready` deltaP `37.7439` edge `0.0794` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.3459` n `147` status `ready` deltaP `16.2947` edge `0.3217` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.161` n `147` status `ready` deltaP `25.7795` edge `0.2055` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.8041` n `40` status `ready` deltaP `29.8611` edge `0.0346` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8041` n `40` status `ready` deltaP `29.8611` edge `0.0346` maxDD `0.0`
- `market_context_high->equity_24h` score `2.4922` n `147` status `ready` deltaP `18.2044` edge `0.3893` maxDD `-14.5715`
- `market_context_high->equity_4h` score `2.2687` n `159` status `ready` deltaP `20.1181` edge `0.1852` maxDD `-7.0879`
- `risk_on_high->crypto_major_4h` score `1.9294` n `40` status `ready` deltaP `20.9756` edge `0.0875` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.9294` n `40` status `ready` deltaP `20.9756` edge `0.0875` maxDD `-2.6576`
- `market_context_high->crypto_major_4h` score `1.6998` n `159` status `ready` deltaP `18.2869` edge `0.1764` maxDD `-7.8662`
- `market_context_high->crypto_major_1h` score `1.4371` n `159` status `ready` deltaP `11.7256` edge `0.0958` maxDD `-2.3372`
- `market_context_high->equity_1h` score `0.9528` n `159` status `ready` deltaP `8.6723` edge `0.078` maxDD `-2.1799`
- `risk_on_high->commodity_24h` score `0.9075` n `40` status `ready` deltaP `4.1667` edge `0.276` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
