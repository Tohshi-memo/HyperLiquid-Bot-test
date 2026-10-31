# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T14:07:27.752099+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7269`

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

- `market_context_high->unknown_24h` score `2527.9294` n `107` status `ready` deltaP `-8.0754` edge `210.7576` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `80.279` n `102` status `ready` deltaP `-6.0526` edge `6.7589` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `67.1447` n `107` status `ready` deltaP `0.9274` edge `5.6025` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `17.453` n `50` status `ready` deltaP `45.3056` edge `1.1575` maxDD `-0.0763`
- `market_context_high->equity_24h` score `11.0913` n `107` status `ready` deltaP `26.9827` edge `1.0201` maxDD `-14.0571`
- `market_context_high->index_24h` score `4.7534` n `107` status `ready` deltaP `42.6044` edge `0.1304` maxDD `-0.1315`
- `news_risk_high->crypto_alt_4h` score `4.5688` n `98` status `ready` deltaP `16.9612` edge `0.4063` maxDD `-7.4246`
- `market_context_high->metal_4h` score `1.8326` n `107` status `ready` deltaP `22.665` edge `0.0441` maxDD `-0.7323`
- `market_context_high->equity_4h` score `1.3545` n `107` status `ready` deltaP `8.1163` edge `0.1981` maxDD `-4.48`
- `market_context_high->metal_1h` score `1.0113` n `107` status `ready` deltaP `14.2635` edge `0.0182` maxDD `-0.3209`
- `market_context_high->equity_1h` score `0.7219` n `107` status `ready` deltaP `7.4584` edge `0.098` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.7143` n `107` status `ready` deltaP `10.784` edge `0.0904` maxDD `-5.2213`
- `news_risk_high->crypto_alt_1h` score `0.4165` n `102` status `ready` deltaP `6.0174` edge `0.09` maxDD `-3.9659`
- `market_context_high->fx_1h` score `0.3023` n `107` status `ready` deltaP `7.867` edge `-0.0005` maxDD `-0.1407`
- `market_context_high->metal_24h` score `0.1969` n `107` status `ready` deltaP `15.036` edge `0.1897` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `0.1966` n `107` status `ready` deltaP `17.3695` edge `0.1746` maxDD `-14.5879`
- `market_context_high->fx_4h` score `0.0471` n `107` status `ready` deltaP `6.4395` edge `0.0001` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `-0.0036` n `107` status `ready` deltaP `10.3231` edge `0.0526` maxDD `-1.0837`
- `market_context_high->index_1h` score `-0.2596` n `107` status `ready` deltaP `4.7275` edge `0.0027` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.4957` n `107` status `ready` deltaP `-0.6128` edge `0.0142` maxDD `-0.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
