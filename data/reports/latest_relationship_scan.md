# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T19:07:35.151976+00:00`
- Price records: `672`
- Market context records: `7383`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14654`

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

- `risk_on_high->crypto_major_4h` score `6.1382` n `32` status `ready` deltaP `35.4421` edge `0.2945` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.1382` n `32` status `ready` deltaP `35.4421` edge `0.2945` maxDD `-0.8742`
- `risk_on_high->unknown_4h` score `4.9147` n `32` status `ready` deltaP `15.3963` edge `0.3499` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.9147` n `32` status `ready` deltaP `15.3963` edge `0.3499` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.7824` n `32` status `ready` deltaP `28.125` edge `0.2354` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.7824` n `32` status `ready` deltaP `28.125` edge `0.2354` maxDD `-0.9492`
- `risk_on_high->crypto_major_1h` score `1.0897` n `32` status `ready` deltaP `19.1804` edge `0.0363` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.0897` n `32` status `ready` deltaP `19.1804` edge `0.0363` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.352` n `32` status `ready` deltaP `4.8986` edge `0.0246` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.352` n `32` status `ready` deltaP `4.8986` edge `0.0246` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1125` n `32` status `ready` deltaP `3.4535` edge `0.0291` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1125` n `32` status `ready` deltaP `3.4535` edge `0.0291` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `-0.0379` n `32` status `ready` deltaP `-0.5988` edge `0.0362` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `-0.0379` n `32` status `ready` deltaP `-0.5988` edge `0.0362` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.1728` n `131` status `ready` deltaP `4.0357` edge `-0.0001` maxDD `-0.583`
- `risk_on_high->metal_4h` score `-0.2518` n `32` status `ready` deltaP `-1.2195` edge `0.0695` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.2518` n `32` status `ready` deltaP `-1.2195` edge `0.0695` maxDD `-0.5882`
- `market_context_high->commodity_1h` score `-0.5824` n `131` status `ready` deltaP `-1.7331` edge `-0.0059` maxDD `-1.5775`
- `market_context_high->commodity_4h` score `-0.7135` n `129` status `ready` deltaP `-0.1707` edge `0.0065` maxDD `-2.4139`
- `market_context_high->unknown_4h` score `-0.8483` n `129` status `ready` deltaP `3.3323` edge `0.1049` maxDD `-6.2031`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
