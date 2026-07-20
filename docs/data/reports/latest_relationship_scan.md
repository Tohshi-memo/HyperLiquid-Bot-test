# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T22:37:28.940154+00:00`
- Price records: `672`
- Market context records: `7398`
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

- `risk_on_high->crypto_major_4h` score `6.2722` n `32` status `ready` deltaP `36.0518` edge `0.3016` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.2722` n `32` status `ready` deltaP `36.0518` edge `0.3016` maxDD `-0.8742`
- `risk_on_high->unknown_4h` score `4.9039` n `32` status `ready` deltaP `15.3963` edge `0.349` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.9039` n `32` status `ready` deltaP `15.3963` edge `0.349` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.7252` n `32` status `ready` deltaP `27.5152` edge `0.2347` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.7252` n `32` status `ready` deltaP `27.5152` edge `0.2347` maxDD `-0.9492`
- `risk_on_high->crypto_major_1h` score `1.0983` n `32` status `ready` deltaP `19.1804` edge `0.0374` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.0983` n `32` status `ready` deltaP `19.1804` edge `0.0374` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.3844` n `32` status `ready` deltaP `5.1989` edge `0.0253` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.3844` n `32` status `ready` deltaP `5.1989` edge `0.0253` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1687` n `32` status `ready` deltaP `4.0541` edge `0.0323` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1687` n `32` status `ready` deltaP `4.0541` edge `0.0323` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `-0.0496` n `32` status `ready` deltaP `-0.5988` edge `0.0347` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `-0.0496` n `32` status `ready` deltaP `-0.5988` edge `0.0347` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.1553` n `132` status `ready` deltaP `4.3817` edge `0.0` maxDD `-0.5967`
- `risk_on_high->metal_4h` score `-0.1606` n `32` status `ready` deltaP `-0.3049` edge `0.071` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.1606` n `32` status `ready` deltaP `-0.3049` edge `0.071` maxDD `-0.5882`
- `market_context_high->commodity_1h` score `-0.5376` n `132` status `ready` deltaP `-1.0511` edge `-0.0047` maxDD `-1.5775`
- `market_context_high->unknown_4h` score `-0.8319` n `132` status `ready` deltaP `3.8433` edge `0.1036` maxDD `-6.2031`
- `market_context_high->commodity_4h` score `-0.9714` n `132` status `ready` deltaP `0.8687` edge `0.0101` maxDD `-2.4139`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
