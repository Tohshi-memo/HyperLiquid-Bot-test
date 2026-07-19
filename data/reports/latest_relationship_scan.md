# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T12:37:31.289696+00:00`
- Price records: `672`
- Market context records: `7250`
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

- `risk_on_high->crypto_major_4h` score `6.0369` n `34` status `ready` deltaP `27.5377` edge `0.3578` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `6.0369` n `34` status `ready` deltaP `27.5377` edge `0.3578` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.386` n `34` status `ready` deltaP `17.8623` edge `0.2857` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.386` n `34` status `ready` deltaP `17.8623` edge `0.2857` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1146` n `34` status `ready` deltaP `22.7168` edge `0.0398` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1146` n `34` status `ready` deltaP `22.7168` edge `0.0398` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.1172` n `34` status `ready` deltaP `5.8374` edge `0.1385` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.1172` n `34` status `ready` deltaP `5.8374` edge `0.1385` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.316` n `34` status `ready` deltaP `8.075` edge `0.0157` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.316` n `34` status `ready` deltaP `8.075` edge `0.0157` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.2582` n `34` status `ready` deltaP `3.0648` edge `0.0311` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.2582` n `34` status `ready` deltaP `3.0648` edge `0.0311` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.1342` n `34` status `ready` deltaP `3.2192` edge `0.0212` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.1342` n `34` status `ready` deltaP `3.2192` edge `0.0212` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.2351` n `156` status `ready` deltaP `2.7143` edge `0.0007` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.6072` n `156` status `ready` deltaP `-0.5487` edge `-0.0121` maxDD `-1.9668`
- `risk_on_high->commodity_4h` score `-0.7075` n `34` status `ready` deltaP `-0.7185` edge `-0.0114` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.7075` n `34` status `ready` deltaP `-0.7185` edge `-0.0114` maxDD `-0.7546`
- `market_context_high->crypto_alt_1h` score `-0.7217` n `156` status `ready` deltaP `-0.5758` edge `0.0152` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.8024` n `156` status `ready` deltaP `2.4566` edge `0.0218` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
