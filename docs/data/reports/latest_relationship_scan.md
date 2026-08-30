# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T01:07:23.150891+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11474`

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

- `risk_on_high->crypto_alt_4h` score `6.4517` n `55` status `ready` deltaP `23.7833` edge `0.4101` maxDD `-0.4812`
- `risk_on_and_context->crypto_alt_4h` score `6.4517` n `55` status `ready` deltaP `23.7833` edge `0.4101` maxDD `-0.4812`
- `risk_on_high->crypto_major_4h` score `5.7901` n `55` status `ready` deltaP `32.1008` edge `0.2961` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `5.7901` n `55` status `ready` deltaP `32.1008` edge `0.2961` maxDD `-1.208`
- `market_context_high->metal_24h` score `4.6826` n `104` status `ready` deltaP `34.415` edge `0.2627` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `3.0856` n `45` status `ready` deltaP `-11.7398` edge `0.3711` maxDD `-0.8558`
- `news_risk_high->unknown_4h` score `3.0092` n `45` status `ready` deltaP `-6.3346` edge `0.352` maxDD `-1.7205`
- `risk_on_high->metal_4h` score `2.696` n `55` status `ready` deltaP `30.8592` edge `0.0317` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `2.696` n `55` status `ready` deltaP `30.8592` edge `0.0317` maxDD `-0.0208`
- `risk_on_high->equity_4h` score `2.5578` n `55` status `ready` deltaP `21.9429` edge `0.0918` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.5578` n `55` status `ready` deltaP `21.9429` edge `0.0918` maxDD `-0.3281`
- `market_context_high->unknown_4h` score `2.5148` n `157` status `ready` deltaP `17.7276` edge `0.1384` maxDD `-1.0945`
- `news_risk_high->crypto_alt_24h` score `2.3284` n `42` status `ready` deltaP `19.6181` edge `0.5053` maxDD `-22.3391`
- `risk_on_high->unknown_1h` score `1.8026` n `66` status `ready` deltaP `3.0077` edge `0.1741` maxDD `-1.5148`
- `risk_on_and_context->unknown_1h` score `1.8026` n `66` status `ready` deltaP `3.0077` edge `0.1741` maxDD `-1.5148`
- `risk_on_high->unknown_4h` score `1.7497` n `55` status `ready` deltaP `19.928` edge `0.0558` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `1.7497` n `55` status `ready` deltaP `19.928` edge `0.0558` maxDD `-1.0945`
- `market_context_high->unknown_1h` score `1.7147` n `168` status `ready` deltaP `9.0142` edge `0.1309` maxDD `-1.5148`
- `risk_on_high->index_4h` score `1.674` n `55` status `ready` deltaP `23.9135` edge `0.011` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.674` n `55` status `ready` deltaP `23.9135` edge `0.011` maxDD `-0.1405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
