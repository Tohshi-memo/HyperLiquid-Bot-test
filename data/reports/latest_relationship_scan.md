# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T11:22:29.676404+00:00`
- Price records: `672`
- Market context records: `7244`
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

- `risk_on_high->crypto_major_4h` score `5.9355` n `34` status `ready` deltaP `27.0804` edge `0.3524` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `5.9355` n `34` status `ready` deltaP `27.0804` edge `0.3524` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.2819` n `34` status `ready` deltaP `17.1001` edge `0.2821` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.2819` n `34` status `ready` deltaP `17.1001` edge `0.2821` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1403` n `34` status `ready` deltaP `22.9474` edge `0.0404` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1403` n `34` status `ready` deltaP `22.9474` edge `0.0404` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.0405` n `34` status `ready` deltaP `5.0741` edge `0.1372` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.0405` n `34` status `ready` deltaP `5.0741` edge `0.1372` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.263` n `34` status `ready` deltaP `7.4762` edge `0.0129` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.263` n `34` status `ready` deltaP `7.4762` edge `0.0129` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.2059` n `34` status `ready` deltaP `2.5311` edge `0.0303` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.2059` n `34` status `ready` deltaP `2.5311` edge `0.0303` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.1398` n `34` status `ready` deltaP `3.0667` edge `0.0215` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.1398` n `34` status `ready` deltaP `3.0667` edge `0.0215` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.2679` n `161` status `ready` deltaP `2.0989` edge `0.0006` maxDD `-0.5817`
- `risk_on_high->commodity_4h` score `-0.6502` n `34` status `ready` deltaP `-0.1078` edge `-0.0107` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.6502` n `34` status `ready` deltaP `-0.1078` edge `-0.0107` maxDD `-0.7546`
- `market_context_high->commodity_1h` score `-0.6597` n `161` status `ready` deltaP `-1.3493` edge `-0.0135` maxDD `-1.9668`
- `market_context_high->crypto_alt_1h` score `-0.681` n `161` status `ready` deltaP `-0.0335` edge `0.0168` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.7322` n `161` status `ready` deltaP `3.3111` edge `0.0251` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
