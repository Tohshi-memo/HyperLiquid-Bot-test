# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T14:07:23.969461+00:00`
- Price records: `672`
- Market context records: `7256`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13743`

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

- `risk_on_high->crypto_major_4h` score `6.1493` n `34` status `ready` deltaP `28.1474` edge `0.3631` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `6.1493` n `34` status `ready` deltaP `28.1474` edge `0.3631` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.4832` n `34` status `ready` deltaP `18.7769` edge `0.2877` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.4832` n `34` status `ready` deltaP `18.7769` edge `0.2877` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1399` n `34` status `ready` deltaP `23.0171` edge `0.0399` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1399` n `34` status `ready` deltaP `23.0171` edge `0.0399` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.111` n `34` status `ready` deltaP `5.6848` edge `0.139` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.111` n `34` status `ready` deltaP `5.6848` edge `0.139` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.3339` n `34` status `ready` deltaP `8.3744` edge `0.016` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.3339` n `34` status `ready` deltaP `8.3744` edge `0.016` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.2402` n `34` status `ready` deltaP `2.9147` edge `0.0306` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.2402` n `34` status `ready` deltaP `2.9147` edge `0.0306` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.1603` n `34` status `ready` deltaP `2.7619` edge `0.0209` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.1603` n `34` status `ready` deltaP `2.7619` edge `0.0209` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.2652` n `150` status `ready` deltaP `2.1502` edge `0.0006` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.6235` n `150` status `ready` deltaP `-0.7868` edge `-0.0126` maxDD `-1.9668`
- `risk_on_high->commodity_4h` score `-0.6624` n `34` status `ready` deltaP `-0.2605` edge `-0.0107` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.6624` n `34` status `ready` deltaP `-0.2605` edge `-0.0107` maxDD `-0.7546`
- `market_context_high->crypto_alt_1h` score `-0.6964` n `150` status `ready` deltaP `-0.2854` edge `0.0165` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.825` n `150` status `ready` deltaP `2.2176` edge `0.0205` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
