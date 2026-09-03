# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T07:37:26.627194+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11563`

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

- `risk_on_high->unknown_4h` score `38.2237` n `120` status `ready` deltaP `16.8801` edge `3.1346` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `38.2237` n `120` status `ready` deltaP `16.8801` edge `3.1346` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `26.7118` n `162` status `ready` deltaP `13.6085` edge `2.2048` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `20.1081` n `132` status `ready` deltaP `2.4269` edge `1.7172` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `20.1081` n `132` status `ready` deltaP `2.4269` edge `1.7172` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.4768` n `174` status `ready` deltaP `1.0685` edge `1.179` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `4.7252` n `107` status `ready` deltaP `21.7923` edge `0.663` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `4.7252` n `107` status `ready` deltaP `21.7923` edge `0.663` maxDD `-19.828`
- `risk_on_high->crypto_alt_24h` score `2.3615` n `107` status `ready` deltaP `21.6041` edge `0.8491` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.3615` n `107` status `ready` deltaP `21.6041` edge `0.8491` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.3326` n `59` status `ready` deltaP `21.5249` edge `0.449` maxDD `-19.4761`
- `news_risk_high->equity_24h` score `1.7253` n `59` status `ready` deltaP `7.7419` edge `0.3389` maxDD `-15.4056`
- `news_risk_high->crypto_major_24h` score `1.6517` n `59` status `ready` deltaP `14.6952` edge `0.478` maxDD `-30.7329`
- `market_context_high->equity_24h` score `1.4168` n `147` status `ready` deltaP `17.7615` edge `0.5441` maxDD `-24.4698`
- `risk_on_high->crypto_major_24h` score `0.9213` n `107` status `ready` deltaP `21.0313` edge `0.8523` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.9213` n `107` status `ready` deltaP `21.0313` edge `0.8523` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.7587` n `147` status `ready` deltaP `24.0576` edge `0.8833` maxDD `-61.3797`
- `market_context_high->crypto_alt_24h` score `0.5083` n `147` status `ready` deltaP `15.6215` edge `0.7109` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.2101` n `67` status `ready` deltaP `5.0328` edge `0.0293` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0546` n `132` status `ready` deltaP `11.2412` edge `0.0033` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
