# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T17:07:29.203268+00:00`
- Price records: `672`
- Market context records: `7374`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14631`

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

- `risk_on_high->crypto_major_4h` score `6.4612` n `32` status `ready` deltaP `36.5091` edge `0.3143` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.4612` n `32` status `ready` deltaP `36.5091` edge `0.3143` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.1464` n `32` status `ready` deltaP `29.3445` edge `0.2576` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.1464` n `32` status `ready` deltaP `29.3445` edge `0.2576` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.1155` n `32` status `ready` deltaP `16.6159` edge `0.3585` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.1155` n `32` status `ready` deltaP `16.6159` edge `0.3585` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.1217` n `32` status `ready` deltaP `19.4798` edge `0.0384` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.1217` n `32` status `ready` deltaP `19.4798` edge `0.0384` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.346` n `32` status `ready` deltaP `5.0488` edge `0.0231` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.346` n `32` status `ready` deltaP `5.0488` edge `0.0231` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1172` n `32` status `ready` deltaP `3.6036` edge `0.0287` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1172` n `32` status `ready` deltaP `3.6036` edge `0.0287` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.0369` n `32` status `ready` deltaP `0.1497` edge `0.0408` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.0369` n `32` status `ready` deltaP `0.1497` edge `0.0408` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.1535` n `129` status `ready` deltaP `4.3893` edge `0.0` maxDD `-0.5821`
- `risk_on_high->metal_4h` score `-0.275` n `32` status `ready` deltaP `-1.5244` edge `0.0696` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.275` n `32` status `ready` deltaP `-1.5244` edge `0.0696` maxDD `-0.5882`
- `market_context_high->commodity_1h` score `-0.6511` n `129` status `ready` deltaP `-2.364` edge `-0.0105` maxDD `-1.5775`
- `market_context_high->unknown_4h` score `-0.7178` n `129` status `ready` deltaP `4.5519` edge `0.1135` maxDD `-6.2031`
- `market_context_high->commodity_4h` score `-0.7513` n `129` status `ready` deltaP `-0.4765` edge `0.0037` maxDD `-2.4139`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
