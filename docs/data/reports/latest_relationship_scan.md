# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T22:22:24.070884+00:00`
- Price records: `672`
- Market context records: `7397`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14677`

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

- `risk_on_high->crypto_major_4h` score `6.2312` n `32` status `ready` deltaP `35.8994` edge `0.2992` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.2312` n `32` status `ready` deltaP `35.8994` edge `0.2992` maxDD `-0.8742`
- `risk_on_high->unknown_4h` score `4.8967` n `32` status `ready` deltaP `15.3963` edge `0.3484` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.8967` n `32` status `ready` deltaP `15.3963` edge `0.3484` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.6854` n `32` status `ready` deltaP `27.3628` edge `0.2324` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.6854` n `32` status `ready` deltaP `27.3628` edge `0.2324` maxDD `-0.9492`
- `risk_on_high->crypto_major_1h` score `1.0804` n `32` status `ready` deltaP `19.0307` edge `0.0361` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.0804` n `32` status `ready` deltaP `19.0307` edge `0.0361` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.3832` n `32` status `ready` deltaP `5.1989` edge `0.0252` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.3832` n `32` status `ready` deltaP `5.1989` edge `0.0252` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1593` n `32` status `ready` deltaP `3.9039` edge `0.0321` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1593` n `32` status `ready` deltaP `3.9039` edge `0.0321` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `-0.0667` n `32` status `ready` deltaP `-0.7485` edge `0.0335` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `-0.0667` n `32` status `ready` deltaP `-0.7485` edge `0.0335` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.1553` n `132` status `ready` deltaP `4.3817` edge `0.0` maxDD `-0.5967`
- `risk_on_high->metal_4h` score `-0.1594` n `32` status `ready` deltaP `-0.3049` edge `0.0711` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.1594` n `32` status `ready` deltaP `-0.3049` edge `0.0711` maxDD `-0.5882`
- `market_context_high->commodity_1h` score `-0.5384` n `132` status `ready` deltaP `-1.0511` edge `-0.0048` maxDD `-1.5775`
- `market_context_high->unknown_4h` score `-0.8366` n `132` status `ready` deltaP `3.8433` edge `0.103` maxDD `-6.2031`
- `market_context_high->commodity_4h` score `-0.9896` n `132` status `ready` deltaP `0.7158` edge `0.0096` maxDD `-2.4139`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
