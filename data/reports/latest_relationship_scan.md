# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-21T06:37:24.731702+00:00`
- Price records: `672`
- Market context records: `7431`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14659`

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

- `risk_on_high->crypto_major_4h` score `6.1873` n `32` status `ready` deltaP `35.8305` edge `0.296` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.1873` n `32` status `ready` deltaP `35.8305` edge `0.296` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `5.7839` n `32` status `ready` deltaP `16.7732` edge `0.4723` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `5.7839` n `32` status `ready` deltaP `16.7732` edge `0.4723` maxDD `-5.8371`
- `risk_on_high->unknown_4h` score `4.9442` n `32` status `ready` deltaP `15.9151` edge `0.3489` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.9442` n `32` status `ready` deltaP `15.9151` edge `0.3489` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.6966` n `32` status `ready` deltaP `27.5923` edge `0.2318` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.6966` n `32` status `ready` deltaP `27.5923` edge `0.2318` maxDD `-0.9492`
- `risk_on_high->crypto_alt_24h` score `2.6583` n `32` status `ready` deltaP `17.0927` edge `0.3197` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.6583` n `32` status `ready` deltaP `17.0927` edge `0.3197` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.205` n `33` status `ready` deltaP `19.7333` edge `0.0474` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.205` n `33` status `ready` deltaP `19.7333` edge `0.0474` maxDD `-0.957`
- `risk_on_high->equity_24h` score `1.0749` n `31` status `ready` deltaP `13.0996` edge `0.2736` maxDD `-19.375`
- `risk_on_and_context->equity_24h` score `1.0749` n `31` status `ready` deltaP `13.0996` edge `0.2736` maxDD `-19.375`
- `risk_on_high->commodity_1h` score `0.2652` n `33` status `ready` deltaP `3.7947` edge `0.0249` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.2652` n `33` status `ready` deltaP `3.7947` edge `0.0249` maxDD `-0.2479`
- `risk_on_high->equity_1h` score `0.2263` n `33` status `ready` deltaP `4.6684` edge `0.0356` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2263` n `33` status `ready` deltaP `4.6684` edge `0.0356` maxDD `-1.3497`
- `risk_on_high->fx_24h` score `0.1319` n `31` status `ready` deltaP `10.7602` edge `-0.0092` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.1319` n `31` status `ready` deltaP `10.7602` edge `-0.0092` maxDD `-1.3162`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
