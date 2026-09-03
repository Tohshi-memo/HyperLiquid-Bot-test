# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T06:07:30.619818+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11543`

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

- `risk_on_high->unknown_4h` score `39.8316` n `114` status `ready` deltaP `18.8142` edge `3.2557` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `39.8316` n `114` status `ready` deltaP `18.8142` edge `3.2557` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `27.5025` n `156` status `ready` deltaP `14.7319` edge `2.2632` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.29` n `126` status `ready` deltaP `1.4114` edge `1.6558` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.29` n `126` status `ready` deltaP `1.4114` edge `1.6558` maxDD `-1.95`
- `market_context_high->unknown_1h` score `12.7574` n `168` status `ready` deltaP `0.2209` edge `1.1247` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `4.9933` n `107` status `ready` deltaP `22.8339` edge `0.6784` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `4.9933` n `107` status `ready` deltaP `22.8339` edge `0.6784` maxDD `-19.828`
- `risk_on_high->crypto_alt_24h` score `2.3662` n `107` status `ready` deltaP `21.6041` edge `0.8497` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.3662` n `107` status `ready` deltaP `21.6041` edge `0.8497` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.3373` n `59` status `ready` deltaP `21.5249` edge `0.4496` maxDD `-19.4761`
- `news_risk_high->equity_24h` score `1.9934` n `59` status `ready` deltaP `8.7835` edge `0.3543` maxDD `-15.4056`
- `market_context_high->equity_24h` score `1.5911` n `147` status `ready` deltaP `18.8031` edge `0.5595` maxDD `-24.4698`
- `news_risk_high->crypto_major_24h` score `1.5137` n `59` status `ready` deltaP `14.6952` edge `0.4665` maxDD `-30.7329`
- `risk_on_high->crypto_major_24h` score `0.8316` n `107` status `ready` deltaP `21.0313` edge `0.8408` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.8316` n `107` status `ready` deltaP `21.0313` edge `0.8408` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.669` n `147` status `ready` deltaP `24.0576` edge `0.8718` maxDD `-61.3797`
- `market_context_high->crypto_alt_24h` score `0.513` n `147` status `ready` deltaP `15.6215` edge `0.7115` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.1321` n `67` status `ready` deltaP `4.1181` edge `0.0254` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.072` n `126` status `ready` deltaP `11.546` edge `0.0035` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
